import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import lib
import colorednoise as cn
from fathon import fathonUtils as fu
import fathon

# plt.rcParams.update({'axes.facecolor':'black'})

def pink_noise_generator2(number_of_sets,targets_per_set,RM,time_per_set,percentage_of_mean,max_perc,min_perc,H=1):
    """
    Generation of pink noise signal
    Inputs:
            number_of_sets:     Total number of sets
            targets_per_set:    Total targets for each set
            RM:                 Max Force assessment
            time_per_set =      Total time of each set
            std:                Standard Deviation of generated time series
            H =                 Hurst exponent, the resulted signal will have Hurst exponent ± 0.02, default H = 1
            percentage_of_mean: This is the percentage of 1Rm which will be the mean value for our signal
     Outputs:
            signal:             A list with a pink noise signal
            Time:               A list with the Time
    """
    beta=1

    total_number_targets=number_of_sets*targets_per_set
    found_time_series = False
    i=0
    std = (10*RM)/100
    while not found_time_series:
        signal = cn.powerlaw_psd_gaussian(beta, total_number_targets)
        mean = (percentage_of_mean*RM)/100
        print("mean")
        print(mean)
        signal = [i + mean for i in signal]
        signal = [i * std for i in signal]
        mean_post = np.mean(signal)
        signal = [i + (mean - mean_post) for i in signal]
        DFA_a = DFA(signal)
        # the mean value is 70% of 1RM therefore we want our signal to be between 50% and 90% of 1RM
        max = (mean * max_perc) / 70
        min = (mean * min_perc) / 70
        i += 1
        if DFA_a > (H - 0.02) and DFA_a < (H + 0.02) and np.max(signal)<max and np.min(signal)>min:
            print(f"Found a pink signal with the right characteristics after {i} efforts")
            found_time_series = True
    total_time = number_of_sets * time_per_set
    step_for_time = total_time / (number_of_sets * targets_per_set)
    Time = np.arange(0, total_time, step_for_time)
    return signal,Time

def DFA(variable):
    """
    Calculation of an exponent of a given signal
    """

    a = fu.toAggregated(variable)

    pydfa = fathon.DFA(a)

    winSizes = fu.linRangeByStep(start=10, end=int(len(variable)/8))
    revSeg = True
    polOrd = 1

    n, F = pydfa.computeFlucVec(winSizes, revSeg=revSeg, polOrd=polOrd)

    H, H_intercept = pydfa.fitFlucVec()
    # plt.plot(np.log(n), np.log(F), 'ro')
    # plt.plot(np.log(n), H_intercept + H * np.log(n), 'k-', label='H = {:.2f}'.format(H))
    # plt.xlabel('ln(n)', fontsize=14)
    # plt.ylabel('ln(F(n))', fontsize=14)
    # plt.title('DFA', fontsize=14)
    # plt.legend(loc=0, fontsize=14)
    # # plt.clf()
    # plt.show()
    return H

def Rigid_targets_generator (number_of_sets,targets_per_set,RM,time_per_set,percentage_of_mean,max_perc):
    """
    Generation of rigid signal
    Inputs:
            amplitude:          amplitude of signal
            number_of_sets:     Total number of sets
            targets_per_set:    Total targets for each set
            RM:                 Max Force assessment
            time_per_set:       Total time of each set
            percentage_of_mean: This is the percentage of 1Rm which will be the mean value for our signal
            max_perc:           max value of percentage of 1RM (%)
            min_perc:           min value of percentage of 1RM (%)

     Outputs:
            signal:             A list with a pink noise signal
            Time:               A list with the Time
    """
    mean = (percentage_of_mean * RM) / 100
    max = (mean * max_perc) / percentage_of_mean
    difference_max_mean = max-mean
    amplitude = difference_max_mean
    total_time = number_of_sets*time_per_set
    step_for_time = total_time / (number_of_sets * targets_per_set)
    Time = np.arange(0,total_time,step_for_time)
    total_number_of_targets = number_of_sets * targets_per_set
    targets = np.arange(0, total_number_of_targets, 1)
    signal = amplitude * np.sin(targets) + mean
    return signal,Time

def Total_force_output(data_series,number_of_sets,time_per_set,targets_per_set):
    total_force_output = 0
    for i in range(len(data_series)):
        total_force_output = total_force_output + data_series[i]
        print(data_series[i])
        print(total_force_output)
    # Calculation of area under the force curve
    Total_area = 0
    total_time = number_of_sets * time_per_set
    step_for_time = total_time / (number_of_sets * targets_per_set)
    for i in range(len(data_series)):
        if i - 1 > 0:
            Total_area = Total_area + (((data_series[i - 1] + data_series[i])*step_for_time)/2)
        else:
            pass
    return total_force_output, Total_area


total_force_output_pink = []
total_force_output_rigid = []
area_under_force_curve_pink = []
area_under_force_curve_rigid = []

pink_signals = []
rigid_signals = []


