import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
from matplotlib.lines import Line2D
import seaborn as sns
import lib


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 16


# directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Data collection\Results'
# os.chdir(directory)
# Resuls_all = pd.read_excel(r'Results all Lowpass 50Hz only best iso trials all pert trials.xlsx')
# print(Resuls_all.columns)
# print(Resuls_all)
#
#
# SaEn_Iso_80_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_80'].to_numpy()
# SaEn_Iso_60_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_60'].to_numpy()
# SaEn_Iso_40_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_40'].to_numpy()
# SaEn_Iso_20_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_20'].to_numpy()
# SaEn_Iso_05_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_05'].to_numpy()
# SaEn_Iso_Average_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Average_SaEn'].to_numpy()
#
# sd_Iso_80_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['sd_80'].to_numpy()
# sd_Iso_60_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['sd_60'].to_numpy()
# sd_Iso_40_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['sd_40'].to_numpy()
# sd_Iso_20_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['sd_20'].to_numpy()
# sd_Iso_05_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['sd_05'].to_numpy()
# CoV_Iso_80_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['CoV_80'].to_numpy()
# CoV_Iso_60_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['CoV_60'].to_numpy()
# CoV_Iso_40_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['CoV_40'].to_numpy()
# CoV_Iso_20_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['CoV_20'].to_numpy()
# CoV_Iso_05_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['CoV_05'].to_numpy()
# SaEn_Adaptation_down_min_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_min'].to_numpy()
# SaEn_Adaptation_down_max_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_max'].to_numpy()
# SaEn_Adaptation_down_T1_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_T1'].to_numpy()
# SaEn_Adaptation_down_T2_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_T2'].to_numpy()
# SaEn_Adaptation_up_min_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_min'].to_numpy()
# SaEn_Adaptation_up_max_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_max'].to_numpy()
# SaEn_Adaptation_up_T1_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_T1'].to_numpy()
# SaEn_Adaptation_up_T2_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_T2'].to_numpy()
# SaEn_Adaptation_down_min_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_min_before_pert'].to_numpy()
# SaEn_Adaptation_down_max_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_max_before_pert'].to_numpy()
# SaEn_Adaptation_down_T1_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_T1_before_pert'].to_numpy()
# SaEn_Adaptation_down_T2_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_down_T2_before_pert'].to_numpy()
# SaEn_Adaptation_up_min_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_min_before_pert'].to_numpy()
# SaEn_Adaptation_up_max_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_max_before_pert'].to_numpy()
# SaEn_Adaptation_up_T1_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_T1_before_pert'].to_numpy()
# SaEn_Adaptation_up_T2_old_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Old']['SaEn_Adaptation_up_T2_before_pert'].to_numpy()
# Adaptation_down_min_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_down_min'].to_numpy()
# Adaptation_down_max_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_down_max'].to_numpy()
# Adaptation_down_T1_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_down_T1'].to_numpy()
# Adaptation_down_T2_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_down_T2'].to_numpy()
# Adaptation_up_min_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_up_min'].to_numpy()
# Adaptation_up_max_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_up_max'].to_numpy()
# Adaptation_up_T1_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_up_T1'].to_numpy()
# Adaptation_up_T2_old = Resuls_all[Resuls_all['ID_group'] == 'Old']['Adaptation_up_T2'].to_numpy()
#
# SaEn_Iso_80_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_80'].to_numpy()
# SaEn_Iso_60_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_60'].to_numpy()
# SaEn_Iso_40_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_40'].to_numpy()
# SaEn_Iso_20_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_20'].to_numpy()
# SaEn_Iso_05_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_05'].to_numpy()
# SaEn_Iso_Average_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Average_SaEn'].to_numpy()
# sd_Iso_80_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['sd_80'].to_numpy()
# sd_Iso_60_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['sd_60'].to_numpy()
# sd_Iso_40_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['sd_40'].to_numpy()
# sd_Iso_20_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['sd_20'].to_numpy()
# sd_Iso_05_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['sd_05'].to_numpy()
# CoV_Iso_80_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['CoV_80'].to_numpy()
# CoV_Iso_60_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['CoV_60'].to_numpy()
# CoV_Iso_40_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['CoV_40'].to_numpy()
# CoV_Iso_20_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['CoV_20'].to_numpy()
# CoV_Iso_05_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['CoV_05'].to_numpy()
# SaEn_Adaptation_down_min_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_min'].to_numpy()
# SaEn_Adaptation_down_max_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_max'].to_numpy()
# SaEn_Adaptation_down_T1_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_T1'].to_numpy()
# SaEn_Adaptation_down_T2_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_T2'].to_numpy()
# SaEn_Adaptation_up_min_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_min'].to_numpy()
# SaEn_Adaptation_up_max_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_max'].to_numpy()
# SaEn_Adaptation_up_T1_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_T1'].to_numpy()
# SaEn_Adaptation_up_T2_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_T2'].to_numpy()
# SaEn_Adaptation_down_min_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_min_before_pert'].to_numpy()
# SaEn_Adaptation_down_max_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_max_before_pert'].to_numpy()
# SaEn_Adaptation_down_T1_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_T1_before_pert'].to_numpy()
# SaEn_Adaptation_down_T2_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_down_T2_before_pert'].to_numpy()
# SaEn_Adaptation_up_min_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_min_before_pert'].to_numpy()
# SaEn_Adaptation_up_max_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_max_before_pert'].to_numpy()
# SaEn_Adaptation_up_T1_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_T1_before_pert'].to_numpy()
# SaEn_Adaptation_up_T2_young_before_pert = Resuls_all[Resuls_all['ID_group'] == 'Young']['SaEn_Adaptation_up_T2_before_pert'].to_numpy()
# Adaptation_down_min_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_down_min'].to_numpy()
# Adaptation_down_max_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_down_max'].to_numpy()
# Adaptation_down_T1_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_down_T1'].to_numpy()
# Adaptation_down_T2_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_down_T2'].to_numpy()
# Adaptation_up_min_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_up_min'].to_numpy()
# Adaptation_up_max_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_up_max'].to_numpy()
# Adaptation_up_T1_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_up_T1'].to_numpy()
# Adaptation_up_T2_young = Resuls_all[Resuls_all['ID_group'] == 'Young']['Adaptation_up_T2'].to_numpy()
#
# up_adaptation = Resuls_all['Adaptation_up_min'].to_numpy()
# down_adaptation = Resuls_all['Adaptation_down_min'].to_numpy()
# ID = Resuls_all['ID_group'].to_numpy()
#
#
# print(len(SaEn_Iso_80_old))
# print(len(SaEn_Iso_80_young))
#
# y_axis_old = [SaEn_Iso_80_old, SaEn_Iso_60_old, SaEn_Iso_40_old, SaEn_Iso_20_old, SaEn_Iso_05_old, sd_Iso_80_old, sd_Iso_60_old, sd_Iso_40_old, sd_Iso_20_old, sd_Iso_05_old, CoV_Iso_80_old, CoV_Iso_60_old, CoV_Iso_40_old, CoV_Iso_20_old, CoV_Iso_05_old, SaEn_Adaptation_down_min_old, SaEn_Adaptation_down_max_old, SaEn_Adaptation_down_T1_old, SaEn_Adaptation_down_T2_old, SaEn_Adaptation_up_min_old, SaEn_Adaptation_up_max_old, SaEn_Adaptation_up_T1_old, SaEn_Adaptation_up_T2_old, Adaptation_down_min_old, Adaptation_down_max_old, Adaptation_down_T1_old, Adaptation_down_T2_old, Adaptation_up_min_old, Adaptation_up_max_old, Adaptation_up_T1_old, Adaptation_up_T2_old]
# y_labels_old = ['SaEn_Iso_80_old', 'SaEn_Iso_60_old', 'SaEn_Iso_40_old', 'SaEn_Iso_20_old', 'SaEn_Iso_05_old', 'sd_Iso_80_old', 'sd_Iso_60_old', 'sd_Iso_40_old', 'sd_Iso_20_old', 'sd_Iso_05_old', 'CoV_Iso_80_old', 'CoV_Iso_60_old', 'CoV_Iso_40_old', 'CoV_Iso_20_old', 'CoV_Iso_05_old', 'SaEn_Adaptation_down_min_old', 'SaEn_Adaptation_down_max_old', 'SaEn_Adaptation_down_T1_old', 'SaEn_Adaptation_down_T2_old', 'SaEn_Adaptation_up_min_old', 'SaEn_Adaptation_up_max_old', 'SaEn_Adaptation_up_T1_old', 'SaEn_Adaptation_up_T2_old', 'Adaptation_down_min_old', 'Adaptation_down_max_old', 'Adaptation_down_T1_old', 'Adaptation_down_T2_old', 'Adaptation_up_min_old', 'Adaptation_up_max_old', 'Adaptation_up_T1_old', 'Adaptation_up_T2_old']
#
# y_axis_young = [SaEn_Iso_80_young, SaEn_Iso_60_young, SaEn_Iso_40_young, SaEn_Iso_20_young, SaEn_Iso_05_young, sd_Iso_80_young, sd_Iso_60_young, sd_Iso_40_young, sd_Iso_20_young, sd_Iso_05_young, CoV_Iso_80_young, CoV_Iso_60_young, CoV_Iso_40_young, CoV_Iso_20_young, CoV_Iso_05_young, SaEn_Adaptation_down_min_young, SaEn_Adaptation_down_max_young, SaEn_Adaptation_down_T1_young, SaEn_Adaptation_down_T2_young, SaEn_Adaptation_up_min_young, SaEn_Adaptation_up_max_young, SaEn_Adaptation_up_T1_young, SaEn_Adaptation_up_T2_young, Adaptation_down_min_young, Adaptation_down_max_young, Adaptation_down_T1_young, Adaptation_down_T2_young, Adaptation_up_min_young, Adaptation_up_max_young, Adaptation_up_T1_young, Adaptation_up_T2_young]
# y_labels_young = ['SaEn_Iso_80_Young', 'SaEn_Iso_60_Young', 'SaEn_Iso_40_Young', 'SaEn_Iso_20_Young', 'SaEn_Iso_05_Young', 'sd_Iso_80_Young', 'sd_Iso_60_Young', 'sd_Iso_40_Young', 'sd_Iso_20_Young', 'sd_Iso_05_Young', 'CoV_Iso_80_Young', 'CoV_Iso_60_Young', 'CoV_Iso_40_Young', 'CoV_Iso_20_Young', 'CoV_Iso_05_Young', 'SaEn_Adaptation_down_min_Young', 'SaEn_Adaptation_down_max_Young', 'SaEn_Adaptation_down_T1_Young', 'SaEn_Adaptation_down_T2_Young', 'SaEn_Adaptation_up_min_Young', 'SaEn_Adaptation_up_max_Young', 'SaEn_Adaptation_up_T1_Young', 'SaEn_Adaptation_up_T2_Young', 'Adaptation_down_min_Young', 'Adaptation_down_max_Young', 'Adaptation_down_T1_Young', 'Adaptation_down_T2_Young', 'Adaptation_up_min_Young', 'Adaptation_up_max_Young', 'Adaptation_up_T1_Young', 'Adaptation_up_T2_Young']
#
# SaEn_Iso_Average = Resuls_all['Average_SaEn'].to_numpy()
# Sd_Iso_Average = Resuls_all['Average_Sd'].to_numpy()
#
# Adaptation_up = Resuls_all['Adaptation_up_min'].to_numpy()
#
#
# plt.scatter(SaEn_Adaptation_down_min_young_before_pert, Adaptation_down_min_young, label='young')
# plt.scatter(SaEn_Adaptation_down_min_old_before_pert, Adaptation_down_min_old, label='old')
# plt.legend()
#
# from scipy import stats
# print(stats.pearsonr(SaEn_Adaptation_down_min_young_before_pert, Adaptation_down_min_young))
# print(stats.pearsonr(SaEn_Adaptation_down_min_old_before_pert, Adaptation_down_min_old))
#
#
#
# plt.show()


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


