import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Malvina 10-7-2024\Raw'
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

print(len(Isometric_80_T2['Performance']))

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


starting_point = 0.2
start_Isometric_80_T1 = int(abs(len(Isometric_80_T1['Performance']) * starting_point))
start_Isometric_80_T2 = int(abs(len(Isometric_80_T2['Performance']) * starting_point))
start_Isometric_80_T3 = int(abs(len(Isometric_80_T3['Performance']) * starting_point))
start_Isometric_60_T1 = int(abs(len(Isometric_60_T1['Performance']) * starting_point))
start_Isometric_60_T2 = int(abs(len(Isometric_60_T2['Performance']) * starting_point))
start_Isometric_60_T3 = int(abs(len(Isometric_60_T3['Performance']) * starting_point))
start_Isometric_40_T1 = int(abs(len(Isometric_40_T1['Performance']) * starting_point))
start_Isometric_40_T2 = int(abs(len(Isometric_40_T2['Performance']) * starting_point))
start_Isometric_40_T3 = int(abs(len(Isometric_40_T3['Performance']) * starting_point))
start_Isometric_20_T1 = int(abs(len(Isometric_20_T1['Performance']) * starting_point))
start_Isometric_20_T2 = int(abs(len(Isometric_20_T2['Performance']) * starting_point))
start_Isometric_5_T1 = int(abs(len(Isometric_5_T1['Performance']) * starting_point))
start_Isometric_5_T2 = int(abs(len(Isometric_5_T2['Performance']) * starting_point))
start_Isometric_5_T3 = int(abs(len(Isometric_5_T3['Performance']) * starting_point))

ending_point = 0.3
end_Isometric_80_T1 = int(len(Isometric_80_T1['Performance']) - (len(Isometric_80_T1['Performance']) * ending_point))
end_Isometric_80_T2 = int(len(Isometric_80_T2['Performance']) - (len(Isometric_80_T2['Performance']) * ending_point))
end_Isometric_80_T3 = int(len(Isometric_80_T3['Performance']) - (len(Isometric_80_T3['Performance']) * ending_point))
end_Isometric_60_T1 = int(len(Isometric_60_T1['Performance']) - (len(Isometric_60_T1['Performance']) * ending_point))
end_Isometric_60_T2 = int(len(Isometric_60_T2['Performance']) - (len(Isometric_60_T2['Performance']) * ending_point))
end_Isometric_60_T3 = int(len(Isometric_60_T3['Performance']) - (len(Isometric_60_T3['Performance']) * ending_point))
end_Isometric_40_T1 = int(len(Isometric_40_T1['Performance']) - (len(Isometric_40_T1['Performance']) * ending_point))
end_Isometric_40_T2 = int(len(Isometric_40_T2['Performance']) - (len(Isometric_40_T2['Performance']) * ending_point))
end_Isometric_40_T3 = int(len(Isometric_40_T3['Performance']) - (len(Isometric_40_T3['Performance']) * ending_point))
end_Isometric_20_T1 = int(len(Isometric_20_T1['Performance']) - (len(Isometric_20_T1['Performance']) * ending_point))
end_Isometric_20_T2 = int(len(Isometric_20_T2['Performance']) - (len(Isometric_20_T2['Performance']) * ending_point))
end_Isometric_5_T1 = int(len(Isometric_5_T1['Performance']) - (len(Isometric_5_T1['Performance']) * ending_point))
end_Isometric_5_T2 = int(len(Isometric_5_T2['Performance']) - (len(Isometric_5_T2['Performance']) * ending_point))
end_Isometric_5_T3 = int(len(Isometric_5_T3['Performance']) - (len(Isometric_5_T3['Performance']) * ending_point))
print(start_Isometric_80_T1)
print(end_Isometric_80_T1)



