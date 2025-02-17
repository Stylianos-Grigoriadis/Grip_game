import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
from matplotlib.lines import Line2D
import seaborn as sns


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 10


directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Data collection\Results'
os.chdir(directory)
Resuls_all = pd.read_excel(r'Results all Lowpass 50Hz only best iso trials all pert trials.xlsx')
print(Resuls_all.columns)
print(Resuls_all)


SaEn_Iso_80_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_80'].to_numpy()
SaEn_Iso_60_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_60'].to_numpy()
SaEn_Iso_40_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_40'].to_numpy()
SaEn_Iso_20_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_20'].to_numpy()
SaEn_Iso_05_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_05'].to_numpy()
SaEn_Iso_Average_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Average_SaEn'].to_numpy()

sd_Iso_80_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['sd_80'].to_numpy()
sd_Iso_60_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['sd_60'].to_numpy()
sd_Iso_40_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['sd_40'].to_numpy()
sd_Iso_20_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['sd_20'].to_numpy()
sd_Iso_05_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['sd_05'].to_numpy()
CoV_Iso_80_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['CoV_80'].to_numpy()
CoV_Iso_60_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['CoV_60'].to_numpy()
CoV_Iso_40_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['CoV_40'].to_numpy()
CoV_Iso_20_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['CoV_20'].to_numpy()
CoV_Iso_05_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['CoV_05'].to_numpy()
SaEn_Adaptation_down_min_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_min'].to_numpy()
SaEn_Adaptation_down_max_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_max'].to_numpy()
SaEn_Adaptation_down_T1_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_T1'].to_numpy()
SaEn_Adaptation_down_T2_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_T2'].to_numpy()
SaEn_Adaptation_up_min_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_min'].to_numpy()
SaEn_Adaptation_up_max_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_max'].to_numpy()
SaEn_Adaptation_up_T1_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_T1'].to_numpy()
SaEn_Adaptation_up_T2_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_T2'].to_numpy()
SaEn_Adaptation_down_min_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_min_before_pert'].to_numpy()
SaEn_Adaptation_down_max_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_max_before_pert'].to_numpy()
SaEn_Adaptation_down_T1_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_T1_before_pert'].to_numpy()
SaEn_Adaptation_down_T2_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_T2_before_pert'].to_numpy()
SaEn_Adaptation_up_min_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_min_before_pert'].to_numpy()
SaEn_Adaptation_up_max_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_max_before_pert'].to_numpy()
SaEn_Adaptation_up_T1_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_T1_before_pert'].to_numpy()
SaEn_Adaptation_up_T2_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_T2_before_pert'].to_numpy()
Adaptation_down_min_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_down_min'].to_numpy()
Adaptation_down_max_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_down_max'].to_numpy()
Adaptation_down_T1_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_down_T1'].to_numpy()
Adaptation_down_T2_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_down_T2'].to_numpy()
Adaptation_up_min_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_up_min'].to_numpy()
Adaptation_up_max_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_up_max'].to_numpy()
Adaptation_up_T1_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_up_T1'].to_numpy()
Adaptation_up_T2_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_up_T2'].to_numpy()

SaEn_Iso_80_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_80'].to_numpy()
SaEn_Iso_60_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_60'].to_numpy()
SaEn_Iso_40_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_40'].to_numpy()
SaEn_Iso_20_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_20'].to_numpy()
SaEn_Iso_05_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_05'].to_numpy()
SaEn_Iso_Average_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Average_SaEn'].to_numpy()
sd_Iso_80_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['sd_80'].to_numpy()
sd_Iso_60_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['sd_60'].to_numpy()
sd_Iso_40_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['sd_40'].to_numpy()
sd_Iso_20_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['sd_20'].to_numpy()
sd_Iso_05_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['sd_05'].to_numpy()
CoV_Iso_80_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['CoV_80'].to_numpy()
CoV_Iso_60_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['CoV_60'].to_numpy()
CoV_Iso_40_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['CoV_40'].to_numpy()
CoV_Iso_20_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['CoV_20'].to_numpy()
CoV_Iso_05_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['CoV_05'].to_numpy()
SaEn_Adaptation_down_min_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_min'].to_numpy()
SaEn_Adaptation_down_max_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_max'].to_numpy()
SaEn_Adaptation_down_T1_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_T1'].to_numpy()
SaEn_Adaptation_down_T2_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_T2'].to_numpy()
SaEn_Adaptation_up_min_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_min'].to_numpy()
SaEn_Adaptation_up_max_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_max'].to_numpy()
SaEn_Adaptation_up_T1_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_T1'].to_numpy()
SaEn_Adaptation_up_T2_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_T2'].to_numpy()
SaEn_Adaptation_down_min_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_min_before_pert'].to_numpy()
SaEn_Adaptation_down_max_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_max_before_pert'].to_numpy()
SaEn_Adaptation_down_T1_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_T1_before_pert'].to_numpy()
SaEn_Adaptation_down_T2_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_T2_before_pert'].to_numpy()
SaEn_Adaptation_up_min_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_min_before_pert'].to_numpy()
SaEn_Adaptation_up_max_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_max_before_pert'].to_numpy()
SaEn_Adaptation_up_T1_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_T1_before_pert'].to_numpy()
SaEn_Adaptation_up_T2_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_T2_before_pert'].to_numpy()
Adaptation_down_min_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_down_min'].to_numpy()
Adaptation_down_max_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_down_max'].to_numpy()
Adaptation_down_T1_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_down_T1'].to_numpy()
Adaptation_down_T2_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_down_T2'].to_numpy()
Adaptation_up_min_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_up_min'].to_numpy()
Adaptation_up_max_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_up_max'].to_numpy()
Adaptation_up_T1_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_up_T1'].to_numpy()
Adaptation_up_T2_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_up_T2'].to_numpy()

