import Lib_grip as lb
import lib
import colorednoise as cn
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import pandas as pd

# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['font.size'] = 15
#
#
# N=200
# time = np.linspace(0,10,N)
#
# brown = cn.powerlaw_psd_gaussian(1.3,N)
# brown_z = lb.z_transform(brown,5,40)
# pink = lb.fgn_sim(N,0.99)
# pink_z = lb.z_transform(pink,2.5,40)
#
# SaEn_brown = round(lb.Ent_Samp(brown_z, 2, 0.2),2)
# SaEn_pink = round(lb.Ent_Samp(pink_z, 2, 0.2),2)
# SD_brown = round(np.std(brown_z),2)
# SD_pink = round(np.std(pink_z),2)
#
# # plt.plot(brown_z, label=f'Signal 1, SaEn = {SaEn_brown}, SD = {SD_brown}')
# # plt.plot(pink_z, label=f'Signal 2, SaEn = {SaEn_pink}, SD = {SD_pink}')
# # plt.legend()
# # plt.show()
#
#
# plt.figure(figsize=(8, 4))
# plt.plot(time, brown_z, color='red', linewidth=3, label=f'Signal 1, SaEn = {SaEn_brown}, SD = {SD_brown}')
# plt.plot(time, pink_z, color='blue', linewidth=3, label=f'Signal 2, SaEn = {SaEn_pink}, SD = {SD_pink}')
# plt.legend(prop={'weight': 'bold'})
# # Styling
# # plt.legend(
# #     loc='upper right',
# #     frameon=True,
# #     fancybox=True,
# #     shadow=True,
# #     framealpha=0.9,
# #     prop={'weight': 'bold'}  # <-- makes legend text bold
# # )
#
# plt.title('Signals Comparison', fontweight='bold')
# plt.xlabel('Time (s)')
# plt.ylabel('Force output (N)')
#
# plt.tight_layout()
# plt.show()
#
#
# lb.quality_assessment_of_temporal_structure_FFT_method(brown_z)
# lb.quality_assessment_of_temporal_structure_FFT_method(pink_z)
#

file = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Data collection\Data\Strength data\Old.1'


Adaptation_down_T1_list = []
Adaptation_down_T2_list = []
Adaptation_up_T1_list = []
Adaptation_up_T2_list = []
ID_list = []

os.chdir(file)
ID = os.path.basename(file)
ID_list.append(ID)
print(ID)
Isometric_80_T1 = pd.read_csv(r'Isometric_80_T1.csv', skiprows=2)
Isometric_60_T1 = pd.read_csv(r'Isometric_60_T1.csv', skiprows=2)
Isometric_40_T1 = pd.read_csv(r'Isometric_40_T1.csv', skiprows=2)
Isometric_20_T1 = pd.read_csv(r'Isometric_20_T1.csv', skiprows=2)
Isometric_05_T1 = pd.read_csv(r'Isometric_05_T1.csv', skiprows=2)

# list_cutoff_freq = np.arange(1, 37, 1)

# lib.residual_analysis(Pert_down_T1['Performance'], 75, list_cutoff_freq)
# lib.residual_analysis(Pert_down_T2['Performance'], 75, list_cutoff_freq)
# lib.residual_analysis(Pert_up_T1['Performance'], 75, list_cutoff_freq)
# lib.residual_analysis(Pert_up_T2['Performance'], 75, list_cutoff_freq)


Isometric_80_T1['Performance'] = lib.Butterworth(75, 10, Isometric_80_T1['Performance'])
Isometric_60_T1['Performance'] = lib.Butterworth(75, 10, Isometric_60_T1['Performance'])
Isometric_40_T1['Performance'] = lib.Butterworth(75, 10, Isometric_40_T1['Performance'])
Isometric_20_T1['Performance'] = lib.Butterworth(75, 10, Isometric_20_T1['Performance'])
Isometric_05_T1['Performance'] = lib.Butterworth(75, 10, Isometric_05_T1['Performance'])

