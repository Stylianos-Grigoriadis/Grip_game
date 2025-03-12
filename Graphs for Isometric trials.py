import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import glob
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm




plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 16

directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Data collection\Results'
os.chdir(directory)
results = pd.read_excel(r'Results all Lowpass 50Hz only best iso trials all pert trials.xlsx')

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



#
# # Graph for SaEn
#
# fig, ax = plt.subplots(figsize=(8, 6))
# young_positions = [1, 4, 7, 10, 13]
# plus_factor = 0.6
# old_positions = [young_positions[0]+plus_factor, young_positions[1]+plus_factor, young_positions[2]+plus_factor, young_positions[3]+plus_factor, young_positions[4]+plus_factor]
# # Create the box plot
# ax.boxplot(young_SaEn,
#            positions=young_positions,
#            patch_artist=True,
#            showmeans=True,
#            showfliers=False,
#            boxprops=dict(facecolor='lightblue', color='blue'),
#            meanprops=dict(marker='o', markeredgecolor='blue', markerfacecolor='blue'),
#            medianprops=dict(color='none'))
#
# ax.boxplot(old_SaEn,
#            positions=old_positions,
#            patch_artist=True,
#            showmeans=True,
#            showfliers=False,
#            boxprops=dict(facecolor='lightcoral', color='red'),
#            meanprops=dict(marker='o', markeredgecolor='red', markerfacecolor='red'),
#            medianprops=dict(color='none'))
#
# # Calculate means for each group
# young_means = [np.mean(data) for data in young_SaEn]
# old_means = [np.mean(data) for data in old_SaEn]
#
# # Plot dashed lines connecting the mean markers
# ax.plot(young_positions, young_means, color='blue', linestyle='--')
# ax.plot(old_positions, old_means, color='red', linestyle='--')
#
#
# # Manually create legend elements
# legend_elements = [
#     mpatches.Patch(color='lightblue', label='  Young'),
#     mlines.Line2D([], [], color='blue', marker='o', markersize=8, label='  Young Average', linestyle='None'),
#     mpatches.Patch(color='lightcoral', label='  Old'),
#     mlines.Line2D([], [], color='red', marker='o', markersize=8, label='  Old Average', linestyle='None'),
#     # mlines.Line2D([], [], color='k', marker=r'$\ast$', markersize=10, linestyle='None',
#     #               label=r'  Sig > $SaEn_{5\%}$ Both Groups'),
#     # mlines.Line2D([], [], color='k', marker=r'$\ast\ast$', markersize=25, linestyle='None',
#     #               label=r'  Sig > $SaEn_{20\%}$ Both Groups'),
# ]
#
# # y_text_position = 0.35
# # minus_factor = 0.02
# #
# # ax.text(young_positions[2] + plus_factor/2, y_text_position, '*', ha='center', va='bottom', fontsize=40, color='k', fontweight='bold')
# # ax.text(young_positions[2] + plus_factor/2, y_text_position - minus_factor, '**', ha='center', va='bottom', fontsize=40, color='k', fontweight='bold')
# #
# # ax.text(young_positions[3] + plus_factor/2, y_text_position, '*', ha='center', va='bottom', fontsize=40, color='k', fontweight='bold')
# # ax.text(young_positions[3] + plus_factor/2, y_text_position - minus_factor, '**', ha='center', va='bottom', fontsize=40, color='k', fontweight='bold')
#
#
#
#
# # Add the legend to the plot
# ax.legend(handles=legend_elements, loc='upper left', frameon=False)
#
# # Customize the plot
# # ax.set_title(f'Sample Entropy Curve between Young (n={len(SaEn_80_Young)}) and Old (n={len(SaEn_80_Old)}) adults')
# ax.set_title(f'Sample Entropy Curve between Young and Old adults')
#
# ax.set_xticks([(x + y) / 2 for x, y in zip(young_positions, old_positions)])
# ax.set_xticklabels(['5%', '20%', '40%', '60%', '80%'])
# ax.set_ylabel('Sample Entropy')
# ax.set_xlabel('Percentage of MVC')
# ax.set_ylim([0, 0.5])
#
# # Display the plot
# plt.show()
#
#
# # Graph for SD
#
# fig, ax = plt.subplots(figsize=(8, 6))
# young_positions = [1, 4, 7, 10, 13]
# plus_factor = 0.6
#
# old_positions = [young_positions[0]+plus_factor, young_positions[1]+plus_factor, young_positions[2]+plus_factor, young_positions[3]+plus_factor, young_positions[4]+plus_factor]
# # Create the box plot
# ax.boxplot(young_sd,
#            positions=young_positions,
#            patch_artist=True,
#            showmeans=True,
#            showfliers=False,
#            boxprops=dict(facecolor='lightblue', color='blue'),
#            meanprops=dict(marker='o', markeredgecolor='blue', markerfacecolor='blue'),
#            medianprops=dict(color='none'))
#
# ax.boxplot(old_sd,
#            positions=old_positions,
#            patch_artist=True,
#            showmeans=True,
#            showfliers=False,
#            boxprops=dict(facecolor='lightcoral', color='red'),
#            meanprops=dict(marker='o', markeredgecolor='red', markerfacecolor='red'),
#            medianprops=dict(color='none'))
#
# # Calculate means for each group
# young_means = [np.mean(data) for data in young_sd]
# old_means = [np.mean(data) for data in old_sd]
#
# # Plot dashed lines connecting the mean markers
# ax.plot(young_positions, young_means, color='blue', linestyle='--')
# ax.plot(old_positions, old_means, color='red', linestyle='--')
#
# old_adults_color = 'red'
# young_adults_color = 'blue'
#
# # Manually create legend elements
# legend_elements = [
#     mpatches.Patch(color='lightblue', label='  Young'),
#     mlines.Line2D([], [], color='blue', marker='o', markersize=8, label='  Young Average', linestyle='None'),
#     mpatches.Patch(color='lightcoral', label='  Old'),
#     mlines.Line2D([], [], color='red', marker='o', markersize=8, label='  Old Average', linestyle='None'),
#     #
#     # # SD markers for older adults
#     # mlines.Line2D([], [], color=young_adults_color, marker=r'$\ast$', markersize=10, linestyle='None', label=r'  Sig > $SD_{5\%}$ Young Adults'),
#     # mlines.Line2D([], [], color=young_adults_color, marker=r'$\ast\ast$', markersize=25, linestyle='None', label=r'  Sig > $SD_{20\%}$ Young Adults'),
#     # mlines.Line2D([], [], color=young_adults_color, marker=r'$\ast\ast\ast$', markersize=40, linestyle='None', label=r'  Sig > $SD_{40\%}$ Young Adults'),
#     # mlines.Line2D([], [], color=young_adults_color, marker=r'$\ast\ast\ast\ast$', markersize=55, linestyle='None', label=r'  Sig > $SD_{60\%}$ Young Adults'),
#     #
#     # # SD markers for older adults
#     # mlines.Line2D([], [], color=old_adults_color, marker=r'$\ast$', markersize=10, linestyle='None', label=r'  Sig > $SD_{5\%}$ Older Adults'),
#     # mlines.Line2D([], [], color=old_adults_color, marker=r'$\ast\ast$', markersize=25, linestyle='None', label=r'  Sig > $SD_{20\%}$ Older Adults'),
#     # mlines.Line2D([], [], color=old_adults_color, marker=r'$\ast\ast\ast$', markersize=40, linestyle='None', label=r'  Sig > $SD_{40\%}$ Older Adults'),
#
# ]
# #
# # minus_factor = 0.17
# # old_basic_40 = 0.9
# # old_basic_60 = 1.7
# # old_basic_80 = 2.7
# #
# # young_basic_20 = -0.3
# # young_basic_40 = -0.3
# # young_basic_60 = -0.3
# # young_basic_80 = -0.3
# #
# # ax.text(young_positions[1] + plus_factor/2, young_basic_20, '*', ha='center', va='bottom', fontsize=40, color=young_adults_color, fontweight='bold')
# # ax.text(young_positions[2] + plus_factor/2, young_basic_40, '*', ha='center', va='bottom', fontsize=40, color=young_adults_color, fontweight='bold')
# # ax.text(young_positions[3] + plus_factor/2, young_basic_60, '*', ha='center', va='bottom', fontsize=40, color=young_adults_color, fontweight='bold')
# # ax.text(young_positions[4] + plus_factor/2, young_basic_80, '*', ha='center', va='bottom', fontsize=40, color=young_adults_color, fontweight='bold')
# #
# # ax.text(young_positions[2] + plus_factor/2, young_basic_40 - minus_factor, '**', ha='center', va='bottom', fontsize=40, color=young_adults_color, fontweight='bold')
# # ax.text(young_positions[3] + plus_factor/2, young_basic_60 - minus_factor, '**', ha='center', va='bottom', fontsize=40, color=young_adults_color, fontweight='bold')
# # ax.text(young_positions[4] + plus_factor/2, young_basic_80 - minus_factor, '**', ha='center', va='bottom', fontsize=40, color=young_adults_color, fontweight='bold')
# #
# # ax.text(young_positions[3] + plus_factor/2, young_basic_60 - 2*minus_factor, '***', ha='center', va='bottom', fontsize=40, color=young_adults_color, fontweight='bold')
# # ax.text(young_positions[4] + plus_factor/2, young_basic_80 - 2*minus_factor, '***', ha='center', va='bottom', fontsize=40, color=young_adults_color, fontweight='bold')
# #
# # ax.text(young_positions[4] + plus_factor/2, young_basic_80 - 3*minus_factor, '****', ha='center', va='bottom', fontsize=40, color=young_adults_color, fontweight='bold')
# #
# #
# # ax.text(young_positions[2] + plus_factor/2, old_basic_40, '*', ha='center', va='bottom', fontsize=40, color=old_adults_color, fontweight='bold')
# # ax.text(young_positions[3] + plus_factor/2, old_basic_60, '*', ha='center', va='bottom', fontsize=40, color=old_adults_color, fontweight='bold')
# # ax.text(young_positions[4] + plus_factor/2, old_basic_80, '*', ha='center', va='bottom', fontsize=40, color=old_adults_color, fontweight='bold')
# #
# # ax.text(young_positions[2] + plus_factor/2, old_basic_40 - minus_factor, '**', ha='center', va='bottom', fontsize=40, color=old_adults_color, fontweight='bold')
# # ax.text(young_positions[3] + plus_factor/2, old_basic_60 - minus_factor, '**', ha='center', va='bottom', fontsize=40, color=old_adults_color, fontweight='bold')
# # ax.text(young_positions[4] + plus_factor/2, old_basic_80 - minus_factor, '**', ha='center', va='bottom', fontsize=40, color=old_adults_color, fontweight='bold')
# #
# # ax.text(young_positions[3] + plus_factor/2, old_basic_60 - 2*minus_factor, '***', ha='center', va='bottom', fontsize=40, color=old_adults_color, fontweight='bold')
# # ax.text(young_positions[4] + plus_factor/2, old_basic_80 - 2*minus_factor, '***', ha='center', va='bottom', fontsize=40, color=old_adults_color, fontweight='bold')
#
#
# # Add the legend to the plot
# ax.legend(handles=legend_elements, loc='upper left', frameon=False)
#
#
#
# # Customize the plot
# # ax.set_title(f'Standard Deviation curve between Young (n={len(SaEn_80_Young)}) and Old (n={len(SaEn_80_Old)}) adults')
# ax.set_title(f'Standard Deviation curve between Young and Old adults')
# ax.set_xticks([(x + y) / 2 for x, y in zip(young_positions, old_positions)])
# ax.set_xticklabels(['5%', '20%', '40%', '60%', '80%'])
# ax.set_ylabel('Standard Deviation')
# ax.set_xlabel('Percentage of MVC')
# ax.set_ylim([-1.5, 4.5])
#
# # Display the plot
# plt.show()
#
#
#
# # Graph for time of adaptation
#
# fig, ax = plt.subplots(figsize=(8, 6))
# young_positions = [1, 4]
# plus_factor = 0.6
# old_positions = [young_positions[0]+plus_factor, young_positions[1]+plus_factor]
# # Create the box plot
# ax.boxplot(young_time_of_adaptation,
#            positions=young_positions,
#            patch_artist=True,
#            showmeans=True,
#            showfliers=False,
#            boxprops=dict(facecolor='lightblue', color='blue'),
#            meanprops=dict(marker='o', markeredgecolor='blue', markerfacecolor='blue'),
#            medianprops=dict(color='none'))
#
# ax.boxplot(old_time_of_adaptation,
#            positions=old_positions,
#            patch_artist=True,
#            showmeans=True,
#            showfliers=False,
#            boxprops=dict(facecolor='lightcoral', color='red'),
#            meanprops=dict(marker='o', markeredgecolor='red', markerfacecolor='red'),
#            medianprops=dict(color='none'))
#
# # Calculate means for each group
# young_means = [np.mean(data) for data in young_time_of_adaptation]
# old_means = [np.mean(data) for data in old_time_of_adaptation]
#
# # Plot dashed lines connecting the mean markers
# ax.plot(young_positions, young_means, color='blue', linestyle='--')
# ax.plot(old_positions, old_means, color='red', linestyle='--')
#
#
# # Manually create legend elements
# legend_elements = [
#     mpatches.Patch(color='lightblue', label='Young'),
#     mlines.Line2D([], [], color='blue', marker='o', markersize=8, label='Young Average', linestyle='None'),
#     mpatches.Patch(color='lightcoral', label='Old'),
#     mlines.Line2D([], [], color='red', marker='o', markersize=8, label='Old Average', linestyle='None')
# ]
#
# # Add the legend to the plot
# ax.legend(handles=legend_elements, loc='upper right', frameon=False)
#
# # Customize the plot
# ax.set_title(f'Time to adapt curve between Young (n={len(SaEn_80_Young)}) and Old (n={len(SaEn_80_Old)}) adults')
#
# ax.set_xticks([(x + y) / 2 for x, y in zip(young_positions, old_positions)])
# ax.set_xticklabels(['Perturbation\ndownwards', 'Perturbation\nupwards'])
# ax.set_ylabel('Time to adapt')
# ax.set_ylim([0, 7])
#
# # Display the plot
# plt.show()



