import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import glob


# Define the directory path
directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\Stylianos 10-16-2024'

files = glob.glob(os.path.join(directory_path, "*"))
for file in files:
    file_name = os.path.basename(file)
    print(file_name)

    signal = pd.read_csv(file, skiprows=2)
    plt.plot(signal['Performance'])
    plt.show()


