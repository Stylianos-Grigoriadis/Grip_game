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

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 16
MVC = 34
Perc_80 = 0.8*MVC
Perc_60 = 0.6*MVC
Perc_40 = 0.4*MVC
Perc_20 = 0.2*MVC
Perc_05 = 0.05*MVC



directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Strength data\Old.6'
os.chdir(directory)

Isometric_80_T1_75Hz = pd.read_csv(r'Isometric_80_T1.csv', skiprows=2)
Isometric_80_T2_75Hz = pd.read_csv(r'Isometric_80_T2.csv', skiprows=2)
Isometric_60_T1_75Hz = pd.read_csv(r'Isometric_60_T1.csv', skiprows=2)
Isometric_60_T2_75Hz = pd.read_csv(r'Isometric_60_T2.csv', skiprows=2)
Isometric_40_T1_75Hz = pd.read_csv(r'Isometric_40_T1.csv', skiprows=2)
Isometric_40_T2_75Hz = pd.read_csv(r'Isometric_40_T2.csv', skiprows=2)
Isometric_20_T1_75Hz = pd.read_csv(r'Isometric_20_T1.csv', skiprows=2)
Isometric_20_T2_75Hz = pd.read_csv(r'Isometric_20_T2.csv', skiprows=2)
Isometric_05_T1_75Hz = pd.read_csv(r'Isometric_05_T1.csv', skiprows=2)
Isometric_05_T2_75Hz = pd.read_csv(r'Isometric_05_T2.csv', skiprows=2)


plt.plot(Isometric_80_T1_75Hz['Performance'], label='Isometric_80_T1')
plt.plot(Isometric_80_T2_75Hz['Performance'], label='Isometric_80_T2')

plt.plot(Isometric_60_T1_75Hz['Performance'], label='Isometric_60_T1')
plt.plot(Isometric_60_T2_75Hz['Performance'], label='Isometric_60_T2')

plt.plot(Isometric_40_T1_75Hz['Performance'], label='Isometric_40_T1')
plt.plot(Isometric_40_T2_75Hz['Performance'], label='Isometric_40_T2')

plt.plot(Isometric_20_T1_75Hz['Performance'], label='Isometric_20_T1')
plt.plot(Isometric_20_T2_75Hz['Performance'], label='Isometric_20_T2')

plt.plot(Isometric_05_T1_75Hz['Performance'], label='Isometric_05_T1')
plt.plot(Isometric_05_T2_75Hz['Performance'], label='Isometric_05_T2')





plt.axhline(y=Perc_80, label='80%')
plt.axhline(y=Perc_60, label='60%')
plt.axhline(y=Perc_40, label='40%')
plt.axhline(y=Perc_20, label='20%')
plt.axhline(y=Perc_05, label='05%')

plt.legend()
plt.show()



