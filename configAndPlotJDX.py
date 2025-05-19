from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
import io

#ignore the name solar and replace, just copied this from some template code too lazy to change it
solar_df = pd.read_csv('12125-02-9-IR_raw.csv.csv', encoding='ISO-8859-1', header=None)
solar_df.head()
# Keep only the relevant column
data_lines = solar_df[0].dropna().astype(str).tolist()



yfactor = 5.566457e-10 #double check
deltax = -0.96450084 #double check

x_vals = []
y_vals = []

# Parse each line
for line in data_lines:
    parts = re.split(r'\+|\s+', line.strip())
    if len(parts) < 2:
        continue
    try:
        x_start = float(parts[0])
        y_raw = [int(p) for p in parts[1:] if p]
        for i, y in enumerate(y_raw):
            x = x_start + i * deltax
            x_vals.append(x)
            y_vals.append(y * yfactor)
    except ValueError:
        continue  # skip lines that don't parse

# Convert to numpy arrays (if not already)
x_vals = np.array(x_vals)
y_vals = np.array(y_vals)

# Sort by X (wavenumber, descending)
sorted_indices = np.argsort(x_vals)[::-1]
x_vals = x_vals[sorted_indices]
y_vals = y_vals[sorted_indices]

# Now plot
plt.figure(figsize=(12, 6))
plt.plot(x_vals, y_vals)
plt.xlabel("Wavenumber (cm⁻¹)")
plt.ylabel("Reflectance")
plt.title("Ammonium Chloride IR Spectrum")
plt.grid(True)
plt.tight_layout()
plt.show()