number_of_sets = 5
targets_per_set = 20
time_per_set = 30
RM = 50
percentage_of_mean = 70
max_perc = 90
min_perc = 50
pink_signal = pink_noise_generator2(number_of_sets=number_of_sets,targets_per_set=targets_per_set,time_per_set=time_per_set,RM=RM,percentage_of_mean=percentage_of_mean,max_perc=max_perc,min_perc=min_perc)
rigid_signal = Rigid_targets_generator(number_of_sets=number_of_sets, targets_per_set=targets_per_set,time_per_set=time_per_set,RM=RM,percentage_of_mean=percentage_of_mean,max_perc=max_perc)
total_force_rigid = Total_force_output(rigid_signal[0],number_of_sets=number_of_sets,targets_per_set=targets_per_set,time_per_set=time_per_set)
total_force_pink = Total_force_output(pink_signal[0],number_of_sets=number_of_sets,targets_per_set=targets_per_set,time_per_set=time_per_set)
results= {' ' : ['Total force', 'Area under force', 'Std', 'Average'],
        'Pink signal' : [total_force_pink[0], total_force_pink[1], np.std(pink_signal[0]), np.mean(rigid_signal[0])],
        'Rigid signal' : [total_force_rigid[0], total_force_rigid[1], np.std(rigid_signal[0]), np.mean(pink_signal[0])]}
df = pd.DataFrame(results)
print(df)
total_force_output_pink.append(total_force_pink[0])
total_force_output_rigid.append(total_force_rigid[0])
area_under_force_curve_pink.append(total_force_pink[1])
area_under_force_curve_rigid.append(total_force_rigid[1])
total_time = number_of_sets*time_per_set
step_for_time = total_time / (number_of_sets * targets_per_set)
Time = np.arange(0,total_time,step_for_time)
for i in range(1,number_of_sets+1):
    plt.axvline(x=i*Time[-1]/number_of_sets,color='blue')
# plt.style.use('dark_background')
plt.scatter(pink_signal[1], pink_signal[0],color="red",lw=4)
plt.scatter(rigid_signal[1], rigid_signal[0],color="black",lw=4)
plt.plot(rigid_signal[1], rigid_signal[0],color="black", label="Rigid Signal")
plt.plot(pink_signal[1],pink_signal[0],color="red", label="Pink Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend(labelcolor='linecolor')
plt.show()

    # dict = {'Time': rigid_signal[1], 'Pink signal': pink_signal[0], 'Rigid signal': rigid_signal[0]}
    # df = pd.DataFrame(dict)
    # print(df)
rigid_signals.append(rigid_signal[0])
pink_signals.append(pink_signal[0])
    # df.to_excel(f'Signals {j}.xlsx', index=False)
# dict = {'Pink signal': total_force_output_pink, 'Rigid signal': total_force_output_rigid}
# df = pd.DataFrame(dict)
# df.to_excel(f'Total force output.xlsx', index=False)
# dict = {'Pink signal': area_under_force_curve_pink, 'Rigid signal': area_under_force_curve_rigid}
# df = pd.DataFrame(dict)

# print(len(rigid_signals))
# print(len(rigid_signals[0]))
# # df.to_excel(f'Area under force curve.xlsx', index=False)
# df_rigid_signals = pd.DataFrame(rigid_signals)
# df_rigid_signals=df_rigid_signals.transpose()
# print(df_rigid_signals)
#
# rigid_names = [f"Rigid Signal {i}" for i in range(1,21)]
# print(rigid_names)
# df_rigid_signals.columns = rigid_names
# print(df_rigid_signals)
# df_rigid_signals.to_excel(f'Rigid signals.xlsx', index=False)
#
# df_pink_signals = pd.DataFrame(pink_signals)
# df_pink_signals=df_pink_signals.transpose()
# print(df_pink_signals)
#
# pink_names = [f"Pink Signal {i}" for i in range(1,21)]
# print(pink_names)
# df_pink_signals.columns = pink_names
# print(df_pink_signals)
# df_pink_signals.to_excel(f'Pink signals.xlsx', index=False)

""" Generation of a pink noise signal as percentage of its max value"""

beta = 1
number_of_sets = 5
targets_per_set = 20
total_number_targets=number_of_sets*targets_per_set
list_average = []
totalforc_list = []
max_percentage= 90
min_percentage = 50
diff_perc = max_percentage-min_percentage
signal = cn.powerlaw_psd_gaussian(beta, total_number_targets)
min = np.min(signal)
for i in range(len(signal)):
    signal[i] = signal[i] -min
max = np.max(signal)
for i in range(len(signal)):
    signal[i] = signal[i]*100/max
for i in range(len(signal)):
    signal[i] = (signal[i] * diff_perc / 100)
for i in range(len(signal)):
    signal[i] = signal[i] + min_percentage

plt.plot(signal)
plt.show()
print()
print(np.mean(signal))
print(np.std(signal))
# df = pd.DataFrame(signal)
# df.to_excel("Pink Noise Signal.xlsx", index=False)



