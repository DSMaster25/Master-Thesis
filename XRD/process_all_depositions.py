"""
XRD Analysis for All Depositions
This script processes XRD data from multiple deposition folders automatically.
"""

import pandas as pd
import numpy as np
import os, glob, re, csv
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, peak_widths, savgol_filter
from scipy.optimize import curve_fit
from matplotlib.tri import Triangulation
from matplotlib.colors import LinearSegmentedColormap, PowerNorm, Normalize
from pathlib import Path
from scipy.interpolate import griddata

# =============================================================================
# CONFIGURATION
# =============================================================================

# Define all deposition folders to process
BASE_DIR = r"C:\Dilan\Study\Master Thesis\Characterization\XRD"

DEPOSITIONS = [
    "30-09-2025 Dep 1",
    "22-09-2025 Dep 2",
    "24-09-2025 Dep 3",
    "07-10-2025 Dep 6",
    "08-10-2025 Dep 7",
    "09-10-2025 Dep 8"
]

# Target position (mm) - same for all depositions
target_x = 399.88
target_y = 224.1
target_z = 332.15

# Wafer center position (x=0, y=0 in XRD coordinates corresponds to this)
wafer_center_x = 242.5
wafer_center_y = 257.0
wafer_center_z = 435.0

# XRD analysis parameters
REGIONS = [
    (20.5, 23.0),   # (100)
    (30.5, 33.0),   # (110)
    (37.5, 40.0),   # (111)
    (44.0, 47.0),   # (200)
    (50.0, 52.5),   # (210)
    (55.0, 57.5),   # (112)
]
REGION_NAMES = ["(100)", "(110)", "(111)", "(200)", "(210)", "(112)"]

# Peak finding settings
window_pts = 12
polyorder = 2
min_sep_deg = 0.25
width_deg = (0.06, 1.2)
ratio_min = 1.2
frac_min = 0.00

print(f"Base directory: {BASE_DIR}")
print(f"\nDepositions to process: {len(DEPOSITIONS)}")
for dep in DEPOSITIONS:
    print(f"  - {dep}")

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def _safe_window(n, w, p):
    if n < 5:
        return None, None
    w = min(w, n - (1 - (n % 2)))
    if w % 2 == 0: w += 1
    w = max(5, w)
    p = min(p, w - 2)
    return w, p

def extract_xy_from_filename(filename):
    """Extract X and Y coordinates from filename like 'something_X-value_Y-value.xy'"""
    name = os.path.basename(filename).rsplit('.', 1)[0]
    parts = name.split('_')
    try:
        x_str, y_str = parts[-2], parts[-1]
        def tok_to_float(t):
            if '-' in t[1:]:
                t = ('-' + t[1:].replace('-', '.', 1)) if t.startswith('-') else t.replace('-', '.', 1)
            return float(t)
        x_val, y_val = tok_to_float(x_str), tok_to_float(y_str)
        return x_val, y_val
    except Exception:
        return None, None

def _unique_xy(x, y, z):
    arr = np.column_stack([x, y, z])
    keys = np.ascontiguousarray(arr[:, :2]).view(
        np.dtype((np.void, arr[:, :2].dtype.itemsize * 2))
    ).ravel()
    _, idx = np.unique(keys, return_index=True)
    idx = np.sort(idx)
    return arr[idx, 0], arr[idx, 1], arr[idx, 2]

def _robust_minmax(zs):
    vmin = np.nanpercentile(zs, 5)
    vmax = np.nanpercentile(zs, 95)
    if not np.isfinite(vmin) or not np.isfinite(vmax) or vmin == vmax:
        vmin = float(np.nanmin(zs))
        vmax = float(np.nanmax(zs))
    return vmin, vmax

def normalize_six(arr, N):
    """Normalize data into shape (N, 6)"""
    a = np.asarray(arr)
    if a.ndim == 2 and a.shape == (N, 6):
        return a
    if a.ndim == 1 and a.size == N * 6:
        return a.reshape(N, 6)
    if a.ndim == 2 and a.shape[0] == N * 6 and a.shape[1] == 6:
        blocks = np.split(a, 6, axis=0)
        return np.column_stack([blocks[j][:, j] for j in range(6)])
    if a.ndim == 2 and a.shape == (N * 6, 1):
        return a.reshape(N, 6)
    raise ValueError(f"Cannot reshape array with shape {a.shape} to (N,6).")

