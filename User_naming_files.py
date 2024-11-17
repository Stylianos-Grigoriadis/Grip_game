import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import glob
import numpy as np


# Define the directory path
directory_path = r'C:\Users\user\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 10\Data\3.Young'
# Warm_up_1
# Warm_up_2
# Warm_up_3
# Warm_up_4
# Warm_up_5
# Isometric_05_T1
# Isometric_05_T2
# Isometric_05_T3
# Isometric_20_T1
# Isometric_20_T2
# Isometric_20_T3
# Isometric_40_T1
# Isometric_40_T2
# Isometric_40_T3
# Isometric_60_T1
# Isometric_60_T2
# Isometric_60_T3
# Isometric_80_T1
# Isometric_80_T2
# Isometric_80_T3
# Pert_down_T1
# Pert_down_T2
# Pert_up_T1
# Pert_up_T2

max = 30
print(f'5% : {0.05*max}')
print(f'20% : {0.2*max}')
print(f'40% : {0.4*max}')
print(f'60% : {0.6*max}')
print(f'80% : {0.8*max}')

files = glob.glob(os.path.join(directory_path, "*"))
for file in files:
    file_name = os.path.basename(file)
    print(file_name)


    signal = pd.read_csv(file, skiprows=2)
    print(np.mean(signal['Performance'][200:300]))
    plt.plot(signal['Performance'])
    plt.title(file_name)
    # plt.show()






