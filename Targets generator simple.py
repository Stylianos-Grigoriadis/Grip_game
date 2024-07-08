import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import lib
import colorednoise as cn
from fathon import fathonUtils as fu
import fathon


beta = 1
number_of_sets = 5
targets_per_set = 20
total_number_targets=number_of_sets*targets_per_set
list_average = []
totalforc_list = []
max_percentage= 90
min_percentage = 30
# df = pd.read_excel(r"G:\My Drive\Εργαστήριον\Python_projects\PhD\Grip strength\Pink Noise Signal.xlsx")
# print(df)
signal_all=[]
for i in range(5):
    print(i)
    signal = cn.powerlaw_psd_gaussian(beta, 100)
    # min = np.max(df[0])
    # print(min)
    min = np.min(signal)
    for i in range(len(signal)):
        signal[i] = signal[i] -min
    max = np.max(signal)
    for i in range(len(signal)):
        signal[i] = signal[i]*100/max
    for i in range(len(signal)):
        signal_all.append(signal[i])
    DFA = lib.DFA(signal)
    print("DFA_gen")
    print(DFA)
# plt.plot(signal_all)
# plt.show()
a = lib.DFA(signal_all)
signal_0 = pd.read_excel(r"G:\My Drive\Εργαστήριον\Python_projects\PhD\Grip strength\Signals\Signals 1.xlsx")
print(signal_0)
signal_1 = pd.read_excel(r"G:\My Drive\Εργαστήριον\Python_projects\PhD\Grip strength\Signals\Signals 9.xlsx")
signal_2 = pd.read_excel(r"G:\My Drive\Εργαστήριον\Python_projects\PhD\Grip strength\Signals\Signals 4.xlsx")
signal_3 = pd.read_excel(r"G:\My Drive\Εργαστήριον\Python_projects\PhD\Grip strength\Signals\Signals 2.xlsx")
signal_4 = pd.read_excel(r"G:\My Drive\Εργαστήριον\Python_projects\PhD\Grip strength\Signals\Signals 7.xlsx")

min = np.min(signal_0["Pink signal"])
for i in range(len(signal_0["Pink signal"])):
    signal_0["Pink signal"][i]=signal_0["Pink signal"][i]-min
max = np.max(signal_0["Pink signal"])
for i in range(len(signal_0["Pink signal"])):
    signal_0["Pink signal"][i]=(100*signal_0["Pink signal"][i])/max
plt.plot(signal_0["Pink signal"])
plt.title("signal_0")
plt.show()

min = np.min(signal_1["Pink signal"])
for i in range(len(signal_1["Pink signal"])):
    signal_1["Pink signal"][i]=signal_1["Pink signal"][i]-min
max = np.max(signal_1["Pink signal"])
for i in range(len(signal_1["Pink signal"])):
    signal_1["Pink signal"][i]=(100*signal_1["Pink signal"][i])/max
plt.plot(signal_1["Pink signal"])
plt.title("signal_1")
plt.show()

min = np.min(signal_2["Pink signal"])
for i in range(len(signal_2["Pink signal"])):
    signal_2["Pink signal"][i]=signal_2["Pink signal"][i]-min
max = np.max(signal_2["Pink signal"])
for i in range(len(signal_2["Pink signal"])):
    signal_2["Pink signal"][i]=(100*signal_2["Pink signal"][i])/max
plt.plot(signal_2["Pink signal"])
plt.title("signal_2")
plt.show()

min = np.min(signal_3["Pink signal"])
for i in range(len(signal_3["Pink signal"])):
    signal_3["Pink signal"][i]=signal_3["Pink signal"][i]-min
max = np.max(signal_3["Pink signal"])
for i in range(len(signal_3["Pink signal"])):
    signal_3["Pink signal"][i]=(100*signal_3["Pink signal"][i])/max
plt.plot(signal_3["Pink signal"])
plt.title("signal_3")
plt.show()

min = np.min(signal_4["Pink signal"])
for i in range(len(signal_4["Pink signal"])):
    signal_4["Pink signal"][i]=signal_4["Pink signal"][i]-min
max = np.max(signal_4["Pink signal"])
for i in range(len(signal_4["Pink signal"])):
    signal_4["Pink signal"][i]=(100*signal_4["Pink signal"][i])/max
plt.plot(signal_4["Pink signal"])
plt.title("signal_4")
plt.show()


signal_all_2 =[]

for i in range(len(signal_0["Pink signal"])):
    signal_all_2.append(signal_0["Pink signal"][i])
for i in range(len(signal_1["Pink signal"])):
    signal_all_2.append(signal_1["Pink signal"][i])
for i in range(len(signal_2["Pink signal"])):
    signal_all_2.append(signal_2["Pink signal"][i])
for i in range(len(signal_3["Pink signal"])):
    signal_all_2.append(signal_3["Pink signal"][i])
for i in range(len(signal_4["Pink signal"])):
    signal_all_2.append(signal_4["Pink signal"][i])

b=lib.DFA(signal_all_2)
print("DFA b")
print(b)
plt.plot(signal_all_2)
plt.title("Signal_all")
plt.show()

# Generate 6 different signals
signals = [signal_0["Pink signal"],
           signal_1["Pink signal"],
           signal_2["Pink signal"],
           signal_3["Pink signal"],
           signal_4["Pink signal"],
           signal_all_2]

# Create subplots
fig, axes = plt.subplots(3, 2, figsize=(10, 8))

# Plot each signal in a subplot
for i, signal in enumerate(signals):
    row = i // 2
    col = i % 2
    axes[row, col].plot(signal)
    axes[row, col].set_title(f'Signal {i+1}')
    axes[row, col].set_xlabel('X')
    axes[row, col].set_ylabel('Amplitude')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
df = pd.DataFrame({'Signal': signal_all_2})
df.to_excel('signal_data_500_points.xlsx', index=False)
# print("DFA a")
# print(a)
#
# RM = 11
# diff_perc = max_percentage-min_percentage
# for i in range(len(signal)):
#     signal[i] = (signal[i] * diff_perc / 100)
# for i in range(len(signal)):
#     signal[i] = signal[i] + min_percentage
# for i in range(len(signal)):
#     signal[i] = signal[i] *RM/100
#
# plt.plot(signal)
# plt.title("MAX")
# plt.show()

# min = np.min(signal)
# for i in range(len(signal)):
#     signal[i] = signal[i] *100/RM
# max = np.max(signal)
# for i in range(len(signal)):
#     signal[i] = signal[i]- min_percentage
#
# for i in range(len(signal)):
#     signal[i] = (signal[i] * 100 / diff_perc)
#
# plt.plot(signal)
# plt.title("MAX")
# plt.show()
# print()
# print(np.mean(signal))
# print(np.std(signal))