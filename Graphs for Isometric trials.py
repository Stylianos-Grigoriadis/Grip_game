import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import glob
import matplotlib.patches as mpatches
import matplotlib.lines as mlines


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 16

directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Results\Isometric'
os.chdir(directory)
old_data = pd.read_excel(r'results Isometrics all.xlsx', sheet_name='Old')
young_data = pd.read_excel(r'results Isometrics all.xlsx', sheet_name='Young')

print(old_data)
print(young_data)
print(old_data.columns)

old_SaEn_80_Average = old_data['SaEn_80_Average'].to_list()
old_SaEn_60_Average = old_data['SaEn_60_Average'].to_list()
old_SaEn_40_Average = old_data['SaEn_40_Average'].to_list()
old_SaEn_20_Average = old_data['SaEn_20_Average'].to_list()
old_SaEn_05_Average = old_data['SaEn_05_Average'].to_list()

young_SaEn_80_Average = young_data['SaEn_80_Average'].to_list()
young_SaEn_60_Average = young_data['SaEn_60_Average'].to_list()
young_SaEn_40_Average = young_data['SaEn_40_Average'].to_list()
young_SaEn_20_Average = young_data['SaEn_20_Average'].to_list()
young_SaEn_05_Average = young_data['SaEn_05_Average'].to_list()

old_sd_80_Average = old_data['sd_80_Average'].to_list()
old_sd_60_Average = old_data['sd_60_Average'].to_list()
old_sd_40_Average = old_data['sd_40_Average'].to_list()
old_sd_20_Average = old_data['sd_20_Average'].to_list()
old_sd_05_Average = old_data['sd_05_Average'].to_list()

young_sd_80_Average = young_data['sd_80_Average'].to_list()
young_sd_60_Average = young_data['sd_60_Average'].to_list()
young_sd_40_Average = young_data['sd_40_Average'].to_list()
young_sd_20_Average = young_data['sd_20_Average'].to_list()
young_sd_05_Average = young_data['sd_05_Average'].to_list()

old_CoV_80_Average = old_data['CoV_80_Average'].to_list()
old_CoV_60_Average = old_data['CoV_60_Average'].to_list()
old_CoV_40_Average = old_data['CoV_40_Average'].to_list()
old_CoV_20_Average = old_data['CoV_20_Average'].to_list()
old_CoV_05_Average = old_data['CoV_05_Average'].to_list()

young_CoV_80_Average = young_data['CoV_80_Average'].to_list()
young_CoV_60_Average = young_data['CoV_60_Average'].to_list()
young_CoV_40_Average = young_data['CoV_40_Average'].to_list()
young_CoV_20_Average = young_data['CoV_20_Average'].to_list()
young_CoV_05_Average = young_data['CoV_05_Average'].to_list()

old_DFA_80_Average = old_data['DFA_80_Average'].to_list()
old_DFA_60_Average = old_data['DFA_60_Average'].to_list()
old_DFA_40_Average = old_data['DFA_40_Average'].to_list()
old_DFA_20_Average = old_data['DFA_20_Average'].to_list()
old_DFA_05_Average = old_data['DFA_05_Average'].to_list()

young_DFA_80_Average = young_data['DFA_80_Average'].to_list()
young_DFA_60_Average = young_data['DFA_60_Average'].to_list()
young_DFA_40_Average = young_data['DFA_40_Average'].to_list()
young_DFA_20_Average = young_data['DFA_20_Average'].to_list()
young_DFA_05_Average = young_data['DFA_05_Average'].to_list()

old_SaEn = [old_SaEn_05_Average, old_SaEn_20_Average, old_SaEn_40_Average, old_SaEn_60_Average, old_SaEn_80_Average]
young_SaEn = [young_SaEn_05_Average, young_SaEn_20_Average, young_SaEn_40_Average, young_SaEn_60_Average, young_SaEn_80_Average]

old_sd = [old_sd_05_Average, old_sd_20_Average, old_sd_40_Average, old_sd_60_Average, old_sd_80_Average]
young_sd = [young_sd_05_Average, young_sd_20_Average, young_sd_40_Average, young_sd_60_Average, young_sd_80_Average]

old_CoV = [old_CoV_05_Average, old_CoV_20_Average, old_CoV_40_Average, old_CoV_60_Average, old_CoV_80_Average]
young_CoV = [young_CoV_05_Average, young_CoV_20_Average, young_CoV_40_Average, young_CoV_60_Average, young_CoV_80_Average]

old_DFA = [old_DFA_05_Average, old_DFA_20_Average, old_DFA_40_Average, old_DFA_60_Average, old_DFA_80_Average]
young_DFA = [young_DFA_05_Average, young_DFA_20_Average, young_DFA_40_Average, young_DFA_60_Average, young_DFA_80_Average]



