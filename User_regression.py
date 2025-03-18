import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import glob
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import statsmodels.api as sm
import scipy.stats as stats

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 16

directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Data collection\Results'
os.chdir(directory)
results = pd.read_excel(r'Results all Lowpass 50Hz only best iso trials all pert trials.xlsx')
print(results.columns)
# print(results['ID'])

SaEn_40 = results['SaEn_40'].to_numpy()
SaEn_20 = results['SaEn_20'].to_numpy()
SaEn_Adaptation_up_min_before_pert = results['SaEn_Adaptation_up_min_before_pert'].to_numpy()
SaEn_Adaptation_down_min_before_pert = results['SaEn_Adaptation_down_min_before_pert'].to_numpy()
columns_to_consider_for_max_SaEn = ['SaEn_80', 'SaEn_60', 'SaEn_40', 'SaEn_20', 'SaEn_05']
SaEn_max = results[columns_to_consider_for_max_SaEn].max(axis=1).to_numpy()
SaEn_average = results['Average_SaEn'].to_numpy()
Adaptation_up_min = results['Adaptation_up_min'].to_numpy()
Adaptation_down_min = results['Adaptation_down_min'].to_numpy()

# Sort based on SaEn40
sorted_indices_SaEn_40 = np.argsort(SaEn_40)
sortd_SaEn_40 = SaEn_40[sorted_indices_SaEn_40]
sortd_Adaptation_up_min_SaEn_40 = Adaptation_up_min[sorted_indices_SaEn_40]
sortd_Adaptation_down_min_SaEn_40 = Adaptation_down_min[sorted_indices_SaEn_40]
dist_sort_SaEn_40 = {'sortd_SaEn_40': sortd_SaEn_40,
                     'sortd_Adaptation_up_min_SaEn_40': sortd_Adaptation_up_min_SaEn_40,
                     'sortd_Adaptation_down_min_SaEn_40': sortd_Adaptation_down_min_SaEn_40}
df_sort_SaEn_40 = pd.DataFrame(dist_sort_SaEn_40)

# Sort based on SaEn60
sorted_indices_SaEn_20 = np.argsort(SaEn_20)
sortd_SaEn_20 = SaEn_20[sorted_indices_SaEn_20]
sortd_Adaptation_up_min_SaEn_20 = Adaptation_up_min[sorted_indices_SaEn_20]
sortd_Adaptation_down_min_SaEn_20 = Adaptation_down_min[sorted_indices_SaEn_20]
dist_sort_SaEn_20 = {'sortd_SaEn_20': sortd_SaEn_20,
                     'sortd_Adaptation_up_min_SaEn_20': sortd_Adaptation_up_min_SaEn_20,
                     'sortd_Adaptation_down_min_SaEn_20': sortd_Adaptation_down_min_SaEn_20}
df_sort_SaEn_20 = pd.DataFrame(dist_sort_SaEn_20)

# Sort based on SaEn_max
sorted_indices_SaEn_max = np.argsort(SaEn_max)
sortd_SaEn_max = SaEn_max[sorted_indices_SaEn_max]
sortd_Adaptation_up_min_SaEn_max = Adaptation_up_min[sorted_indices_SaEn_max]
sortd_Adaptation_down_min_SaEn_max = Adaptation_down_min[sorted_indices_SaEn_max]
dist_sort_SaEn_max = {'sortd_SaEn_max': sortd_SaEn_max,
                     'sortd_Adaptation_up_min_SaEn_max': sortd_Adaptation_up_min_SaEn_max,
                     'sortd_Adaptation_down_min_SaEn_max': sortd_Adaptation_down_min_SaEn_max}
df_sort_SaEn_max = pd.DataFrame(dist_sort_SaEn_max)

# Sort based on SaEn_average
sorted_indices_SaEn_average = np.argsort(SaEn_average)
sortd_SaEn_average = SaEn_average[sorted_indices_SaEn_average]
sortd_Adaptation_up_min_SaEn_average = Adaptation_up_min[sorted_indices_SaEn_average]
sortd_Adaptation_down_min_SaEn_average = Adaptation_down_min[sorted_indices_SaEn_average]
dist_sort_SaEn_average = {'sortd_SaEn_average': sortd_SaEn_average,
                     'sortd_Adaptation_up_min_SaEn_average': sortd_Adaptation_up_min_SaEn_average,
                     'sortd_Adaptation_down_min_SaEn_average': sortd_Adaptation_down_min_SaEn_average}
df_sort_SaEn_average = pd.DataFrame(dist_sort_SaEn_average)

# Sort based on SaEn_Adaptation_up_min_before_pert
sorted_indices_SaEn_Adaptation_up_min_before_pert = np.argsort(SaEn_Adaptation_up_min_before_pert)
sortd_SaEn_Adaptation_up_min_before_pert = SaEn_Adaptation_up_min_before_pert[sorted_indices_SaEn_Adaptation_up_min_before_pert]
sortd_Adaptation_up_min_SaEn_Adaptation_up_min_before_pert = Adaptation_up_min[sorted_indices_SaEn_Adaptation_up_min_before_pert]
dist_sort_SaEn_Adaptation_up_min_before_pert = {'sortd_SaEn_Adaptation_up_min_before_pert': sortd_SaEn_Adaptation_up_min_before_pert,
                     'sortd_Adaptation_up_min_SaEn_Adaptation_up_min_before_pert': sortd_Adaptation_up_min_SaEn_Adaptation_up_min_before_pert}
df_sort_SaEn_Adaptation_up_min_before_pert = pd.DataFrame(dist_sort_SaEn_Adaptation_up_min_before_pert)

# Sort based on SaEn_Adaptation_down_min_before_pert
sorted_indices_SaEn_Adaptation_down_min_before_pert = np.argsort(SaEn_Adaptation_down_min_before_pert)
sortd_SaEn_Adaptation_down_min_before_pert = SaEn_Adaptation_down_min_before_pert[sorted_indices_SaEn_Adaptation_down_min_before_pert]
sortd_Adaptation_down_min_SaEn_Adaptation_down_min_before_pert = Adaptation_down_min[sorted_indices_SaEn_Adaptation_down_min_before_pert]
dist_sort_SaEn_Adaptation_down_min_before_pert = {'sortd_SaEn_Adaptation_down_min_before_pert': sortd_SaEn_Adaptation_down_min_before_pert,
                     'sortd_Adaptation_down_min_SaEn_Adaptation_down_min_before_pert': sortd_Adaptation_down_min_SaEn_Adaptation_down_min_before_pert}
df_sort_SaEn_Adaptation_down_min_before_pert = pd.DataFrame(dist_sort_SaEn_Adaptation_down_min_before_pert)


# plt.plot(sortd_SaEn_40)
# plt.show()
# plt.plot(sortd_Adaptation_up_min_SaEn_40)
# plt.show()
# plt.plot(sortd_Adaptation_down_min_SaEn_40)
# plt.show()
#
# plt.plot(sortd_SaEn_20)
# plt.show()
# plt.plot(sortd_Adaptation_up_min_SaEn_20)
# plt.show()
# plt.plot(sortd_Adaptation_down_min_SaEn_20)
# plt.show()

# plt.scatter(sortd_SaEn_40,sortd_Adaptation_up_min_SaEn_40, label='SaEn_40 * Up')
# plt.legend()
# plt.show()
#
# plt.scatter(sortd_SaEn_40,sortd_Adaptation_down_min_SaEn_40, label='SaEn_40 * Down')
# plt.legend()
# plt.show()
#
# plt.scatter(sortd_SaEn_20,sortd_Adaptation_up_min_SaEn_20, label='SaEn_20 * Up')
# plt.legend()
# plt.show()
#
# plt.scatter(sortd_SaEn_20,sortd_Adaptation_down_min_SaEn_20, label='SaEn_20 * Down')
# plt.legend()
# plt.show()




# Regression of the SaEn_40 by taking out one participant at the time from the lowest to the highest entropy
# for i in range(len(sortd_SaEn_40)-1):
#     print(i)
#     new_sortd_SaEn_40 = sortd_SaEn_40[i:]
#     new_sortd_Adaptation_up_min_SaEn_40 = sortd_Adaptation_up_min_SaEn_40[i:]
#     new_sortd_Adaptation_down_min_SaEn_40 = sortd_Adaptation_down_min_SaEn_40[i:]
#
#     slope_up, intercept_up, r_value_up, p_value_up, std_err_up = stats.linregress(new_sortd_SaEn_40, new_sortd_Adaptation_up_min_SaEn_40)
#     slope_down, intercept_down, r_value_down, p_value_down, std_err_down = stats.linregress(new_sortd_SaEn_40, new_sortd_Adaptation_down_min_SaEn_40)
#
#     R_squared_up = r_value_up**2
#     R_squared_down = r_value_down**2
#
#     predicted_values_up = slope_up * new_sortd_SaEn_40 + intercept_up
#     predicted_values_down = slope_down * new_sortd_SaEn_40 + intercept_down

    # plt.scatter(new_sortd_SaEn_40, new_sortd_Adaptation_up_min_SaEn_40, label="Data", color="blue")
    # plt.plot(new_sortd_SaEn_40, predicted_values_up, color="red", label=f"y={round(slope_up,2)}x+{round(intercept_up,2)}\nR^2={round(R_squared_up,3)}\np={round(p_value_up,3)}")
    # plt.xlabel("Sorted SaEn 40")
    # plt.ylabel("Sorted Adaptation Up (min) SaEn 40")
    # plt.title(f'Perturbation Up without the first {i} participants')
    # plt.legend()
    # plt.show()

    # plt.scatter(new_sortd_SaEn_40, new_sortd_Adaptation_down_min_SaEn_40, label="Data", color="blue")
    # plt.plot(new_sortd_SaEn_40, predicted_values_down, color="red", label=f"y={round(slope_down,2)}x+{round(intercept_down,2)}\nR^2 = {round(R_squared_down,3)}\np={round(p_value_down,3)}")
    # plt.xlabel("Sorted SaEn 40")
    # plt.ylabel("Sorted Adaptation Down (min) SaEn 40")
    # plt.title(f'Perturbation Down without the first {i} participants')
    # plt.legend()
    # plt.show()

