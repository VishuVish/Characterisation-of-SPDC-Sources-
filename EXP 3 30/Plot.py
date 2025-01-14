import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the Excel file
file_path = 'Aye.xlsx'  # Path to the uploaded file
data = pd.read_excel(file_path)

# Inspect the columns to identify relevant data
print(data.columns)

# Assuming the columns are named 'Angle', 'Heralding Efficiency (Idler)', and 'Heralding Efficiency (Signal)'
angles = data['HWP Angle (in Degrees)']  # Replace with the actual column name for angle
idler_efficiency = data['Heralding Efficiency for Idler']  # Replace with the actual column name
signal_efficiency = data['Heralding Efficiency for Signal']  # Replace with the actual column name

# Define the custom order of angles for plotting
custom_order = [330, 340, 350, 0, 10, 20, 30, 40]  # Your hand-drawn order
angle_mapping = {val: idx for idx, val in enumerate(custom_order)}  # Map for sorting
sorted_indices = angles.map(angle_mapping)  # Sort angles based on custom order

# Sort data based on the custom order
angles = angles.iloc[sorted_indices.argsort()]
idler_eff = idler_efficiency.iloc[sorted_indices.argsort()]
signal_eff = signal_efficiency.iloc[sorted_indices.argsort()]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(angles, idler_efficiency, label='Heralding Efficiency (Idler)', marker='o')
plt.plot(angles, signal_efficiency, label='Heralding Efficiency (Signal)', marker='s')

plt.xticks(custom_order, [f"{angle}°" for angle in custom_order])
plt.title('Heralding Efficiencies as a Function of Angle Values')
plt.xlabel('Angle')
plt.ylabel('Heralding Efficiency')
plt.legend()
plt.grid(True)
plt.show()