# Graph for SaEn

fig, ax = plt.subplots(figsize=(8, 6))
young_positions = [1, 4, 7, 10, 13]
plus_factor = 0.6
old_positions = [young_positions[0]+plus_factor, young_positions[1]+plus_factor, young_positions[2]+plus_factor, young_positions[3]+plus_factor, young_positions[4]+plus_factor]
# Create the box plot
ax.boxplot(young_SaEn,
           positions=young_positions,
           patch_artist=True,
           showmeans=True,
           showfliers=False,
           boxprops=dict(facecolor='lightblue', color='blue'),
           meanprops=dict(marker='o', markeredgecolor='blue', markerfacecolor='blue'),
           medianprops=dict(color='none'))

ax.boxplot(old_SaEn,
           positions=old_positions,
           patch_artist=True,
           showmeans=True,
           showfliers=False,
           boxprops=dict(facecolor='lightcoral', color='red'),
           meanprops=dict(marker='o', markeredgecolor='red', markerfacecolor='red'),
           medianprops=dict(color='none'))

# Calculate means for each group
young_means = [np.mean(data) for data in young_SaEn]
old_means = [np.mean(data) for data in old_SaEn]

# Plot dashed lines connecting the mean markers
ax.plot(young_positions, young_means, color='blue', linestyle='--')
ax.plot(old_positions, old_means, color='red', linestyle='--')


# Manually create legend elements
legend_elements = [
    mpatches.Patch(color='lightblue', label='Young'),
    mlines.Line2D([], [], color='blue', marker='o', markersize=8, label='Young Average', linestyle='None'),
    mpatches.Patch(color='lightcoral', label='Old'),
    mlines.Line2D([], [], color='red', marker='o', markersize=8, label='Old Average', linestyle='None')
]

# Add the legend to the plot
ax.legend(handles=legend_elements, loc='upper right', frameon=False)

# Customize the plot
ax.set_title(f'Sample Entropy Curve between Young (n={len(young_SaEn_80_Average)}) and Old (n={len(old_SaEn_80_Average)}) adults')
ax.set_xticks([(x + y) / 2 for x, y in zip(young_positions, old_positions)])
ax.set_xticklabels(['5%', '20%', '40%', '60%', '80%'])
ax.set_ylabel('Sample Entropy')
ax.set_xlabel('Percentage of MVC')

# Display the plot
plt.show()



# Graph for SD

fig, ax = plt.subplots(figsize=(8, 6))
young_positions = [1, 4, 7, 10, 13]
plus_factor = 0.6
old_positions = [young_positions[0]+plus_factor, young_positions[1]+plus_factor, young_positions[2]+plus_factor, young_positions[3]+plus_factor, young_positions[4]+plus_factor]
# Create the box plot
ax.boxplot(young_sd,
           positions=young_positions,
           patch_artist=True,
           showmeans=True,
           showfliers=False,
           boxprops=dict(facecolor='lightblue', color='blue'),
           meanprops=dict(marker='o', markeredgecolor='blue', markerfacecolor='blue'),
           medianprops=dict(color='none'))

ax.boxplot(old_sd,
           positions=old_positions,
           patch_artist=True,
           showmeans=True,
           showfliers=False,
           boxprops=dict(facecolor='lightcoral', color='red'),
           meanprops=dict(marker='o', markeredgecolor='red', markerfacecolor='red'),
           medianprops=dict(color='none'))

# Calculate means for each group
young_means = [np.mean(data) for data in young_sd]
old_means = [np.mean(data) for data in old_sd]

# Plot dashed lines connecting the mean markers
ax.plot(young_positions, young_means, color='blue', linestyle='--')
ax.plot(old_positions, old_means, color='red', linestyle='--')


# Manually create legend elements
legend_elements = [
    mpatches.Patch(color='lightblue', label='Young'),
    mlines.Line2D([], [], color='blue', marker='o', markersize=8, label='Young Average', linestyle='None'),
    mpatches.Patch(color='lightcoral', label='Old'),
    mlines.Line2D([], [], color='red', marker='o', markersize=8, label='Old Average', linestyle='None')
]

# Add the legend to the plot
ax.legend(handles=legend_elements, loc='upper right', frameon=False)

# Customize the plot
ax.set_title(f'Standard Deviation curve between Young (n={len(young_sd_80_Average)}) and Old (n={len(old_sd_80_Average)}) adults')
ax.set_xticks([(x + y) / 2 for x, y in zip(young_positions, old_positions)])
ax.set_xticklabels(['5%', '20%', '40%', '60%', '80%'])
ax.set_ylabel('Standard Deviation')
ax.set_xlabel('Percentage of MVC')

