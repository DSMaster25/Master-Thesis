# Example: How to loop through all 6 depositions in your notebook

import os
import glob

# Define your deposition list
BASE_DIR = r"C:\Dilan\Study\Master Thesis\Characterization\XRD"

DEPOSITIONS = [
    "30-09-2025 Dep 1",
    "22-09-2025 Dep 2",
    "24-09-2025 Dep 3",
    "07-10-2025 Dep 6",
    "08-10-2025 Dep 7",
    "09-10-2025 Dep 8"
]

# =============================================================================
# BASIC LOOP STRUCTURE
# =============================================================================

# Loop through each deposition
for dep_name in DEPOSITIONS:
    print(f"\n{'='*80}")
    print(f"Processing: {dep_name}")
    print(f"{'='*80}")

    # Build the path to this deposition's XY Data folder
    dep_folder = os.path.join(BASE_DIR, dep_name)
    xy_data_folder = os.path.join(dep_folder, "XY Data")

    # Check if folder exists
    if not os.path.exists(xy_data_folder):
        print(f"  WARNING: XY Data folder not found in {dep_name}")
        continue  # Skip to next deposition

    # Change to the XY Data folder
    os.chdir(xy_data_folder)

    # Get all .xy files in this folder
    files = sorted(glob.glob("*.xy"))

    if len(files) == 0:
        print(f"  WARNING: No .xy files found in {dep_name}")
        continue  # Skip to next deposition

    print(f"  Found {len(files)} XRD data files")

    # =========================================================================
    # YOUR PROCESSING CODE GOES HERE
    # =========================================================================

    # Example: Process each file in this deposition
    for file in files:
        # Your code to read and process each file
        # data = np.loadtxt(file)
        # ... your processing ...
        pass

    # Example: Create plots for this deposition
    # plt.figure()
    # ... your plotting code ...
    # plt.title(f"{dep_name}: Your Plot Title")
    # plt.show()

    print(f"  Completed processing {dep_name}")

print("\n" + "="*80)
print("All depositions processed!")
print("="*80)


# =============================================================================
# EXAMPLE: SPECIFIC USE CASE - Distance to Target Analysis
# =============================================================================

# First, store results from all depositions
all_deposition_results = {}

for dep_name in DEPOSITIONS:
    dep_folder = os.path.join(BASE_DIR, dep_name)
    xy_data_folder = os.path.join(dep_folder, "XY Data")

    if not os.path.exists(xy_data_folder):
        continue

    os.chdir(xy_data_folder)
    files = sorted(glob.glob("*.xy"))

    if len(files) == 0:
        continue

    # Process files and store results
    # ... your processing code ...

    # Store in dictionary with deposition name as key
    all_deposition_results[dep_name] = {
        'x_coordinates': [],  # Your data here
        'y_coordinates': [],  # Your data here
        'fwhm': [],          # Your data here
        # ... etc
    }

# Then, loop through results to create plots
for dep_name in DEPOSITIONS:
    if dep_name not in all_deposition_results:
        continue

    # Get the data for this deposition
    data = all_deposition_results[dep_name]

    # Create your plots using this data
    # plt.figure()
    # plt.plot(data['x_coordinates'], data['fwhm'])
    # plt.title(f"{dep_name}: FWHM")
    # plt.show()
