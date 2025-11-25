import json
import os

# Read the template notebook
template_path = r"C:\Dilan\Study\Master Thesis\Characterization\XRD\30-09-2025 Dep 1\Plots_and_Graphs_Dep_1.ipynb"
output_path = r"C:\Dilan\Study\Master Thesis\Characterization\XRD\Plots_and_Graphs_All_Depositions.ipynb"

with open(template_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find the first code cell and modify it to add the deposition loop setup
# We'll insert new cells at the beginning

new_cells = []

# Title
new_cells.append({
    'cell_type': 'markdown',
    'metadata': {},
    'source': ['# XRD Analysis for All Depositions\n', '\n', 'This notebook processes XRD data from multiple deposition folders automatically.']
})

# Setup cell with deposition list
setup_code = '''import pandas as pd
import numpy as np
import os, glob, re, csv
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, peak_widths, savgol_filter
from scipy.optimize import curve_fit
from matplotlib.tri import Triangulation
from matplotlib.colors import LinearSegmentedColormap, PowerNorm, Normalize
from pathlib import Path
from scipy.interpolate import griddata

# Define all deposition folders to process
BASE_DIR = r"C:\\Dilan\\Study\\Master Thesis\\Characterization\\XRD"

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

print(f"Base directory: {BASE_DIR}")
print(f"\\nDepositions to process: {len(DEPOSITIONS)}")
for dep in DEPOSITIONS:
    print(f"  - {dep}")'''

new_cells.append({
    'cell_type': 'code',
    'execution_count': None,
    'metadata': {},
    'outputs': [],
    'source': setup_code.split('\n')
})

# Keep only cells we want from the original, but modify them to work with loops
# We'll rebuild the notebook structure

nb['cells'] = new_cells

# Save
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print(f"Created notebook at: {output_path}")
print("Now you need to open it in Jupyter and manually add the processing cells.")
print("The template has been created with the basic structure.")
