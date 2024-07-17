import numpy as np
from fathon import fathonUtils as fu
import fathon
import matplotlib.pyplot as plt
from scipy.stats import linregress
import pandas as pd
import colorednoise as cn
import random


def DFA(variable):
    a = fu.toAggregated(variable)
        #b = fu.toAggregated(b)

    pydfa = fathon.DFA(a)

    winSizes = fu.linRangeByStep(start=4, end=int(len(variable)/4))
    revSeg = True
    polOrd = 1

    n, F = pydfa.computeFlucVec(winSizes, revSeg=revSeg, polOrd=polOrd)

    H, H_intercept = pydfa.fitFlucVec()
    plt.plot(np.log(n), np.log(F), 'ro')
    plt.plot(np.log(n), H_intercept + H * np.log(n), 'k-', label='H = {:.2f}'.format(H))
    plt.xlabel('ln(n)', fontsize=14)
    plt.ylabel('ln(F(n))', fontsize=14)
    plt.title('DFA', fontsize=14)
    plt.legend(loc=0, fontsize=14)
    #plt.clf()
    plt.show()
    return H


def Perc(signal , upper_lim, lower_lim):
    """This function takes a signal as a np.array and turns it as values from upper_lim to lower_lim"""
    if np.min(signal) < 0:
        signal = signal - np.min(signal)
    signal = 100 * signal / np.max(signal)
    min_val = signal.min()
    max_val = signal.max()
    signal = (signal - min_val) / (max_val - min_val)
    new_range = upper_lim - lower_lim
    signal = signal * new_range + lower_lim
    return signal


def read_kinvent(path):
    """This funcion reads the Kinvent csv file for the grip"""
    df = pd.read_csv(path, header=None, delimiter=';')
    index = []
    for i, string in enumerate(df[0]):
        if 'Repetition: ' in string:
            index.append(i)
    print(index)

    df_set_1 = pd.read_csv(path, skiprows=2, nrows=index[1]-index[0] - 3)
    df_set_2 = pd.read_csv(path, skiprows=index[1]+2, nrows=index[2]-index[1] -3)
    df_set_3 = pd.read_csv(path, skiprows=index[2]+2, nrows=index[3]-index[2] -3)
    df_set_4 = pd.read_csv(path, skiprows=index[3]+2, nrows=index[4]-index[3] -3)
    df_set_5 = pd.read_csv(path, skiprows=index[4]+2)

    return df_set_1,df_set_2,df_set_3,df_set_4,df_set_5


def pink_signal_generator(Number_of_data_points, upper_lim, lower_lim):
    """This function creates a pink noise signal as a np.array with N Number_of_data_points between upper_lim and lower_lim"""
    dfa = False
    while dfa == False:
        signal = cn.powerlaw_psd_gaussian(1, Number_of_data_points)
        α_exp = DFA(signal)
        if α_exp < 1.05 and α_exp > 0.95:
            dfa = True
    signal = Perc(signal,upper_lim,lower_lim)

    return signal


def sine_signal_generator(Number_of_data_points, frequency, Total_Time, upper_lim, lower_lim):

    x = np.arange(0, Number_of_data_points)
    signal = np.sin(x*frequency)
    signal = Perc(signal, upper_lim, lower_lim)

    time = np.arange(0, Total_Time, Total_Time / Number_of_data_points)
    return signal, time


def create_txt_file(signal, name, path):
    "This Function takes a np.array and turns it into a txt file so that it can be used in the KINVENT grip game"
    element = ''
    for i in signal:
        element = element + str(i) + ','
    element = element[:-1]
    list_to_save = [element]
    df = pd.DataFrame(list_to_save)
    print(df)
    df.to_csv(rf'{path}\{name}.txt',header=False, index=False, sep=' ')


def make_it_random(up_1, up_2, up_3, down_1, down_2, down_3):
    list1 = [up_1, up_2, up_3, down_1, down_2, down_3]
    random.shuffle(list1)
    print(type(list1))
    return list1


def perturbation_both_force(up_1, up_2, up_3, down_1, down_2, down_3, step_1, step_2, step_3, data_num):
    baseline = np.zeros(data_num)
    pert_up_1 = np.full(data_num, up_1)
    pert_up_2 = np.full(data_num, up_2)
    pert_up_3 = np.full(data_num, up_3)
    pert_down_1 = np.full(data_num, down_1)
    pert_down_2 = np.full(data_num, down_2)
    pert_down_3 = np.full(data_num, down_3)
    pert_step_1 = np.full(int(data_num/5), step_1)
    pert_step_2 = np.full(int(data_num/5), step_2)
    pert_step_3 = np.full(int(data_num/5), step_3)
    pert_down_whole_1 = np.concatenate((pert_step_1, pert_down_1))
    pert_down_whole_2 = np.concatenate((pert_step_2, pert_down_2))
    pert_down_whole_3 = np.concatenate((pert_step_3, pert_down_3))

    overall_list = make_it_random(pert_up_1, pert_up_2, pert_up_3, pert_down_whole_1, pert_down_whole_2, pert_down_whole_3)

    final_pert = np.concatenate((baseline, overall_list[0], baseline, overall_list[1], baseline, overall_list[2], baseline, overall_list[3], baseline, overall_list[4],
                                 baseline, overall_list[5]))
    return final_pert



perturbation = perturbation_both_force(20,40,80,30,60,10,50,90,70,100)
print(len(perturbation))
plt.plot(perturbation)
plt.show()
create_txt_file(perturbation,'Perturbation signal 1', r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Signals')



# pink_signal = pink_signal_generator(500,80,20)
# DFA(pink_signal)
# create_txt_file(pink_signal,'Pink signal 1', r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Signals')

print()