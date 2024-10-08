import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Malvina 7-10-2024\Raw'
os.chdir(directory_path)

Isometric_80_T1 = pd.read_csv(r'Isometric_80_T1.csv', skiprows=2)
Isometric_80_T2 = pd.read_csv(r'Isometric_80_T2.csv', skiprows=2)
Isometric_80_T3 = pd.read_csv(r'Isometric_80_T3.csv', skiprows=2)
Isometric_60_T1 = pd.read_csv(r'Isometric_60_T1.csv', skiprows=2)
Isometric_60_T2 = pd.read_csv(r'Isometric_60_T2.csv', skiprows=2)
Isometric_60_T3 = pd.read_csv(r'Isometric_60_T3.csv', skiprows=2)
Isometric_40_T1 = pd.read_csv(r'Isometric_40_T1.csv', skiprows=2)
Isometric_40_T2 = pd.read_csv(r'Isometric_40_T2.csv', skiprows=2)
Isometric_40_T3 = pd.read_csv(r'Isometric_40_T3.csv', skiprows=2)
Isometric_20_T1 = pd.read_csv(r'Isometric_20_T1.csv', skiprows=2)
Isometric_20_T2 = pd.read_csv(r'Isometric_20_T2.csv', skiprows=2)
Isometric_5_T1 = pd.read_csv(r'Isometric_5_T1.csv', skiprows=2)
Isometric_5_T2 = pd.read_csv(r'Isometric_5_T2.csv', skiprows=2)
Isometric_5_T3 = pd.read_csv(r'Isometric_5_T3.csv', skiprows=2)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].plot(Isometric_80_T1['Performance'])
axs[0].set_title('Isometric_80_T1')

axs[1].plot(Isometric_80_T2['Performance'])
axs[1].set_title('Isometric_80_T2')

axs[2].plot(Isometric_80_T3['Performance'])
axs[2].set_title('Isometric_80_T3')
plt.show()

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].plot(Isometric_60_T1['Performance'])
axs[0].set_title('Isometric_60_T1')

axs[1].plot(Isometric_60_T2['Performance'])
axs[1].set_title('Isometric_60_T2')

axs[2].plot(Isometric_60_T3['Performance'])
axs[2].set_title('Isometric_60_T3')
plt.show()

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].plot(Isometric_40_T1['Performance'])
axs[0].set_title('Isometric_40_T1')

axs[1].plot(Isometric_40_T2['Performance'])
axs[1].set_title('Isometric_40_T2')

axs[2].plot(Isometric_40_T3['Performance'])
axs[2].set_title('Isometric_40_T3')
plt.show()

fig, axs = plt.subplots(1, 2, figsize=(15, 5))

axs[0].plot(Isometric_20_T1['Performance'])
axs[0].set_title('Isometric_20_T1')

axs[1].plot(Isometric_20_T2['Performance'])
axs[1].set_title('Isometric_20_T2')

plt.show()

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].plot(Isometric_5_T1['Performance'])
axs[0].set_title('Isometric_5_T1')

axs[1].plot(Isometric_5_T2['Performance'])
axs[1].set_title('Isometric_5_T2')

axs[2].plot(Isometric_5_T3['Performance'])
axs[2].set_title('Isometric_5_T3')
plt.show()








