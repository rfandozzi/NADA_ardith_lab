import os
import matplotlib.pyplot as plt
import spectrochempy as scp

# Define the path to the main folder
main_folder = "/Users/burtmacklinslaptop/onedrive/lab_etc/NH3H2O"

# Collect all .spa file paths
spa_files = []
for root, _, files in os.walk(main_folder):
    for file in files:
        if file.endswith(".spa"):
            spa_files.append(os.path.join(root, file))

# Initialize plot
plt.figure(figsize=(12, 6))

# Process each file
for file in spa_files:
    try:
        dataset = scp.read(file)
        print(f"Loaded: {file}")
        x = dataset.x.to_numpy()
        y = dataset.y.to_numpy()

        # Handle case where y is shape (1, N) but x is (N,)
        if y.ndim == 2 and y.shape[0] == 1:
            y = y.flatten()

        if x.shape != y.shape:
            print(f"Skipping due to shape mismatch: x={x.shape}, y={y.shape}")
            continue

        # Plot the spectrum
        plt.plot(x, y, alpha=0.3)

    except Exception as e:
        print(f"Error reading {file}: {e}")

# Label and save the plot
plt.xlabel("Wavenumber (cm⁻¹)")
plt.ylabel("Intensity")
plt.title("Overlay of NH₃·H₂O Spectra")
plt.tight_layout()
plt.savefig("all_spectra_overlay.png", dpi=300)
plt.show()