SaEn_Isometric_80_T1 = lb.Ent_Samp(Isometric_80_T1['Performance'][start_Isometric_80_T1:end_Isometric_80_T1], 2,0.2)
SaEn_Isometric_80_T2 = lb.Ent_Samp(Isometric_80_T2['Performance'][start_Isometric_80_T2:end_Isometric_80_T2], 2,0.2)
SaEn_Isometric_80_T3 = lb.Ent_Samp(Isometric_80_T3['Performance'][start_Isometric_80_T3:end_Isometric_80_T3], 2,0.2)
SaEn_Isometric_60_T1 = lb.Ent_Samp(Isometric_60_T1['Performance'][start_Isometric_60_T1:end_Isometric_60_T1], 2,0.2)
SaEn_Isometric_60_T2 = lb.Ent_Samp(Isometric_60_T2['Performance'][start_Isometric_60_T2:end_Isometric_60_T2], 2,0.2)
SaEn_Isometric_60_T3 = lb.Ent_Samp(Isometric_60_T3['Performance'][start_Isometric_60_T3:end_Isometric_60_T3], 2,0.2)
SaEn_Isometric_40_T1 = lb.Ent_Samp(Isometric_40_T1['Performance'][start_Isometric_40_T1:end_Isometric_40_T1], 2,0.2)
SaEn_Isometric_40_T2 = lb.Ent_Samp(Isometric_40_T2['Performance'][start_Isometric_40_T2:end_Isometric_40_T2], 2,0.2)
SaEn_Isometric_40_T3 = lb.Ent_Samp(Isometric_40_T3['Performance'][start_Isometric_40_T3:end_Isometric_40_T3], 2,0.2)
SaEn_Isometric_20_T1 = lb.Ent_Samp(Isometric_20_T1['Performance'][start_Isometric_20_T1:end_Isometric_20_T1], 2,0.2)
SaEn_Isometric_20_T2 = lb.Ent_Samp(Isometric_20_T2['Performance'][start_Isometric_20_T2:end_Isometric_20_T2], 2,0.2)
SaEn_Isometric_20_T3 = SaEn_Isometric_20_T2 #Change this if you have all trials
SaEn_Isometric_5_T1 = lb.Ent_Samp(Isometric_5_T1['Performance'][start_Isometric_5_T1:end_Isometric_5_T1], 2,0.2)
SaEn_Isometric_5_T2 = lb.Ent_Samp(Isometric_5_T2['Performance'][start_Isometric_5_T2:end_Isometric_5_T2], 2,0.2)
SaEn_Isometric_5_T3 = lb.Ent_Samp(Isometric_5_T3['Performance'][start_Isometric_5_T3:end_Isometric_5_T3], 2,0.2)

Sd_Isometric_80_T1 = np.std(Isometric_80_T1['Performance'][start_Isometric_80_T1:end_Isometric_80_T1])
Sd_Isometric_80_T2 = np.std(Isometric_80_T2['Performance'][start_Isometric_80_T2:end_Isometric_80_T2])
Sd_Isometric_80_T3 = np.std(Isometric_80_T3['Performance'][start_Isometric_80_T3:end_Isometric_80_T3])
Sd_Isometric_60_T1 = np.std(Isometric_60_T1['Performance'][start_Isometric_60_T1:end_Isometric_60_T1])
Sd_Isometric_60_T2 = np.std(Isometric_60_T2['Performance'][start_Isometric_60_T2:end_Isometric_60_T2])
Sd_Isometric_60_T3 = np.std(Isometric_60_T3['Performance'][start_Isometric_60_T3:end_Isometric_60_T3])
Sd_Isometric_40_T1 = np.std(Isometric_40_T1['Performance'][start_Isometric_40_T1:end_Isometric_40_T1])
Sd_Isometric_40_T2 = np.std(Isometric_40_T2['Performance'][start_Isometric_40_T2:end_Isometric_40_T2])
Sd_Isometric_40_T3 = np.std(Isometric_40_T3['Performance'][start_Isometric_40_T3:end_Isometric_40_T3])
Sd_Isometric_20_T1 = np.std(Isometric_20_T1['Performance'][start_Isometric_20_T1:end_Isometric_20_T1])
Sd_Isometric_20_T2 = np.std(Isometric_20_T2['Performance'][start_Isometric_20_T2:end_Isometric_20_T2])
Sd_Isometric_20_T3 = Sd_Isometric_20_T2 #Change this if you have all trials
Sd_Isometric_5_T1 = np.std(Isometric_5_T1['Performance'][start_Isometric_5_T1:end_Isometric_5_T1])
Sd_Isometric_5_T2 = np.std(Isometric_5_T2['Performance'][start_Isometric_5_T2:end_Isometric_5_T2])
Sd_Isometric_5_T3 = np.std(Isometric_5_T3['Performance'][start_Isometric_5_T3:end_Isometric_5_T3])
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


Perturbation_up = pd.read_csv(r'Perturbation_up.csv', skiprows=2)
Perturbation_down = pd.read_csv(r'Perturbation_down.csv', skiprows=2)

Perturbation_up = lb.isolate_Target(Perturbation_up)

plt.plot(Perturbation_up['Time'], Perturbation_up['Performance'])
plt.scatter(Perturbation_up['Time'],Perturbation_up['Target'])
plt.show()