def _contour_one_custom(ax, xs_all, ys_all, zs_all, title, nlevels=100, cmap="coolwarm", levels=None):
    """Create smooth contour plot using triangulation. Shows all measurement points with markers."""
    mask_finite = np.isfinite(xs_all) & np.isfinite(ys_all) & np.isfinite(zs_all)
    xs = xs_all[mask_finite]
    ys = ys_all[mask_finite]
    zs = zs_all[mask_finite]

    if len(xs) == 0:
        ax.text(0.5, 0.5, "No data", ha="center", va="center", transform=ax.transAxes)
        ax.scatter(xs_all, ys_all, s=30, c='red', marker='x', alpha=0.6, linewidths=2)
        ax.set_title(title, fontsize=11)
        ax.set_xlabel("X [mm]")
        ax.set_ylabel("Y [mm]")
        ax.set_aspect('equal', adjustable='box')
        return None

    xs, ys, zs = _unique_xy(xs, ys, zs)

    if len(xs) < 3:
        ax.text(0.5, 0.5, "Too few points", ha="center", va="center", transform=ax.transAxes)
        ax.scatter(xs_all, ys_all, s=30, c='red', marker='x', alpha=0.6, linewidths=2)
        ax.set_title(title, fontsize=11)
        ax.set_xlabel("X [mm]")
        ax.set_ylabel("Y [mm]")
        ax.set_aspect('equal', adjustable='box')
        return None

    finite_levels = None
    if levels is not None:
        finite_levels = np.asarray(levels, dtype=float)
        finite_levels = finite_levels[np.isfinite(finite_levels)]

    if finite_levels is None or finite_levels.size == 0:
        vmin, vmax = _robust_minmax(zs)
        if not np.isfinite(vmin) or not np.isfinite(vmax) or vmin == vmax:
            ax.text(0.5, 0.5, "No variation", ha="center", va="center", transform=ax.transAxes)
            ax.set_title(title, fontsize=11)
            ax.set_xlabel("X [mm]")
            ax.set_ylabel("Y [mm]")
            ax.set_aspect('equal', adjustable='box')
            return None
        finite_levels = np.linspace(vmin, vmax, nlevels)

    try:
        tri = Triangulation(xs, ys)
        cf = ax.tricontourf(tri, zs, levels=finite_levels, extend="both", cmap=cmap)
    except Exception:
        gx = np.linspace(xs.min(), xs.max(), 100)
        gy = np.linspace(ys.min(), ys.max(), 100)
        GX, GY = np.meshgrid(gx, gy)
        GZ = griddata((xs, ys), zs, (GX, GY), method="linear")
        if np.isnan(GZ).all():
            GZ = griddata((xs, ys), zs, (GX, GY), method="nearest")
        if np.isnan(GZ).all():
            ax.text(0.5, 0.5, "Triangulation failed", ha="center", va="center", transform=ax.transAxes)
            ax.set_title(title, fontsize=11)
            ax.set_xlabel("X [mm]")
            ax.set_ylabel("Y [mm]")
            ax.set_aspect('equal', adjustable='box')
            return None

        cf = ax.contourf(GX, GY, GZ, levels=finite_levels, extend="both", cmap=cmap)

    # Scatter plot: show ALL measurement points
    if np.sum(mask_finite) > 0:
        ax.scatter(xs_all[mask_finite], ys_all[mask_finite],
                   s=30, c="k", alpha=0.6, edgecolors='white', linewidths=0.5, zorder=5)

    if np.sum(~mask_finite) > 0:
        ax.scatter(xs_all[~mask_finite], ys_all[~mask_finite],
                   s=30, c="red", marker='x', alpha=0.8, linewidths=2, zorder=5)

    ax.set_title(title, fontsize=11)
    ax.set_xlabel("X [mm]")
    ax.set_ylabel("Y [mm]")
    ax.set_aspect('equal', adjustable='box')

    return cf

# =============================================================================
# MAIN PROCESSING LOOP
# =============================================================================

print("\n" + "="*80)
print("PROCESSING ALL DEPOSITIONS")
print("="*80)

all_deposition_results = {}

