import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Malvina 10-7-2024\Raw'
os.chdir(directory_path)


# Perturbation_up = pd.read_csv(r'Perturbation_up_800points.csv', skiprows=2)
# # Perturbation_down = pd.read_csv(r'Perturbation_down.csv', skiprows=2)
# print(len(Perturbation_up['Target']))
# Perturbation_up_isolate = lb.isolate_Target(Perturbation_up)
# print(len(Perturbation_up_isolate['Target']))
# plt.plot(Perturbation_up_isolate['Time'], Perturbation_up_isolate['Performance'])
# plt.scatter(Perturbation_up_isolate['Time'],Perturbation_up_isolate['Target'], c='red')
# plt.scatter(Perturbation_up['Time'],Perturbation_up['Target'], c='black')
# plt.show()
#
my_txt_perturbation_up_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 7\Signals\Sine signal N500 freq0.1 Max50.txt'
my_txt_perturbation_up = lb.read_my_txt_file(my_txt_perturbation_up_path)
# print(len(my_txt_perturbation_up))
kinvent_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 7\Data\Stylianos 10.11.2024\Sine signal N500 freq0.1 Max50.csv'
MVC = 50


signal_kinvent = pd.read_csv(kinvent_path, skiprows=2)
print(signal_kinvent)
signal_kinvent = lb.isolate_Target(signal_kinvent)
print(signal_kinvent)
dif_index = []
for i in range(len(signal_kinvent['Index']) -1):
    dif_index.append(signal_kinvent['Index'][i+1] - signal_kinvent['Index'][i])
plt.plot(dif_index)
plt.show()



signal = lb.add_generated_signal(kinvent_path, my_txt_perturbation_up_path, MVC)
plt.plot(signal['Target'], label='Target')
plt.plot(signal['Generated_Signal'], label='Generated_Signal')
# plt.plot(signal['Performance'], label='Performance')
plt.legend()
plt.show()