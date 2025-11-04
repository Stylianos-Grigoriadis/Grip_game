import matplotlib.pyplot as plt
import pandas as pd
import os
import glob
import numpy as np
import Lib_grip as lb
import lib

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 16

directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Data collection\Data\Strength data'
files = glob.glob(os.path.join(directory_path, "*"))
ID_list = []
Adaptation_down_T1_list = []
Adaptation_down_T2_list = []
Adaptation_up_T1_list = []
Adaptation_up_T2_list = []

for file in files:
    os.chdir(file)
    ID = os.path.basename(file)
    ID_list.append(ID)
    print(ID)
    Pert_down_T1 = pd.read_csv(r'Pert_down_T1.csv', skiprows=2)
    Pert_down_T2 = pd.read_csv(r'Pert_down_T2.csv', skiprows=2)
    Pert_up_T1 = pd.read_csv(r'Pert_up_T1.csv', skiprows=2)
    Pert_up_T2 = pd.read_csv(r'Pert_up_T2.csv', skiprows=2)

    Pert_down_T1_for_filter = lb.synchronization_of_Time_and_ClosestSampleTime_Anestis(Pert_down_T1)
    Pert_down_T2_for_filter = lb.synchronization_of_Time_and_ClosestSampleTime_Anestis(Pert_down_T2)
    Pert_up_T1_for_filter = lb.synchronization_of_Time_and_ClosestSampleTime_Anestis(Pert_up_T1)
    Pert_up_T2_for_filter = lb.synchronization_of_Time_and_ClosestSampleTime_Anestis(Pert_up_T2)

    list_cutoff_freq = np.arange(1, 37, 1)

    lib.residual_analysis(Pert_down_T1_for_filter['Performance'], 75, list_cutoff_freq)


    sd_factor = 2
    consecutive_values = 37
    print("hello")
    # df, perturbation_index, sd_factor, first_values, consecutive_values, values_for_sd, name, plot = False

    time_of_adaptation_down_T1 = lb.adaptation_time_using_sd_right_before_perturbation(Pert_down_T1, 250, sd_factor, 100, consecutive_values, 100, 'Pert_down_T1', plot=True)
    time_of_adaptation_down_T2 = lb.adaptation_time_using_sd_right_before_perturbation(Pert_down_T2, 250, sd_factor, 100, consecutive_values, 100, 'Pert_down_T2', plot=True)
    time_of_adaptation_up_T1 = lb.adaptation_time_using_sd_right_before_perturbation(Pert_up_T1, 250, sd_factor, 100, consecutive_values, 100, 'Pert_up_T1', plot=False)
    time_of_adaptation_up_T2 = lb.adaptation_time_using_sd_right_before_perturbation(Pert_up_T2, 250, sd_factor, 100, consecutive_values, 100, 'Pert_up_T2', plot=False)

    if time_of_adaptation_down_T1 != None:
        time_of_adaptation_down_T1 = round(time_of_adaptation_down_T1, 3)

    if time_of_adaptation_down_T2 != None:
        time_of_adaptation_down_T2 = round(time_of_adaptation_down_T2, 3)

    if time_of_adaptation_up_T1 != None:
        time_of_adaptation_up_T1 = round(time_of_adaptation_up_T1, 3)

    if time_of_adaptation_up_T2 != None:
        time_of_adaptation_up_T2 = round(time_of_adaptation_up_T2, 3)
    Adaptation_down_T1_list.append(time_of_adaptation_down_T1)
    Adaptation_down_T2_list.append(time_of_adaptation_down_T2)
    Adaptation_up_T1_list.append(time_of_adaptation_up_T1)
    Adaptation_up_T2_list.append(time_of_adaptation_up_T2)

dist = {'ID': ID_list,
        'Adaptation_down_T1_list': Adaptation_down_T1_list,
        'Adaptation_down_T2_list': Adaptation_down_T2_list,
        'Adaptation_up_T1_list': Adaptation_up_T1_list,
        'Adaptation_up_T2_list': Adaptation_up_T2_list,
        }
df = pd.DataFrame(dist)
print(df)
excel_directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Data collection\Results'
os.chdir(excel_directory)
df.to_excel(r'Results Perturbation Anestis way sd before pert 3.xlsx')



