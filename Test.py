import lib
import Lib_grip as lb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 9\Data\Stylianos 75Hz'
df_75Hz = pd.read_csv(path+r'tablet 75Hz.csv', skiprows=2)
print(df_75Hz)