# Regression of the SaEn_60 by taking out one participant at the time from the lowest to the highest entropy
# for i in range(len(sortd_SaEn_60)-1):
#     print(i)
#     new_sortd_SaEn_60 = sortd_SaEn_60[i:]
#     new_sortd_Adaptation_up_min_SaEn_60 = sortd_Adaptation_up_min_SaEn_60[i:]
#     new_sortd_Adaptation_down_min_SaEn_60 = sortd_Adaptation_down_min_SaEn_60[i:]
#
#     slope_up, intercept_up, r_value_up, p_value_up, std_err_up = stats.linregress(new_sortd_SaEn_60, new_sortd_Adaptation_up_min_SaEn_60)
#     slope_down, intercept_down, r_value_down, p_value_down, std_err_down = stats.linregress(new_sortd_SaEn_60, new_sortd_Adaptation_down_min_SaEn_60)
#
#     R_squared_up = r_value_up ** 2
#     R_squared_down = r_value_down ** 2
#
#     predicted_values_up = slope_up * new_sortd_SaEn_60 + intercept_up
#     predicted_values_down = slope_down * new_sortd_SaEn_60 + intercept_down

    # plt.scatter(new_sortd_SaEn_60, new_sortd_Adaptation_up_min_SaEn_60, label="Data", color="blue")
    # plt.plot(new_sortd_SaEn_60, predicted_values_up, color="red", label=f"y={round(slope_up, 2)}x+{round(intercept_up, 2)}\nR^2 = {round(R_squared_up, 3)}\np={round(p_value_up,3)}")
    # plt.xlabel("Sorted SaEn 60")
    # plt.ylabel("Sorted Adaptation Up (min) SaEn 60")
    # plt.title(f'Perturbation Up without the first {i} participants')
    # plt.legend()
    # plt.show()

    # plt.scatter(new_sortd_SaEn_60, new_sortd_Adaptation_down_min_SaEn_60, label="Data", color="blue")
    # plt.plot(new_sortd_SaEn_60, predicted_values_down, color="red", label=f"y={round(slope_down,2)}x+{round(intercept_down,2)}\nR^2 = {round(R_squared_down,3)}\np={round(p_value_down,3)}")
    # plt.xlabel("Sorted SaEn 60")
    # plt.ylabel("Sorted Adaptation Down (min) SaEn 60")
    # plt.title(f'Perturbation Down without the first {i} participants')
    # plt.legend()
    # plt.show()


# Regression of the SaEn_max by taking out one participant at the time from the lowest to the highest entropy
# for i in range(len(sortd_SaEn_max)-1):
#     print(i)
#     new_sortd_SaEn_max = sortd_SaEn_max[i:]
#     new_sortd_Adaptation_up_min_SaEn_max = sortd_Adaptation_up_min_SaEn_max[i:]
#     new_sortd_Adaptation_down_min_SaEn_max = sortd_Adaptation_down_min_SaEn_max[i:]
#
#     slope_up, intercept_up, r_value_up, p_value_up, std_err_up = stats.linregress(new_sortd_SaEn_max, new_sortd_Adaptation_up_min_SaEn_max)
#     slope_down, intercept_down, r_value_down, p_value_down, std_err_down = stats.linregress(new_sortd_SaEn_max, new_sortd_Adaptation_down_min_SaEn_max)
#
#     R_squared_up = r_value_up**2
#     R_squared_down = r_value_down**2
#
#     predicted_values_up = slope_up * new_sortd_SaEn_max + intercept_up
#     predicted_values_down = slope_down * new_sortd_SaEn_max + intercept_down

    # plt.scatter(new_sortd_SaEn_max, new_sortd_Adaptation_up_min_SaEn_max, label="Data", color="blue")
    # plt.plot(new_sortd_SaEn_max, predicted_values_up, color="red", label=f"y={round(slope_up,2)}x+{round(intercept_up,2)}\nR^2={round(R_squared_up,3)}\np={round(p_value_up,3)}")
    # plt.xlabel("Sorted SaEn max")
    # plt.ylabel("Sorted Adaptation Up (min) SaEn max")
    # plt.title(f'Perturbation Up without the first {i} participants')
    # plt.legend()
    # plt.show()

    # plt.scatter(new_sortd_SaEn_max, new_sortd_Adaptation_down_min_SaEn_max, label="Data", color="blue")
    # plt.plot(new_sortd_SaEn_max, predicted_values_down, color="red", label=f"y={round(slope_down,2)}x+{round(intercept_down,2)}\nR^2 = {round(R_squared_down,3)}\np={round(p_value_down,3)}")
    # plt.xlabel("Sorted SaEn max")
    # plt.ylabel("Sorted Adaptation Down (min) SaEn max")
    # plt.title(f'Perturbation Down without the first {i} participants')
    # plt.legend()
    # plt.show()

# Regression of the SaEn_average by taking out one participant at the time from the lowest to the highest entropy
# for i in range(len(sortd_SaEn_average)-1):
#     print(i)
#     new_sortd_SaEn_average = sortd_SaEn_average[i:]
#     new_sortd_Adaptation_up_min_SaEn_average = sortd_Adaptation_up_min_SaEn_average[i:]
#     new_sortd_Adaptation_down_min_SaEn_average = sortd_Adaptation_down_min_SaEn_average[i:]
#
#     slope_up, intercept_up, r_value_up, p_value_up, std_err_up = stats.linregress(new_sortd_SaEn_average, new_sortd_Adaptation_up_min_SaEn_average)
#     slope_down, intercept_down, r_value_down, p_value_down, std_err_down = stats.linregress(new_sortd_SaEn_average, new_sortd_Adaptation_down_min_SaEn_average)
#
#     R_squared_up = r_value_up**2
#     R_squared_down = r_value_down**2
#
#     predicted_values_up = slope_up * new_sortd_SaEn_average + intercept_up
#     predicted_values_down = slope_down * new_sortd_SaEn_average + intercept_down

    # plt.scatter(new_sortd_SaEn_average, new_sortd_Adaptation_up_min_SaEn_average, label="Data", color="blue")
    # plt.plot(new_sortd_SaEn_average, predicted_values_up, color="red", label=f"y={round(slope_up,2)}x+{round(intercept_up,2)}\nR^2={round(R_squared_up,3)}\np={round(p_value_up,3)}")
    # plt.xlabel("Sorted SaEn average")
    # plt.ylabel("Sorted Adaptation Up (min) SaEn average")
    # plt.title(f'Perturbation Up without the first {i} participants')
    # plt.legend()
    # plt.show()

    # plt.scatter(new_sortd_SaEn_average, new_sortd_Adaptation_down_min_SaEn_average, label="Data", color="blue")
    # plt.plot(new_sortd_SaEn_average, predicted_values_down, color="red", label=f"y={round(slope_down,2)}x+{round(intercept_down,2)}\nR^2 = {round(R_squared_down,3)}\np={round(p_value_down,3)}")
    # plt.xlabel("Sorted SaEn average")
    # plt.ylabel("Sorted Adaptation Down (min) SaEn average")
    # plt.title(f'Perturbation Down without the first {i} participants')
    # plt.legend()
    # plt.show()


# Regression of the SaEn_40 by taking out one participant at the time from the highest to the lowest entropy
# for i in range(len(sortd_SaEn_40)-1):
#     print(i)
#
#     new_sortd_SaEn_40 = sortd_SaEn_40[:len(sortd_SaEn_40)-i]
#     print(new_sortd_SaEn_40)
#     new_sortd_Adaptation_up_min_SaEn_40 = sortd_Adaptation_up_min_SaEn_40[:len(sortd_SaEn_40)-i]
#     new_sortd_Adaptation_down_min_SaEn_40 = sortd_Adaptation_down_min_SaEn_40[:len(sortd_SaEn_40)-i]
#
#     slope_up, intercept_up, r_value_up, p_value_up, std_err_up = stats.linregress(new_sortd_SaEn_40, new_sortd_Adaptation_up_min_SaEn_40)
#     slope_down, intercept_down, r_value_down, p_value_down, std_err_down = stats.linregress(new_sortd_SaEn_40, new_sortd_Adaptation_down_min_SaEn_40)
#
#     R_squared_up = r_value_up**2
#     R_squared_down = r_value_down**2
#
#     predicted_values_up = slope_up * new_sortd_SaEn_40 + intercept_up
#     predicted_values_down = slope_down * new_sortd_SaEn_40 + intercept_down
#
#     plt.scatter(new_sortd_SaEn_40, new_sortd_Adaptation_up_min_SaEn_40, label="Data", color="blue")
#     plt.plot(new_sortd_SaEn_40, predicted_values_up, color="red", label=f"y={round(slope_up,2)}x+{round(intercept_up,2)}\nR^2 = {round(R_squared_up,3)}\np={round(p_value_up,3)}")
#     plt.xlabel("Sorted SaEn 40")
#     plt.ylabel("Sorted Adaptation Up (min) SaEn 40")
#     plt.title(f'Perturbation Up without the first {i} participants')
#     plt.legend()
#     plt.show()
#
#     plt.scatter(new_sortd_SaEn_40, new_sortd_Adaptation_down_min_SaEn_40, label="Data", color="blue")
#     plt.plot(new_sortd_SaEn_40, predicted_values_down, color="red", label=f"y={round(slope_down,2)}x+{round(intercept_down,2)}\nR^2 = {round(R_squared_down,3)}\np={round(p_value_down,3)}")
#     plt.xlabel("Sorted SaEn 40")
#     plt.ylabel("Sorted Adaptation Down (min) SaEn 40")
#     plt.title(f'Perturbation Down without the first {i} participants')
#     plt.legend()
#     plt.show()

