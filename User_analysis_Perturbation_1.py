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
my_txt_perturbation_up_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Signals\Final used\Sine signal N500 freq0.1 Max50.txt'
my_txt_perturbation_up = lb.read_my_txt_file(my_txt_perturbation_up_path)
# print(len(my_txt_perturbation_up))
kinvent_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 10-9-2024\Raw\Sine signal N500 freq0.1 Max50.csv'
MVC = 50
signal = lb.add_generated_signal(kinvent_path, my_txt_perturbation_up_path, MVC)
print(int(len(signal['Target'])*0.5))

print(rf'Average of Kinvent before Perturbation :{np.mean(signal["Target"][50:100])}')
print(rf'Average of Generated_Signal before Perturbation :{np.mean(signal["Generated_Signal"][50:100])}')
print()
print(rf'Average of Kinvent after Perturbation :{np.mean(signal["Target"][200:250])}')
print(rf'Average of Generated_Signal after Perturbation :{np.mean(signal["Generated_Signal"][200:250])}')
print(signal)
# signal.to_excel(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 10-9-2024\Analyse\excel sinewave.xlsx', index=False)

plt.plot(signal['Target'], label='Target')
plt.plot(signal['Generated_Signal'], label='Generated_Signal')
plt.plot(signal['Performance'], label='Performance')
plt.legend()
plt.show()