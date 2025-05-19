import pandas as pd
import matplotlib.pyplot as plt

# Replace with the path to your CSV file
file_path = 'Processed_Spectral_Data_copy.csv'

# Read the CSV file (with header)
data = pd.read_csv(file_path)

# Preview the column names
print(data.columns)

# Extract wavenumber and reflectance
wavenumber = data['Wavenumber (cm-1)']
reflectance = data['Reflectance']

# Convert wavenumber (cm⁻¹) to wavelength (µm)
wavelength_microns = 1e4 / wavenumber

# Plot
plt.figure(figsize=(10, 6))
plt.plot(wavelength_microns, reflectance)
plt.xlabel('Wavelength (µm)')
plt.ylabel('Reflectance')
plt.title('Reflectance vs Wavelength')
plt.grid(True)
plt.tight_layout()
plt.show()