# Regression of the SaEn_60 by taking out one participant at the time from the highest to the lowest entropy
# for i in range(len(sortd_SaEn_60)-1):
#     print(i)
#     new_sortd_SaEn_60 = sortd_SaEn_60[:len(sortd_SaEn_60)-i]
#     new_sortd_Adaptation_up_min_SaEn_60 = sortd_Adaptation_up_min_SaEn_60[:len(sortd_SaEn_60)-i]
#     new_sortd_Adaptation_down_min_SaEn_60 = sortd_Adaptation_down_min_SaEn_60[:len(sortd_SaEn_60)-i]
#
#     slope_up, intercept_up, r_value_up, p_value_up, std_err_up = stats.linregress(new_sortd_SaEn_60, new_sortd_Adaptation_up_min_SaEn_60)
#     slope_down, intercept_down, r_value_down, p_value_down, std_err_down = stats.linregress(new_sortd_SaEn_60, new_sortd_Adaptation_down_min_SaEn_60)
#
#     R_squared_up = r_value_up ** 2
#     R_squared_down = r_value_down ** 2
#
#     predicted_values_up = slope_up * new_sortd_SaEn_60 + intercept_up
#     predicted_values_down = slope_down * new_sortd_SaEn_60 + intercept_down
#
#     plt.scatter(new_sortd_SaEn_60, new_sortd_Adaptation_up_min_SaEn_60, label="Data", color="blue")
#     plt.plot(new_sortd_SaEn_60, predicted_values_up, color="red", label=f"y={round(slope_up, 2)}x+{round(intercept_up, 2)}\nR^2 = {round(R_squared_up, 3)}\np={round(p_value_up,3)}")
#     plt.xlabel("Sorted SaEn 60")
#     plt.ylabel("Sorted Adaptation Up (min) SaEn 60")
#     plt.title(f'Perturbation Up without the first {i} participants')
#     plt.legend()
#     plt.show()
#
#     plt.scatter(new_sortd_SaEn_60, new_sortd_Adaptation_down_min_SaEn_60, label="Data", color="blue")
#     plt.plot(new_sortd_SaEn_60, predicted_values_down, color="red", label=f"y={round(slope_down,2)}x+{round(intercept_down,2)}\nR^2 = {round(R_squared_down,3)}\np={round(p_value_down,3)}")
#     plt.xlabel("Sorted SaEn 60")
#     plt.ylabel("Sorted Adaptation Down (min) SaEn 60")
#     plt.title(f'Perturbation Down without the first {i} participants')
#     plt.legend()
#     plt.show()

# Regression of the SaEn_max by taking out one participant at the time from the highest to the lowest entropy
# for i in range(len(sortd_SaEn_max)-1):
#     print(i)
#     new_sortd_SaEn_max = sortd_SaEn_max[:len(sortd_SaEn_max)-i]
#     new_sortd_Adaptation_up_min_SaEn_max = sortd_Adaptation_up_min_SaEn_max[:len(sortd_SaEn_max)-i]
#     new_sortd_Adaptation_down_min_SaEn_max = sortd_Adaptation_down_min_SaEn_max[:len(sortd_SaEn_max)-i]
#
#     slope_up, intercept_up, r_value_up, p_value_up, std_err_up = stats.linregress(new_sortd_SaEn_max, new_sortd_Adaptation_up_min_SaEn_max)
#     slope_down, intercept_down, r_value_down, p_value_down, std_err_down = stats.linregress(new_sortd_SaEn_max, new_sortd_Adaptation_down_min_SaEn_max)
#
#     R_squared_up = r_value_up**2
#     R_squared_down = r_value_down**2
#
#     predicted_values_up = slope_up * new_sortd_SaEn_max + intercept_up
#     predicted_values_down = slope_down * new_sortd_SaEn_max + intercept_down
#
#     plt.scatter(new_sortd_SaEn_max, new_sortd_Adaptation_up_min_SaEn_max, label="Data", color="blue")
#     plt.plot(new_sortd_SaEn_max, predicted_values_up, color="red", label=f"y={round(slope_up,2)}x+{round(intercept_up,2)}\nR^2={round(R_squared_up,3)}\np={round(p_value_up,3)}")
#     plt.xlabel("Sorted SaEn max")
#     plt.ylabel("Sorted Adaptation Up (min) SaEn max")
#     plt.title(f'Perturbation Up without the first {i} participants')
#     plt.legend()
#     plt.show()
#
#     plt.scatter(new_sortd_SaEn_max, new_sortd_Adaptation_down_min_SaEn_max, label="Data", color="blue")
#     plt.plot(new_sortd_SaEn_max, predicted_values_down, color="red", label=f"y={round(slope_down,2)}x+{round(intercept_down,2)}\nR^2 = {round(R_squared_down,3)}\np={round(p_value_down,3)}")
#     plt.xlabel("Sorted SaEn max")
#     plt.ylabel("Sorted Adaptation Down (min) SaEn max")
#     plt.title(f'Perturbation Down without the first {i} participants')
#     plt.legend()
#     plt.show()

# Regression of the SaEn_average by taking out one participant at the time from the highest to the lowest entropy
# for i in range(len(sortd_SaEn_average)-1):
#     print(i)
#     new_sortd_SaEn_average = sortd_SaEn_average[:len(sortd_SaEn_average)-i]
#     new_sortd_Adaptation_up_min_SaEn_average = sortd_Adaptation_up_min_SaEn_average[:len(sortd_SaEn_average)-i]
#     new_sortd_Adaptation_down_min_SaEn_average = sortd_Adaptation_down_min_SaEn_average[:len(sortd_SaEn_average)-i]
#
#     slope_up, intercept_up, r_value_up, p_value_up, std_err_up = stats.linregress(new_sortd_SaEn_average, new_sortd_Adaptation_up_min_SaEn_average)
#     slope_down, intercept_down, r_value_down, p_value_down, std_err_down = stats.linregress(new_sortd_SaEn_average, new_sortd_Adaptation_down_min_SaEn_average)
#
#     R_squared_up = r_value_up**2
#     R_squared_down = r_value_down**2
#
#     predicted_values_up = slope_up * new_sortd_SaEn_average + intercept_up
#     predicted_values_down = slope_down * new_sortd_SaEn_average + intercept_down
#
#     plt.scatter(new_sortd_SaEn_average, new_sortd_Adaptation_up_min_SaEn_average, label="Data", color="blue")
#     plt.plot(new_sortd_SaEn_average, predicted_values_up, color="red", label=f"y={round(slope_up,2)}x+{round(intercept_up,2)}\nR^2={round(R_squared_up,3)}\np={round(p_value_up,3)}")
#     plt.xlabel("Sorted SaEn average")
#     plt.ylabel("Sorted Adaptation Up (min) SaEn average")
#     plt.title(f'Perturbation Up without the first {i} participants')
#     plt.legend()
#     plt.show()
#
#     plt.scatter(new_sortd_SaEn_average, new_sortd_Adaptation_down_min_SaEn_average, label="Data", color="blue")
#     plt.plot(new_sortd_SaEn_average, predicted_values_down, color="red", label=f"y={round(slope_down,2)}x+{round(intercept_down,2)}\nR^2 = {round(R_squared_down,3)}\np={round(p_value_down,3)}")
#     plt.xlabel("Sorted SaEn average")
#     plt.ylabel("Sorted Adaptation Down (min) SaEn average")
#     plt.title(f'Perturbation Down without the first {i} participants')
#     plt.legend()
#     plt.show()

# Separate the SaEn and perturbations based on the quartiles of SaEn of 40
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Adjust width to fit all columns
pd.set_option('display.max_colwidth', None)  # Show full content in each cell

q1 = np.percentile(df_sort_SaEn_40['sortd_SaEn_40'], 25)
q2 = np.percentile(df_sort_SaEn_40['sortd_SaEn_40'], 50)
q3 = np.percentile(df_sort_SaEn_40['sortd_SaEn_40'], 75)

# Creating quartile-based subsets
Q1 = df_sort_SaEn_40[df_sort_SaEn_40['sortd_SaEn_40'] <= q1]
Q2 = df_sort_SaEn_40[(df_sort_SaEn_40['sortd_SaEn_40'] > q1) & (df_sort_SaEn_40['sortd_SaEn_40'] <= q2)]
Q3 = df_sort_SaEn_40[(df_sort_SaEn_40['sortd_SaEn_40'] > q2) & (df_sort_SaEn_40['sortd_SaEn_40'] <= q3)]
Q4 = df_sort_SaEn_40[df_sort_SaEn_40['sortd_SaEn_40'] > q3]

print(Q1.columns)
slope_up_Q1, intercept_up_Q1, r_value_up_Q1, p_value_up_Q1, std_err_up_Q1 = stats.linregress(Q1['sortd_SaEn_40'], Q1['sortd_Adaptation_up_min_SaEn_40'])
slope_up_Q2, intercept_up_Q2, r_value_up_Q2, p_value_up_Q2, std_err_up_Q2 = stats.linregress(Q2['sortd_SaEn_40'], Q2['sortd_Adaptation_up_min_SaEn_40'])
slope_up_Q3, intercept_up_Q3, r_value_up_Q3, p_value_up_Q3, std_err_up_Q3 = stats.linregress(Q3['sortd_SaEn_40'], Q3['sortd_Adaptation_up_min_SaEn_40'])
slope_up_Q4, intercept_up_Q4, r_value_up_Q4, p_value_up_Q4, std_err_up_Q4 = stats.linregress(Q4['sortd_SaEn_40'], Q4['sortd_Adaptation_up_min_SaEn_40'])

slope_down_Q1, intercept_down_Q1, r_value_down_Q1, p_value_down_Q1, std_err_down_Q1 = stats.linregress(Q1['sortd_SaEn_40'], Q1['sortd_Adaptation_down_min_SaEn_40'])
slope_down_Q2, intercept_down_Q2, r_value_down_Q2, p_value_down_Q2, std_err_down_Q2 = stats.linregress(Q2['sortd_SaEn_40'], Q2['sortd_Adaptation_down_min_SaEn_40'])
slope_down_Q3, intercept_down_Q3, r_value_down_Q3, p_value_down_Q3, std_err_down_Q3 = stats.linregress(Q3['sortd_SaEn_40'], Q3['sortd_Adaptation_down_min_SaEn_40'])
slope_down_Q4, intercept_down_Q4, r_value_down_Q4, p_value_down_Q4, std_err_down_Q4 = stats.linregress(Q4['sortd_SaEn_40'], Q4['sortd_Adaptation_down_min_SaEn_40'])

