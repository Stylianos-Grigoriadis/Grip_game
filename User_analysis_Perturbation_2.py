import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np


directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 10\Data\3.Young'
os.chdir(directory_path)

Pert_up_T1 = pd.read_csv(r'Pert_up_T1.csv', skiprows=2)
Pert_up_T2 = pd.read_csv(r'Pert_up_T2.csv', skiprows=2)
Pert_down_T1 = pd.read_csv(r'Pert_down_T1.csv', skiprows=2)
Pert_down_T2 = pd.read_csv(r'Pert_down_T2.csv', skiprows=2)



time_of_adaptation_up_T1 = lb.adaptation_time_using_sd(Pert_up_T1, 250, 2, 100, 10, 500, plot=True)
time_of_adaptation_up_T2 = lb.adaptation_time_using_sd(Pert_up_T2, 250, 2, 100, 10, 500, plot=True)
time_of_adaptation_down_T1 = lb.adaptation_time_using_sd(Pert_down_T1, 250, 2, 100, 10, 500, plot=True)
time_of_adaptation_down_T2 = lb.adaptation_time_using_sd(Pert_down_T2, 250, 2, 100, 10, 500, plot=True)