# Graph for perturbation trials
#
# def synchronization_of_Time_and_ClosestSampleTime_Anestis(df):
#     """ This function creates a new dataframe by synchronizing the Time column to the ClosestSampleTime column and then returns a new dataframe with the correct values"""
#
#     time_index = []
#     for i in range(len(df)):
#         # Calculate the difference of the element i of the column ClosestSampleTime with every value of the column Time
#         closest_index = (df['Time'] - df['ClosestSampleTime'].iloc[i]).abs()
#         # Drop the None values of the closest_index so that in the next step the .empty attribute if it has only None values it would show False
#         closest_index = closest_index.dropna()
#
#         if not closest_index.empty:
#             # Find the index of the minimum difference
#             closest_index = closest_index.idxmin()
#             # Keep only the index of minimum difference
#             time_index.append(closest_index)
#     # Create all other columns
#     time = df.loc[time_index, 'Time'].to_numpy()
#     performance = df.loc[time_index, 'Performance'].to_numpy()
#     targets = df['Target'].dropna().to_numpy()
#     time_close_to_target = df['ClosestSampleTime'].dropna().to_numpy()
#
#     # Create the dataframe which will be returned afterward.
#     dist = {'Indices': time_index,
#             'Time': time,
#             'Performance': performance,
#             'ClosestSampleTime': time_close_to_target,
#             'Target': targets}
#     new_df = pd.DataFrame(dist)
#
#     return new_df
#
# def spatial_error(df):
#     """ Calculate the spatial error of the Performance and Target
#     Parameters
#     Input
#             df              :   the Dataframe
#     Output
#             spatial_error   :   the spatial_error between the Performance and Target
#     """
#
#     spatial_error = []
#     for i in range(len(df['Time'])):
#         spatial_error.append((abs(df['Performance'][i]-df['Target'][i])))
#     spatial_error = np.array(spatial_error)
#     return spatial_error
#
# def adaptation_time_using_sd(df, perturbation_index, sd_factor, first_values, consecutive_values, values_for_sd, name, plot=False):
#     """
#     This function returns the time after the perturbation which was needed to adapt to the perturbation
#     Parameters
#     Input
#             df                  :   The Dataframe
#             perturbation_index  :   The index where the perturbation occurred
#             sd_factor           :   This will be multiplied with the sd of the error before the perturbation
#                                     and if the error after the is less than the mean + sd*sd_factor and more than
#                                     the mean - sd*sd_factor, the algorithm will consider that the adaptation of the
#                                     perturbation occurred
#             first_values        :   At first the error will be too much so to calculate the mean and sd before the perturbation
#                                     right, we erase some values from the beginning
#             consecutive_values  :   This is how many values the algorithm needs to consider so that it decides that the adaptation occurred.
#             total targets       :   The total number of targets
#             Plot                :   Plot the spatial error and the time of adaptation (default value False)
#
#     Output
#             time_of_adaptation  :   The time it took the df['Performance'] to steadily reach df['Target']. This
#                                     number corresponds to the first value of time at which for the next X consecutive_values
#                                     the spatial error was lower than the average +- (sd * sd_factor)
#     """
#     # First synchronize the Time and ClosestSampleTime columns and create a new df with
#     # only the synchronized values
#     df = synchronization_of_Time_and_ClosestSampleTime_Anestis(df)
#
#     # Calculate the spatial error and the average and sd of the spatial error
#     # after the first_values
#     spatial_er = spatial_error(df)
#
#     # The following 2 lines calculate the mean and sd of the 'first_values' before the perturbation
#     # to use for calculating the adaptation time
#     mean = np.mean(spatial_er[first_values:perturbation_index])
#     sd_before_perturbation = np.std(spatial_er[first_values:perturbation_index])
#
#     # The following line calculate the lowest sd for 'values_for_sd' in overlapping window and
#     # the lowest sd is the sd used for further analysis
#     list_for_mean_and_sd = spatial_er[perturbation_index:]
#     list_of_sd = []
#     list_of_means = []
#     for i in range(len(list_for_mean_and_sd) - values_for_sd):
#         average = np.mean(list_for_mean_and_sd[i:i+values_for_sd])
#         sd = np.std(list_for_mean_and_sd[i:i+values_for_sd])
#         list_of_means.append(average)
#         list_of_sd.append(sd)
#     min_sd = min(list_of_sd)
#     min_sd_index = list_of_sd.index(min_sd)
#     average_at_min_sd = list_of_means[min_sd_index]
#     # plt.plot(list_of_sd)
#     # plt.show()
#
#     # Create an array with consecutive_values equal number
#     consecutive_values_list = np.arange(0,consecutive_values,1)
#     print((consecutive_values_list))
#
#     # Iterate the spatial error after the perturbation_index to calculate the time of adaptation
#     for i in range(len(spatial_er) - consecutive_values+1):
#         if i >= perturbation_index:
#
#             if (all(spatial_er[i + j] < average_at_min_sd + min_sd * sd_factor for j in consecutive_values_list) and
#                 all(spatial_er[i + j] > average_at_min_sd - min_sd * sd_factor for j in consecutive_values_list)):
#                 time_of_adaptation = df['Time'][i] - df['Time'][perturbation_index]
#                 break
#
#     if plot == True:
#         try:
#             time_of_adaptation
#             time = np.linspace(-10,10,len(spatial_er))
#             plt.plot(time, spatial_er, label='Spatial Error')
#             plt.axhline(y=average_at_min_sd, c='k', label = 'Average')
#             plt.axhline(y=average_at_min_sd + min_sd*sd_factor, c='k', ls=":", label=f'{sd_factor}*Sd')
#             plt.axhline(y=average_at_min_sd - min_sd*sd_factor, c='k', ls=":")
#             plt.axvline(x=time_of_adaptation, lw=3, c='red', label='Adaptation instance')
#             plt.axvline(x=0, linestyle='--', c='gray', label='Perturbation instance')
#
#             plt.legend()
#             plt.ylabel('Spatial Error (kg)')
#             plt.xlabel('Time (sec)')
#             # plt.title(f'{name}\ntime for adaptation: {round(time_of_adaptation,3)} sec')
#             plt.title('Perturbation Trial')
#
#             plt.show()
#         except NameError:
#             print(f"No adaptation was evident for {name}")
#
#     try:
#         time_of_adaptation
#         return time_of_adaptation
#     except:
#         time_of_adaptation = None
#         return time_of_adaptation
#
#
# # Calculation of time to adaptation for all perturbation trials
#
# directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Data collection\Data\Strength data\Young.8'
# os.chdir(directory)
#
# Pert_down_T1 = pd.read_csv('Pert_down_T1.csv', skiprows=2)
# Pert_down_T2 = pd.read_csv('Pert_down_T2.csv', skiprows=2)
# Pert_up_T1 = pd.read_csv('Pert_up_T1.csv', skiprows=2)
# Pert_up_T2 = pd.read_csv('Pert_up_T2.csv', skiprows=2)
#
# Pert_down_T1['Performance'] = lib.Butterworth(75, 50, Pert_down_T1['Performance'])
# Pert_down_T2['Performance'] = lib.Butterworth(75, 50, Pert_down_T2['Performance'])
# Pert_up_T1['Performance'] = lib.Butterworth(75, 50, Pert_up_T1['Performance'])
# Pert_up_T2['Performance'] = lib.Butterworth(75, 50, Pert_up_T2['Performance'])
#
# sd = 2
# consecutive_values = 37
#
# time_of_adaptation_down_T1 = adaptation_time_using_sd(Pert_down_T1, 250, sd, 100, consecutive_values, 100, 'Pert_down_T1', plot=True)
# time_of_adaptation_down_T2 = adaptation_time_using_sd(Pert_down_T2, 250, sd, 100, consecutive_values, 100, 'Pert_down_T2', plot=True)
# time_of_adaptation_up_T1 = adaptation_time_using_sd(Pert_up_T1, 250, sd, 100, consecutive_values, 100, 'Pert_up_T1', plot=True)
# time_of_adaptation_up_T2 = adaptation_time_using_sd(Pert_up_T2, 250, sd, 100, consecutive_values, 100, 'Pert_up_T2', plot=True)

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 25

