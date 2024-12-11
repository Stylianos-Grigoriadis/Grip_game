import os

import numpy as np
from fathon import fathonUtils as fu
import fathon
import matplotlib.pyplot as plt
from scipy.stats import linregress
import pandas as pd
import colorednoise as cn
import random
from scipy.optimize import curve_fit
from scipy.signal import decimate
import Lib_grip as lb

directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game Paper 1\Pilot Study 10\Data\Strength data\Old.1'
os.chdir(directory)
Pert_down_T1 = pd.read_csv(r'Pert_down_T1.csv', skiprows=2)
Pert_down_T2 = pd.read_csv(r'Pert_down_T2.csv', skiprows=2)
Pert_up_T1 = pd.read_csv(r'Pert_up_T1.csv', skiprows=2)
Pert_up_T2 = pd.read_csv(r'Pert_up_T2.csv', skiprows=2)
sd = 2
consecutive_values = 37

time_of_adaptation_down_T1 = lb.adaptation_time_using_sd(Pert_down_T1, 250, sd, 100, consecutive_values, 100, 500, 'Pert_down_T1',plot=True)
time_of_adaptation_down_T2 = lb.adaptation_time_using_sd(Pert_down_T2, 250, sd, 100, consecutive_values, 100, 500, 'Pert_down_T2',plot=True)
time_of_adaptation_up_T1 = lb.adaptation_time_using_sd(Pert_up_T1, 250, sd, 100, consecutive_values, 100, 500, 'Pert_up_T1', plot=True)
time_of_adaptation_up_T2 = lb.adaptation_time_using_sd(Pert_up_T2, 250, sd, 100, consecutive_values, 100, 500, 'Pert_up_T2', plot=True)


