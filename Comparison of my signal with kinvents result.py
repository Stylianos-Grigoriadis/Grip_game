import pandas as pd
import matplotlib.pyplot as plt
import lib
import numpy as np

original_signal = pd.read_excel(r"G:\Το Drive μου\Εργαστήριον\Python_projects\PhD\Grip strength\Signals\Pink Noise Signal.xlsx")

kinvent_signal = pd.read_csv(r"G:\Το Drive μου\Εργαστήριον\Operation Doctora\Specific Aims\Grip game\Pilot study 2\grip_strength_Grig_Styl___31Mar24_16_14_36.csv", delimiter=",", decimal=".",skiprows=2)
print(kinvent_signal.columns)
kinvent_list = []
for i in range(len(kinvent_signal["Target"])):
    print(kinvent_signal["Target"][i])
    if kinvent_signal["Target"][i] != "-":
        kinvent_list.append(kinvent_signal["Target"][i])
print(kinvent_list)
new_kinvent_list=[]
for i in range(len(kinvent_list)-1):
    if kinvent_list[i+1]!=kinvent_list[i]:
        new_kinvent_list.append(float(kinvent_list[i]))
print(len(kinvent_list))
print(len(new_kinvent_list))
max_percentage = np.max(new_kinvent_list)
min_percentage = np.min(new_kinvent_list)
RM = 35
diff_perc = max_percentage-min_percentage
for i in range(len(original_signal[0])):
    original_signal[0][i] = (original_signal[0][i] * diff_perc / 100)
for i in range(len(original_signal[0])):
    original_signal[0][i] = original_signal[0][i] + min_percentage


time_kinvent = np.arange(0,100,100/(len(new_kinvent_list)))
time_original = np.arange(0,100,1)
plt.plot(time_kinvent,new_kinvent_list, label = "Kinvent data", linewidth= 3)
plt.plot(time_original,original_signal[0], label = "Original data", linewidth= 3, linestyle='--')
plt.legend()
plt.show()