# X axis: %MVC
x = np.linspace(0, 100, 500)

# Primary Y axis: Sample Entropy (red)
y_saen = 0.5 + 0.1 * np.exp(-0.5 * ((x - 40) / 10)**2)

# Secondary Y axis: Standard Deviation (blue), exponential from 0.1 to 2.1
y_sd = 0.1 * (2.1 / 0.1) ** (x / 100)

# Create figure and first axis
fig, ax1 = plt.subplots(figsize=(8, 5))

# Plot Sample Entropy (SaEn)
ax1.plot(x, y_saen, color='red', linewidth=2, label='Sample Entropy (SaEn)')
ax1.set_xlabel('Percentage of MVC (%)')
ax1.set_ylabel('Sample Entropy (SaEn)', color='red')
ax1.tick_params(axis='y', labelcolor='red')
# Set specific y-ticks and labels
yticks = [0.45, 0.50, 0.55, 0.60, 0.65]
ax1.set_yticks(yticks)
ax1.set_yticklabels([f"{ytick:.2f}" for ytick in yticks])
ax1.set_xlim(0, 100)
# ax1.set_yticklabels([])  # Remove numbers from primary y-axis
ax1.grid(True, linestyle='--', alpha=0.6)

# Create secondary axis
ax2 = ax1.twinx()
ax2.plot(x, y_sd, color='blue', linewidth=2, linestyle='--', label='Standard Deviation (SD)')
ax2.set_ylabel('Standard Deviation (SD)', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')
# ax2.set_yticklabels([])  # Remove numbers from primary y-axis

# Title
# plt.title('Sample Entropy and Standard Deviation Across %MVC', fontsize=14)

plt.show()