import lib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import Lib_grip as lb
from fathon import fathonUtils as fu
import colorednoise as cn

directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Strength data\Young.1'
os.chdir(directory_path)
ID = os.path.basename(directory_path)
print(ID)

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

index = pd.read_excel('index.xlsx')

iso_80_T1_75Hz = Isometric_80_T1_75Hz['Performance'][index['T1_iso_80_75Hz'][0]:index['T1_iso_80_75Hz'][1]].to_numpy()
iso_80_T2_75Hz = Isometric_80_T2_75Hz['Performance'][index['T2_iso_80_75Hz'][0]:index['T2_iso_80_75Hz'][1]].to_numpy()
iso_60_T1_75Hz = Isometric_60_T1_75Hz['Performance'][index['T1_iso_60_75Hz'][0]:index['T1_iso_60_75Hz'][1]].to_numpy()
iso_60_T2_75Hz = Isometric_60_T2_75Hz['Performance'][index['T2_iso_60_75Hz'][0]:index['T2_iso_60_75Hz'][1]].to_numpy()
iso_40_T1_75Hz = Isometric_40_T1_75Hz['Performance'][index['T1_iso_40_75Hz'][0]:index['T1_iso_40_75Hz'][1]].to_numpy()
iso_40_T2_75Hz = Isometric_40_T2_75Hz['Performance'][index['T2_iso_40_75Hz'][0]:index['T2_iso_40_75Hz'][1]].to_numpy()
iso_20_T1_75Hz = Isometric_20_T1_75Hz['Performance'][index['T1_iso_20_75Hz'][0]:index['T1_iso_20_75Hz'][1]].to_numpy()
iso_20_T2_75Hz = Isometric_20_T2_75Hz['Performance'][index['T2_iso_20_75Hz'][0]:index['T2_iso_20_75Hz'][1]].to_numpy()
iso_05_T1_75Hz = Isometric_05_T1_75Hz['Performance'][index['T1_iso_05_75Hz'][0]:index['T1_iso_05_75Hz'][1]].to_numpy()
iso_05_T2_75Hz = Isometric_05_T2_75Hz['Performance'][index['T2_iso_05_75Hz'][0]:index['T2_iso_05_75Hz'][1]].to_numpy()

iso_80_T1_75Hz = lb.index_to_500(iso_80_T1_75Hz)
iso_80_T2_75Hz = lb.index_to_500(iso_80_T2_75Hz)
iso_60_T1_75Hz = lb.index_to_500(iso_60_T1_75Hz)
iso_60_T2_75Hz = lb.index_to_500(iso_60_T2_75Hz)
iso_40_T1_75Hz = lb.index_to_500(iso_40_T1_75Hz)
iso_40_T2_75Hz = lb.index_to_500(iso_40_T2_75Hz)
iso_20_T1_75Hz = lb.index_to_500(iso_20_T1_75Hz)
iso_20_T2_75Hz = lb.index_to_500(iso_20_T2_75Hz)
iso_05_T1_75Hz = lb.index_to_500(iso_05_T1_75Hz)
iso_05_T2_75Hz = lb.index_to_500(iso_05_T2_75Hz)

# plt.plot(iso_80_T1_75Hz, label='iso_80_T1')
# plt.plot(iso_80_T2_75Hz, label='iso_80_T2')
# plt.plot(iso_60_T1_75Hz, label='iso_60_T1')
# plt.plot(iso_60_T2_75Hz, label='iso_60_T2')
# plt.plot(iso_40_T1_75Hz, label='iso_40_T1')
# plt.plot(iso_40_T2_75Hz, label='iso_40_T2')
# plt.plot(iso_20_T1_75Hz, label='iso_20_T1')
# plt.plot(iso_20_T2_75Hz, label='iso_20_T2')
# plt.plot(iso_05_T1_75Hz, label='iso_05_T1')
# plt.plot(iso_05_T2_75Hz, label='iso_05_T2')
# plt.legend()
# plt.show()