R_squared_up_Q1 = r_value_up_Q1**2
R_squared_up_Q2 = r_value_up_Q2**2
R_squared_up_Q3 = r_value_up_Q3**2
R_squared_up_Q4 = r_value_up_Q4**2
R_squared_down_Q1 = r_value_down_Q1**2
R_squared_down_Q2 = r_value_down_Q2**2
R_squared_down_Q3 = r_value_down_Q3**2
R_squared_down_Q4 = r_value_down_Q4**2

predicted_values_up_Q1 = slope_up_Q1 * Q1['sortd_SaEn_40'] + intercept_up_Q1
predicted_values_up_Q2 = slope_up_Q2 * Q2['sortd_SaEn_40'] + intercept_up_Q2
predicted_values_up_Q3 = slope_up_Q3 * Q3['sortd_SaEn_40'] + intercept_up_Q3
predicted_values_up_Q4 = slope_up_Q4 * Q4['sortd_SaEn_40'] + intercept_up_Q4

predicted_values_down_Q1 = slope_down_Q1 * Q1['sortd_SaEn_40'] + intercept_down_Q1
predicted_values_down_Q2 = slope_down_Q2 * Q2['sortd_SaEn_40'] + intercept_down_Q2
predicted_values_down_Q3 = slope_down_Q3 * Q3['sortd_SaEn_40'] + intercept_down_Q3
predicted_values_down_Q4 = slope_down_Q4 * Q4['sortd_SaEn_40'] + intercept_down_Q4


# Plot for perturbation up
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Sorted based on SaEn 40 and Perturbation Up")

axes[0, 0].scatter(Q1['sortd_SaEn_40'], Q1['sortd_Adaptation_up_min_SaEn_40'], color="blue")
axes[0, 0].plot(Q1['sortd_SaEn_40'], predicted_values_up_Q1, color="red")
axes[0, 0].set_title(f"Q1 y={round(slope_up_Q1, 2)}x+{round(intercept_up_Q1, 2)}\nR^2 = {round(R_squared_up_Q1, 3)}, p={round(p_value_up_Q1,3)}")
axes[0, 0].set_ylabel("Adaptation Time")

axes[1, 0].scatter(Q2['sortd_SaEn_40'], Q2['sortd_Adaptation_up_min_SaEn_40'], color="blue")
axes[1, 0].plot(Q2['sortd_SaEn_40'], predicted_values_up_Q2, color="red")
axes[1, 0].set_title(f"Q2 y={round(slope_up_Q2, 2)}x+{round(intercept_up_Q2, 2)}\nR^2 = {round(R_squared_up_Q2, 3)}, p={round(p_value_up_Q2,3)}")
axes[1, 0].set_xlabel("SaEn_40")
axes[1, 0].set_ylabel("Adaptation Time")

axes[0, 1].scatter(Q3['sortd_SaEn_40'], Q3['sortd_Adaptation_up_min_SaEn_40'], color="blue")
axes[0, 1].plot(Q3['sortd_SaEn_40'], predicted_values_up_Q3, color="red")
axes[0, 1].set_title(f"Q3 y={round(slope_up_Q3, 2)}x+{round(intercept_up_Q3, 2)}\nR^2 = {round(R_squared_up_Q3, 3)}, p={round(p_value_up_Q3,3)}")

axes[1, 1].scatter(Q4['sortd_SaEn_40'], Q4['sortd_Adaptation_up_min_SaEn_40'], color="blue")
axes[1, 1].plot(Q4['sortd_SaEn_40'], predicted_values_up_Q4, color="red")
axes[1, 1].set_title(f"Q4 y={round(slope_up_Q4, 2)}x+{round(intercept_up_Q4, 2)}\nR^2 = {round(R_squared_up_Q4, 3)}, p={round(p_value_up_Q4,3)}")
axes[1, 1].set_ylabel("Adaptation Time")
axes[1, 1].set_xlabel("SaEn_40")

# Adjust layout
plt.tight_layout()
plt.show()


# Plot for perturbation down
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Sorted based on SaEn 40 and Perturbation down")

axes[0, 0].scatter(Q1['sortd_SaEn_40'], Q1['sortd_Adaptation_down_min_SaEn_40'], color="blue")
axes[0, 0].plot(Q1['sortd_SaEn_40'], predicted_values_down_Q1, color="red")
axes[0, 0].set_title(f"Q1 y={round(slope_down_Q1, 2)}x+{round(intercept_down_Q1, 2)}\nR^2 = {round(R_squared_down_Q1, 3)}, p={round(p_value_down_Q1,3)}")
axes[0, 0].set_ylabel("Adaptation Time")

axes[1, 0].scatter(Q2['sortd_SaEn_40'], Q2['sortd_Adaptation_down_min_SaEn_40'], color="blue")
axes[1, 0].plot(Q2['sortd_SaEn_40'], predicted_values_down_Q2, color="red")
axes[1, 0].set_title(f"Q2 y={round(slope_down_Q2, 2)}x+{round(intercept_down_Q2, 2)}\nR^2 = {round(R_squared_down_Q2, 3)}, p={round(p_value_down_Q2,3)}")
axes[1, 0].set_xlabel("SaEn_40")
axes[1, 0].set_ylabel("Adaptation Time")

axes[0, 1].scatter(Q3['sortd_SaEn_40'], Q3['sortd_Adaptation_down_min_SaEn_40'], color="blue")
axes[0, 1].plot(Q3['sortd_SaEn_40'], predicted_values_down_Q3, color="red")
axes[0, 1].set_title(f"Q3 y={round(slope_down_Q3, 2)}x+{round(intercept_down_Q3, 2)}\nR^2 = {round(R_squared_down_Q3, 3)}, p={round(p_value_down_Q3,3)}")

axes[1, 1].scatter(Q4['sortd_SaEn_40'], Q4['sortd_Adaptation_down_min_SaEn_40'], color="blue")
axes[1, 1].plot(Q4['sortd_SaEn_40'], predicted_values_down_Q4, color="red")
axes[1, 1].set_title(f"Q4 y={round(slope_down_Q4, 2)}x+{round(intercept_down_Q4, 2)}\nR^2 = {round(R_squared_down_Q4, 3)}, p={round(p_value_down_Q4,3)}")
axes[1, 1].set_ylabel("Adaptation Time")
axes[1, 1].set_xlabel("SaEn_40")

# Adjust layout
plt.tight_layout()
plt.show()


# Separate the SaEn and perturbations based on the quartiles of SaEn of 20
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Adjust width to fit all columns
pd.set_option('display.max_colwidth', None)  # Show full content in each cell

q1 = np.percentile(df_sort_SaEn_20['sortd_SaEn_20'], 25)
q2 = np.percentile(df_sort_SaEn_20['sortd_SaEn_20'], 50)
q3 = np.percentile(df_sort_SaEn_20['sortd_SaEn_20'], 75)

# Creating quartile-based subsets
Q1 = df_sort_SaEn_20[df_sort_SaEn_20['sortd_SaEn_20'] <= q1]
Q2 = df_sort_SaEn_20[(df_sort_SaEn_20['sortd_SaEn_20'] > q1) & (df_sort_SaEn_20['sortd_SaEn_20'] <= q2)]
Q3 = df_sort_SaEn_20[(df_sort_SaEn_20['sortd_SaEn_20'] > q2) & (df_sort_SaEn_20['sortd_SaEn_20'] <= q3)]
Q4 = df_sort_SaEn_20[df_sort_SaEn_20['sortd_SaEn_20'] > q3]

print(Q1.columns)
slope_up_Q1, intercept_up_Q1, r_value_up_Q1, p_value_up_Q1, std_err_up_Q1 = stats.linregress(Q1['sortd_SaEn_20'], Q1['sortd_Adaptation_up_min_SaEn_20'])
slope_up_Q2, intercept_up_Q2, r_value_up_Q2, p_value_up_Q2, std_err_up_Q2 = stats.linregress(Q2['sortd_SaEn_20'], Q2['sortd_Adaptation_up_min_SaEn_20'])
slope_up_Q3, intercept_up_Q3, r_value_up_Q3, p_value_up_Q3, std_err_up_Q3 = stats.linregress(Q3['sortd_SaEn_20'], Q3['sortd_Adaptation_up_min_SaEn_20'])
slope_up_Q4, intercept_up_Q4, r_value_up_Q4, p_value_up_Q4, std_err_up_Q4 = stats.linregress(Q4['sortd_SaEn_20'], Q4['sortd_Adaptation_up_min_SaEn_20'])

slope_down_Q1, intercept_down_Q1, r_value_down_Q1, p_value_down_Q1, std_err_down_Q1 = stats.linregress(Q1['sortd_SaEn_20'], Q1['sortd_Adaptation_down_min_SaEn_20'])
slope_down_Q2, intercept_down_Q2, r_value_down_Q2, p_value_down_Q2, std_err_down_Q2 = stats.linregress(Q2['sortd_SaEn_20'], Q2['sortd_Adaptation_down_min_SaEn_20'])
slope_down_Q3, intercept_down_Q3, r_value_down_Q3, p_value_down_Q3, std_err_down_Q3 = stats.linregress(Q3['sortd_SaEn_20'], Q3['sortd_Adaptation_down_min_SaEn_20'])
slope_down_Q4, intercept_down_Q4, r_value_down_Q4, p_value_down_Q4, std_err_down_Q4 = stats.linregress(Q4['sortd_SaEn_20'], Q4['sortd_Adaptation_down_min_SaEn_20'])

R_squared_up_Q1 = r_value_up_Q1**2
R_squared_up_Q2 = r_value_up_Q2**2
R_squared_up_Q3 = r_value_up_Q3**2
R_squared_up_Q4 = r_value_up_Q4**2
R_squared_down_Q1 = r_value_down_Q1**2
R_squared_down_Q2 = r_value_down_Q2**2
R_squared_down_Q3 = r_value_down_Q3**2
R_squared_down_Q4 = r_value_down_Q4**2