up_adaptation = Resuls_all['Adaptation_up_min'].to_numpy()
down_adaptation = Resuls_all['Adaptation_down_min'].to_numpy()
ID = Resuls_all['ID_group'].to_numpy()


print(len(SaEn_Iso_80_old))
print(len(SaEn_Iso_80_young))

y_axis_old = [SaEn_Iso_80_old, SaEn_Iso_60_old, SaEn_Iso_40_old, SaEn_Iso_20_old, SaEn_Iso_05_old, sd_Iso_80_old, sd_Iso_60_old, sd_Iso_40_old, sd_Iso_20_old, sd_Iso_05_old, CoV_Iso_80_old, CoV_Iso_60_old, CoV_Iso_40_old, CoV_Iso_20_old, CoV_Iso_05_old, SaEn_Adaptation_down_min_old, SaEn_Adaptation_down_max_old, SaEn_Adaptation_down_T1_old, SaEn_Adaptation_down_T2_old, SaEn_Adaptation_up_min_old, SaEn_Adaptation_up_max_old, SaEn_Adaptation_up_T1_old, SaEn_Adaptation_up_T2_old, Adaptation_down_min_old, Adaptation_down_max_old, Adaptation_down_T1_old, Adaptation_down_T2_old, Adaptation_up_min_old, Adaptation_up_max_old, Adaptation_up_T1_old, Adaptation_up_T2_old]
y_labels_old = ['SaEn_Iso_80_old', 'SaEn_Iso_60_old', 'SaEn_Iso_40_old', 'SaEn_Iso_20_old', 'SaEn_Iso_05_old', 'sd_Iso_80_old', 'sd_Iso_60_old', 'sd_Iso_40_old', 'sd_Iso_20_old', 'sd_Iso_05_old', 'CoV_Iso_80_old', 'CoV_Iso_60_old', 'CoV_Iso_40_old', 'CoV_Iso_20_old', 'CoV_Iso_05_old', 'SaEn_Adaptation_down_min_old', 'SaEn_Adaptation_down_max_old', 'SaEn_Adaptation_down_T1_old', 'SaEn_Adaptation_down_T2_old', 'SaEn_Adaptation_up_min_old', 'SaEn_Adaptation_up_max_old', 'SaEn_Adaptation_up_T1_old', 'SaEn_Adaptation_up_T2_old', 'Adaptation_down_min_old', 'Adaptation_down_max_old', 'Adaptation_down_T1_old', 'Adaptation_down_T2_old', 'Adaptation_up_min_old', 'Adaptation_up_max_old', 'Adaptation_up_T1_old', 'Adaptation_up_T2_old']

