import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import glob
import statistics
import matplotlib.patches as mpatches
import matplotlib.lines as mlines


directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 10\Data\Strength data'
files = glob.glob(os.path.join(directory_path, "*"))
name_young = []
name_old = []
for file in files:
    name = os.path.basename(file)
    if 'Old' in name:
        name_old.append(name)
    elif 'Young' in name:
        name_young.append(name)

sorted_name_young = sorted(name_young, key=lambda x: int(x.split('.')[1]))
sorted_name_old = sorted(name_old, key=lambda x: int(x.split('.')[1]))

young_SaEn_80_list = []
young_SaEn_60_list = []
young_SaEn_40_list = []
young_SaEn_20_list = []
young_SaEn_05_list = []
young_sd_80_list = []
young_sd_60_list = []
young_sd_40_list = []
young_sd_20_list = []
young_sd_05_list = []

old_SaEn_80_list = []
old_SaEn_60_list = []
old_SaEn_40_list = []
old_SaEn_20_list = []
old_SaEn_05_list = []
old_sd_80_list = []
old_sd_60_list = []
old_sd_40_list = []
old_sd_20_list = []
old_sd_05_list = []
for name in sorted_name_young:
    directory_path_young = directory_path
    directory_path_young = directory_path_young + f'\{name}'
    print(directory_path_young)
    os.chdir(directory_path_young)
    results_isometric = pd.read_excel(r'Results Isometric.xlsx')

    young_SaEn_80_list.append(results_isometric['SaEn_Average'][0])
    young_SaEn_60_list.append(results_isometric['SaEn_Average'][1])
    young_SaEn_40_list.append(results_isometric['SaEn_Average'][2])
    young_SaEn_20_list.append(results_isometric['SaEn_Average'][3])
    young_SaEn_05_list.append(results_isometric['SaEn_Average'][4])

    young_sd_80_list.append(results_isometric['std_Average'][0])
    young_sd_60_list.append(results_isometric['std_Average'][1])
    young_sd_40_list.append(results_isometric['std_Average'][2])
    young_sd_20_list.append(results_isometric['std_Average'][3])
    young_sd_05_list.append(results_isometric['std_Average'][4])

for name in sorted_name_old:
    directory_path_old = directory_path
    directory_path_old = directory_path_old + f'\{name}'
    print(directory_path_old)
    os.chdir(directory_path_old)
    results_isometric = pd.read_excel(r'Results Isometric.xlsx')

    old_SaEn_80_list.append(results_isometric['SaEn_Average'][0])
    old_SaEn_60_list.append(results_isometric['SaEn_Average'][1])
    old_SaEn_40_list.append(results_isometric['SaEn_Average'][2])
    old_SaEn_20_list.append(results_isometric['SaEn_Average'][3])
    old_SaEn_05_list.append(results_isometric['SaEn_Average'][4])

    old_sd_80_list.append(results_isometric['std_Average'][0])
    old_sd_60_list.append(results_isometric['std_Average'][1])
    old_sd_40_list.append(results_isometric['std_Average'][2])
    old_sd_20_list.append(results_isometric['std_Average'][3])
    old_sd_05_list.append(results_isometric['std_Average'][4])

young_SaEn_80_average = statistics.mean(young_SaEn_80_list)
young_SaEn_60_average = statistics.mean(young_SaEn_60_list)
young_SaEn_40_average = statistics.mean(young_SaEn_40_list)
young_SaEn_20_average = statistics.mean(young_SaEn_20_list)
young_SaEn_05_average = statistics.mean(young_SaEn_05_list)

young_SaEn_80_sd = statistics.stdev(young_SaEn_80_list)
young_SaEn_60_sd = statistics.stdev(young_SaEn_60_list)
young_SaEn_40_sd = statistics.stdev(young_SaEn_40_list)
young_SaEn_20_sd = statistics.stdev(young_SaEn_20_list)
young_SaEn_05_sd = statistics.stdev(young_SaEn_05_list)

old_SaEn_80_average = statistics.mean(old_SaEn_80_list)
old_SaEn_60_average = statistics.mean(old_SaEn_60_list)
old_SaEn_40_average = statistics.mean(old_SaEn_40_list)
old_SaEn_20_average = statistics.mean(old_SaEn_20_list)
old_SaEn_05_average = statistics.mean(old_SaEn_05_list)

