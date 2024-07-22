import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import Lib_grip as lb
#
# path_pink = (r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Data\Pink signal N350 Max100 Min0.csv')
# set_1_pink,set_2_pink,set_3_pink,set_4_pink,set_5_pink = lb.read_kinvent(path_pink)

# path_sine = (r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Data\Sine signal 3 N350 freq0.5 Max60 Min40 UpperPerc30 LowerPerc1.csv')
# set_1_sine,set_2_sine,set_3_sine,set_4_sine,set_5_sine = lb.read_kinvent(path_sine)

# set_1_Target_pink = lb.isolate_Target(set_1_pink)
# set_2_Target_pink = lb.isolate_Target(set_2_pink)
# set_3_Target_pink = lb.isolate_Target(set_3_pink)
# set_4_Target_pink = lb.isolate_Target(set_4_pink)
# set_5_Target_pink = lb.isolate_Target(set_5_pink)
#
# set_1_Target_sine = lb.isolate_Target(set_1_sine)
# set_2_Target_sine = lb.isolate_Target(set_2_sine)
# set_3_Target_sine = lb.isolate_Target(set_3_sine)
# set_4_Target_sine = lb.isolate_Target(set_4_sine)
# set_5_Target_sine = lb.isolate_Target(set_5_sine)
#
# set_1_only_Target_sine = set_1_Target_sine['Target'].to_list()
# set_2_only_Target_sine = set_2_Target_sine['Target'].to_list()
# set_3_only_Target_sine = set_3_Target_sine['Target'].to_list()
# set_4_only_Target_sine = set_4_Target_sine['Target'].to_list()
# set_5_only_Target_sine = set_5_Target_sine['Target'].to_list()
#
# target_sine = set_1_only_Target_sine + set_2_only_Target_sine + set_3_only_Target_sine + set_4_only_Target_sine + set_5_only_Target_sine
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

# plt.plot(sp_er_pink, c='pink', label='pink')
# plt.plot(sp_er_sine, c='black', label='black')
# plt.legend()
# plt.show()


# df_pert = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Signals\Perturbation N15.txt', delimiter=',', decimal='.',header=None)
# print(df_pert)
# pert_list = []
# for i in range(194):
#     pert_list.append(df_pert[i][0])
# print(pert_list)
# time_pert = np.arange(len(pert_list))
#
# plt.scatter([i for i in range(len(pert_list))],pert_list)
#
#
# df = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Data\Perturbation N15.csv',skiprows=2, delimiter=',' )
# print(df)
#
# pert_target = lb.isolate_Target(df)
# plt.plot(pert_target['Target'])
# plt.show()
# print('len')
# print(len(pert_target['Target']))
# print(len(pert_list))
# step = 154/30
# #
# print(len(pert_target['Time']))
# plt.plot(df['Time'], df['Performance'])
# plt.scatter(pert_target['Time'], pert_target['Target'], c='red', lw=3)
# # plt.scatter(pert_target['Time'], pert_list, c='black', lw=3)
# plt.show()
# print(len(set_1_only_Target_sine))
# print(len(set_2_only_Target_sine))
# print(len(set_3_only_Target_sine))
# print(len(set_4_only_Target_sine))
# print(len(set_5_only_Target_sine))




