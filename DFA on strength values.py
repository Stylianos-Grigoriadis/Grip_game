import lib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def read_kinvent(path):
    df = pd.read_csv(path, header=None, delimiter=';')
    index = []
    for i, string in enumerate(df[0]):
        if 'Repetition: ' in string:
            index.append(i)
    print(index)

    df_set_1 = pd.read_csv(path, skiprows=7, nrows=index[1]-index[0] - 8)
    df_set_2 = pd.read_csv(path, skiprows=index[1]+7, nrows=index[2]-index[1] -8)
    df_set_3 = pd.read_csv(path, skiprows=index[2]+7)
    return df_set_1,df_set_2,df_set_3


path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Data of max stren gth\grip_strength_Grig_Stylian__15Jul24_16_36_57_15Jul24_16_37_50.csv'
df_set_1,df_set_2,df_set_3 = read_kinvent(path)

print(df_set_1)
print(df_set_2)
print(df_set_3)
df_set_1 = df_set_1[150:].reset_index()
df_set_2 = df_set_2[150:].reset_index()
df_set_3 = df_set_3[150:].reset_index()
set_1 = np.array(df_set_1['CHANNEL_1'])
set_2 = np.array(df_set_2['CHANNEL_1'])
set_3 = np.array(df_set_3['CHANNEL_1'])
step = 3
set_1 = lib.Linear_Interpolation(set_1,step,0)
set_2 = lib.Linear_Interpolation(set_2,step,0)
set_3 = lib.Linear_Interpolation(set_3,step,0)

plt.plot(set_1, label = 'df_set_1')
plt.plot(set_2, label = 'df_set_2')
plt.plot(set_3, label = 'df_set_3')
plt.legend()
plt.show()


DFA1 = lib.DFA(set_1)
DFA2 = lib.DFA(set_2)
DFA3 = lib.DFA(set_3)