old_SaEn_80_sd = statistics.stdev(old_SaEn_80_list)
old_SaEn_60_sd = statistics.stdev(old_SaEn_60_list)
old_SaEn_40_sd = statistics.stdev(old_SaEn_40_list)
old_SaEn_20_sd = statistics.stdev(old_SaEn_20_list)
old_SaEn_05_sd = statistics.stdev(old_SaEn_05_list)

young_SaEn_list = [young_SaEn_05_list, young_SaEn_20_list, young_SaEn_40_list, young_SaEn_60_list, young_SaEn_80_list]
old_SaEn_list = [old_SaEn_05_list, old_SaEn_20_list, old_SaEn_40_list, old_SaEn_60_list, old_SaEn_80_list]

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 16

fig, ax = plt.subplots(figsize=(8, 6))
young_positions = [1, 4, 7, 10, 13]
plus_factor = 0.6
old_positions = [young_positions[0]+plus_factor, young_positions[1]+plus_factor, young_positions[2]+plus_factor, young_positions[3]+plus_factor, young_positions[4]+plus_factor]
# Create the box plot
ax.boxplot(young_SaEn_list,
           positions=young_positions,
           patch_artist=True,
           showmeans=True,
           showfliers=False,
           boxprops=dict(facecolor='lightblue', color='blue'),
           meanprops=dict(marker='o', markeredgecolor='blue', markerfacecolor='blue'),
           medianprops=dict(color='none'))

ax.boxplot(old_SaEn_list,
           positions=old_positions,
           patch_artist=True,
           showmeans=True,
           showfliers=False,
           boxprops=dict(facecolor='lightcoral', color='red'),
           meanprops=dict(marker='o', markeredgecolor='red', markerfacecolor='red'),
           medianprops=dict(color='none'))

# Calculate means for each group
young_means = [np.mean(data) for data in young_SaEn_list]
old_means = [np.mean(data) for data in old_SaEn_list]

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
ax.set_title(f'Sample Entropy Curve between Young (n={len(young_SaEn_80_list)}) and Old (n={len(old_SaEn_80_list)}) adults')
ax.set_xticks([(x + y) / 2 for x, y in zip(young_positions, old_positions)])
ax.set_xticklabels(['5%', '20%', '40%', '60%', '80%'])
ax.set_ylabel('Sample Entropy')
ax.set_xlabel('Percentage of MVC')

# Display the plot
plt.show()

young_sd_list = [young_sd_05_list, young_sd_20_list, young_sd_40_list, young_sd_60_list, young_sd_80_list]
old_sd_list = [old_sd_05_list, old_sd_20_list, old_sd_40_list, old_sd_60_list, old_sd_80_list]

fig, ax = plt.subplots(figsize=(8, 6))
young_positions = [1, 4, 7, 10, 13]
plus_factor = 0.6
old_positions = [young_positions[0]+plus_factor, young_positions[1]+plus_factor, young_positions[2]+plus_factor, young_positions[3]+plus_factor, young_positions[4]+plus_factor]
# Create the box plot
ax.boxplot(young_sd_list,
           positions=young_positions,
           patch_artist=True,
           showmeans=True,
           showfliers=False,
           boxprops=dict(facecolor='lightblue', color='blue'),
           meanprops=dict(marker='o', markeredgecolor='blue', markerfacecolor='blue'),
           medianprops=dict(color='none'))

ax.boxplot(old_sd_list,
           positions=old_positions,
           patch_artist=True,
           showmeans=True,
           showfliers=False,
           boxprops=dict(facecolor='lightcoral', color='red'),
           meanprops=dict(marker='o', markeredgecolor='red', markerfacecolor='red'),
           medianprops=dict(color='none'))

# Calculate means for each group
young_means = [np.mean(data) for data in young_sd_list]
old_means = [np.mean(data) for data in old_sd_list]

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
ax.set_title(f'Standard Deviation Curve between Young (n={len(young_sd_80_list)}) and Old (n={len(old_sd_80_list)}) adults')
ax.set_xticks([(x + y) / 2 for x, y in zip(young_positions, old_positions)])
ax.set_xticklabels(['5%', '20%', '40%', '60%', '80%'])
ax.set_ylabel('Standard Deviation')
ax.set_xlabel('Percentage of MVC')

# Display the plot
plt.show()

