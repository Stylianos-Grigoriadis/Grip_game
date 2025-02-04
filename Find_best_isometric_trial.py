import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import glob
import statistics
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import lib
directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Strength data\Old.1'
os.chdir(directory)

Isometric_80_T1 = pd.read_csv(r'Isometric_80_T1.csv', skiprows=2)
Isometric_80_T2 = pd.read_csv(r'Isometric_80_T2.csv', skiprows=2)
Isometric_60_T1 = pd.read_csv(r'Isometric_60_T1.csv', skiprows=2)
Isometric_60_T2 = pd.read_csv(r'Isometric_60_T2.csv', skiprows=2)
Isometric_40_T1 = pd.read_csv(r'Isometric_40_T1.csv', skiprows=2)
Isometric_40_T2 = pd.read_csv(r'Isometric_40_T2.csv', skiprows=2)
Isometric_20_T1 = pd.read_csv(r'Isometric_20_T1.csv', skiprows=2)
Isometric_20_T2 = pd.read_csv(r'Isometric_20_T2.csv', skiprows=2)
Isometric_05_T1 = pd.read_csv(r'Isometric_05_T1.csv', skiprows=2)
Isometric_05_T2 = pd.read_csv(r'Isometric_05_T2.csv', skiprows=2)

Isometric_80_T1_sync = lb.synchronization_of_Time_and_ClosestSampleTime(Isometric_80_T1, 500, 10)
Spatial_error = lb.spatial_error(Isometric_80_T1_sync)
print(Isometric_80_T1_sync)
plt.plot(Spatial_error)
plt.show()

