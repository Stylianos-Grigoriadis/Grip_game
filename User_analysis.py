import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import Lib_grip as lb

path_pink = (r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Data\Pink signal N350 Max100 Min0.csv')
set_1_pink,set_2_pink,set_3_pink,set_4_pink,set_5_pink = lb.read_kinvent(path_pink)

path_sine = (r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Data\Sine signal 3 N350 freq0.5 Max60 Min40.csv')
set_1_sine,set_2_sine,set_3_sine,set_4_sine,set_5_sine = lb.read_kinvent(path_sine)

set_1_Target_pink = lb.isolate_Target(set_1_pink)
set_2_Target_pink = lb.isolate_Target(set_2_pink)
set_3_Target_pink = lb.isolate_Target(set_3_pink)
set_4_Target_pink = lb.isolate_Target(set_4_pink)
set_5_Target_pink = lb.isolate_Target(set_5_pink)
#
set_1_Target_sine = lb.isolate_Target(set_1_sine)
set_2_Target_sine = lb.isolate_Target(set_2_sine)
set_3_Target_sine = lb.isolate_Target(set_3_sine)
set_4_Target_sine = lb.isolate_Target(set_4_sine)
set_5_Target_sine = lb.isolate_Target(set_5_sine)
#
# fig, axs = plt.subplots(5, 2, figsize=(12, 15))
#
# axs[0,0].plot(set_1_pink['Time'], set_1_pink['Performance'])
# axs[0,0].scatter(set_1_Target_pink['Time'], set_1_Target_pink['Target'], c='red')
# axs[0,0].set_title('Pink Signal')
# axs[0,0].set_ylabel('Set 1')
#
# axs[1,0].plot(set_2_pink['Time'], set_2_pink['Performance'])
# axs[1,0].scatter(set_2_Target_pink['Time'], set_2_Target_pink['Target'], c='red')
# axs[1,0].set_ylabel('Set 2')
#
# axs[2,0].plot(set_3_pink['Time'], set_3_pink['Performance'])
# axs[2,0].scatter(set_3_Target_pink['Time'], set_3_Target_pink['Target'], c='red')
# axs[2,0].set_ylabel('Set 3')
#
# axs[3,0].plot(set_4_pink['Time'], set_4_pink['Performance'])
# axs[3,0].scatter(set_4_Target_pink['Time'], set_4_Target_pink['Target'], c='red')
# axs[3,0].set_ylabel('Set 4')
#
# axs[4,0].plot(set_5_pink['Time'], set_5_pink['Performance'])
# axs[4,0].scatter(set_5_Target_pink['Time'], set_5_Target_pink['Target'], c='red')
#
# axs[4,0].set_xlabel('Time')
# axs[4,0].set_ylabel('Set 5')
#
# axs[0,1].plot(set_1_sine['Time'], set_1_sine['Performance'])
# axs[0,1].scatter(set_1_Target_sine['Time'], set_1_Target_sine['Target'], c='red')
# axs[0,1].set_title('Sine Signal')
# axs[0,1].set_ylabel('Set 1')
#
#
# axs[1,1].plot(set_2_sine['Time'], set_2_sine['Performance'])
# axs[1,1].scatter(set_2_Target_sine['Time'], set_2_Target_sine['Target'], c='red')
# axs[1,1].set_ylabel('Set 2')
#
# axs[2,1].plot(set_3_sine['Time'], set_3_sine['Performance'])
# axs[2,1].scatter(set_3_Target_sine['Time'], set_3_Target_sine['Target'], c='red')
# axs[2,1].set_ylabel('Set 3')
#
# axs[3,1].plot(set_4_sine['Time'], set_4_sine['Performance'])
# axs[3,1].scatter(set_4_Target_sine['Time'], set_4_Target_sine['Target'], c='red')
# axs[3,1].set_ylabel('Set 4')
#
#
# axs[4,1].plot(set_5_sine['Time'], set_5_sine['Performance'])
# axs[4,1].scatter(set_5_Target_sine['Time'], set_5_Target_sine['Target'], c='red')
# axs[4,1].set_xlabel('Time')
# axs[4,1].set_ylabel('Set 5')
#
# # plt.tight_layout()
# plt.show()
#
#
#
#
# sp_er_pink_1 = lb.spacial_error(set_1_pink)
# sp_er_pink_2 = lb.spacial_error(set_2_pink)
# sp_er_pink_3 = lb.spacial_error(set_3_pink)
# sp_er_pink_4 = lb.spacial_error(set_4_pink)
# sp_er_pink_5 = lb.spacial_error(set_5_pink)
# sp_er_pink = sp_er_pink_1 + sp_er_pink_2 + sp_er_pink_3 + sp_er_pink_4 + sp_er_pink_5
#
# sp_er_sine_1 = lb.spacial_error(set_1_sine)
# sp_er_sine_2 = lb.spacial_error(set_2_sine)
# sp_er_sine_3 = lb.spacial_error(set_3_sine)
# sp_er_sine_4 = lb.spacial_error(set_4_sine)
# sp_er_sine_5 = lb.spacial_error(set_5_sine)
# sp_er_sine = sp_er_sine_1 + sp_er_sine_2 + sp_er_sine_3 + sp_er_sine_4 + sp_er_sine_5
#
# fig, axs = plt.subplots(5, 2, figsize=(12, 15))
#
# axs[0,0].plot(sp_er_pink_1, c='pink', lw = 3)
# axs[0,0].set_title('Pink Signal')
# axs[0,0].set_ylabel('Set 1')
#
# axs[1,0].plot(sp_er_pink_2, c='pink', lw = 3)
# axs[1,0].set_ylabel('Set 2')
#
# axs[2,0].plot(sp_er_pink_3, c='pink', lw = 3)
# axs[2,0].set_ylabel('Set 3')
#
# axs[3,0].plot(sp_er_pink_4, c='pink', lw = 3)
# axs[3,0].set_ylabel('Set 4')
#
# axs[4,0].plot(sp_er_pink_5, c='pink', lw = 3)
# axs[4,0].set_xlabel('Time')
# axs[4,0].set_ylabel('Set 5')
#
# axs[0,1].plot(sp_er_sine_1, c='black', lw = 3)
# axs[0,1].set_title('Sine Signal')
# axs[0,1].set_ylabel('Set 1')
#
# axs[1,1].plot(sp_er_sine_2, c='black', lw = 3)
# axs[1,1].set_ylabel('Set 2')
#
# axs[2,1].plot(sp_er_sine_3, c='black', lw = 3)
# axs[2,1].set_ylabel('Set 3')
#
# axs[3,1].plot(sp_er_sine_4, c='black', lw = 3)
# axs[3,1].set_ylabel('Set 4')
#
# axs[4,1].plot(sp_er_sine_5, c='black', lw = 3)
# axs[4,1].set_xlabel('Time')
# axs[4,1].set_ylabel('Set 5')
# plt.show()
#
#
# plt.plot(sp_er_pink, c='pink', label='pink')
# plt.plot(sp_er_sine, c='black', label='black')
# plt.legend()
# plt.show()

# perturbation = lb.perturbation_both_force(60,40,90,30,50,10,60,90,70,15)
# plt.plot(perturbation)
# plt.show()
# lb.create_txt_file(perturbation,'Perturbation N15', r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Signals')
###############
# df_pert = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Signals\Perturbation N15.txt', delimiter=',', decimal='.',header=None)
# print(df_pert)
# pert_list = []
# for i in range(194):
#     pert_list.append(df_pert[i][0])
# print(pert_list)
# time_pert = np.arange(len(pert_list))
#
#
#
# df = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Data\Perturbation N15.csv',skiprows=2, delimiter=',' )
# print(df)
#
# pert_target = lb.isolate_Target(df)
# plt.plot(pert_target['Target'])
# plt.show()
#
#
# plt.plot(df['Time'], df['Performance'])
# plt.scatter(pert_target['Time'], pert_target['Target'], c='red', lw=3)
# # plt.scatter(pert_target['Time'], pert_list, c='black', lw=3)
# plt.show()

# array = np.full(120, 40)
# plt.plot(array)
# plt.show()
# lb.create_txt_file(array, 'Isometric Test of constant 40%', r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Signals')

my_signal_pink = lb.read_my_txt_file(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Signals\Pink signal N350 Max100 Min0.txt')
my_signal_pink = my_signal_pink*10/100
my_signal_pink_time = np.arange(0,len(my_signal_pink))
print(my_signal_pink_time)
print(len(my_signal_pink_time))

set_1_pink_list = set_1_Target_pink['Target'].to_list()
set_2_pink_list = set_2_Target_pink['Target'].to_list()
set_3_pink_list = set_3_Target_pink['Target'].to_list()
set_4_pink_list = set_4_Target_pink['Target'].to_list()
set_5_pink_list = set_5_Target_pink['Target'].to_list()
pink_list = set_1_pink_list + set_2_pink_list + set_3_pink_list + set_4_pink_list + set_5_pink_list
time_pink = np.arange(0,len(pink_list))
print(time_pink)
print(len(time_pink))

plt.scatter(time_pink,pink_list, label='Generated from KInvent', c='orange', lw=3)
plt.plot(pink_list, c='orange')
plt.scatter(my_signal_pink_time,my_signal_pink, label='Generated from Lab', c='pink', lw=3)
plt.plot(my_signal_pink, c='pink')
plt.legend()
plt.show()


my_signal_sine = lb.read_my_txt_file(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Signals\Sine signal 3 N350 freq0.5 Max60 Min40.txt')
my_signal_sine = my_signal_sine - 40
my_signal_sine = my_signal_sine*100/np.max(my_signal_sine)
my_signal_sine = my_signal_sine*0.1
my_signal_sine_time = np.arange(0,len(my_signal_sine))


set_1_sine_list = set_1_Target_sine['Target'].to_list()
set_2_sine_list = set_2_Target_sine['Target'].to_list()
set_3_sine_list = set_3_Target_sine['Target'].to_list()
set_4_sine_list = set_4_Target_sine['Target'].to_list()
set_5_sine_list = set_5_Target_sine['Target'].to_list()
sine_list = set_1_sine_list + set_2_sine_list + set_3_sine_list + set_4_sine_list + set_5_sine_list
time_sine = np.arange(0,len(sine_list))

plt.scatter(time_sine,sine_list, label='Generated from KInvent', c='orange', lw=3)
plt.plot(sine_list, c='orange')
plt.scatter(my_signal_sine_time,my_signal_sine, label='Generated from Lab', c='black', lw=3)
plt.plot(my_signal_sine, c='black')
plt.legend()
plt.show()