for dep_name in DEPOSITIONS:
    print(f"\n{'='*80}")
    print(f"Processing: {dep_name}")
    print(f"{'='*80}")

    dep_folder = os.path.join(BASE_DIR, dep_name)
    xy_data_folder = os.path.join(dep_folder, "XY Data")

    if not os.path.exists(xy_data_folder):
        print(f"  WARNING: XY Data folder not found in {dep_name}")
        continue

    os.chdir(xy_data_folder)
    files = sorted(glob.glob("*.xy"))

    if len(files) == 0:
        print(f"  WARNING: No .xy files found in {dep_name}")
        continue

    print(f"  Found {len(files)} XRD data files")

    # Initialize storage for this deposition
    all_file_results = []
    x_coordinates = []
    y_coordinates = []

    # Process each file
    for fp in files:
        data = np.loadtxt(fp)
        x, y = data[:,0], data[:,1]
        step = float(np.mean(np.diff(x)))

        # Smooth for peak detection
        w_use, p_use = _safe_window(len(x), window_pts, polyorder)
        ys = savgol_filter(y, w_use, p_use, mode="interp") if w_use is not None else y.copy()

        distance = max(1, int(min_sep_deg/step))
        width_s = (max(1, int(width_deg[0]/step)), max(2, int(width_deg[1]/step)))

        # Storage for THIS file: 6 values (one per region)
        file_fwhm = np.full(6, np.nan)
        file_intensity = np.full(6, np.nan)
        file_area = np.full(6, np.nan)
        file_peak_positions = [None] * 6

        per_region_count = {i: 0 for i in range(1, len(REGIONS)+1)}

        for rid, (lo, hi) in enumerate(REGIONS, start=1):
            m = (x >= lo) & (x <= hi)
            if np.count_nonzero(m) < 7:
                continue

            xr = x[m]
            yr = ys[m]
            idx0 = np.nonzero(m)[0][0]

            # Find peaks
            cand_r, prop = find_peaks(yr, distance=distance, width=width_s)
            if cand_r.size == 0:
                continue

            keep_r = []
            for i, pk in enumerate(cand_r):
                lb = prop["left_bases"][i]
                rb = prop["right_bases"][i]
                base = max(yr[lb], yr[rb])
                amp = yr[pk] - base
                if amp <= 0: continue
                if yr[pk] / max(base, 1e-9) < ratio_min: continue
                if amp < frac_min * base: continue
                keep_r.append(i)

            if not keep_r:
                continue

            peaks_r = cand_r[keep_r]
            widths, w_left, w_right, _ = peak_widths(yr, peaks_r, rel_height=0.5)

            idx_axis = np.arange(len(xr), dtype=float)
            left_x = np.interp(w_left, idx_axis, xr)
            right_x = np.interp(w_right, idx_axis, xr)
            fwhm_deg = np.abs(right_x - left_x)

            for j, pk in enumerate(peaks_r):
                lb = prop["left_bases"][keep_r[j]]
                rb = prop["right_bases"][keep_r[j]]

                x_lb, y_lb = xr[lb], yr[lb]
                x_rb, y_rb = xr[rb], yr[rb]

                lx, rx = x_lb, x_rb
                if lx >= rx:
                    lx = left_x[j]
                    rx = right_x[j]

                seg_mask = (xr >= lx) & (xr <= rx)
                if np.count_nonzero(seg_mask) < 2:
                    k0 = max(0, pk - 3)
                    k1 = min(len(xr), pk + 4)
                    seg_mask = np.zeros_like(xr, dtype=bool)
                    seg_mask[k0:k1] = True

                xs = xr[seg_mask]
                ys_seg = yr[seg_mask]

                if x_rb != x_lb:
                    slope = (y_rb - y_lb) / (x_rb - x_lb)
                    y_base = y_lb + slope * (xs - x_lb)
                else:
                    y_base = np.full_like(xs, np.mean([y_lb, y_rb]))

                area = np.trapz(np.maximum(ys_seg - y_base, 0.0), xs)

                if area == 0.0 or not np.isfinite(area):
                    peak_height = yr[pk] - np.mean([y_lb, y_rb])
                    area = peak_height * fwhm_deg[j] * 0.5 * np.sqrt(np.pi / np.log(2))

                gi = idx0 + pk
                per_region_count[rid] += 1

                # Store first peak per region
                if per_region_count[rid] == 1:
                    file_fwhm[rid-1] = float(fwhm_deg[j])
                    file_intensity[rid-1] = float(yr[pk])
                    file_area[rid-1] = float(area)
                    file_peak_positions[rid-1] = float(x[gi])

        # Extract X and Y coordinates from filename
        x_val, y_val = extract_xy_from_filename(fp)
        if x_val is not None and y_val is not None:
            x_coordinates.append(x_val)
            y_coordinates.append(y_val)

        # Store results for this file
        all_file_results.append({
            'fwhm': file_fwhm,
            'intensity': file_intensity,
            'area': file_area,
            'peak_positions': file_peak_positions,
            'filename': fp
        })

    # Convert to numpy arrays
    results = np.array([f['fwhm'] for f in all_file_results])
    peak_intensity = np.array([f['intensity'] for f in all_file_results])
    peak_areas = np.array([f['area'] for f in all_file_results])

    # Take absolute values of FWHM
    results = np.abs(results)

    # Store results for this deposition
    all_deposition_results[dep_name] = {
        'x_coordinates': np.array(x_coordinates),
        'y_coordinates': np.array(y_coordinates),
        'fwhm': results,
        'peak_intensity': peak_intensity,
        'peak_areas': peak_areas,
        'num_files': len(files),
        'num_processed': len(all_file_results),
        'files': files,
        'file_results': all_file_results
    }

    print(f"  Processed {len(all_file_results)} files successfully")