predicted_values_up_Q1 = slope_up_Q1 * Q1['sortd_SaEn_20'] + intercept_up_Q1
predicted_values_up_Q2 = slope_up_Q2 * Q2['sortd_SaEn_20'] + intercept_up_Q2
predicted_values_up_Q3 = slope_up_Q3 * Q3['sortd_SaEn_20'] + intercept_up_Q3
predicted_values_up_Q4 = slope_up_Q4 * Q4['sortd_SaEn_20'] + intercept_up_Q4

predicted_values_down_Q1 = slope_down_Q1 * Q1['sortd_SaEn_20'] + intercept_down_Q1
predicted_values_down_Q2 = slope_down_Q2 * Q2['sortd_SaEn_20'] + intercept_down_Q2
predicted_values_down_Q3 = slope_down_Q3 * Q3['sortd_SaEn_20'] + intercept_down_Q3
predicted_values_down_Q4 = slope_down_Q4 * Q4['sortd_SaEn_20'] + intercept_down_Q4


# Plot for perturbation up
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Sorted based on SaEn 20")

axes[0, 0].scatter(Q1['sortd_SaEn_20'], Q1['sortd_Adaptation_up_min_SaEn_20'], color="blue")
axes[0, 0].plot(Q1['sortd_SaEn_20'], predicted_values_up_Q1, color="red")
axes[0, 0].set_title(f"Q1 y={round(slope_up_Q1, 2)}x+{round(intercept_up_Q1, 2)}\nR^2 = {round(R_squared_up_Q1, 3)}, p={round(p_value_up_Q1,3)}")
axes[0, 0].set_ylabel("Adaptation Time")

axes[1, 0].scatter(Q2['sortd_SaEn_20'], Q2['sortd_Adaptation_up_min_SaEn_20'], color="blue")
axes[1, 0].plot(Q2['sortd_SaEn_20'], predicted_values_up_Q2, color="red")
axes[1, 0].set_title(f"Q2 y={round(slope_up_Q2, 2)}x+{round(intercept_up_Q2, 2)}\nR^2 = {round(R_squared_up_Q2, 3)}, p={round(p_value_up_Q2,3)}")
axes[1, 0].set_xlabel("SaEn_20")
axes[1, 0].set_ylabel("Adaptation Time")

axes[0, 1].scatter(Q3['sortd_SaEn_20'], Q3['sortd_Adaptation_up_min_SaEn_20'], color="blue")
axes[0, 1].plot(Q3['sortd_SaEn_20'], predicted_values_up_Q3, color="red")
axes[0, 1].set_title(f"Q3 y={round(slope_up_Q3, 2)}x+{round(intercept_up_Q3, 2)}\nR^2 = {round(R_squared_up_Q3, 3)}, p={round(p_value_up_Q3,3)}")

axes[1, 1].scatter(Q4['sortd_SaEn_20'], Q4['sortd_Adaptation_up_min_SaEn_20'], color="blue")
axes[1, 1].plot(Q4['sortd_SaEn_20'], predicted_values_up_Q4, color="red")
axes[1, 1].set_title(f"Q4 y={round(slope_up_Q4, 2)}x+{round(intercept_up_Q4, 2)}\nR^2 = {round(R_squared_up_Q4, 3)}, p={round(p_value_up_Q4,3)}")
axes[1, 1].set_ylabel("Adaptation Time")
axes[1, 1].set_xlabel("SaEn_20")


# Adjust layout
plt.tight_layout()
plt.show()

# Plot for perturbation down
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Sorted based on SaEn 20")

axes[0, 0].scatter(Q1['sortd_SaEn_20'], Q1['sortd_Adaptation_down_min_SaEn_20'], color="blue")
axes[0, 0].plot(Q1['sortd_SaEn_20'], predicted_values_down_Q1, color="red")
axes[0, 0].set_title(f"Q1 y={round(slope_down_Q1, 2)}x+{round(intercept_down_Q1, 2)}\nR^2 = {round(R_squared_down_Q1, 3)}, p={round(p_value_down_Q1,3)}")
axes[0, 0].set_ylabel("Adaptation Time")

axes[1, 0].scatter(Q2['sortd_SaEn_20'], Q2['sortd_Adaptation_down_min_SaEn_20'], color="blue")
axes[1, 0].plot(Q2['sortd_SaEn_20'], predicted_values_down_Q2, color="red")
axes[1, 0].set_title(f"Q2 y={round(slope_down_Q2, 2)}x+{round(intercept_down_Q2, 2)}\nR^2 = {round(R_squared_down_Q2, 3)}, p={round(p_value_down_Q2,3)}")
axes[1, 0].set_xlabel("SaEn_20")
axes[1, 0].set_ylabel("Adaptation Time")

axes[0, 1].scatter(Q3['sortd_SaEn_20'], Q3['sortd_Adaptation_down_min_SaEn_20'], color="blue")
axes[0, 1].plot(Q3['sortd_SaEn_20'], predicted_values_down_Q3, color="red")
axes[0, 1].set_title(f"Q3 y={round(slope_down_Q3, 2)}x+{round(intercept_down_Q3, 2)}\nR^2 = {round(R_squared_down_Q3, 3)}, p={round(p_value_down_Q3,3)}")

axes[1, 1].scatter(Q4['sortd_SaEn_20'], Q4['sortd_Adaptation_down_min_SaEn_20'], color="blue")
axes[1, 1].plot(Q4['sortd_SaEn_20'], predicted_values_down_Q4, color="red")
axes[1, 1].set_title(f"Q4 y={round(slope_down_Q4, 2)}x+{round(intercept_down_Q4, 2)}\nR^2 = {round(R_squared_down_Q4, 3)}, p={round(p_value_down_Q4,3)}")
axes[1, 1].set_ylabel("Adaptation Time")
axes[1, 1].set_xlabel("SaEn_20")


# Adjust layout
plt.tight_layout()
plt.show()


