import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 10\Data\Strength data\Young.14'
os.chdir(directory_path)

Pert_down_T1 = pd.read_csv(r'Pert_down_T1.csv', skiprows=2)
Pert_down_T2 = pd.read_csv(r'Pert_down_T2.csv', skiprows=2)
Pert_up_T1 = pd.read_csv(r'Pert_up_T1.csv', skiprows=2)
Pert_up_T2 = pd.read_csv(r'Pert_up_T2.csv', skiprows=2)

time_of_adaptation_down_T1 = lb.adaptation_time_using_sd(Pert_down_T1, 250, 6, 100, 25, 500, 'Pert_down_T1',  plot=True)
time_of_adaptation_down_T2 = lb.adaptation_time_using_sd(Pert_down_T2, 250, 6, 100, 25, 500, 'Pert_down_T2', plot=True)
time_of_adaptation_up_T1 = lb.adaptation_time_using_sd(Pert_up_T1, 250, 6, 100, 25, 500, 'Pert_up_T1', plot=True)
time_of_adaptation_up_T2 = lb.adaptation_time_using_sd(Pert_up_T2, 250, 6, 100, 25, 500, 'Pert_up_T2', plot=True)

time_of_adaptation_down_T1 = round(time_of_adaptation_down_T1,3)
time_of_adaptation_down_T2 = round(time_of_adaptation_down_T2,3)
time_of_adaptation_up_T1 = round(time_of_adaptation_up_T1,3)
time_of_adaptation_up_T2 = round(time_of_adaptation_up_T2,3)

print('for 25 concecutive values')
print(f'time_of_adaptation_down_T1 = {time_of_adaptation_down_T1}')
print(f'time_of_adaptation_down_T2 = {time_of_adaptation_down_T2}')
print(f'time_of_adaptation_up_T1 = {time_of_adaptation_up_T1}')
print(f'time_of_adaptation_up_T2 = {time_of_adaptation_up_T2}')

dist = {'Trials': ['T1_down','T2_down','T1_up','T2_up'],
        'Time': [time_of_adaptation_down_T1,time_of_adaptation_down_T2, time_of_adaptation_up_T1, time_of_adaptation_up_T2]}
df_excel = pd.DataFrame(dist)
print(df_excel)
# df_excel.to_excel('Results Perturbation.xlsx')