print(f"\n\n{'='*80}")
print(f"Processing complete! Results stored for {len(all_deposition_results)} depositions.")
print(f"{'='*80}")

# =============================================================================
# DISTANCE TO TARGET ANALYSIS
# =============================================================================

print("\n" + "="*80)
print("DISTANCE TO TARGET ANALYSIS")
print("="*80)

for dep_name in DEPOSITIONS:
    if dep_name not in all_deposition_results:
        print(f"\nSkipping {dep_name} - no results available")
        continue

    print(f"\n{'='*80}")
    print(f"Distance analysis for: {dep_name}")
    print(f"{'='*80}")

    # Get results for this deposition
    dep_data = all_deposition_results[dep_name]
    x_coordinates = dep_data['x_coordinates']
    y_coordinates = dep_data['y_coordinates']
    fwhm = dep_data['fwhm']
    peakI = dep_data['peak_intensity']
    peakA = dep_data['peak_areas']

    # Convert XRD coordinates to real-world coordinates
    # The x_coordinates from XRD need to have their sign flipped
    x_pos_real = -x_coordinates + wafer_center_x
    y_pos_real = y_coordinates + wafer_center_y
    z_pos_real = np.full_like(x_pos_real, wafer_center_z)

    # Calculate 3D distance from each point to target
    distances_3d = np.sqrt(
        (x_pos_real - target_x)**2 +
        (y_pos_real - target_y)**2 +
        (z_pos_real - target_z)**2
    )

    print(f"  3D Distance range: {distances_3d.min():.2f} - {distances_3d.max():.2f} mm")

    # Get data for (100) and (110) planes
    area_100 = peakA[:, 0]
    area_110 = peakA[:, 1]
    fwhm_100 = fwhm[:, 0]
    fwhm_110 = fwhm[:, 1]
    intensity_100 = peakI[:, 0]
    intensity_110 = peakI[:, 1]

    # Calculate area ratio
    with np.errstate(divide='ignore', invalid='ignore'):
        area_ratio = area_100 / area_110
    area_ratio[~np.isfinite(area_ratio)] = np.nan

    # ===============================================================
    # PLOT 1: FWHM vs 3D Distance
    # ===============================================================
    fig, axes = plt.subplots(1, 2, figsize=(14, 5), constrained_layout=True)

    # (100) FWHM
    ax = axes[0]
    mask_finite = np.isfinite(fwhm_100) & np.isfinite(distances_3d)
    ax.scatter(distances_3d[mask_finite], fwhm_100[mask_finite],
               c='blue', s=50, alpha=0.7, edgecolors='black', linewidths=0.5)
    ax.set_xlabel('3D Distance to Target Center (mm)', fontsize=11)
    ax.set_ylabel('FWHM (°)', fontsize=11)
    ax.set_title('(100) Plane: FWHM vs 3D Distance', fontsize=12)
    ax.grid(True, alpha=0.3)

    if np.sum(mask_finite) > 3:
        z = np.polyfit(distances_3d[mask_finite], fwhm_100[mask_finite], 2)
        p = np.poly1d(z)
        x_trend = np.linspace(distances_3d[mask_finite].min(), distances_3d[mask_finite].max(), 100)
        ax.plot(x_trend, p(x_trend), 'r--', linewidth=2, alpha=0.7, label='Quadratic fit')
        ax.legend()

    # (110) FWHM
    ax = axes[1]
    mask_finite = np.isfinite(fwhm_110) & np.isfinite(distances_3d)
    ax.scatter(distances_3d[mask_finite], fwhm_110[mask_finite],
               c='red', s=50, alpha=0.7, edgecolors='black', linewidths=0.5)
    ax.set_xlabel('3D Distance to Target Center (mm)', fontsize=11)
    ax.set_ylabel('FWHM (°)', fontsize=11)
    ax.set_title('(110) Plane: FWHM vs 3D Distance', fontsize=12)
    ax.grid(True, alpha=0.3)

    if np.sum(mask_finite) > 3:
        z = np.polyfit(distances_3d[mask_finite], fwhm_110[mask_finite], 2)
        p = np.poly1d(z)
        x_trend = np.linspace(distances_3d[mask_finite].min(), distances_3d[mask_finite].max(), 100)
        ax.plot(x_trend, p(x_trend), 'r--', linewidth=2, alpha=0.7, label='Quadratic fit')
        ax.legend()

    plt.suptitle(f'{dep_name}: FWHM by Distance to Target Center', y=1.00, fontsize=14)
    plt.show()

    # ===============================================================
    # PLOT 2: Peak Intensity vs 3D Distance
    # ===============================================================
    fig, axes = plt.subplots(1, 2, figsize=(14, 5), constrained_layout=True)

    # (100) Peak Intensity
    ax = axes[0]
    mask_finite = np.isfinite(intensity_100) & np.isfinite(distances_3d)
    ax.scatter(distances_3d[mask_finite], intensity_100[mask_finite],
               c='blue', s=50, alpha=0.7, edgecolors='black', linewidths=0.5)
    ax.set_xlabel('3D Distance to Target Center (mm)', fontsize=11)
    ax.set_ylabel('Peak Intensity (counts per second)', fontsize=11)
    ax.set_title('(100) Plane: Peak Intensity vs 3D Distance', fontsize=12)
    ax.grid(True, alpha=0.3)

    if np.sum(mask_finite) > 3:
        z = np.polyfit(distances_3d[mask_finite], intensity_100[mask_finite], 2)
        p = np.poly1d(z)
        x_trend = np.linspace(distances_3d[mask_finite].min(), distances_3d[mask_finite].max(), 100)
        ax.plot(x_trend, p(x_trend), 'r--', linewidth=2, alpha=0.7, label='Quadratic fit')
        ax.legend()

    # (110) Peak Intensity
    ax = axes[1]
    mask_finite = np.isfinite(intensity_110) & np.isfinite(distances_3d)
    ax.scatter(distances_3d[mask_finite], intensity_110[mask_finite],
               c='red', s=50, alpha=0.7, edgecolors='black', linewidths=0.5)
    ax.set_xlabel('3D Distance to Target Center (mm)', fontsize=11)
    ax.set_ylabel('Peak Intensity (counts per second)', fontsize=11)
    ax.set_title('(110) Plane: Peak Intensity vs 3D Distance', fontsize=12)
    ax.grid(True, alpha=0.3)

    if np.sum(mask_finite) > 3:
        z = np.polyfit(distances_3d[mask_finite], intensity_110[mask_finite], 2)
        p = np.poly1d(z)
        x_trend = np.linspace(distances_3d[mask_finite].min(), distances_3d[mask_finite].max(), 100)
        ax.plot(x_trend, p(x_trend), 'r--', linewidth=2, alpha=0.7, label='Quadratic fit')
        ax.legend()

    plt.suptitle(f'{dep_name}: Peak Intensity by Distance to Target Center', y=1.00, fontsize=14)
    plt.show()

    # ===============================================================
    # PLOT 3: Integrated Area vs 3D Distance
    # ===============================================================
    fig, axes = plt.subplots(1, 2, figsize=(14, 5), constrained_layout=True)

    # (100) Integrated Area
    ax = axes[0]
    mask_finite = np.isfinite(area_100) & np.isfinite(distances_3d)
    ax.scatter(distances_3d[mask_finite], area_100[mask_finite],
               c='blue', s=50, alpha=0.7, edgecolors='black', linewidths=0.5)
    ax.set_xlabel('3D Distance to Target Center (mm)', fontsize=11)
    ax.set_ylabel('Integrated Area (a.u.)', fontsize=11)
    ax.set_title('(100) Plane: Integrated Area vs 3D Distance', fontsize=12)
    ax.grid(True, alpha=0.3)

    if np.sum(mask_finite) > 3:
        z = np.polyfit(distances_3d[mask_finite], area_100[mask_finite], 2)
        p = np.poly1d(z)
        x_trend = np.linspace(distances_3d[mask_finite].min(), distances_3d[mask_finite].max(), 100)
        ax.plot(x_trend, p(x_trend), 'r--', linewidth=2, alpha=0.7, label='Quadratic fit')
        ax.legend()

    # (110) Integrated Area
    ax = axes[1]
    mask_finite = np.isfinite(area_110) & np.isfinite(distances_3d)
    ax.scatter(distances_3d[mask_finite], area_110[mask_finite],
               c='red', s=50, alpha=0.7, edgecolors='black', linewidths=0.5)
    ax.set_xlabel('3D Distance to Target Center (mm)', fontsize=11)
    ax.set_ylabel('Integrated Area (a.u.)', fontsize=11)
    ax.set_title('(110) Plane: Integrated Area vs 3D Distance', fontsize=12)
    ax.grid(True, alpha=0.3)

    if np.sum(mask_finite) > 3:
        z = np.polyfit(distances_3d[mask_finite], area_110[mask_finite], 2)
        p = np.poly1d(z)
        x_trend = np.linspace(distances_3d[mask_finite].min(), distances_3d[mask_finite].max(), 100)
        ax.plot(x_trend, p(x_trend), 'r--', linewidth=2, alpha=0.7, label='Quadratic fit')
        ax.legend()

    plt.suptitle(f'{dep_name}: Integrated Area by Distance to Target Center', y=1.00, fontsize=14)
    plt.show()

    # ===============================================================
    # PLOT 4: Area Ratio (100)/(110) vs 3D Distance
    # ===============================================================
    fig, ax = plt.subplots(1, 1, figsize=(8, 6), constrained_layout=True)

    mask_finite = np.isfinite(area_ratio) & np.isfinite(distances_3d)
    ax.scatter(distances_3d[mask_finite], area_ratio[mask_finite],
               c='green', s=50, alpha=0.7, edgecolors='black', linewidths=0.5)
    ax.set_xlabel('3D Distance to Target Center (mm)', fontsize=11)
    ax.set_ylabel('Area Ratio (100)/(110)', fontsize=11)
    ax.set_title(f'{dep_name}: Area Ratio vs 3D Distance to Target', fontsize=12)
    ax.grid(True, alpha=0.3)

    if np.sum(mask_finite) > 3:
        z = np.polyfit(distances_3d[mask_finite], area_ratio[mask_finite], 2)
        p = np.poly1d(z)
        x_trend = np.linspace(distances_3d[mask_finite].min(), distances_3d[mask_finite].max(), 100)
        ax.plot(x_trend, p(x_trend), 'r--', linewidth=2, alpha=0.7, label='Quadratic fit')
        ax.legend()

    plt.show()

    # Print correlation statistics
    print(f"\nCorrelation coefficients (Pearson) with 3D distance:")
    for metric_name, data_100, data_110 in [
        ("FWHM", fwhm_100, fwhm_110),
        ("Peak Intensity", intensity_100, intensity_110),
        ("Integrated Area", area_100, area_110)
    ]:
        print(f"\n  {metric_name}:")
        for plane_name, data in [("(100)", data_100), ("(110)", data_110)]:
            mask = np.isfinite(data) & np.isfinite(distances_3d)
            if np.sum(mask) > 2:
                corr = np.corrcoef(distances_3d[mask], data[mask])[0, 1]
                print(f"    {plane_name}: r = {corr:.3f}")

    # Area ratio
    mask = np.isfinite(area_ratio) & np.isfinite(distances_3d)
    if np.sum(mask) > 2:
        corr = np.corrcoef(distances_3d[mask], area_ratio[mask])[0, 1]
        print(f"\n  Area Ratio (100)/(110): r = {corr:.3f}")

print(f"\n\n{'='*80}")
print("All depositions analyzed successfully!")
print(f"{'='*80}")