# # Separate the SaEn and perturbations based on the quartiles of max SaEn
# pd.set_option('display.max_rows', None)  # Show all rows
# pd.set_option('display.max_columns', None)  # Show all columns
# pd.set_option('display.width', None)  # Adjust width to fit all columns
# pd.set_option('display.max_colwidth', None)  # Show full content in each cell
#
# q1 = np.percentile(df_sort_SaEn_max['sortd_SaEn_max'], 25)
# q2 = np.percentile(df_sort_SaEn_max['sortd_SaEn_max'], 50)
# q3 = np.percentile(df_sort_SaEn_max['sortd_SaEn_max'], 75)
#
# # Creating quartile-based subsets
# Q1 = df_sort_SaEn_max[df_sort_SaEn_max['sortd_SaEn_max'] <= q1]
# Q2 = df_sort_SaEn_max[(df_sort_SaEn_max['sortd_SaEn_max'] > q1) & (df_sort_SaEn_max['sortd_SaEn_max'] <= q2)]
# Q3 = df_sort_SaEn_max[(df_sort_SaEn_max['sortd_SaEn_max'] > q2) & (df_sort_SaEn_max['sortd_SaEn_max'] <= q3)]
# Q4 = df_sort_SaEn_max[df_sort_SaEn_max['sortd_SaEn_max'] > q3]
#
# print(Q1.columns)
# slope_up_Q1, intercept_up_Q1, r_value_up_Q1, p_value_up_Q1, std_err_up_Q1 = stats.linregress(Q1['sortd_SaEn_max'], Q1['sortd_Adaptation_up_min_SaEn_max'])
# slope_up_Q2, intercept_up_Q2, r_value_up_Q2, p_value_up_Q2, std_err_up_Q2 = stats.linregress(Q2['sortd_SaEn_max'], Q2['sortd_Adaptation_up_min_SaEn_max'])
# slope_up_Q3, intercept_up_Q3, r_value_up_Q3, p_value_up_Q3, std_err_up_Q3 = stats.linregress(Q3['sortd_SaEn_max'], Q3['sortd_Adaptation_up_min_SaEn_max'])
# slope_up_Q4, intercept_up_Q4, r_value_up_Q4, p_value_up_Q4, std_err_up_Q4 = stats.linregress(Q4['sortd_SaEn_max'], Q4['sortd_Adaptation_up_min_SaEn_max'])
#
# slope_down_Q1, intercept_down_Q1, r_value_down_Q1, p_value_down_Q1, std_err_down_Q1 = stats.linregress(Q1['sortd_SaEn_max'], Q1['sortd_Adaptation_down_min_SaEn_max'])
# slope_down_Q2, intercept_down_Q2, r_value_down_Q2, p_value_down_Q2, std_err_down_Q2 = stats.linregress(Q2['sortd_SaEn_max'], Q2['sortd_Adaptation_down_min_SaEn_max'])
# slope_down_Q3, intercept_down_Q3, r_value_down_Q3, p_value_down_Q3, std_err_down_Q3 = stats.linregress(Q3['sortd_SaEn_max'], Q3['sortd_Adaptation_down_min_SaEn_max'])
# slope_down_Q4, intercept_down_Q4, r_value_down_Q4, p_value_down_Q4, std_err_down_Q4 = stats.linregress(Q4['sortd_SaEn_max'], Q4['sortd_Adaptation_down_min_SaEn_max'])
#
# R_squared_up_Q1 = r_value_up_Q1**2
# R_squared_up_Q2 = r_value_up_Q2**2
# R_squared_up_Q3 = r_value_up_Q3**2
# R_squared_up_Q4 = r_value_up_Q4**2
# R_squared_down_Q1 = r_value_down_Q1**2
# R_squared_down_Q2 = r_value_down_Q2**2
# R_squared_down_Q3 = r_value_down_Q3**2
# R_squared_down_Q4 = r_value_down_Q4**2
#
# predicted_values_up_Q1 = slope_up_Q1 * Q1['sortd_SaEn_max'] + intercept_up_Q1
# predicted_values_up_Q2 = slope_up_Q2 * Q2['sortd_SaEn_max'] + intercept_up_Q2
# predicted_values_up_Q3 = slope_up_Q3 * Q3['sortd_SaEn_max'] + intercept_up_Q3
# predicted_values_up_Q4 = slope_up_Q4 * Q4['sortd_SaEn_max'] + intercept_up_Q4
#
# predicted_values_down_Q1 = slope_down_Q1 * Q1['sortd_SaEn_max'] + intercept_down_Q1
# predicted_values_down_Q2 = slope_down_Q2 * Q2['sortd_SaEn_max'] + intercept_down_Q2
# predicted_values_down_Q3 = slope_down_Q3 * Q3['sortd_SaEn_max'] + intercept_down_Q3
# predicted_values_down_Q4 = slope_down_Q4 * Q4['sortd_SaEn_max'] + intercept_down_Q4
#
#
# # Plot for perturbation up
# fig, axes = plt.subplots(2, 2, figsize=(10, 8))
# fig.suptitle("Sorted based on SaEn Max")
#
# # Plot for sortd_Adaptation_up_min_SaEn_max
# axes[0, 0].scatter(Q1['sortd_SaEn_max'], Q1['sortd_Adaptation_up_min_SaEn_max'], color="blue")
# axes[0, 0].plot(Q1['sortd_SaEn_max'], predicted_values_up_Q1, color="red")
# axes[0, 0].set_title(f"Q1 y={round(slope_up_Q1, 2)}x+{round(intercept_up_Q1, 2)}\nR^2 = {round(R_squared_up_Q1, 3)}, p={round(p_value_up_Q1,3)}")
# axes[0, 0].set_ylabel("Adaptation Time")
#
# axes[1, 0].scatter(Q2['sortd_SaEn_max'], Q2['sortd_Adaptation_up_min_SaEn_max'], color="blue")
# axes[1, 0].plot(Q2['sortd_SaEn_max'], predicted_values_up_Q2, color="red")
# axes[1, 0].set_title(f"Q2 y={round(slope_up_Q2, 2)}x+{round(intercept_up_Q2, 2)}\nR^2 = {round(R_squared_up_Q2, 3)}, p={round(p_value_up_Q2,3)}")
# axes[1, 0].set_xlabel("SaEn_max")
# axes[1, 0].set_ylabel("Adaptation Time")
#
# axes[0, 1].scatter(Q3['sortd_SaEn_max'], Q3['sortd_Adaptation_up_min_SaEn_max'], color="blue")
# axes[0, 1].plot(Q3['sortd_SaEn_max'], predicted_values_up_Q3, color="red")
# axes[0, 1].set_title(f"Q3 y={round(slope_up_Q3, 2)}x+{round(intercept_up_Q3, 2)}\nR^2 = {round(R_squared_up_Q3, 3)}, p={round(p_value_up_Q3,3)}")
#
# axes[1, 1].scatter(Q4['sortd_SaEn_max'], Q4['sortd_Adaptation_up_min_SaEn_max'], color="blue")
# axes[1, 1].plot(Q4['sortd_SaEn_max'], predicted_values_up_Q4, color="red")
# axes[1, 1].set_title(f"Q4 y={round(slope_up_Q4, 2)}x+{round(intercept_up_Q4, 2)}\nR^2 = {round(R_squared_up_Q4, 3)}, p={round(p_value_up_Q4,3)}")
# axes[1, 1].set_ylabel("Adaptation Time")
# axes[1, 1].set_xlabel("SaEn_max")
#
#
# # Adjust layout
# plt.tight_layout()
# plt.show()
#
# # Plot for perturbation down
# fig, axes = plt.subplots(2, 2, figsize=(10, 8))
# fig.suptitle("Sorted based on SaEn Max")
#
# # Plot for sortd_Adaptation_down_min_SaEn_max
# axes[0, 0].scatter(Q1['sortd_SaEn_max'], Q1['sortd_Adaptation_down_min_SaEn_max'], color="blue")
# axes[0, 0].plot(Q1['sortd_SaEn_max'], predicted_values_down_Q1, color="red")
# axes[0, 0].set_title(f"Q1 y={round(slope_down_Q1, 2)}x+{round(intercept_down_Q1, 2)}\nR^2 = {round(R_squared_down_Q1, 3)}, p={round(p_value_down_Q1,3)}")
# axes[0, 0].set_ylabel("Adaptation Time")
#
# axes[1, 0].scatter(Q2['sortd_SaEn_max'], Q2['sortd_Adaptation_down_min_SaEn_max'], color="blue")
# axes[1, 0].plot(Q2['sortd_SaEn_max'], predicted_values_down_Q2, color="red")
# axes[1, 0].set_title(f"Q2 y={round(slope_down_Q2, 2)}x+{round(intercept_down_Q2, 2)}\nR^2 = {round(R_squared_down_Q2, 3)}, p={round(p_value_down_Q2,3)}")
# axes[1, 0].set_xlabel("SaEn_max")
# axes[1, 0].set_ylabel("Adaptation Time")
#
# axes[0, 1].scatter(Q3['sortd_SaEn_max'], Q3['sortd_Adaptation_down_min_SaEn_max'], color="blue")
# axes[0, 1].plot(Q3['sortd_SaEn_max'], predicted_values_down_Q3, color="red")
# axes[0, 1].set_title(f"Q3 y={round(slope_down_Q3, 2)}x+{round(intercept_down_Q3, 2)}\nR^2 = {round(R_squared_down_Q3, 3)}, p={round(p_value_down_Q3,3)}")
#
# axes[1, 1].scatter(Q4['sortd_SaEn_max'], Q4['sortd_Adaptation_down_min_SaEn_max'], color="blue")
# axes[1, 1].plot(Q4['sortd_SaEn_max'], predicted_values_down_Q4, color="red")
# axes[1, 1].set_title(f"Q4 y={round(slope_down_Q4, 2)}x+{round(intercept_down_Q4, 2)}\nR^2 = {round(R_squared_down_Q4, 3)}, p={round(p_value_down_Q4,3)}")
# axes[1, 1].set_ylabel("Adaptation Time")
# axes[1, 1].set_xlabel("SaEn_max")
#
#
# # Adjust layout
# plt.tight_layout()
# plt.show()

