import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import glob

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 16

directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Strength data'
files = glob.glob(os.path.join(directory_path, "*"))
ID_list = []
Sd_Isometric_80_T1_list = []
Sd_Isometric_80_T2_list = []
Sd_Isometric_60_T1_list = []
Sd_Isometric_60_T2_list = []
Sd_Isometric_40_T1_list = []
Sd_Isometric_40_T2_list = []
Sd_Isometric_20_T1_list = []
Sd_Isometric_20_T2_list = []
Sd_Isometric_5_T1_list = []
Sd_Isometric_5_T2_list = []

CoV_Isometric_80_T1_list = []
CoV_Isometric_80_T2_list = []
CoV_Isometric_60_T1_list = []
CoV_Isometric_60_T2_list = []
CoV_Isometric_40_T1_list = []
CoV_Isometric_40_T2_list = []
CoV_Isometric_20_T1_list = []
CoV_Isometric_20_T2_list = []
CoV_Isometric_5_T1_list = []
CoV_Isometric_5_T2_list = []

SaEn_Isometric_80_T1_list = []
SaEn_Isometric_80_T2_list = []
SaEn_Isometric_60_T1_list = []
SaEn_Isometric_60_T2_list = []
SaEn_Isometric_40_T1_list = []
SaEn_Isometric_40_T2_list = []
SaEn_Isometric_20_T1_list = []
SaEn_Isometric_20_T2_list = []
SaEn_Isometric_5_T1_list = []
SaEn_Isometric_5_T2_list = []
for file in files:
    os.chdir(file)
    ID = os.path.basename(file)
    ID_list.append(ID)
    print(ID)

    if ID ==
    Isometric_80_T1 = pd.read_csv(r'Iso_80_1.csv', skiprows=2)
    Isometric_80_T2 = pd.read_csv(r'Iso_80_2.csv', skiprows=2)
    Isometric_60_T1 = pd.read_csv(r'Iso_60_1.csv', skiprows=2)
    Isometric_60_T2 = pd.read_csv(r'Iso_60_2.csv', skiprows=2)
    Isometric_40_T1 = pd.read_csv(r'Iso_40_1.csv', skiprows=2)
    Isometric_40_T2 = pd.read_csv(r'Iso_40_2.csv', skiprows=2)
    Isometric_20_T1 = pd.read_csv(r'Iso_20_1.csv', skiprows=2)
    Isometric_20_T2 = pd.read_csv(r'Iso_20_2.csv', skiprows=2)
    Isometric_5_T1 = pd.read_csv(r'Iso_5_1.csv', skiprows=2)
    Isometric_5_T2 = pd.read_csv(r'Iso_5_2.csv', skiprows=2)

    SaEn_Isometric_80_T1 = lb.Ent_Samp(Isometric_80_T1['Performance'][2000:7000], 2,0.2)
    SaEn_Isometric_80_T2 = lb.Ent_Samp(Isometric_80_T2['Performance'][2000:7000], 2,0.2)
    SaEn_Isometric_60_T1 = lb.Ent_Samp(Isometric_60_T1['Performance'][2000:7000], 2,0.2)
    SaEn_Isometric_60_T2 = lb.Ent_Samp(Isometric_60_T2['Performance'][2000:7000], 2,0.2)
    SaEn_Isometric_40_T1 = lb.Ent_Samp(Isometric_40_T1['Performance'][2000:7000], 2,0.2)
    SaEn_Isometric_40_T2 = lb.Ent_Samp(Isometric_40_T2['Performance'][2000:7000], 2,0.2)
    SaEn_Isometric_20_T1 = lb.Ent_Samp(Isometric_20_T1['Performance'][2000:7000], 2,0.2)
    SaEn_Isometric_20_T2 = lb.Ent_Samp(Isometric_20_T2['Performance'][2000:7000], 2,0.2)
    SaEn_Isometric_5_T1 = lb.Ent_Samp(Isometric_5_T1['Performance'][2000:7000], 2,0.2)
    SaEn_Isometric_5_T2 = lb.Ent_Samp(Isometric_5_T2['Performance'][2000:7000], 2,0.2)

Sd_Isometric_80_T1 = np.std(Isometric_80_T1['Performance'][2000:7000])
Sd_Isometric_80_T2 = np.std(Isometric_80_T2['Performance'][2000:7000])
Sd_Isometric_80_T3 = np.std(Isometric_80_T3['Performance'][2000:7000])
Sd_Isometric_60_T1 = np.std(Isometric_60_T1['Performance'][2000:7000])
Sd_Isometric_60_T2 = np.std(Isometric_60_T2['Performance'][2000:7000])
Sd_Isometric_60_T3 = np.std(Isometric_60_T3['Performance'][2000:7000])
Sd_Isometric_40_T1 = np.std(Isometric_40_T1['Performance'][2000:7000])
Sd_Isometric_40_T2 = np.std(Isometric_40_T2['Performance'][2000:7000])
Sd_Isometric_40_T3 = np.std(Isometric_40_T3['Performance'][2000:7000])
Sd_Isometric_20_T1 = np.std(Isometric_20_T1['Performance'][2000:7000])
Sd_Isometric_20_T2 = np.std(Isometric_20_T2['Performance'][2000:7000])
Sd_Isometric_20_T3 = np.std(Isometric_20_T3['Performance'][2000:7000])
Sd_Isometric_5_T1 = np.std(Isometric_5_T1['Performance'][2000:7000])
Sd_Isometric_5_T2 = np.std(Isometric_5_T2['Performance'][2000:7000])
Sd_Isometric_5_T3 = np.std(Isometric_5_T3['Performance'][2000:7000])
#
# print(SaEn_Isometric_80_T1)
# print(SaEn_Isometric_80_T2)
# print(SaEn_Isometric_80_T3)

