import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np


# directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\1. Stylianos Grigoriadis'
# directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\2. Malvina Tziouref'
# directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\3. Niki Giannopapa'
# directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\4. Christos Chalitsios'
# directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\5. Damianou Anestis'
# directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\6. Despoina Arampatzidou'
# directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\7. Nick Stergiou'
# -*- coding: utf-8 -*-

directory_path = [r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\1. Stylianos Grigoriadis',
                  r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\2. Malvina Tziouref',
                  r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\3. Niki Giannopapa',
                  r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\4. Christos Chalitsios',
                  r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\5. Damianou Anestis',
                  r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\6. Despoina Arampatzidou',
                  r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\7. Nick Stergiou']
names = ['Stylianos Grigoriadis', 'Malvina Tziouref','Niki Giannopapa','Christos Chalitsios','Damianou Anestis','Despoina Arampatzidou','Nick Stergiou']
time_of_adaptation_up_list = []
time_of_adaptation_down_list = []
for i in directory_path:

    os.chdir(i)

    Pert_down = pd.read_csv(r'Pert_down.csv', skiprows=2)
    Pert_up = pd.read_csv(r'Pert_up.csv', skiprows=2)

    time_of_adaptation_up = lb.adaptation_time_using_sd(Pert_up, 250, 2, 100, 10, 500, plot=True)
    time_of_adaptation_down = lb.adaptation_time_using_sd(Pert_down, 250, 2, 100, 10, 500)

    time_of_adaptation_up_list.append(time_of_adaptation_up)
    time_of_adaptation_down_list.append(time_of_adaptation_down)

dist = {'Participants': names,
        'time_of_adaptation_up' :time_of_adaptation_up_list,
        'time_of_adaptation_down' :time_of_adaptation_down_list}
df = pd.DataFrame(dist)
print(df)




# plt.plot(Pert_down['Time'], Pert_down['Performance'], label='Performance')
# plt.plot(Pert_down['Time'], Pert_down['Target'], label='Target')
# plt.legend()
# plt.title('Perturbation Down')
# plt.show()
#
# plt.plot(Pert_up['Time'], Pert_up['Performance'], label='Performance')
# plt.plot(Pert_up['Time'], Pert_up['Target'], label='Target')
# plt.legend()
# plt.title('Perturbation Up')
# plt.show()



#
# plt.plot(Pert_down['Performance'], label='Perc_down')
# plt.plot(Pert_up['Performance'], label='Pert_up')
# plt.legend()
# plt.show()

# pd.set_option('display.max_rows', 600)
# print(Pert_down.head(600))


# print(new_time)
#
# df = lb.isolate_Target(Pert_down)
# fig, ax1 = plt.subplots()
# ax1.plot(df['ClosestSampleTime'], label='ClosestSampleTime')
# plt.legend()
# ax2 = ax1.twiny()
# ax2.plot(df['Time'],label='Time', color='red')
# plt.legend()
# plt.show()
# for i,j in zip(new_Time,ClosestSampleTime1):
#     print(i,j)




