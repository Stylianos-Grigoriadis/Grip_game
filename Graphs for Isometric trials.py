import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import glob
import matplotlib.patches as mpatches
import matplotlib.lines as mlines


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 16

directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\Education\Classes\Advanced Statistics\Final project'
os.chdir(directory)
results = pd.read_excel(r'Results all Lowpass 50Hz only best iso trials for graphs.xlsx')
print(results['sd_80'])

SaEn_80_Old = results[results['ID_group'] == 'Old']['SaEn_80'].to_numpy()
SaEn_60_Old = results[results['ID_group'] == 'Old']['SaEn_60'].to_numpy()
SaEn_40_Old = results[results['ID_group'] == 'Old']['SaEn_40'].to_numpy()
SaEn_20_Old = results[results['ID_group'] == 'Old']['SaEn_20'].to_numpy()
SaEn_05_Old = results[results['ID_group'] == 'Old']['SaEn_05'].to_numpy()

SaEn_80_Young = results[results['ID_group'] == 'Young']['SaEn_80'].to_numpy()
SaEn_60_Young = results[results['ID_group'] == 'Young']['SaEn_60'].to_numpy()
SaEn_40_Young = results[results['ID_group'] == 'Young']['SaEn_40'].to_numpy()
SaEn_20_Young = results[results['ID_group'] == 'Young']['SaEn_20'].to_numpy()
SaEn_05_Young = results[results['ID_group'] == 'Young']['SaEn_05'].to_numpy()

sd_80_Old = results[results['ID_group'] == 'Old']['sd_80'].dropna().to_numpy()
sd_60_Old = results[results['ID_group'] == 'Old']['sd_60'].dropna().to_numpy()
sd_40_Old = results[results['ID_group'] == 'Old']['sd_40'].to_numpy()
sd_20_Old = results[results['ID_group'] == 'Old']['sd_20'].to_numpy()
sd_05_Old = results[results['ID_group'] == 'Old']['sd_05'].to_numpy()

sd_80_Young = results[results['ID_group'] == 'Young']['sd_80'].to_numpy()
sd_60_Young = results[results['ID_group'] == 'Young']['sd_60'].to_numpy()
sd_40_Young = results[results['ID_group'] == 'Young']['sd_40'].to_numpy()
sd_20_Young = results[results['ID_group'] == 'Young']['sd_20'].to_numpy()
sd_05_Young = results[results['ID_group'] == 'Young']['sd_05'].to_numpy()

Pert_down_Old = results[results['ID_group'] == 'Old']['Adaptation_down_min'].to_numpy()
Pert_up_Old = results[results['ID_group'] == 'Old']['Adaptation_up_min'].to_numpy()

Pert_down_Young = results[results['ID_group'] == 'Young']['Adaptation_down_min'].to_numpy()
Pert_up_Young = results[results['ID_group'] == 'Young']['Adaptation_up_min'].to_numpy()





old_SaEn = [SaEn_05_Old, SaEn_20_Old, SaEn_40_Old, SaEn_60_Old, SaEn_80_Old]
young_SaEn = [SaEn_05_Young, SaEn_20_Young, SaEn_40_Young, SaEn_60_Young, SaEn_80_Young]

old_sd = [sd_05_Old, sd_20_Old, sd_40_Old, sd_60_Old, sd_80_Old]
young_sd = [sd_05_Young, sd_20_Young, sd_40_Young, sd_60_Young, sd_80_Young]

old_time_of_adaptation = [Pert_down_Old, Pert_up_Old]
young_time_of_adaptation = [Pert_down_Young, Pert_up_Young]




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
# ax.set_title(f'Sample Entropy Curve between Young (n={len(SaEn_80_Young)}) and Old (n={len(SaEn_80_Old)}) adults')
ax.set_title(f'Sample Entropy Curve between Young (n=17) and Old (n=17) adults')
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
# ax.set_title(f'Standard Deviation curve between Young (n={len(SaEn_80_Young)}) and Old (n={len(SaEn_80_Old)}) adults')
ax.set_title(f'Standard Deviation curve between Young (n=17) and Old (n=17) adults')

ax.set_xticks([(x + y) / 2 for x, y in zip(young_positions, old_positions)])
ax.set_xticklabels(['5%', '20%', '40%', '60%', '80%'])
ax.set_ylabel('Standard Deviation')
ax.set_xlabel('Percentage of MVC')

# Display the plot
plt.show()



# Graph for time of adaptation

fig, ax = plt.subplots(figsize=(8, 6))
young_positions = [1, 4]
plus_factor = 0.6
old_positions = [young_positions[0]+plus_factor, young_positions[1]+plus_factor]
# Create the box plot
ax.boxplot(young_time_of_adaptation,
           positions=young_positions,
           patch_artist=True,
           showmeans=True,
           showfliers=False,
           boxprops=dict(facecolor='lightblue', color='blue'),
           meanprops=dict(marker='o', markeredgecolor='blue', markerfacecolor='blue'),
           medianprops=dict(color='none'))

ax.boxplot(old_time_of_adaptation,
           positions=old_positions,
           patch_artist=True,
           showmeans=True,
           showfliers=False,
           boxprops=dict(facecolor='lightcoral', color='red'),
           meanprops=dict(marker='o', markeredgecolor='red', markerfacecolor='red'),
           medianprops=dict(color='none'))

# Calculate means for each group
young_means = [np.mean(data) for data in young_time_of_adaptation]
old_means = [np.mean(data) for data in old_time_of_adaptation]

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
# ax.set_title(f'Time to adapt curve between Young (n={len(SaEn_80_Young)}) and Old (n={len(SaEn_80_Old)}) adults')
ax.set_title(f'Time to adapt curve between Young (n=17) and Old (n=17) adults')

ax.set_xticks([(x + y) / 2 for x, y in zip(young_positions, old_positions)])
ax.set_xticklabels(['Perturbation\ndownwards', 'Perturbation\nupwards'])
ax.set_ylabel('Time to adapt')

# Display the plot
plt.show()