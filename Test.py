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

directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Data collection\Data\Strength data'
files = glob.glob(os.path.join(directory_path, "*"))

Adaptation_down_T1_list = []
Adaptation_down_T2_list = []
Adaptation_up_T1_list = []
Adaptation_up_T2_list = []
ID_list = []

for file in files:
    os.chdir(file)
    ID = os.path.basename(file)
    ID_list.append(ID)
    print(ID)
    Pert_down_T1 = pd.read_csv(r'Pert_down_T1.csv', skiprows=2)
    Pert_down_T2 = pd.read_csv(r'Pert_down_T2.csv', skiprows=2)
    Pert_up_T1 = pd.read_csv(r'Pert_up_T1.csv', skiprows=2)
    Pert_up_T2 = pd.read_csv(r'Pert_up_T2.csv', skiprows=2)

    # list_cutoff_freq = np.arange(1, 37, 1)
    #
    # lib.residual_analysis(Pert_down_T1['Performance'], 75, list_cutoff_freq)
    # lib.residual_analysis(Pert_down_T2['Performance'], 75, list_cutoff_freq)
    # lib.residual_analysis(Pert_up_T1['Performance'], 75, list_cutoff_freq)
    # lib.residual_analysis(Pert_up_T2['Performance'], 75, list_cutoff_freq)


    Pert_down_T1['Performance'] = lib.Butterworth(75, 10, Pert_down_T1['Performance'])
    Pert_down_T2['Performance'] = lib.Butterworth(75, 10, Pert_down_T2['Performance'])
    Pert_up_T1['Performance'] = lib.Butterworth(75, 10, Pert_up_T1['Performance'])
    Pert_up_T2['Performance'] = lib.Butterworth(75, 10, Pert_up_T2['Performance'])

    sd_factor = 2
    consecutive_values = 37
    print("hello")
    # df, perturbation_index, sd_factor, first_values, consecutive_values, values_for_sd, name, plot = False
    plt.rcParams['font.family'] = 'Arial'  # or 'Helvetica'
    plt.rcParams['font.size'] = 15
    plt.rcParams['font.weight'] = 'bold'

    time_of_adaptation_down_T1 = lb.adaptation_time_using_sd_right_before_perturbation(Pert_down_T1, 250, sd_factor, 100, consecutive_values, 100, 'Pert_down_T1', plot=True)
    time_of_adaptation_down_T2 = lb.adaptation_time_using_sd_right_before_perturbation(Pert_down_T2, 250, sd_factor, 100, consecutive_values, 100, 'Pert_down_T2', plot=True)
    time_of_adaptation_up_T1 = lb.adaptation_time_using_sd_right_before_perturbation(Pert_up_T1, 250, sd_factor, 100, consecutive_values, 100, 'Pert_up_T1', plot=False)
    time_of_adaptation_up_T2 = lb.adaptation_time_using_sd_right_before_perturbation(Pert_up_T2, 250, sd_factor, 100, consecutive_values, 100, 'Pert_up_T2', plot=False)