# BETAS_iso_80_T1_75Hz = lb.DFBETAS2(iso_80_T1_75Hz, [3,250], s='80_T1')
# BETAS_iso_80_T2_75Hz = lb.DFBETAS2(iso_80_T2_75Hz, [3,250], s='80_T2')
# BETAS_iso_60_T1_75Hz = lb.DFBETAS2(iso_60_T1_75Hz, [3,250], s='60_T1')
# BETAS_iso_60_T2_75Hz = lb.DFBETAS2(iso_60_T2_75Hz, [3,250], s='60_T2')
# BETAS_iso_40_T1_75Hz = lb.DFBETAS2(iso_40_T1_75Hz, [3,250], s='40_T1')
# BETAS_iso_40_T2_75Hz = lb.DFBETAS2(iso_40_T2_75Hz, [3,250], s='40_T2')
# BETAS_iso_20_T1_75Hz = lb.DFBETAS2(iso_20_T1_75Hz, [3,250], s='20_T1')
# BETAS_iso_20_T2_75Hz = lb.DFBETAS2(iso_20_T2_75Hz, [3,250], s='20_T2')
# BETAS_iso_05_T1_75Hz = lb.DFBETAS2(iso_05_T1_75Hz, [3,250], s='05_T1')
# BETAS_iso_05_T2_75Hz = lb.DFBETAS2(iso_05_T2_75Hz, [3,250], s='05_T2')
pink_signal = cn.powerlaw_psd_gaussian(1, 500)
# white_signal = np.random.random(500)
#
# lb.DFA(pink_signal, 16, 9)
# lb.DFA(white_signal, 16, 9)


# plt.plot(pink_signal, label='pink_signal')
# plt.plot(white_signal, label='white_signal')
# plt.legend()
# plt.show()
# H_iso_80_T1_75Hz = lb.DFA(iso_80_T1_75Hz, 16, 9)
# H_iso_80_T2_75Hz = lb.DFA(iso_80_T2_75Hz, 16, 9)
# H_iso_60_T1_75Hz = lb.DFA(iso_60_T1_75Hz, 16, 9)
# H_iso_60_T2_75Hz = lb.DFA(iso_60_T2_75Hz, 16, 9)
# H_iso_40_T1_75Hz = lb.DFA(iso_40_T1_75Hz, 16, 9)
# H_iso_40_T2_75Hz = lb.DFA(iso_40_T2_75Hz, 16, 9)
# H_iso_20_T1_75Hz = lb.DFA(iso_20_T1_75Hz, 16, 9)
# H_iso_20_T2_75Hz = lb.DFA(iso_20_T2_75Hz, 16, 9)
# H_iso_05_T1_75Hz = lb.DFA(iso_05_T1_75Hz, 16, 9)
# H_iso_05_T2_75Hz = lb.DFA(iso_05_T2_75Hz, 16, 9)
#
# H_T1 = [H_iso_80_T1_75Hz, H_iso_60_T1_75Hz, H_iso_40_T1_75Hz, H_iso_20_T1_75Hz, H_iso_05_T1_75Hz]
# H_T2 = [H_iso_80_T2_75Hz, H_iso_60_T2_75Hz, H_iso_40_T2_75Hz, H_iso_20_T2_75Hz, H_iso_05_T2_75Hz]
# H_Taverage =    [(H_T1[0] + H_T2[0])/2,
#                 (H_T1[1] + H_T2[1])/2,
#                 (H_T1[2] + H_T2[2])/2,
#                 (H_T1[3] + H_T2[3])/2,
#                 (H_T1[4] + H_T2[4])/2]
# y = [80,60,40,20,5]
# plt.plot(y, H_T1, label='H_T1')
# plt.plot(y, H_T2, label='H_T2')
# plt.plot(y, H_Taverage, label='H_Taverage')
# plt.legend()
# plt.show()
start = 4
end = 250
winSizes = fu.linRangeByStep(start=start, end=end)
log_n = np.log(winSizes)
log_F = np.log(iso_60_T2_75Hz)

stable_indices = lb.identify_stable_box_sizes(log_n, log_F)
print(stable_indices)

















# print(rf'BETAS_iso_80_T1_75Hz = {BETAS_iso_80_T1_75Hz}')
# print(rf'BETAS_iso_80_T2_75Hz = {BETAS_iso_80_T2_75Hz}')
# print(rf'BETAS_iso_60_T1_75Hz = {BETAS_iso_60_T1_75Hz}')
# print(rf'BETAS_iso_60_T2_75Hz = {BETAS_iso_60_T2_75Hz}')
# print(rf'BETAS_iso_40_T1_75Hz = {BETAS_iso_40_T1_75Hz}')
# print(rf'BETAS_iso_40_T2_75Hz = {BETAS_iso_40_T2_75Hz}')
# print(rf'BETAS_iso_20_T1_75Hz = {BETAS_iso_20_T1_75Hz}')
# print(rf'BETAS_iso_20_T2_75Hz = {BETAS_iso_20_T2_75Hz}')
# print(rf'BETAS_iso_05_T1_75Hz = {BETAS_iso_05_T1_75Hz}')
# print(rf'BETAS_iso_05_T2_75Hz = {BETAS_iso_05_T2_75Hz}')



plt.show()