y_axis_young = [SaEn_Iso_80_young, SaEn_Iso_60_young, SaEn_Iso_40_young, SaEn_Iso_20_young, SaEn_Iso_05_young, sd_Iso_80_young, sd_Iso_60_young, sd_Iso_40_young, sd_Iso_20_young, sd_Iso_05_young, CoV_Iso_80_young, CoV_Iso_60_young, CoV_Iso_40_young, CoV_Iso_20_young, CoV_Iso_05_young, SaEn_Adaptation_down_min_young, SaEn_Adaptation_down_max_young, SaEn_Adaptation_down_T1_young, SaEn_Adaptation_down_T2_young, SaEn_Adaptation_up_min_young, SaEn_Adaptation_up_max_young, SaEn_Adaptation_up_T1_young, SaEn_Adaptation_up_T2_young, Adaptation_down_min_young, Adaptation_down_max_young, Adaptation_down_T1_young, Adaptation_down_T2_young, Adaptation_up_min_young, Adaptation_up_max_young, Adaptation_up_T1_young, Adaptation_up_T2_young]
y_labels_young = ['SaEn_Iso_80_Young', 'SaEn_Iso_60_Young', 'SaEn_Iso_40_Young', 'SaEn_Iso_20_Young', 'SaEn_Iso_05_Young', 'sd_Iso_80_Young', 'sd_Iso_60_Young', 'sd_Iso_40_Young', 'sd_Iso_20_Young', 'sd_Iso_05_Young', 'CoV_Iso_80_Young', 'CoV_Iso_60_Young', 'CoV_Iso_40_Young', 'CoV_Iso_20_Young', 'CoV_Iso_05_Young', 'SaEn_Adaptation_down_min_Young', 'SaEn_Adaptation_down_max_Young', 'SaEn_Adaptation_down_T1_Young', 'SaEn_Adaptation_down_T2_Young', 'SaEn_Adaptation_up_min_Young', 'SaEn_Adaptation_up_max_Young', 'SaEn_Adaptation_up_T1_Young', 'SaEn_Adaptation_up_T2_Young', 'Adaptation_down_min_Young', 'Adaptation_down_max_Young', 'Adaptation_down_T1_Young', 'Adaptation_down_T2_Young', 'Adaptation_up_min_Young', 'Adaptation_up_max_Young', 'Adaptation_up_T1_Young', 'Adaptation_up_T2_Young']

SaEn_Iso_Average = Resuls_all['Average_SaEn'].to_numpy()
Sd_Iso_Average = Resuls_all['Average_Sd'].to_numpy()

Adaptation_up = Resuls_all['Adaptation_up_min'].to_numpy()


plt.scatter(SaEn_Adaptation_down_min_young_before_pert, Adaptation_down_min_young, label='young')
plt.scatter(SaEn_Adaptation_down_min_old_before_pert, Adaptation_down_min_old, label='old')
plt.legend()

from scipy import stats
print(stats.pearsonr(SaEn_Adaptation_down_min_young_before_pert, Adaptation_down_min_young))
print(stats.pearsonr(SaEn_Adaptation_down_min_old_before_pert, Adaptation_down_min_old))



plt.show()


# for index_x, x in enumerate(x_axis):
#     for index_y, y in enumerate(y_axis):
#         colors = ['red' if age == "Old" else 'blue' for age in ID]
#         plt.scatter(x, y, c=colors, label="Old (red) / Young (blue)")
#         plt.xlabel(x_labels[index_x])
#         plt.ylabel(y_labels[index_y])
#         plt.title("Scatter Plot with Age Group Colors")
#         legend_elements = [Line2D([0], [0], marker='o', color='w', label='Old', markersize=8, markerfacecolor='red'),
#                            Line2D([0], [0], marker='o', color='w', label='Young', markersize=8, markerfacecolor='blue')]
#         plt.legend(handles=legend_elements)
#         plt.show()


# for i in range(len(y_axis_old)):
#
#     # Calculate IQR
#     Q1 = np.percentile(data, 25)
#     Q3 = np.percentile(data, 75)
#     IQR = Q3 - Q1
#
#     # Define thresholds for outliers
#     mild_outlier_threshold = Q3 + 1.5 * IQR
#     extreme_outlier_threshold = Q3 + 3 * IQR
#
#     # Identify outliers
#     mild_outliers = data[(data > mild_outlier_threshold) & (data <= extreme_outlier_threshold)]
#     extreme_outliers = data[data > extreme_outlier_threshold]
#
#     # Create Boxplot
#     plt.figure(figsize=(6, 4))
#     sns.boxplot(y=data, color="lightblue", width=0.3)
#
#     # Highlight mild outliers (orange)
#     plt.scatter(np.zeros_like(mild_outliers), mild_outliers, color="orange", label="Mild Outliers", zorder=3)
#
#     # Highlight extreme outliers (red)
#     plt.scatter(np.zeros_like(extreme_outliers), extreme_outliers, color="red", label="Extreme Outliers", zorder=3)
#
#     plt.title(f"Boxplot {y_labels[index]} with Mild & Extreme Outliers", fontsize=14)
#     plt.ylabel("Values")
#     plt.legend()
#     plt.grid(True)
#     plt.show()