import numpy as np
import pandas as pd
import Lib_grip as lb
import matplotlib.pyplot as plt

data_5perc_1,data_5perc_2,data_5perc_3 = lb.read_kinvent(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 9-30-2024\Raw data\Isometric_5%.csv')
data_20perc_1,data_20perc_2,data_20perc_3 = lb.read_kinvent(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 9-30-2024\Raw data\Isometric_20%.csv')
data_40perc_1,data_40perc_2,data_40perc_3 = lb.read_kinvent(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 9-30-2024\Raw data\Isometric_40%.csv')
data_60perc_1,data_60perc_2,data_60perc_3 = lb.read_kinvent(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 9-30-2024\Raw data\Isometric_60%.csv')
data_80perc_1,data_80perc_2,data_80perc_3 = lb.read_kinvent(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 9-30-2024\Raw data\Isometric_80%.csv')
print(len(data_5perc_1["Performance"]))
print(len(data_5perc_2["Performance"]))
print(len(data_5perc_3["Performance"]))
Perc_list = [5,20,40,60,80]

SaEn_list_1 = []
SaEn_list_1.append(lb.Ent_Samp(data_5perc_1['Performance'], 2, 0.2))
SaEn_list_1.append(lb.Ent_Samp(data_20perc_1['Performance'], 2, 0.2))
SaEn_list_1.append(lb.Ent_Samp(data_40perc_1['Performance'], 2, 0.2))
SaEn_list_1.append(lb.Ent_Samp(data_60perc_1['Performance'], 2, 0.2))
SaEn_list_1.append(lb.Ent_Samp(data_80perc_1['Performance'], 2, 0.2))

SaEn_list_2 = []
SaEn_list_2.append(lb.Ent_Samp(data_5perc_2['Performance'], 2, 0.2))
SaEn_list_2.append(lb.Ent_Samp(data_20perc_2['Performance'], 2, 0.2))
SaEn_list_2.append(lb.Ent_Samp(data_40perc_2['Performance'], 2, 0.2))
SaEn_list_2.append(lb.Ent_Samp(data_60perc_2['Performance'], 2, 0.2))
SaEn_list_2.append(lb.Ent_Samp(data_80perc_2['Performance'], 2, 0.2))

SaEn_list_3 = []
SaEn_list_3.append(lb.Ent_Samp(data_5perc_3['Performance'], 2, 0.2))
SaEn_list_3.append(lb.Ent_Samp(data_20perc_3['Performance'], 2, 0.2))
SaEn_list_3.append(lb.Ent_Samp(data_40perc_3['Performance'], 2, 0.2))
SaEn_list_3.append(lb.Ent_Samp(data_60perc_3['Performance'], 2, 0.2))
SaEn_list_3.append(lb.Ent_Samp(data_80perc_3['Performance'], 2, 0.2))

Sd_list_1 = []
Sd_list_1.append(np.std(data_5perc_1['Performance']))
Sd_list_1.append(np.std(data_20perc_1['Performance']))
Sd_list_1.append(np.std(data_40perc_1['Performance']))
Sd_list_1.append(np.std(data_60perc_1['Performance']))
Sd_list_1.append(np.std(data_80perc_1['Performance']))

Sd_list_2 = []
Sd_list_2.append(np.std(data_5perc_2['Performance']))
Sd_list_2.append(np.std(data_20perc_2['Performance']))
Sd_list_2.append(np.std(data_40perc_2['Performance']))
Sd_list_2.append(np.std(data_60perc_2['Performance']))
Sd_list_2.append(np.std(data_80perc_2['Performance']))

Sd_list_3 = []
Sd_list_3.append(np.std(data_5perc_3['Performance']))
Sd_list_3.append(np.std(data_20perc_3['Performance']))
Sd_list_3.append(np.std(data_40perc_3['Performance']))
Sd_list_3.append(np.std(data_60perc_3['Performance']))
Sd_list_3.append(np.std(data_80perc_3['Performance']))


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
#
# path_kinvent = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-9-2024\Raw data\Perturbation up.csv'
# Perturbation_up = pd.read_csv(path_kinvent, delimiter=',',skiprows=2)
#
# path_generated_signal=r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Signals\Final used\Single Perturbation N1000 bas30 pert45.txt'
# max = 54
# max_perc = 54*0.6
#
#
# Perturbation_up_my_txt = lb.add_generated_signal(path_kinvent,path_generated_signal,max_perc)
# print(Perturbation_up_my_txt)
# my_signal = Perturbation_up_my_txt['Signal']
# Kinvent_singal = Perturbation_up_my_txt['Target']
# force = Perturbation_up_my_txt['Performance']
# time = Perturbation_up_my_txt['Time']
# # plt.plot(time, Kinvent_singal, label='Kinvent_singal')
# # plt.plot(time, force, label='force')
# # plt.plot(time, my_signal, label='my_signal')
# # plt.legend()
# # plt.show()
#
#
# Spacial_error = lb.spatial_error(force,my_signal)
#
# time_of_adaptation, index_after_pert = lb.adaptation_time_using_sd(time,force,my_signal,345,2,50,30)
# print(f'time_of_adaptation is {time_of_adaptation}')
# print(f'index_after_pert is {index_after_pert}')
#
#
#
#
#
#