#
# time = np.linspace(0,7,525)
# fig, ax1 = plt.subplots(figsize=(8, 5))
#
# lw=8
# ax1.plot(time, Isometric_80_T1['Performance'][100:625], lw=lw)
# ax1.plot(time, Isometric_60_T1['Performance'][100:625], lw=lw)
# ax1.plot(time, Isometric_40_T1['Performance'][100:625], lw=lw)
# ax1.plot(time, Isometric_20_T1['Performance'][100:625], lw=lw)
# ax1.plot(time, Isometric_05_T1['Performance'][100:625], lw=lw)
#
# ax1.tick_params(axis='x', labelcolor='k', labelsize=50)
#
# # Set background colors
# fig.patch.set_facecolor('#F6F6F0')
# ax1.set_facecolor('#F6F6F0')
#
# # Force x-axis ticks
# ax1.set_xticks([0,1,2,3,4,5,6,7])
# ax1.set_yticklabels([])
#
#
# plt.show()

#
# fig, ax1 = plt.subplots(figsize=(8, 5))
#
# # Primary axis (spatial error)
# ax1.plot(df['Time'], spatial_er, label='Spatial Error', color='#1F497D', lw=8)
# ax1.axhline(y=average_at_min_sd, c='k', label='Average')
# ax1.axhline(y=average_at_min_sd + min_sd * sd_factor, c='k', ls=":")
# ax1.axhline(y=average_at_min_sd - min_sd * sd_factor, c='k', ls=":")
# ax1.axvline(x=df['Time'][perturbation_index] + time_of_adaptation, lw=5, c='red',
#             label='Adaptation instance')
# ax1.axvline(x=df['Time'][perturbation_index], linestyle='--', c='gray', label='Perturbation instance')
#
# # ax1.set_xlabel('Time (sec)', fontweight='bold')
# # ax1.set_ylabel('Force difference between \ntarget and avatar (kg)', color='blue', fontweight='bold')
# ax1.tick_params(axis='y', labelcolor='#1F497D', labelsize=50)
# ax1.tick_params(axis='x', labelcolor='red', labelsize=50)
#
# fig.patch.set_facecolor('#F6F6F0')
# ax1.set_facecolor('#F6F6F0')
# plt.show()

Pert_down_T1 = pd.read_csv(r'Pert_down_T1.csv', skiprows=2)
Pert_down_T2 = pd.read_csv(r'Pert_down_T2.csv', skiprows=2)
Pert_up_T1 = pd.read_csv(r'Pert_up_T1.csv', skiprows=2)
Pert_up_T2 = pd.read_csv(r'Pert_up_T2.csv', skiprows=2)

Pert_down_T1['Performance'] = lib.Butterworth(75, 10, Pert_down_T1['Performance'])
Pert_down_T2['Performance'] = lib.Butterworth(75, 10, Pert_down_T2['Performance'])
Pert_up_T1['Performance'] = lib.Butterworth(75, 10, Pert_up_T1['Performance'])
Pert_up_T2['Performance'] = lib.Butterworth(75, 10, Pert_up_T2['Performance'])

sd_factor = 2
consecutive_values = 37
print("hello")
plt.rcParams['font.family'] = 'Arial'  # or 'Helvetica'
plt.rcParams['font.size'] = 16
plt.rcParams['font.weight'] = 'bold'

time_of_adaptation_down_T1 = lb.adaptation_time_using_sd_right_before_perturbation(Pert_down_T1, 250, sd_factor, 100, consecutive_values, 100, 'Pert_down_T1', plot=True)
time_of_adaptation_down_T2 = lb.adaptation_time_using_sd_right_before_perturbation(Pert_down_T2, 250, sd_factor, 100, consecutive_values, 100, 'Pert_down_T2', plot=True)
time_of_adaptation_up_T1 = lb.adaptation_time_using_sd_right_before_perturbation(Pert_up_T1, 250, sd_factor, 100, consecutive_values, 100, 'Pert_up_T1', plot=False)
time_of_adaptation_up_T2 = lb.adaptation_time_using_sd_right_before_perturbation(Pert_up_T2, 250, sd_factor, 100, consecutive_values, 100, 'Pert_up_T2', plot=False)