# # Separate the SaEn and perturbations based on the quartiles of average SaEn
# pd.set_option('display.max_rows', None)  # Show all rows
# pd.set_option('display.max_columns', None)  # Show all columns
# pd.set_option('display.width', None)  # Adjust width to fit all columns
# pd.set_option('display.max_colwidth', None)  # Show full content in each cell
#
# q1 = np.percentile(df_sort_SaEn_average['sortd_SaEn_average'], 25)
# q2 = np.percentile(df_sort_SaEn_average['sortd_SaEn_average'], 50)
# q3 = np.percentile(df_sort_SaEn_average['sortd_SaEn_average'], 75)
#
# # Creating quartile-based subsets
# Q1 = df_sort_SaEn_average[df_sort_SaEn_average['sortd_SaEn_average'] <= q1]
# Q2 = df_sort_SaEn_average[(df_sort_SaEn_average['sortd_SaEn_average'] > q1) & (df_sort_SaEn_average['sortd_SaEn_average'] <= q2)]
# Q3 = df_sort_SaEn_average[(df_sort_SaEn_average['sortd_SaEn_average'] > q2) & (df_sort_SaEn_average['sortd_SaEn_average'] <= q3)]
# Q4 = df_sort_SaEn_average[df_sort_SaEn_average['sortd_SaEn_average'] > q3]
#
# print(Q1.columns)
# slope_up_Q1, intercept_up_Q1, r_value_up_Q1, p_value_up_Q1, std_err_up_Q1 = stats.linregress(Q1['sortd_SaEn_average'], Q1['sortd_Adaptation_up_min_SaEn_average'])
# slope_up_Q2, intercept_up_Q2, r_value_up_Q2, p_value_up_Q2, std_err_up_Q2 = stats.linregress(Q2['sortd_SaEn_average'], Q2['sortd_Adaptation_up_min_SaEn_average'])
# slope_up_Q3, intercept_up_Q3, r_value_up_Q3, p_value_up_Q3, std_err_up_Q3 = stats.linregress(Q3['sortd_SaEn_average'], Q3['sortd_Adaptation_up_min_SaEn_average'])
# slope_up_Q4, intercept_up_Q4, r_value_up_Q4, p_value_up_Q4, std_err_up_Q4 = stats.linregress(Q4['sortd_SaEn_average'], Q4['sortd_Adaptation_up_min_SaEn_average'])
#
# slope_down_Q1, intercept_down_Q1, r_value_down_Q1, p_value_down_Q1, std_err_down_Q1 = stats.linregress(Q1['sortd_SaEn_average'], Q1['sortd_Adaptation_down_min_SaEn_average'])
# slope_down_Q2, intercept_down_Q2, r_value_down_Q2, p_value_down_Q2, std_err_down_Q2 = stats.linregress(Q2['sortd_SaEn_average'], Q2['sortd_Adaptation_down_min_SaEn_average'])
# slope_down_Q3, intercept_down_Q3, r_value_down_Q3, p_value_down_Q3, std_err_down_Q3 = stats.linregress(Q3['sortd_SaEn_average'], Q3['sortd_Adaptation_down_min_SaEn_average'])
# slope_down_Q4, intercept_down_Q4, r_value_down_Q4, p_value_down_Q4, std_err_down_Q4 = stats.linregress(Q4['sortd_SaEn_average'], Q4['sortd_Adaptation_down_min_SaEn_average'])
#
# R_squared_up_Q1 = r_value_up_Q1**2
# R_squared_up_Q2 = r_value_up_Q2**2
# R_squared_up_Q3 = r_value_up_Q3**2
# R_squared_up_Q4 = r_value_up_Q4**2
# R_squared_down_Q1 = r_value_down_Q1**2
# R_squared_down_Q2 = r_value_down_Q2**2
# R_squared_down_Q3 = r_value_down_Q3**2
# R_squared_down_Q4 = r_value_down_Q4**2
#
# predicted_values_up_Q1 = slope_up_Q1 * Q1['sortd_SaEn_average'] + intercept_up_Q1
# predicted_values_up_Q2 = slope_up_Q2 * Q2['sortd_SaEn_average'] + intercept_up_Q2
# predicted_values_up_Q3 = slope_up_Q3 * Q3['sortd_SaEn_average'] + intercept_up_Q3
# predicted_values_up_Q4 = slope_up_Q4 * Q4['sortd_SaEn_average'] + intercept_up_Q4
#
# predicted_values_down_Q1 = slope_down_Q1 * Q1['sortd_SaEn_average'] + intercept_down_Q1
# predicted_values_down_Q2 = slope_down_Q2 * Q2['sortd_SaEn_average'] + intercept_down_Q2
# predicted_values_down_Q3 = slope_down_Q3 * Q3['sortd_SaEn_average'] + intercept_down_Q3
# predicted_values_down_Q4 = slope_down_Q4 * Q4['sortd_SaEn_average'] + intercept_down_Q4
#
#
# # Plot for perturbation up
# fig, axes = plt.subplots(2, 2, figsize=(10, 8))
# fig.suptitle("Sorted based on SaEn Average")
#
# axes[0, 0].scatter(Q1['sortd_SaEn_average'], Q1['sortd_Adaptation_up_min_SaEn_average'], color="blue")
# axes[0, 0].plot(Q1['sortd_SaEn_average'], predicted_values_up_Q1, color="red")
# axes[0, 0].set_title(f"Q1 y={round(slope_up_Q1, 2)}x+{round(intercept_up_Q1, 2)}\nR^2 = {round(R_squared_up_Q1, 3)}, p={round(p_value_up_Q1,3)}")
# axes[0, 0].set_ylabel("Adaptation Time")
#
# axes[1, 0].scatter(Q2['sortd_SaEn_average'], Q2['sortd_Adaptation_up_min_SaEn_average'], color="blue")
# axes[1, 0].plot(Q2['sortd_SaEn_average'], predicted_values_up_Q2, color="red")
# axes[1, 0].set_title(f"Q2 y={round(slope_up_Q2, 2)}x+{round(intercept_up_Q2, 2)}\nR^2 = {round(R_squared_up_Q2, 3)}, p={round(p_value_up_Q2,3)}")
# axes[1, 0].set_xlabel("SaEn_average")
# axes[1, 0].set_ylabel("Adaptation Time")
#
# axes[0, 1].scatter(Q3['sortd_SaEn_average'], Q3['sortd_Adaptation_up_min_SaEn_average'], color="blue")
# axes[0, 1].plot(Q3['sortd_SaEn_average'], predicted_values_up_Q3, color="red")
# axes[0, 1].set_title(f"Q3 y={round(slope_up_Q3, 2)}x+{round(intercept_up_Q3, 2)}\nR^2 = {round(R_squared_up_Q3, 3)}, p={round(p_value_up_Q3,3)}")
#
# axes[1, 1].scatter(Q4['sortd_SaEn_average'], Q4['sortd_Adaptation_up_min_SaEn_average'], color="blue")
# axes[1, 1].plot(Q4['sortd_SaEn_average'], predicted_values_up_Q4, color="red")
# axes[1, 1].set_title(f"Q4 y={round(slope_up_Q4, 2)}x+{round(intercept_up_Q4, 2)}\nR^2 = {round(R_squared_up_Q4, 3)}, p={round(p_value_up_Q4,3)}")
# axes[1, 1].set_ylabel("Adaptation Time")
# axes[1, 1].set_xlabel("SaEn_average")
#
#
# # Adjust layout
# plt.tight_layout()
# plt.show()
#
# # Plot for perturbation down
# fig, axes = plt.subplots(2, 2, figsize=(10, 8))
# fig.suptitle("Sorted based on SaEn Average")
#
# axes[0, 0].scatter(Q1['sortd_SaEn_average'], Q1['sortd_Adaptation_down_min_SaEn_average'], color="blue")
# axes[0, 0].plot(Q1['sortd_SaEn_average'], predicted_values_down_Q1, color="red")
# axes[0, 0].set_title(f"Q1 y={round(slope_down_Q1, 2)}x+{round(intercept_down_Q1, 2)}\nR^2 = {round(R_squared_down_Q1, 3)}, p={round(p_value_down_Q1,3)}")
# axes[0, 0].set_ylabel("Adaptation Time")
#
# axes[1, 0].scatter(Q2['sortd_SaEn_average'], Q2['sortd_Adaptation_down_min_SaEn_average'], color="blue")
# axes[1, 0].plot(Q2['sortd_SaEn_average'], predicted_values_down_Q2, color="red")
# axes[1, 0].set_title(f"Q2 y={round(slope_down_Q2, 2)}x+{round(intercept_down_Q2, 2)}\nR^2 = {round(R_squared_down_Q2, 3)}, p={round(p_value_down_Q2,3)}")
# axes[1, 0].set_xlabel("SaEn_average")
# axes[1, 0].set_ylabel("Adaptation Time")
#
# axes[0, 1].scatter(Q3['sortd_SaEn_average'], Q3['sortd_Adaptation_down_min_SaEn_average'], color="blue")
# axes[0, 1].plot(Q3['sortd_SaEn_average'], predicted_values_down_Q3, color="red")
# axes[0, 1].set_title(f"Q3 y={round(slope_down_Q3, 2)}x+{round(intercept_down_Q3, 2)}\nR^2 = {round(R_squared_down_Q3, 3)}, p={round(p_value_down_Q3,3)}")
#
# axes[1, 1].scatter(Q4['sortd_SaEn_average'], Q4['sortd_Adaptation_down_min_SaEn_average'], color="blue")
# axes[1, 1].plot(Q4['sortd_SaEn_average'], predicted_values_down_Q4, color="red")
# axes[1, 1].set_title(f"Q4 y={round(slope_down_Q4, 2)}x+{round(intercept_down_Q4, 2)}\nR^2 = {round(R_squared_down_Q4, 3)}, p={round(p_value_down_Q4,3)}")
# axes[1, 1].set_ylabel("Adaptation Time")
# axes[1, 1].set_xlabel("SaEn_average")
#
#
# # Adjust layout
# plt.tight_layout()
# plt.show()


# Separate the SaEn and perturbations based on the quartiles of SaEn_Adaptation_up_min_before_pert
# pd.set_option('display.max_rows', None)  # Show all rows
# pd.set_option('display.max_columns', None)  # Show all columns
# pd.set_option('display.width', None)  # Adjust width to fit all columns
# pd.set_option('display.max_colwidth', None)  # Show full content in each cell
#
# q1 = np.percentile(df_sort_SaEn_Adaptation_up_min_before_pert['sortd_SaEn_Adaptation_up_min_before_pert'], 25)
# q2 = np.percentile(df_sort_SaEn_Adaptation_up_min_before_pert['sortd_SaEn_Adaptation_up_min_before_pert'], 50)
# q3 = np.percentile(df_sort_SaEn_Adaptation_up_min_before_pert['sortd_SaEn_Adaptation_up_min_before_pert'], 75)
#
# # Creating quartile-based subsets
# Q1 = df_sort_SaEn_Adaptation_up_min_before_pert[df_sort_SaEn_Adaptation_up_min_before_pert['sortd_SaEn_Adaptation_up_min_before_pert'] <= q1]
# Q2 = df_sort_SaEn_Adaptation_up_min_before_pert[(df_sort_SaEn_Adaptation_up_min_before_pert['sortd_SaEn_Adaptation_up_min_before_pert'] > q1) & (df_sort_SaEn_Adaptation_up_min_before_pert['sortd_SaEn_Adaptation_up_min_before_pert'] <= q2)]
# Q3 = df_sort_SaEn_Adaptation_up_min_before_pert[(df_sort_SaEn_Adaptation_up_min_before_pert['sortd_SaEn_Adaptation_up_min_before_pert'] > q2) & (df_sort_SaEn_Adaptation_up_min_before_pert['sortd_SaEn_Adaptation_up_min_before_pert'] <= q3)]
# Q4 = df_sort_SaEn_Adaptation_up_min_before_pert[df_sort_SaEn_Adaptation_up_min_before_pert['sortd_SaEn_Adaptation_up_min_before_pert'] > q3]
#
# print(Q1.columns)
# slope_up_Q1, intercept_up_Q1, r_value_up_Q1, p_value_up_Q1, std_err_up_Q1 = stats.linregress(Q1['sortd_SaEn_Adaptation_up_min_before_pert'], Q1['sortd_Adaptation_up_min_SaEn_Adaptation_up_min_before_pert'])
# slope_up_Q2, intercept_up_Q2, r_value_up_Q2, p_value_up_Q2, std_err_up_Q2 = stats.linregress(Q2['sortd_SaEn_Adaptation_up_min_before_pert'], Q2['sortd_Adaptation_up_min_SaEn_Adaptation_up_min_before_pert'])
# slope_up_Q3, intercept_up_Q3, r_value_up_Q3, p_value_up_Q3, std_err_up_Q3 = stats.linregress(Q3['sortd_SaEn_Adaptation_up_min_before_pert'], Q3['sortd_Adaptation_up_min_SaEn_Adaptation_up_min_before_pert'])
# slope_up_Q4, intercept_up_Q4, r_value_up_Q4, p_value_up_Q4, std_err_up_Q4 = stats.linregress(Q4['sortd_SaEn_Adaptation_up_min_before_pert'], Q4['sortd_Adaptation_up_min_SaEn_Adaptation_up_min_before_pert'])
#
#
# R_squared_up_Q1 = r_value_up_Q1**2
# R_squared_up_Q2 = r_value_up_Q2**2
# R_squared_up_Q3 = r_value_up_Q3**2
# R_squared_up_Q4 = r_value_up_Q4**2
#
#
# predicted_values_up_Q1 = slope_up_Q1 * Q1['sortd_SaEn_Adaptation_up_min_before_pert'] + intercept_up_Q1
# predicted_values_up_Q2 = slope_up_Q2 * Q2['sortd_SaEn_Adaptation_up_min_before_pert'] + intercept_up_Q2
# predicted_values_up_Q3 = slope_up_Q3 * Q3['sortd_SaEn_Adaptation_up_min_before_pert'] + intercept_up_Q3
# predicted_values_up_Q4 = slope_up_Q4 * Q4['sortd_SaEn_Adaptation_up_min_before_pert'] + intercept_up_Q4
#
#
# # Plot for perturbation up
# fig, axes = plt.subplots(2, 2, figsize=(10, 8))
# fig.suptitle("Sorted based on SaEn Before Perturbation")
#
# axes[0, 0].scatter(Q1['sortd_SaEn_Adaptation_up_min_before_pert'], Q1['sortd_Adaptation_up_min_SaEn_Adaptation_up_min_before_pert'], color="blue")
# axes[0, 0].plot(Q1['sortd_SaEn_Adaptation_up_min_before_pert'], predicted_values_up_Q1, color="red")
# axes[0, 0].set_title(f"Q1 y={round(slope_up_Q1, 2)}x+{round(intercept_up_Q1, 2)}\nR^2 = {round(R_squared_up_Q1, 3)}, p={round(p_value_up_Q1,3)}")
# axes[0, 0].set_ylabel("Adaptation Time")
#
# axes[1, 0].scatter(Q2['sortd_SaEn_Adaptation_up_min_before_pert'], Q2['sortd_Adaptation_up_min_SaEn_Adaptation_up_min_before_pert'], color="blue")
# axes[1, 0].plot(Q2['sortd_SaEn_Adaptation_up_min_before_pert'], predicted_values_up_Q2, color="red")
# axes[1, 0].set_title(f"Q2 y={round(slope_up_Q2, 2)}x+{round(intercept_up_Q2, 2)}\nR^2 = {round(R_squared_up_Q2, 3)}, p={round(p_value_up_Q2,3)}")
# axes[1, 0].set_xlabel("SaEn_before_pert")
# axes[1, 0].set_ylabel("Adaptation Time")
#
# axes[0, 1].scatter(Q3['sortd_SaEn_Adaptation_up_min_before_pert'], Q3['sortd_Adaptation_up_min_SaEn_Adaptation_up_min_before_pert'], color="blue")
# axes[0, 1].plot(Q3['sortd_SaEn_Adaptation_up_min_before_pert'], predicted_values_up_Q3, color="red")
# axes[0, 1].set_title(f"Q3 y={round(slope_up_Q3, 2)}x+{round(intercept_up_Q3, 2)}\nR^2 = {round(R_squared_up_Q3, 3)}, p={round(p_value_up_Q3,3)}")
#
# axes[1, 1].scatter(Q4['sortd_SaEn_Adaptation_up_min_before_pert'], Q4['sortd_Adaptation_up_min_SaEn_Adaptation_up_min_before_pert'], color="blue")
# axes[1, 1].plot(Q4['sortd_SaEn_Adaptation_up_min_before_pert'], predicted_values_up_Q4, color="red")
# axes[1, 1].set_title(f"Q4 y={round(slope_up_Q4, 2)}x+{round(intercept_up_Q4, 2)}\nR^2 = {round(R_squared_up_Q4, 3)}, p={round(p_value_up_Q4,3)}")
# axes[1, 1].set_xlabel("SaEn_average")
#
#
# # Adjust layout
# plt.tight_layout()
# plt.show()

