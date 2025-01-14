#VishnuthirthaSandurHuliraj Code For Processing the Spectroscopy Data obtained for different Temperatures.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, savgol_filter

file_path = "30.txt"
with open(file_path, 'r') as file:
    data = file.readlines()

# Find where the spectral data starts
start_index = data.index(">>>>>Begin Spectral Data<<<<<\n") + 1
spectral_data = data[start_index:]

df = pd.DataFrame([line.strip().replace(',', '.').split('\t') for line in spectral_data], columns=['Wavelength', 'Intensity'])
df = df.astype(float)  # Converting strings to floats
wavelength = df['Wavelength']
intensity = df['Intensity']

ranges_to_exclude = [
    (295, 300),
    (844, 846),
   (980, 1000)
]

mask = np.ones(len(wavelength), dtype=bool)
for r in ranges_to_exclude:
    mask &= ~((wavelength >= r[0]) & (wavelength <= r[1]))

filtered_wavelength = wavelength[mask]
filtered_intensity = intensity[mask]
smoothed_intensity = savgol_filter(intensity, window_length= 7, polyorder=1)

# Detection of peaks
peaks, properties = find_peaks(
    smoothed_intensity,
    prominence = 0,
    width= 3,
    height=(65, 130)
)
plt.figure(figsize=(10, 6))
plt.plot(filtered_wavelength, filtered_intensity, label='Raw Data')
plt.scatter(wavelength[peaks], intensity[peaks], color='red', label='Detected Peaks', zorder=3)
plt.title('Spectroscopy Data at Temperature 35°')
plt.xlabel('Wavelength (in nm)')
plt.ylabel('Intensity')
plt.legend()
plt.grid(True)
plt.show()
valid_peak_data = pd.DataFrame({
    "Wavelength": wavelength.iloc[peaks].values,
    "Intensity": intensity.iloc[peaks].values
})
print("Valid Detected Peaks:")
print(valid_peak_data)



