import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np


directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\4. Christos Chalitsios'
os.chdir(directory_path)

Pert_down = pd.read_csv(r'Pert_down.csv', skiprows=2)
Pert_up = pd.read_csv(r'Pert_up.csv', skiprows=2)
#
# plt.plot(Pert_down['Performance'], label='Perc_down')
# plt.plot(Pert_up['Performance'], label='Pert_up')
# plt.legend()
# plt.show()


print(Pert_down)

df = lb.isolate_Target(Pert_down)
fig, ax1 = plt.subplots()
ax1.plot(df['ClosestSampleTime'], label='ClosestSampleTime')
plt.legend()
ax2 = ax1.twiny()
ax2.plot(df['Time'],label='Time', color='red')
plt.legend()
plt.show()
# for i,j in zip(new_Time,ClosestSampleTime1):
#     print(i,j)




