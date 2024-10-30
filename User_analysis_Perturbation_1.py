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

NewPercDown = lb.isolate_Target(Pert_down)
print(NewPercDown)

