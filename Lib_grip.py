import numpy as np
from fathon import fathonUtils as fu
import fathon
import matplotlib.pyplot as plt
from scipy.stats import linregress
import pandas as pd
import colorednoise as cn


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
    """This function takes a signal as a list and turns is in a 0 to 100% ratio"""
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
    signal = cn.powerlaw_psd_gaussian(1, Number_of_data_points)
    signal = Perc(signal,upper_lim,lower_lim)

    return signal

def sine_signal_generator():
    pass
signal = pink_signal_generator(500, 11, 9)
print(type(signal))
plt.plot(signal)
plt.show()
DFA(signal)