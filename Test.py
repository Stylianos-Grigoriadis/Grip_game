import pandas as pd
from fathon import fathonUtils as fu
import fathon
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import Lib_grip as lb

for i in range(1,19):
    try:
        directory = rf'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Strength data\Old.{i}'
        os.chdir(directory)

        Isometric_80_T1 = pd.read_csv(r'Isometric_80_T1.csv', skiprows=2)
        Isometric_80_T2 = pd.read_csv(r'Isometric_80_T2.csv', skiprows=2)
        Isometric_60_T1 = pd.read_csv(r'Isometric_60_T1.csv', skiprows=2)
        Isometric_60_T2 = pd.read_csv(r'Isometric_60_T2.csv', skiprows=2)
        Isometric_40_T1 = pd.read_csv(r'Isometric_40_T1.csv', skiprows=2)
        Isometric_40_T2 = pd.read_csv(r'Isometric_40_T2.csv', skiprows=2)
        Isometric_20_T1 = pd.read_csv(r'Isometric_20_T1.csv', skiprows=2)
        Isometric_20_T2 = pd.read_csv(r'Isometric_20_T2.csv', skiprows=2)
        Isometric_5_T1 = pd.read_csv(r'Isometric_05_T1.csv', skiprows=2)
        Isometric_5_T2 = pd.read_csv(r'Isometric_05_T2.csv', skiprows=2)
        Pert_down_T1 = pd.read_csv(r'Pert_down_T1.csv', skiprows=2)
        Pert_down_T2 = pd.read_csv(r'Pert_down_T2.csv', skiprows=2)
        Pert_up_T1 = pd.read_csv(r'Pert_up_T1.csv', skiprows=2)
        Pert_up_T2 = pd.read_csv(r'Pert_up_T2.csv', skiprows=2)
        print(rf'Old {i}')
        print(rf"Isometric_80_T1: {len(Isometric_80_T1['Performance'])}")
        print(rf"Isometric_80_T2: {len(Isometric_80_T2['Performance'])}")
        print(rf"Isometric_60_T1: {len(Isometric_60_T1['Performance'])}")
        print(rf"Isometric_60_T2: {len(Isometric_60_T2['Performance'])}")
        print(rf"Isometric_40_T1: {len(Isometric_40_T1['Performance'])}")
        print(rf"Isometric_40_T2: {len(Isometric_40_T2['Performance'])}")
        print(rf"Isometric_20_T1: {len(Isometric_20_T1['Performance'])}")
        print(rf"Isometric_20_T2: {len(Isometric_20_T2['Performance'])}")
        print(rf"Isometric_5_T1: {len(Isometric_5_T1['Performance'])}")
        print(rf"Isometric_5_T2: {len(Isometric_5_T2['Performance'])}")
        print(rf"Pert_down_T1: {len(Pert_down_T1['Performance'])}")
        print(rf"Pert_down_T2: {len(Pert_down_T2['Performance'])}")
        print(rf"Pert_up_T1: {len(Pert_up_T1['Performance'])}")
        print(rf"Pert_up_T2: {len(Pert_up_T2['Performance'])}")

    except:
        pass
    # directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game Paper 1\Pilot Study 10\Data\Strength data\Old.8'
# signal = pd.read_csv(directory+r'\grip_strength_Mpoura_Vasiliki__05Dec24_10_31_34.csv', skiprows=2)
# print(signal)
# signal_target = signal['Target'].dropna().loc[signal['Target'] != ''].tolist()
# print(signal_target)
# fig, ax1 = plt.subplots()
#
# ax1.plot(signal['Performance'], label='big_tablet', c='orange')
# ax2 = ax1.twiny()
# ax2.plot(signal_target, label='big_tablet_target', c='red')
# plt.show()

# directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip  game Paper 1\Pilot Study 10\Data\Strength data\Old.3'
# # os.chdir(directory)
# files = glob.glob(os.path.join(directory, "*"))
# print(files)
# for file in files:
#     big_tablet = pd.read_csv(file, skiprows=2)
#     big_tablet_target = big_tablet['Target'].dropna().loc[big_tablet['Target'] != ''].tolist()
#     max = 22.8
#     print(f'5% = {0.05*max}')
#     print(f'20% = {0.2*max}')
#     print(f'40% = {0.4*max}')
#     print(f'60% = {0.6*max}')
#     print(f'80% = {0.8*max}')
#     print(os.path.basename(file))
#
#     fig, ax1 = plt.subplots()
#     plt.title(big_tablet_target[0])
#     ax1.plot(big_tablet['Performance'], label='big_tablet', c='orange')
#
#     ax2 = ax1.twiny()
#     ax2.plot(big_tablet_target, label='big_tablet_target', c='red')
#
#     plt.show()



# fig, ax1 = plt.subplots()
#
# ax1.plot(big_tablet['Performance'], label='big_tablet', c='orange')
# ax1.plot(small_tablet['Performance'], label='small_tablet', c='lightblue')
# ax1.plot(koutlinaos_tablet['Performance'], label='koutlianos_tablet', c='black')
#
#
# ax2 = ax1.twiny()
#
# ax2.plot(big_tablet_target, label='big_tablet_target', c='red')
# ax2.plot(small_tablet_target, label='small_tablet_target', c='blue')
# ax2.plot(koutlinaos_tablet_target, label='koutlinaos_tablet_target', c='gray')
#
#
# plt.show()

