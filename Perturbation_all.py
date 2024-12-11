import matplotlib.pyplot as plt
import pandas as pd
import os
import glob
import numpy as np
import Lib_grip as lb
directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game Paper 1\Pilot Study 10\Data\Strength data'
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
    sd = 2
    consecutive_values = 37

    time_of_adaptation_down_T1 = lb.adaptation_time_using_sd(Pert_down_T1, 250, sd, 100, consecutive_values, 100, 500,'Pert_down_T1', plot=False)
    time_of_adaptation_down_T2 = lb.adaptation_time_using_sd(Pert_down_T2, 250, sd, 100, consecutive_values, 100, 500,'Pert_down_T2', plot=False)
    time_of_adaptation_up_T1 = lb.adaptation_time_using_sd(Pert_up_T1, 250, sd, 100, consecutive_values, 100, 500,'Pert_up_T1', plot=False)
    time_of_adaptation_up_T2 = lb.adaptation_time_using_sd(Pert_up_T2, 250, sd, 100, consecutive_values, 100, 500,'Pert_up_T2', plot=False)

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
excel_directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game Paper 1\Pilot Study 10\Data\Results'
df.to_excel(excel_directory+fr'\Results Perturbation {sd}sd {consecutive_values}values after change the sd calculation.xlsx')