# sine_generated = lb.read_my_txt_file(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Signals\Sine signal 3 N350 freq0.5 Max60 Min40.txt')
#
# path_sine = (r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Data\Sine signal 3 N350 freq0.5 Max60 Min40 UpperPerc30 LowerPerc1.csv')
# set_1_sine_30,set_2_sine_30,set_3_sine_30,set_4_sine_30,set_5_sine_30 = lb.read_kinvent(path_sine)
#
# set_1_Target_sine_30 = lb.isolate_Target(set_1_sine_30)
# set_2_Target_sine_30 = lb.isolate_Target(set_2_sine_30)
# set_3_Target_sine_30 = lb.isolate_Target(set_3_sine_30)
# set_4_Target_sine_30 = lb.isolate_Target(set_4_sine_30)
# set_5_Target_sine_30 = lb.isolate_Target(set_5_sine_30)
#
# set_1_only_Target_sine_30 = set_1_Target_sine_30['Target'].to_list()
# set_2_only_Target_sine_30 = set_2_Target_sine_30['Target'].to_list()
# set_3_only_Target_sine_30 = set_3_Target_sine_30['Target'].to_list()
# set_4_only_Target_sine_30 = set_4_Target_sine_30['Target'].to_list()
# set_5_only_Target_sine_30 = set_5_Target_sine_30['Target'].to_list()
#
# target_sine_30 = set_1_only_Target_sine_30 + set_2_only_Target_sine_30 + set_3_only_Target_sine_30 + set_4_only_Target_sine_30 + set_5_only_Target_sine_30
#
# path_sine = (r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Data\Sine signal 3 N350 freq0.5 Max60 Min40 UpperPerc10 LowerPerc1.csv')
# set_1_sine_10,set_2_sine_10,set_3_sine_10,set_4_sine_10,set_5_sine_10 = lb.read_kinvent(path_sine)
#
# set_1_Target_sine_10 = lb.isolate_Target(set_1_sine_10)
# set_2_Target_sine_10 = lb.isolate_Target(set_2_sine_10)
# set_3_Target_sine_10 = lb.isolate_Target(set_3_sine_10)
# set_4_Target_sine_10 = lb.isolate_Target(set_4_sine_10)
# set_5_Target_sine_10 = lb.isolate_Target(set_5_sine_10)
#
# set_1_only_Target_sine_10 = set_1_Target_sine_10['Target'].to_list()
# set_2_only_Target_sine_10 = set_2_Target_sine_10['Target'].to_list()
# set_3_only_Target_sine_10 = set_3_Target_sine_10['Target'].to_list()
# set_4_only_Target_sine_10 = set_4_Target_sine_10['Target'].to_list()
# set_5_only_Target_sine_10 = set_5_Target_sine_10['Target'].to_list()
#
# target_sine_10 = set_1_only_Target_sine_10 + set_2_only_Target_sine_10 + set_3_only_Target_sine_10 + set_4_only_Target_sine_10 + set_5_only_Target_sine_10
#
# path_sine = (r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Data\Sine signal 3 N350 freq0.5 Max60 Min40 UpperPerc5 LowerPerc1.csv')
# set_1_sine_5,set_2_sine_5,set_3_sine_5,set_4_sine_5,set_5_sine_5 = lb.read_kinvent(path_sine)
#
# set_1_Target_sine_5 = lb.isolate_Target(set_1_sine_5)
# set_2_Target_sine_5 = lb.isolate_Target(set_2_sine_5)
# set_3_Target_sine_5 = lb.isolate_Target(set_3_sine_5)
# set_4_Target_sine_5 = lb.isolate_Target(set_4_sine_5)
# set_5_Target_sine_5 = lb.isolate_Target(set_5_sine_5)
#
# set_1_only_Target_sine_5 = set_1_Target_sine_5['Target'].to_list()
# set_2_only_Target_sine_5 = set_2_Target_sine_5['Target'].to_list()
# set_3_only_Target_sine_5 = set_3_Target_sine_5['Target'].to_list()
# set_4_only_Target_sine_5 = set_4_Target_sine_5['Target'].to_list()
# set_5_only_Target_sine_5 = set_5_Target_sine_5['Target'].to_list()
#
# target_sine_5 = set_1_only_Target_sine_5 + set_2_only_Target_sine_5 + set_3_only_Target_sine_5 + set_4_only_Target_sine_5 + set_5_only_Target_sine_5
#
# sine_generated_0_to_30 = lb.Perc(sine_generated, 30,1)
# sine_generated_0_to_10 = lb.Perc(sine_generated, 10,1)
# sine_generated_0_to_5 = lb.Perc(sine_generated, 5,1)
#
# #
# # plt.plot(sine_generated_0_to_10, label='Sine Generated')
# # plt.plot(target_sine_30, label='Sine from Kinvent')
# # plt.legend()
# # plt.show()
#
# fig, axs = plt.subplots(3, 1, figsize=(12, 15))
# axs[0].plot(sine_generated_0_to_30)
# axs[0].plot(target_sine_30)
# axs[0].set_title("Sine with 30 max force")
#
# axs[1].plot(sine_generated_0_to_10)
# axs[1].plot(target_sine_10)
# axs[1].set_title("Sine with 10 max force")
#
# axs[2].plot(sine_generated_0_to_5, label='Sine Generated')
# axs[2].plot(target_sine_5, label='Sine Kinvent')
# axs[2].set_title("Sine with 5 max force")
# plt.legend()
# plt.show()

path = r'C:\Users\Βασίλης\OneDrive\Υπολογιστής\Python\Grip_strength\grip_strength_Grig_Styl___22Jul24_17_51_56.csv'
df = pd.read_csv(path, skiprows=2)

target = lb.isolate_Target(df)

plt.plot(target['Performance'])
plt.plot(target['Target'])

spatial_error = lb.spatial_error(df)
plt.plot(spatial_error)

sd_baseline = np.std(spatial_error[:49])
mean_baseline = np.mean(spatial_error[:49])
print(sd_baseline)
print(mean_baseline)
plt.show()
spatial_error = spatial_error[50:65]



lb.asymptotes(spatial_error,sd_baseline,mean_baseline)
