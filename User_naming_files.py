import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import glob


# Define the directory path
directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\Malvina 10-21-2024'
# Warm_up_1
# Warm_up_2
# Warm_up_3
# Warm_up_4
# Warm_up_5
# Isometric_5_T1
# Isometric_5_T2
# Isometric_5_T3
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
# Pert_down
# Pert_up
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
    plt.plot(signal['Performance'])
    plt.title(file_name)
    plt.show()


