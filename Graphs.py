import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import glob

directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Results'
os.chdir(directory)
data = pd.read_excel(r'Results for Katerini 2.xlsx')
print(data)
print(data.columns)

Old_Down_Pert = data['Old Down Pert'].to_list()
Old_Up_Pert = data['Old Up Pert'].to_list()
Young_Down_Pert = data['Young Down Pert'].to_list()
Young_Up_Pert = data['Young Up Pert'].to_list()
data = [Old_Down_Pert, Old_Up_Pert, Young_Down_Pert, Young_Up_Pert]

down = 5.6
up = 2.78
name = 'Μαυρίδης Αθανάσιος'

# plt.boxplot(data, labels=['Old Down Pert', 'Old Up Pert', 'Young Down Pert', 'Young Up Pert'])
# plt.show()
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size for better visibility

# Plot box plot
bp = ax.boxplot(
    data,
    tick_labels=['Ηλικιωμένοι\nΔιαταραχή προς τα κάτω',
            'Ηλικιωμένοι\nΔιαταραχή προς τα πάνω',
            'Νέοι\nΔιαταραχή προς τα κάτω',
            'Νέοι\nΔιαταραχή προς τα πάνω'],
    patch_artist=True,  # Allows customizing box colors
    boxprops=dict(facecolor='lightblue', color='blue', linewidth=1.5),
    whiskerprops=dict(color='blue', linewidth=1.5),
    capprops=dict(color='blue', linewidth=1.5),
    medianprops=dict(color='lightblue', linewidth=0.1),
    flierprops=dict(marker='o', color='purple', markersize=6, alpha=0.5),
)

plt.xticks(rotation=45, fontsize=12, ha='center')  # Rotate and align labels to the right


# Add an asterisk at y=4 on the first box
ax.text(
    x=1,  # Position corresponding to the first box
    y=down - 0.2,  # y-coordinate
    s="***",  # Asterisk
    fontsize=25,  # Font size
    color="red",  # Color of the asterisk
    ha="center"  # Horizontal alignment
)

# Add an asterisk at y=4 on the first box
ax.text(
    x=2,  # Position corresponding to the first box
    y=up - 0.2,  # y-coordinate
    s="***",  # Asterisk
    fontsize=25,  # Font size
    color="red",  # Color of the asterisk
    ha="center"  # Horizontal alignment
)


# Add a title and labels
ax.set_title(f'{name} με κόκκινους αστερίσκους\nΧρόνος προς τα κάτω = {down}\nΧρόνος προς τα πάνω = {up}', fontsize=16, fontweight='bold')
ax.set_ylabel('Χρόνος απόκρισης', fontsize=14)

# Customize grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Customize tick labels
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add background color
ax.set_facecolor('whitesmoke')

plt.tight_layout()
plt.show()