# Display the plot
plt.show()

# Graph for CoV

fig, ax = plt.subplots(figsize=(8, 6))
young_positions = [1, 4, 7, 10, 13]
plus_factor = 0.6
old_positions = [young_positions[0]+plus_factor, young_positions[1]+plus_factor, young_positions[2]+plus_factor, young_positions[3]+plus_factor, young_positions[4]+plus_factor]
# Create the box plot
ax.boxplot(young_CoV,
           positions=young_positions,
           patch_artist=True,
           showmeans=True,
           showfliers=False,
           boxprops=dict(facecolor='lightblue', color='blue'),
           meanprops=dict(marker='o', markeredgecolor='blue', markerfacecolor='blue'),
           medianprops=dict(color='none'))

ax.boxplot(old_CoV,
           positions=old_positions,
           patch_artist=True,
           showmeans=True,
           showfliers=False,
           boxprops=dict(facecolor='lightcoral', color='red'),
           meanprops=dict(marker='o', markeredgecolor='red', markerfacecolor='red'),
           medianprops=dict(color='none'))

# Calculate means for each group
young_means = [np.mean(data) for data in young_CoV]
old_means = [np.mean(data) for data in old_CoV]

# Plot dashed lines connecting the mean markers
ax.plot(young_positions, young_means, color='blue', linestyle='--')
ax.plot(old_positions, old_means, color='red', linestyle='--')


# Manually create legend elements
legend_elements = [
    mpatches.Patch(color='lightblue', label='Young'),
    mlines.Line2D([], [], color='blue', marker='o', markersize=8, label='Young Average', linestyle='None'),
    mpatches.Patch(color='lightcoral', label='Old'),
    mlines.Line2D([], [], color='red', marker='o', markersize=8, label='Old Average', linestyle='None')
]

# Add the legend to the plot
ax.legend(handles=legend_elements, loc='upper right', frameon=False)

# Customize the plot
ax.set_title(f'CoV curve between Young (n={len(young_CoV_80_Average)}) and Old (n={len(old_CoV_80_Average)}) adults')
ax.set_xticks([(x + y) / 2 for x, y in zip(young_positions, old_positions)])
ax.set_xticklabels(['5%', '20%', '40%', '60%', '80%'])
ax.set_ylabel('Coefficient of Variation')
ax.set_xlabel('Percentage of MVC')

# Display the plot
plt.show()

# Graph for DFA

fig, ax = plt.subplots(figsize=(8, 6))
young_positions = [1, 4, 7, 10, 13]
plus_factor = 0.6
old_positions = [young_positions[0]+plus_factor, young_positions[1]+plus_factor, young_positions[2]+plus_factor, young_positions[3]+plus_factor, young_positions[4]+plus_factor]
# Create the box plot
ax.boxplot(young_DFA,
           positions=young_positions,
           patch_artist=True,
           showmeans=True,
           showfliers=False,
           boxprops=dict(facecolor='lightblue', color='blue'),
           meanprops=dict(marker='o', markeredgecolor='blue', markerfacecolor='blue'),
           medianprops=dict(color='none'))

ax.boxplot(old_DFA,
           positions=old_positions,
           patch_artist=True,
           showmeans=True,
           showfliers=False,
           boxprops=dict(facecolor='lightcoral', color='red'),
           meanprops=dict(marker='o', markeredgecolor='red', markerfacecolor='red'),
           medianprops=dict(color='none'))

# Calculate means for each group
young_means = [np.mean(data) for data in young_DFA]
old_means = [np.mean(data) for data in old_DFA]

# Plot dashed lines connecting the mean markers
ax.plot(young_positions, young_means, color='blue', linestyle='--')
ax.plot(old_positions, old_means, color='red', linestyle='--')


# Manually create legend elements
legend_elements = [
    mpatches.Patch(color='lightblue', label='Young'),
    mlines.Line2D([], [], color='blue', marker='o', markersize=8, label='Young Average', linestyle='None'),
    mpatches.Patch(color='lightcoral', label='Old'),
    mlines.Line2D([], [], color='red', marker='o', markersize=8, label='Old Average', linestyle='None')
]

# Add the legend to the plot
ax.legend(handles=legend_elements, loc='upper right', frameon=False)

# Customize the plot
ax.set_title(f'Exponent α curve between Young (n={len(young_DFA_80_Average)}) and Old (n={len(old_DFA_80_Average)}) adults')
ax.set_xticks([(x + y) / 2 for x, y in zip(young_positions, old_positions)])
ax.set_xticklabels(['5%', '20%', '40%', '60%', '80%'])
ax.set_ylabel('α Exponent')
ax.set_xlabel('Percentage of MVC')

# Display the plot
plt.show()