# for file in files:
#     directory_path = file
#     os.chdir(file)
#     inside_files = glob.glob(os.path.join(directory_path, "*"))
#     participant = os.path.basename(directory_path)
#
#     Isometric_80_T1_75Hz = pd.read_csv(r'Isometric_80_T1.csv', skiprows=2)
#     Isometric_80_T2_75Hz = pd.read_csv(r'Isometric_80_T2.csv', skiprows=2)
#     Isometric_60_T1_75Hz = pd.read_csv(r'Isometric_60_T1.csv', skiprows=2)
#     Isometric_60_T2_75Hz = pd.read_csv(r'Isometric_60_T2.csv', skiprows=2)
#     Isometric_40_T1_75Hz = pd.read_csv(r'Isometric_40_T1.csv', skiprows=2)
#     Isometric_40_T2_75Hz = pd.read_csv(r'Isometric_40_T2.csv', skiprows=2)
#     Isometric_20_T1_75Hz = pd.read_csv(r'Isometric_20_T1.csv', skiprows=2)
#     Isometric_20_T2_75Hz = pd.read_csv(r'Isometric_20_T2.csv', skiprows=2)
#     Isometric_05_T1_75Hz = pd.read_csv(r'Isometric_05_T1.csv', skiprows=2)
#     Isometric_05_T2_75Hz = pd.read_csv(r'Isometric_05_T2.csv', skiprows=2)
#
#     index = pd.read_excel('index.xlsx')
#
#     iso_80_T1_75Hz = Isometric_80_T1_75Hz['Performance'][index['T1_iso_80_75Hz'][0]:index['T1_iso_80_75Hz'][1]].to_numpy()
#     iso_80_T2_75Hz = Isometric_80_T2_75Hz['Performance'][index['T2_iso_80_75Hz'][0]:index['T2_iso_80_75Hz'][1]].to_numpy()
#     iso_60_T1_75Hz = Isometric_60_T1_75Hz['Performance'][index['T1_iso_60_75Hz'][0]:index['T1_iso_60_75Hz'][1]].to_numpy()
#     iso_60_T2_75Hz = Isometric_60_T2_75Hz['Performance'][index['T2_iso_60_75Hz'][0]:index['T2_iso_60_75Hz'][1]].to_numpy()
#     iso_40_T1_75Hz = Isometric_40_T1_75Hz['Performance'][index['T1_iso_40_75Hz'][0]:index['T1_iso_40_75Hz'][1]].to_numpy()
#     iso_40_T2_75Hz = Isometric_40_T2_75Hz['Performance'][index['T2_iso_40_75Hz'][0]:index['T2_iso_40_75Hz'][1]].to_numpy()
#     iso_20_T1_75Hz = Isometric_20_T1_75Hz['Performance'][index['T1_iso_20_75Hz'][0]:index['T1_iso_20_75Hz'][1]].to_numpy()
#     iso_20_T2_75Hz = Isometric_20_T2_75Hz['Performance'][index['T2_iso_20_75Hz'][0]:index['T2_iso_20_75Hz'][1]].to_numpy()
#     iso_05_T1_75Hz = Isometric_05_T1_75Hz['Performance'][index['T1_iso_05_75Hz'][0]:index['T1_iso_05_75Hz'][1]].to_numpy()
#     iso_05_T2_75Hz = Isometric_05_T2_75Hz['Performance'][index['T2_iso_05_75Hz'][0]:index['T2_iso_05_75Hz'][1]].to_numpy()
#
#
#     def index_to_500(array):
#         excess_length_array = len(array) - 500
#         if excess_length_array > 0:
#             remove_each_side = excess_length_array // 2
#             array = array[remove_each_side: len(array) - remove_each_side]
#         elif excess_length_array == 0:
#             pass
#         else:
#             raise ValueError("Length is less than 500 points")
#         return array
#
#
#     iso_80_T1_75Hz = index_to_500(iso_80_T1_75Hz)
#     iso_80_T2_75Hz = index_to_500(iso_80_T2_75Hz)
#     iso_60_T1_75Hz = index_to_500(iso_60_T1_75Hz)
#     iso_60_T2_75Hz = index_to_500(iso_60_T2_75Hz)
#     iso_40_T1_75Hz = index_to_500(iso_40_T1_75Hz)
#     iso_40_T2_75Hz = index_to_500(iso_40_T2_75Hz)
#     iso_20_T1_75Hz = index_to_500(iso_20_T1_75Hz)
#     iso_20_T2_75Hz = index_to_500(iso_20_T2_75Hz)
#     iso_05_T1_75Hz = index_to_500(iso_05_T1_75Hz)
#     iso_05_T2_75Hz = index_to_500(iso_05_T2_75Hz)
#
#     print(f'iso_80_T1_75Hz: {len(iso_80_T1_75Hz)}')
#     print(f'iso_80_T1_75Hz: {len(iso_80_T1_75Hz)}')
#     print(f'iso_60_T1_75Hz: {len(iso_60_T1_75Hz)}')
#     print(f'iso_60_T1_75Hz: {len(iso_60_T1_75Hz)}')
#     print(f'iso_40_T1_75Hz: {len(iso_40_T1_75Hz)}')
#     print(f'iso_40_T1_75Hz: {len(iso_40_T1_75Hz)}')
#     print(f'iso_20_T1_75Hz: {len(iso_20_T1_75Hz)}')
#     print(f'iso_20_T1_75Hz: {len(iso_20_T1_75Hz)}')
#     print(f'iso_05_T1_75Hz: {len(iso_05_T1_75Hz)}')
#     print(f'iso_05_T1_75Hz: {len(iso_05_T1_75Hz)}')
#
#     plt.plot(iso_80_T1_75Hz, label='iso_80_T1')
#     plt.plot(iso_80_T2_75Hz, label='iso_80_T2')
#     plt.plot(iso_60_T1_75Hz, label='iso_60_T1')
#     plt.plot(iso_60_T2_75Hz, label='iso_60_T2')
#     plt.plot(iso_40_T1_75Hz, label='iso_40_T1')
#     plt.plot(iso_40_T2_75Hz, label='iso_40_T2')
#     plt.plot(iso_20_T1_75Hz, label='iso_20_T1')
#     plt.plot(iso_20_T2_75Hz, label='iso_20_T2')
#     plt.plot(iso_05_T1_75Hz, label='iso_05_T1')
#     plt.plot(iso_05_T2_75Hz, label='iso_05_T2')
#     plt.title(participant)
#     plt.legend()
#     plt.show()
#
#     std_iso_80_T1_75Hz = np.std(iso_80_T1_75Hz)
#     std_iso_80_T2_75Hz = np.std(iso_80_T2_75Hz)
#     std_iso_60_T1_75Hz = np.std(iso_60_T1_75Hz)
#     std_iso_60_T2_75Hz = np.std(iso_60_T2_75Hz)
#     std_iso_40_T1_75Hz = np.std(iso_40_T1_75Hz)
#     std_iso_40_T2_75Hz = np.std(iso_40_T2_75Hz)
#     std_iso_20_T1_75Hz = np.std(iso_20_T1_75Hz)
#     std_iso_20_T2_75Hz = np.std(iso_20_T2_75Hz)
#     std_iso_05_T1_75Hz = np.std(iso_05_T1_75Hz)
#     std_iso_05_T2_75Hz = np.std(iso_05_T2_75Hz)
#
#     SaEn_iso_80_T1_75Hz = lb.Ent_Samp(iso_80_T1_75Hz, 2, 0.2)
#     SaEn_iso_80_T2_75Hz = lb.Ent_Samp(iso_80_T2_75Hz, 2, 0.2)
#     SaEn_iso_60_T1_75Hz = lb.Ent_Samp(iso_60_T1_75Hz, 2, 0.2)
#     SaEn_iso_60_T2_75Hz = lb.Ent_Samp(iso_60_T2_75Hz, 2, 0.2)
#     SaEn_iso_40_T1_75Hz = lb.Ent_Samp(iso_40_T1_75Hz, 2, 0.2)
#     SaEn_iso_40_T2_75Hz = lb.Ent_Samp(iso_40_T2_75Hz, 2, 0.2)
#     SaEn_iso_20_T1_75Hz = lb.Ent_Samp(iso_20_T1_75Hz, 2, 0.2)
#     SaEn_iso_20_T2_75Hz = lb.Ent_Samp(iso_20_T2_75Hz, 2, 0.2)
#     SaEn_iso_05_T1_75Hz = lb.Ent_Samp(iso_05_T1_75Hz, 2, 0.2)
#     SaEn_iso_05_T2_75Hz = lb.Ent_Samp(iso_05_T2_75Hz, 2, 0.2)
#
#     DFA_iso_80_T1_75Hz = lb.DFA(iso_80_T1_75Hz)
#     DFA_iso_80_T2_75Hz = lb.DFA(iso_80_T2_75Hz)
#     DFA_iso_60_T1_75Hz = lb.DFA(iso_60_T1_75Hz)
#     DFA_iso_60_T2_75Hz = lb.DFA(iso_60_T2_75Hz)
#     DFA_iso_40_T1_75Hz = lb.DFA(iso_40_T1_75Hz)
#     DFA_iso_40_T2_75Hz = lb.DFA(iso_40_T2_75Hz)
#     DFA_iso_20_T1_75Hz = lb.DFA(iso_20_T1_75Hz)
#     DFA_iso_20_T2_75Hz = lb.DFA(iso_20_T2_75Hz)
#     DFA_iso_05_T1_75Hz = lb.DFA(iso_05_T1_75Hz)
#     DFA_iso_05_T2_75Hz = lb.DFA(iso_05_T2_75Hz)
#
#     std_T1 = [std_iso_80_T1_75Hz, std_iso_60_T1_75Hz, std_iso_40_T1_75Hz, std_iso_20_T1_75Hz, std_iso_05_T1_75Hz]
#     std_T2 = [std_iso_80_T2_75Hz, std_iso_60_T2_75Hz, std_iso_40_T2_75Hz, std_iso_20_T2_75Hz, std_iso_05_T2_75Hz]
#
#     average_std = [np.mean((std_iso_80_T1_75Hz, std_iso_80_T2_75Hz)),
#                    np.mean((std_iso_60_T1_75Hz, std_iso_60_T2_75Hz)),
#                    np.mean((std_iso_40_T1_75Hz, std_iso_40_T2_75Hz)),
#                    np.mean((std_iso_20_T1_75Hz, std_iso_20_T2_75Hz)),
#                    np.mean((std_iso_05_T1_75Hz, std_iso_05_T2_75Hz))]
#
#     SaEn_T1 = [SaEn_iso_80_T1_75Hz, SaEn_iso_60_T1_75Hz, SaEn_iso_40_T1_75Hz, SaEn_iso_20_T1_75Hz, SaEn_iso_05_T1_75Hz]
#     SaEn_T2 = [SaEn_iso_80_T2_75Hz, SaEn_iso_60_T2_75Hz, SaEn_iso_40_T2_75Hz, SaEn_iso_20_T2_75Hz, SaEn_iso_05_T2_75Hz]
#     average_SaEn = [np.mean((SaEn_iso_80_T1_75Hz, SaEn_iso_80_T2_75Hz)),
#                     np.mean((SaEn_iso_60_T1_75Hz, SaEn_iso_60_T2_75Hz)),
#                     np.mean((SaEn_iso_40_T1_75Hz, SaEn_iso_40_T2_75Hz)),
#                     np.mean((SaEn_iso_20_T1_75Hz, SaEn_iso_20_T2_75Hz)),
#                     np.mean((SaEn_iso_05_T1_75Hz, SaEn_iso_05_T2_75Hz))]
#
#     DFA_T1 = [DFA_iso_80_T1_75Hz, DFA_iso_60_T1_75Hz, DFA_iso_40_T1_75Hz, DFA_iso_20_T1_75Hz, DFA_iso_05_T1_75Hz]
#     DFA_T2 = [DFA_iso_80_T2_75Hz, DFA_iso_60_T2_75Hz, DFA_iso_40_T2_75Hz, DFA_iso_20_T2_75Hz, DFA_iso_05_T2_75Hz]
#     average_DFA = [np.mean((DFA_iso_80_T1_75Hz, DFA_iso_80_T2_75Hz)),
#                     np.mean((DFA_iso_60_T1_75Hz, DFA_iso_60_T2_75Hz)),
#                     np.mean((DFA_iso_40_T1_75Hz, DFA_iso_40_T2_75Hz)),
#                     np.mean((DFA_iso_20_T1_75Hz, DFA_iso_20_T2_75Hz)),
#                     np.mean((DFA_iso_05_T1_75Hz, DFA_iso_05_T2_75Hz))]
#
#     Percentage_iso = [80, 60, 40, 20, 5]
#
#     plt.plot(Percentage_iso, std_T1, label='T1')
#     plt.plot(Percentage_iso, std_T2, label='T2')
#     plt.plot(Percentage_iso, average_std, label='average_std', lw=4)
#     plt.title(f'Sd {participant}')
#     plt.legend()
#     plt.show()
#
#     plt.plot(Percentage_iso, SaEn_T1, label='T1')
#     plt.plot(Percentage_iso, SaEn_T2, label='T2')
#     plt.plot(Percentage_iso, average_SaEn, label='average_SaEn', lw=4)
#     plt.title(f'SaEn {participant}')
#     plt.legend()
#     plt.show()
#
#
#     plt.plot(Percentage_iso, DFA_T1, label='T1')
#     plt.plot(Percentage_iso, DFA_T2, label='T2')
#     plt.plot(Percentage_iso, average_DFA, label='average_DFA', lw=4)
#     plt.title(f'DFA {participant}')
#     plt.legend()
#     plt.show()