# Regression Graph

# Independent variables for each group
X_Old = np.column_stack((SaEn_80_Old, SaEn_60_Old, SaEn_40_Old, SaEn_20_Old, SaEn_05_Old,
                         sd_80_Old, sd_60_Old, sd_40_Old, sd_20_Old, sd_05_Old))

X_Young = np.column_stack((SaEn_80_Young, SaEn_60_Young, SaEn_40_Young, SaEn_20_Young, SaEn_05_Young,
                           sd_80_Young, sd_60_Young, sd_40_Young, sd_20_Young, sd_05_Young))

# Function to fit multiple linear regression and predict values
def fit_and_predict(X, y):
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    return y_pred

# Fit models
pred_down_Old = fit_and_predict(X_Old, Pert_down_Old)
pred_down_Young = fit_and_predict(X_Young, Pert_down_Young)
pred_up_Old = fit_and_predict(X_Old, Pert_up_Old)
pred_up_Young = fit_and_predict(X_Young, Pert_up_Young)

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# Plot Down Perturbation
ax1.scatter(range(len(Pert_down_Old)), Pert_down_Old, color='red', label='Old (Down)', alpha=0.5)
ax1.scatter(range(len(Pert_down_Young)), Pert_down_Young, color='blue', label='Young (Down)', alpha=0.5)
ax1.plot(range(len(pred_down_Old)), pred_down_Old, color='red', linestyle='dashed')
ax1.plot(range(len(pred_down_Young)), pred_down_Young, color='blue', linestyle='dashed')
ax1.set_title("Down Perturbation")
ax1.legend()

# Plot Up Perturbation
ax2.scatter(range(len(Pert_up_Old)), Pert_up_Old, color='red', label='Old (Up)', alpha=0.5)
ax2.scatter(range(len(Pert_up_Young)), Pert_up_Young, color='blue', label='Young (Up)', alpha=0.5)
ax2.plot(range(len(pred_up_Old)), pred_up_Old, color='red', linestyle='dashed')
ax2.plot(range(len(pred_up_Young)), pred_up_Young, color='blue', linestyle='dashed')
ax2.set_title("Up Perturbation")
ax2.legend()

plt.tight_layout()
plt.show()