# print(SaEn_Isometric_60_T1)
# print(SaEn_Isometric_60_T2)
# print(SaEn_Isometric_60_T3)
# print(SaEn_Isometric_40_T1)
# print(SaEn_Isometric_40_T2)
# print(SaEn_Isometric_40_T3)
# print(SaEn_Isometric_20_T1)
# print(SaEn_Isometric_20_T2)
# print(SaEn_Isometric_5_T1)
# print(SaEn_Isometric_5_T2)
# print(SaEn_Isometric_5_T3)
#
#
#
SaEn_80 = [SaEn_Isometric_80_T1, SaEn_Isometric_80_T2, SaEn_Isometric_80_T3]
SaEn_60 = [SaEn_Isometric_60_T1, SaEn_Isometric_60_T2, SaEn_Isometric_60_T3]
SaEn_40 = [SaEn_Isometric_40_T1, SaEn_Isometric_40_T2, SaEn_Isometric_40_T3]
SaEn_20 = [SaEn_Isometric_20_T1, SaEn_Isometric_20_T2, SaEn_Isometric_20_T3]
SaEn_5 = [SaEn_Isometric_5_T1, SaEn_Isometric_5_T2, SaEn_Isometric_5_T3]

SaEn_80_mean = np.mean(SaEn_80)
SaEn_60_mean = np.mean(SaEn_60)
SaEn_40_mean = np.mean(SaEn_40)
SaEn_20_mean = np.mean(SaEn_20)
SaEn_5_mean = np.mean(SaEn_5)

SaEn_mean_list = [SaEn_5_mean, SaEn_20_mean, SaEn_40_mean, SaEn_60_mean, SaEn_80_mean]
Percentage_list = [5,20,40,60,80]

plt.plot(SaEn_80, label='80')
plt.plot(SaEn_60, label='60')
plt.plot(SaEn_40, label='40')
plt.plot(SaEn_20, label='20')
plt.plot(SaEn_5, label='5')
plt.legend()
plt.show()
plt.plot(Percentage_list, SaEn_mean_list)
plt.show()
# # plt.plot(signal1['Target'], label='down')
# # plt.plot(signal2['Target'], label='up')
# # plt.plot(signal3['Target'], label='3')
# # plt.plot(signal4['Target'], label='4')
# # plt.plot(signal5['Target'], label='5')
# # plt.plot(signal6['Target'], label='6')
# # plt.plot(signal7['Target'], label='7')
# # plt.plot(signal8['Target'], label='8')
# # plt.plot(signal9['Target'], label='9')
# # plt.plot(signal10['Target'], label='10')
# # plt.plot(signal11['Target'], label='11')
# # plt.plot(signal12['Target'], label='12')
# # plt.plot(signal13['Target'], label='13')
# # plt.plot(signal14['Target'], label='14')


SaEn_list_1 = []
SaEn_list_1.append(SaEn_Isometric_5_T1)
SaEn_list_1.append(SaEn_Isometric_20_T1)
SaEn_list_1.append(SaEn_Isometric_40_T1)
SaEn_list_1.append(SaEn_Isometric_60_T1)
SaEn_list_1.append(SaEn_Isometric_80_T1)

SaEn_list_2 = []
SaEn_list_2.append(SaEn_Isometric_5_T2)
SaEn_list_2.append(SaEn_Isometric_20_T2)
SaEn_list_2.append(SaEn_Isometric_40_T2)
SaEn_list_2.append(SaEn_Isometric_60_T2)
SaEn_list_2.append(SaEn_Isometric_80_T2)

SaEn_list_3 = []
SaEn_list_3.append(SaEn_Isometric_5_T3)
SaEn_list_3.append(SaEn_Isometric_20_T3)
SaEn_list_3.append(SaEn_Isometric_40_T3)
SaEn_list_3.append(SaEn_Isometric_60_T3)
SaEn_list_3.append(SaEn_Isometric_80_T3)

Sd_list_1 = []
Sd_list_1.append(Sd_Isometric_5_T1)
Sd_list_1.append(Sd_Isometric_20_T1)
Sd_list_1.append(Sd_Isometric_40_T1)
Sd_list_1.append(Sd_Isometric_60_T1)
Sd_list_1.append(Sd_Isometric_80_T1)

Sd_list_2 = []
Sd_list_2.append(Sd_Isometric_5_T2)
Sd_list_2.append(Sd_Isometric_20_T2)
Sd_list_2.append(Sd_Isometric_40_T2)
Sd_list_2.append(Sd_Isometric_60_T2)
Sd_list_2.append(Sd_Isometric_80_T2)

Sd_list_3 = []
Sd_list_3.append(Sd_Isometric_5_T3)
Sd_list_3.append(Sd_Isometric_20_T3)
Sd_list_3.append(Sd_Isometric_40_T3)
Sd_list_3.append(Sd_Isometric_60_T3)
Sd_list_3.append(Sd_Isometric_80_T3)

Perc_list = [5,20,40,60,80]

plt.plot(Perc_list,SaEn_list_1, c='k', label='SaEn Trial 1')
plt.plot(Perc_list,SaEn_list_2, c='blue', label='SaEn Trial 2')
plt.plot(Perc_list,SaEn_list_3, c='red', label='SaEn Trial 3')
plt.legend()
plt.show()

plt.plot(Perc_list,Sd_list_1, c='k', label='Sd Trial 1')
plt.plot(Perc_list,Sd_list_2, c='blue', label='Sd Trial 2')
plt.plot(Perc_list,Sd_list_3, c='red', label='Sd Trial 3')
plt.legend()
plt.show()

# plt.plot(Percentage_list, SaEn_mean_list)
# plt.legend()
# plt.show()