# starting_point = 0.2
# start_Isometric_80_T1 = int(abs(len(Isometric_80_T1['Performance']) * starting_point))
# start_Isometric_80_T2 = int(abs(len(Isometric_80_T2['Performance']) * starting_point))
# start_Isometric_80_T3 = int(abs(len(Isometric_80_T3['Performance']) * starting_point))
# start_Isometric_60_T1 = int(abs(len(Isometric_60_T1['Performance']) * starting_point))
# start_Isometric_60_T2 = int(abs(len(Isometric_60_T2['Performance']) * starting_point))
# start_Isometric_60_T3 = int(abs(len(Isometric_60_T3['Performance']) * starting_point))
# start_Isometric_40_T1 = int(abs(len(Isometric_40_T1['Performance']) * starting_point))
# start_Isometric_40_T2 = int(abs(len(Isometric_40_T2['Performance']) * starting_point))
# start_Isometric_40_T3 = int(abs(len(Isometric_40_T3['Performance']) * starting_point))
# start_Isometric_20_T1 = int(abs(len(Isometric_20_T1['Performance']) * starting_point))
# start_Isometric_20_T2 = int(abs(len(Isometric_20_T2['Performance']) * starting_point))
# start_Isometric_5_T1 = int(abs(len(Isometric_5_T1['Performance']) * starting_point))
# start_Isometric_5_T2 = int(abs(len(Isometric_5_T2['Performance']) * starting_point))
# start_Isometric_5_T3 = int(abs(len(Isometric_5_T3['Performance']) * starting_point))
#
# ending_point = 0.3
# end_Isometric_80_T1 = int(abs(len(Isometric_80_T1['Performance']) * ending_point))
# end_Isometric_80_T2 = int(abs(len(Isometric_80_T2['Performance']) * ending_point))
# end_Isometric_80_T3 = int(abs(len(Isometric_80_T3['Performance']) * ending_point))
# end_Isometric_60_T1 = int(abs(len(Isometric_60_T1['Performance']) * ending_point))
# end_Isometric_60_T2 = int(abs(len(Isometric_60_T2['Performance']) * ending_point))
# end_Isometric_60_T3 = int(abs(len(Isometric_60_T3['Performance']) * ending_point))
# end_Isometric_40_T1 = int(abs(len(Isometric_40_T1['Performance']) * ending_point))
# end_Isometric_40_T2 = int(abs(len(Isometric_40_T2['Performance']) * ending_point))
# end_Isometric_40_T3 = int(abs(len(Isometric_40_T3['Performance']) * ending_point))
# end_Isometric_20_T1 = int(abs(len(Isometric_20_T1['Performance']) * ending_point))
# end_Isometric_20_T2 = int(abs(len(Isometric_20_T2['Performance']) * ending_point))
# end_Isometric_5_T1 = int(abs(len(Isometric_5_T1['Performance']) * ending_point))
# end_Isometric_5_T2 = int(abs(len(Isometric_5_T2['Performance']) * ending_point))
# end_Isometric_5_T3 = int(abs(len(Isometric_5_T3['Performance']) * ending_point))
#
#
#
# SaEn_Isometric_80_T1 = lb.Ent_Samp(Isometric_80_T1['Performance'], 2,0.2)
# SaEn_Isometric_80_T2 = lb.Ent_Samp(Isometric_80_T2['Performance'], 2,0.2)
# SaEn_Isometric_80_T3 = lb.Ent_Samp(Isometric_80_T3['Performance'], 2,0.2)
# SaEn_Isometric_60_T1 = lb.Ent_Samp(Isometric_60_T1['Performance'], 2,0.2)
# SaEn_Isometric_60_T2 = lb.Ent_Samp(Isometric_60_T2['Performance'], 2,0.2)
# SaEn_Isometric_60_T3 = lb.Ent_Samp(Isometric_60_T3['Performance'], 2,0.2)
# SaEn_Isometric_40_T1 = lb.Ent_Samp(Isometric_40_T1['Performance'], 2,0.2)
# SaEn_Isometric_40_T2 = lb.Ent_Samp(Isometric_40_T2['Performance'], 2,0.2)
# SaEn_Isometric_40_T3 = lb.Ent_Samp(Isometric_40_T3['Performance'], 2,0.2)
# SaEn_Isometric_20_T1 = lb.Ent_Samp(Isometric_20_T1['Performance'], 2,0.2)
# SaEn_Isometric_20_T2 = lb.Ent_Samp(Isometric_20_T2['Performance'], 2,0.2)
# SaEn_Isometric_5_T1 = lb.Ent_Samp(Isometric_5_T1['Performance'], 2,0.2)
# SaEn_Isometric_5_T2 = lb.Ent_Samp(Isometric_5_T2['Performance'], 2,0.2)
# SaEn_Isometric_5_T3 = lb.Ent_Samp(Isometric_5_T3['Performance'], 2,0.2)
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
# SaEn_80 = [SaEn_Isometric_80_T1, SaEn_Isometric_80_T2, SaEn_Isometric_80_T3]
# SaEn_60 = [SaEn_Isometric_60_T1, SaEn_Isometric_60_T2, SaEn_Isometric_60_T3]
# SaEn_40 = [SaEn_Isometric_40_T1, SaEn_Isometric_40_T2, SaEn_Isometric_40_T3]
# SaEn_20 = [SaEn_Isometric_20_T1, SaEn_Isometric_20_T2]
# SaEn_5 = [SaEn_Isometric_5_T1, SaEn_Isometric_5_T2, SaEn_Isometric_5_T3]
#
# SaEn_80_mean = np.mean(SaEn_80)
# SaEn_60_mean = np.mean(SaEn_60)
# SaEn_40_mean = np.mean(SaEn_40)
# SaEn_20_mean = np.mean(SaEn_20)
# SaEn_5_mean = np.mean(SaEn_5)
#
# SaEn_mean_list = [SaEn_5_mean, SaEn_20_mean, SaEn_40_mean, SaEn_60_mean, SaEn_80_mean]
# Percentage_list = [5,20,40,60,80]
#
# plt.plot(SaEn_80, label='80')
# plt.plot(SaEn_60, label='60')
# plt.plot(SaEn_40, label='40')
# plt.plot(SaEn_20, label='20')
# plt.plot(SaEn_5, label='5')
# plt.legend()
# plt.show()
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
# #
# plt.plot(Percentage_list, SaEn_mean_list)
# plt.legend()
# plt.show()