# Separate the SaEn and perturbations based on the quartiles of SaEn_Adaptation_down_min_before_pert
# pd.set_option('display.max_rows', None)  # Show all rows
# pd.set_option('display.max_columns', None)  # Show all columns
# pd.set_option('display.width', None)  # Adjust width to fit all columns
# pd.set_option('display.max_colwidth', None)  # Show full content in each cell
#
# q1 = np.percentile(df_sort_SaEn_Adaptation_down_min_before_pert['sortd_SaEn_Adaptation_down_min_before_pert'], 25)
# q2 = np.percentile(df_sort_SaEn_Adaptation_down_min_before_pert['sortd_SaEn_Adaptation_down_min_before_pert'], 50)
# q3 = np.percentile(df_sort_SaEn_Adaptation_down_min_before_pert['sortd_SaEn_Adaptation_down_min_before_pert'], 75)
#
# # Creating quartile-based subsets
# Q1 = df_sort_SaEn_Adaptation_down_min_before_pert[df_sort_SaEn_Adaptation_down_min_before_pert['sortd_SaEn_Adaptation_down_min_before_pert'] <= q1]
# Q2 = df_sort_SaEn_Adaptation_down_min_before_pert[(df_sort_SaEn_Adaptation_down_min_before_pert['sortd_SaEn_Adaptation_down_min_before_pert'] > q1) & (df_sort_SaEn_Adaptation_down_min_before_pert['sortd_SaEn_Adaptation_down_min_before_pert'] <= q2)]
# Q3 = df_sort_SaEn_Adaptation_down_min_before_pert[(df_sort_SaEn_Adaptation_down_min_before_pert['sortd_SaEn_Adaptation_down_min_before_pert'] > q2) & (df_sort_SaEn_Adaptation_down_min_before_pert['sortd_SaEn_Adaptation_down_min_before_pert'] <= q3)]
# Q4 = df_sort_SaEn_Adaptation_down_min_before_pert[df_sort_SaEn_Adaptation_down_min_before_pert['sortd_SaEn_Adaptation_down_min_before_pert'] > q3]
#
# print(Q1.columns)
# slope_down_Q1, intercept_down_Q1, r_value_down_Q1, p_value_down_Q1, std_err_down_Q1 = stats.linregress(Q1['sortd_SaEn_Adaptation_down_min_before_pert'], Q1['sortd_Adaptation_down_min_SaEn_Adaptation_down_min_before_pert'])
# slope_down_Q2, intercept_down_Q2, r_value_down_Q2, p_value_down_Q2, std_err_down_Q2 = stats.linregress(Q2['sortd_SaEn_Adaptation_down_min_before_pert'], Q2['sortd_Adaptation_down_min_SaEn_Adaptation_down_min_before_pert'])
# slope_down_Q3, intercept_down_Q3, r_value_down_Q3, p_value_down_Q3, std_err_down_Q3 = stats.linregress(Q3['sortd_SaEn_Adaptation_down_min_before_pert'], Q3['sortd_Adaptation_down_min_SaEn_Adaptation_down_min_before_pert'])
# slope_down_Q4, intercept_down_Q4, r_value_down_Q4, p_value_down_Q4, std_err_down_Q4 = stats.linregress(Q4['sortd_SaEn_Adaptation_down_min_before_pert'], Q4['sortd_Adaptation_down_min_SaEn_Adaptation_down_min_before_pert'])
#
#
# R_squared_down_Q1 = r_value_down_Q1**2
# R_squared_down_Q2 = r_value_down_Q2**2
# R_squared_down_Q3 = r_value_down_Q3**2
# R_squared_down_Q4 = r_value_down_Q4**2
#
#
# predicted_values_down_Q1 = slope_down_Q1 * Q1['sortd_SaEn_Adaptation_down_min_before_pert'] + intercept_down_Q1
# predicted_values_down_Q2 = slope_down_Q2 * Q2['sortd_SaEn_Adaptation_down_min_before_pert'] + intercept_down_Q2
# predicted_values_down_Q3 = slope_down_Q3 * Q3['sortd_SaEn_Adaptation_down_min_before_pert'] + intercept_down_Q3
# predicted_values_down_Q4 = slope_down_Q4 * Q4['sortd_SaEn_Adaptation_down_min_before_pert'] + intercept_down_Q4
#
#
# # Plot for perturbation down
# fig, axes = plt.subplots(2, 2, figsize=(10, 8))
# fig.suptitle("Sorted based on SaEn Before Perturbation")
#
# axes[0, 0].scatter(Q1['sortd_SaEn_Adaptation_down_min_before_pert'], Q1['sortd_Adaptation_down_min_SaEn_Adaptation_down_min_before_pert'], color="blue")
# axes[0, 0].plot(Q1['sortd_SaEn_Adaptation_down_min_before_pert'], predicted_values_down_Q1, color="red")
# axes[0, 0].set_title(f"Q1 y={round(slope_down_Q1, 2)}x+{round(intercept_down_Q1, 2)}\nR^2 = {round(R_squared_down_Q1, 3)}, p={round(p_value_down_Q1,3)}")
# axes[0, 0].set_ylabel("Adaptation Time")
#
# axes[1, 0].scatter(Q2['sortd_SaEn_Adaptation_down_min_before_pert'], Q2['sortd_Adaptation_down_min_SaEn_Adaptation_down_min_before_pert'], color="blue")
# axes[1, 0].plot(Q2['sortd_SaEn_Adaptation_down_min_before_pert'], predicted_values_down_Q2, color="red")
# axes[1, 0].set_title(f"Q2 y={round(slope_down_Q2, 2)}x+{round(intercept_down_Q2, 2)}\nR^2 = {round(R_squared_down_Q2, 3)}, p={round(p_value_down_Q2,3)}")
# axes[1, 0].set_xlabel("SaEn_before_pert")
# axes[1, 0].set_ylabel("Adaptation Time")
#
# axes[0, 1].scatter(Q3['sortd_SaEn_Adaptation_down_min_before_pert'], Q3['sortd_Adaptation_down_min_SaEn_Adaptation_down_min_before_pert'], color="blue")
# axes[0, 1].plot(Q3['sortd_SaEn_Adaptation_down_min_before_pert'], predicted_values_down_Q3, color="red")
# axes[0, 1].set_title(f"Q3 y={round(slope_down_Q3, 2)}x+{round(intercept_down_Q3, 2)}\nR^2 = {round(R_squared_down_Q3, 3)}, p={round(p_value_down_Q3,3)}")
#
# axes[1, 1].scatter(Q4['sortd_SaEn_Adaptation_down_min_before_pert'], Q4['sortd_Adaptation_down_min_SaEn_Adaptation_down_min_before_pert'], color="blue")
# axes[1, 1].plot(Q4['sortd_SaEn_Adaptation_down_min_before_pert'], predicted_values_down_Q4, color="red")
# axes[1, 1].set_title(f"Q4 y={round(slope_down_Q4, 2)}x+{round(intercept_down_Q4, 2)}\nR^2 = {round(R_squared_down_Q4, 3)}, p={round(p_value_down_Q4,3)}")
# axes[1, 1].set_xlabel("SaEn_average")
#
#
# # Adjust layout
# plt.tight_layout()
# plt.show()