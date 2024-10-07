import numpy as np
from fathon import fathonUtils as fu
import fathon
import matplotlib.pyplot as plt
from scipy.stats import linregress
import pandas as pd
import colorednoise as cn
import random
from scipy.optimize import curve_fit


def DFA(variable):
    a = fu.toAggregated(variable)
        #b = fu.toAggregated(b)

    pydfa = fathon.DFA(a)

    winSizes = fu.linRangeByStep(start=4, end=int(len(variable)/4))
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
    # #plt.clf()
    # plt.show()
    return H

def Ent_Ap(data, dim, r):
    """
    Ent_Ap20120321
      data : time-series data
      dim : embedded dimension
      r : tolerance (typically 0.2)

      Changes in version 1
          Ver 0 had a minor error in the final step of calculating ApEn
          because it took logarithm after summation of phi's.
          In Ver 1, I restored the definition according to original paper's
          definition, to be consistent with most of the work in the
          literature. Note that this definition won't work for Sample
          Entropy which doesn't count self-matching case, because the count
          can be zero and logarithm can fail.

      *NOTE: This code is faster and gives the same result as ApEn =
             ApEnt(data,m,R) created by John McCamley in June of 2015.
             -Will Denton

    ---------------------------------------------------------------------
    coded by Kijoon Lee,  kjlee@ntu.edu.sg
    Ver 0 : Aug 4th, 2011
    Ver 1 : Mar 21st, 2012
    ---------------------------------------------------------------------
    """

    r = r * np.std(data)
    N = len(data)
    phim = np.zeros(2)
    for j in range(2):
        m = dim + j
        phi = np.zeros(N - m + 1)
        data_mat = np.zeros((N - m + 1, m))
        for i in range(m):
            data_mat[:, i] = data[i:N - m + i + 1]
        for i in range(N - m + 1):
            temp_mat = np.abs(data_mat - data_mat[i, :])
            AorB = np.unique(np.where(temp_mat > r)[0])
            AorB = len(temp_mat) - len(AorB)
            phi[i] = AorB / (N - m + 1)
        phim[j] = np.sum(np.log(phi)) / (N - m + 1)
    AE = phim[0] - phim[1]
    return AE

def Ent_Samp(data, m, r):
    """
    function SE = Ent_Samp20200723(data,m,r)
    SE = Ent_Samp20200723(data,m,R) Returns the sample entropy value.
    inputs - data, single column time seres
            - m, length of vectors to be compared
            - r, radius for accepting matches (as a proportion of the
              standard deviation)

    output - SE, sample entropy
    Remarks
    - This code finds the sample entropy of a data series using the method
      described by - Richman, J.S., Moorman, J.R., 2000. "Physiological
      time-series analysis using approximate entropy and sample entropy."
      Am. J. Physiol. Heart Circ. Physiol. 278, H2039–H2049.
    - m is generally recommendation as 2
    - R is generally recommendation as 0.2
    May 2016 - Modified by John McCamley, unonbcf@unomaha.edu
             - This is a faster version of the previous code.
    May 2019 - Modified by Will Denton
             - Added code to check version number in relation to a server
               and to automatically update the code.
    Jul 2020 - Modified by Ben Senderling, bmchnonan@unomaha.edu
             - Removed the code that automatically checks for updates and
               keeps a version history.
    Define r as R times the standard deviation
    """
    R = r * np.std(data)
    N = len(data)

    data = np.array(data)

    dij = np.zeros((N - m, m + 1))
    dj = np.zeros((N - m, 1))
    dj1 = np.zeros((N - m, 1))
    Bm = np.zeros((N - m, 1))
    Am = np.zeros((N - m, 1))

    for i in range(N - m):
        for k in range(m + 1):
            dij[:, k] = np.abs(data[k:N - m + k] - data[i + k])
        dj = np.max(dij[:, 0:m], axis=1)
        dj1 = np.max(dij, axis=1)
        d = np.where(dj <= R)
        d1 = np.where(dj1 <= R)
        nm = d[0].shape[0] - 1  # subtract the self match
        Bm[i] = nm / (N - m)
        nm1 = d1[0].shape[0] - 1  # subtract the self match
        Am[i] = nm1 / (N - m)

    Bmr = np.sum(Bm) / (N - m)
    Amr = np.sum(Am) / (N - m)

    return -np.log(Amr / Bmr)

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
    df_set_1 = pd.read_csv(path, skiprows=2, nrows=index[1]-index[0] - 3)
    df_set_2 = pd.read_csv(path, skiprows=index[1]+2, nrows=index[2]-index[1] -3)
    df_set_3 = pd.read_csv(path, skiprows=index[2]+2)
    # df_set_4 = pd.read_csv(path, skiprows=index[3]+2, nrows=index[4]-index[3] -3)
    # df_set_5 = pd.read_csv(path, skiprows=index[4]+2)

    return (df_set_1,
            df_set_2,
            df_set_3)
            # df_set_4,
            # df_set_5)

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

def sine_signal_generator(Number_of_data_points, frequency, upper_lim, lower_lim):

    x = np.arange(0, Number_of_data_points)
    signal = np.sin(x*frequency)
    signal = Perc(signal, upper_lim, lower_lim)

    # time = np.arange(0, Total_Time, Total_Time / Number_of_data_points)
    # return signal, time
    return signal

def isometric_generator_with_reps(Number_of_data_points,value):
    reps_in_set = 20
    total_reps = Number_of_data_points/reps_in_set
    targets_in_each_rep = Number_of_data_points/total_reps
    array_force = np.full(int(targets_in_each_rep/2), value)
    array_zero = np.zeros(int(targets_in_each_rep/2))
    array_single_rep = np.concatenate((array_zero, array_force))
    signal = np.tile(array_single_rep,reps_in_set)
    return signal

def isometric_generator_single_rep(Number_of_data_points,value):
    signal = np.full(Number_of_data_points,value)
    return signal

def create_txt_file(signal, name, path):
    "This Function takes a np.array and turns it into a txt file so that it can be used in the KINVENT grip game"
    element = ''
    for i in signal:
        element = element + str(i) + ','
    element = element[:-1]
    list_to_save = [element]
    df = pd.DataFrame(list_to_save)
    df.to_csv(rf'{path}\{name}.txt',header=False, index=False, sep=' ')

def make_it_random(up_1, up_2, up_3, down_1, down_2, down_3):
    list1 = [up_1, up_2, up_3, down_1, down_2, down_3]
    random.shuffle(list1)

    return list1

def perturbation_both_force(up_1, up_2, up_3, down_1, down_2, down_3, step_1, step_2, step_3, data_num):
    dat_for_each_pert = int(data_num/12)

    baseline = np.zeros(dat_for_each_pert)
    pert_up_1 = np.full(dat_for_each_pert, up_1)
    pert_up_2 = np.full(dat_for_each_pert, up_2)
    pert_up_3 = np.full(dat_for_each_pert, up_3)
    pert_down_1 = np.full(dat_for_each_pert, down_1)
    pert_down_2 = np.full(dat_for_each_pert, down_2)
    pert_down_3 = np.full(dat_for_each_pert, down_3)
    pert_step_1 = np.full(int(dat_for_each_pert/3), step_1)
    pert_step_2 = np.full(int(dat_for_each_pert/3), step_2)
    pert_step_3 = np.full(int(dat_for_each_pert/3), step_3)
    pert_down_whole_1 = np.concatenate((pert_step_1, pert_down_1))
    pert_down_whole_2 = np.concatenate((pert_step_2, pert_down_2))
    pert_down_whole_3 = np.concatenate((pert_step_3, pert_down_3))

    overall_list = make_it_random(pert_up_1, pert_up_2, pert_up_3, pert_down_whole_1, pert_down_whole_2, pert_down_whole_3)

    final_pert = np.concatenate((baseline, overall_list[0],
                                 baseline, overall_list[1],
                                 baseline, overall_list[2],
                                 baseline, overall_list[3],
                                 baseline, overall_list[4],
                                 baseline, overall_list[5]))
    return final_pert

def total_force(signal):
    total = np.sum(signal)
    return total

def isolate_Target(df):
    target = []
    time = []
    performance = []
    index = []
    for i in range(len(df['Target'])):
        if df['Target'][i] != 0.0:
            index.append(i)
            target.append(df['Target'][i])
            time.append(df['Time'][i])
            performance.append(df['Performance'][i])

    df_targets = pd.DataFrame({'Time' : time, 'Target' : target, 'Performance' : performance})
    return df_targets, index

def spatial_error(force, signal):
    spatial_error = []
    for i in range(len(signal)):
        if signal[i] != 0:
            spatial_error.append(abs(force[i] - signal[i]))
    spatial_error = np.array(spatial_error)
    return spatial_error

def read_my_txt_file(path):
    df = pd.read_csv(path, delimiter=',', decimal='.',header=None)

    signal_list = []
    for i in range(df.shape[1]):
        signal_list.append(df[i][0])
    signal = np.array(signal_list)

    return signal

def asymptotes(df):
    index_where_perturbation_occured = 99
    time = 10
    error = spatial_error(df['Performance'], df['Target'])
    mean = np.mean(error[int(index_where_perturbation_occured/2):index_where_perturbation_occured-1])
    sd = np.std(error[int(index_where_perturbation_occured/2):index_where_perturbation_occured-1])
    error = error[index_where_perturbation_occured:]
    print(len(df['Time']))
    time_for_each_target = time/len(df['Time'])
    print(time_for_each_target)

    index = np.array([i for i in range(len(error))])
    def f(x, a, b, c):
        return a * (b ** x) + c

    popt, _ = curve_fit(f, index, error, bounds=((0, 0, -np.inf), (np.inf, 1, np.inf)), maxfev=30000)
    a, b, c = popt
    print(f'y = {a} * {b}**x + {c}')
    x_line = np.arange(0, len(index), 1)
    y_line = f(x_line, a, b, c)

    plt.plot(x_line, y_line, '--', color='green', label='fit')
    plt.axhline(y=c, c='k', label='Asymptote')
    sd_factor = 1
    c = mean
    plt.axhline(y=c, c='red', label='Mean error before perturbation')
    plt.axhline(y=c + sd_factor * sd, c='red', ls=":", label="sd error before perturbation")
    plt.axhline(y=c - sd_factor * sd, c='red', ls=":")
    plt.scatter(index,error)
    plt.legend()
    plt.show()
    for i in range(len(error)-5):
        if c - sd_factor * sd < error[i] < c + sd_factor * sd and c - sd_factor * sd < error[i+1] < c + sd_factor * sd and c - sd_factor * sd < error[i+sd_factor] < c + sd_factor * sd and c - sd_factor * sd < error[i+3] < c + sd_factor * sd and c - sd_factor * sd < error[i+4] < c + sd_factor * sd:
            print(i)
            adaptation_index = i
            break
    print(f'adaptation index was {adaptation_index}')
    print(f'adaptation time was {adaptation_index*time_for_each_target}')
    dict = {'adaptation_index' : adaptation_index,
            'adaptation_time' : adaptation_index*time_for_each_target}
    return dict

def adaptation_time_using_sd(time, force, signal, perturbation_index, sd_factor, first_values, consecutive_values):
    """This function returns the time after the perturbation which was needed to adapt to the perturbation
        Variables explanation:
            time:               the whole time from 0 until the end
            force:              the whole force from 0 until the end
            signal:             the whole signal of perturbation from 0 until the end
            perturbation_index: the index at which the perturbation occurred
            sd_factor:          this will be multiplied with the sd of the error before the perturbation
                                and if the error after the is less than the mean + sd*sd_factor and more than
                                the mean - sd*sd_factor, the algorithm will consider that the adaptation of the
                                perturbation occurred
            first_values:       at first the error will be too much so to calculate the mean and sd before the perturbation
                                right, we erase some values from the beginning
            consecutive_values: this is how many values the algorithm needs to consider so that it decides of the adaptation occurred.
            """

    spatial_er = spatial_error(force, signal)
    mean = np.mean(spatial_er[first_values:perturbation_index])
    sd_before_perturbation = np.std(spatial_er[first_values:perturbation_index])

    plt.plot(spatial_er)
    plt.axhline(y=mean, color='k')
    plt.axhline(y=mean + sd_before_perturbation*sd_factor, c='red', ls=":")
    plt.axhline(y=mean - sd_before_perturbation*sd_factor, c='red', ls=":")
    plt.show()


    consecutive_values_list = np.arange(0,consecutive_values,1)

    for i in range(len(spatial_er) - consecutive_values+1):
        if i >= perturbation_index:
            print(i)
            if (all(spatial_er[i + j] < mean + sd_before_perturbation * sd_factor for j in consecutive_values_list) and
                all(spatial_er[i + j] > mean - sd_before_perturbation * sd_factor for j in consecutive_values_list)
            ):
                time_of_adaptation = time[i] - time[perturbation_index]
                index_after_pert = i - perturbation_index
                break
    return time_of_adaptation, index_after_pert

def single_perturbation_generator(baseline, perturbation, data_num):
    baseline_array = np.full(int(data_num/2), baseline)
    perturbation_array = np.full(int(data_num/2), perturbation)
    final_pert = np.concatenate((baseline_array, perturbation_array))

    return final_pert

def isometric_min_max(MVC):
    sd = 10
    iso_90 = 90
    iso_80 = 80
    iso_70 = 70
    iso_60 = 60
    iso_50 = 50
    iso_40 = 40
    iso_30 = 30
    iso_20 = 20
    iso_15 = 15
    iso_10 = 10
    iso_5 = 5
    iso_2_half = 2.5

    iso_90_perc = MVC * iso_90 / 100
    iso_80_perc = MVC * iso_80 / 100
    iso_70_perc = MVC * iso_70 / 100
    iso_60_perc = MVC * iso_60 / 100
    iso_50_perc = MVC * iso_50 / 100
    iso_40_perc = MVC * iso_40 / 100
    iso_30_perc = MVC * iso_30 / 100
    iso_20_perc = MVC * iso_20 / 100
    iso_15_perc = MVC * iso_15 / 100
    iso_10_perc = MVC * iso_10 / 100
    iso_5_perc = MVC * iso_5 / 100
    iso_2_half_perc = MVC * iso_2_half / 100

    iso_90_min = (iso_90 - sd) * MVC / 100
    iso_80_min = (iso_80 - sd) * MVC / 100
    iso_70_min = (iso_70 - sd) * MVC / 100
    iso_60_min = (iso_60 - sd) * MVC / 100
    iso_50_min = (iso_50 - sd) * MVC / 100
    iso_40_min = (iso_40 - sd) * MVC / 100
    iso_30_min = (iso_30 - sd) * MVC / 100
    iso_20_min = (iso_20 - sd) * MVC / 100
    iso_15_min = (iso_15 - sd) * MVC / 100
    iso_10_min = (iso_10 - sd) * MVC / 100
    iso_5_min = (iso_5 - iso_5) * MVC / 100
    iso_2_half_min = (iso_2_half - iso_2_half) * MVC / 100

    iso_90_max = (iso_90 + sd) * MVC / 100
    iso_80_max = (iso_80 + sd) * MVC / 100
    iso_70_max = (iso_70 + sd) * MVC / 100
    iso_60_max = (iso_60 + sd) * MVC / 100
    iso_50_max = (iso_50 + sd) * MVC / 100
    iso_40_max = (iso_40 + sd) * MVC / 100
    iso_30_max = (iso_30 + sd) * MVC / 100
    iso_20_max = (iso_20 + sd) * MVC / 100
    iso_15_max = (iso_15 + sd) * MVC / 100
    iso_10_max = (iso_10 + sd) * MVC / 100
    iso_5_max = (iso_5 + iso_5) * MVC / 100
    iso_2_half_max = (iso_2_half + iso_2_half) * MVC / 100


    print(f"For 90% of MVC ({iso_90_perc}) the min values is {iso_90_min} and the max values is {iso_90_max}")
    print(f"For 80% of MVC ({iso_80_perc}) the min values is {iso_80_min} and the max values is {iso_80_max}")
    print(f"For 70% of MVC ({iso_70_perc}) the min values is {iso_70_min} and the max values is {iso_70_max}")
    print(f"For 60% of MVC ({iso_60_perc}) the min values is {iso_60_min} and the max values is {iso_60_max}")
    print(f"For 50% of MVC ({iso_50_perc}) the min values is {iso_50_min} and the max values is {iso_50_max}")
    print(f"For 40% of MVC ({iso_40_perc}) the min values is {iso_40_min} and the max values is {iso_40_max}")
    print(f"For 30% of MVC ({iso_30_perc}) the min values is {iso_30_min} and the max values is {iso_30_max}")
    print(f"For 90% of MVC ({iso_20_perc}) the min values is {iso_20_min} and the max values is {iso_20_max}")
    print(f"For 15% of MVC ({iso_15_perc}) the min values is {iso_15_min} and the max values is {iso_15_max}")
    print(f"For 10% of MVC ({iso_10_perc}) the min values is {iso_10_min} and the max values is {iso_10_max}")
    print(f"For 5% of MVC ({iso_5_perc}) the min values is {iso_5_min} and the max values is {iso_5_max}")
    print(f"For 2.5% of MVC ({iso_2_half_perc}) the min values is {iso_2_half_min} and the max values is {iso_2_half_max}")

def signal_from_min_to_max(signal,max):
    signal = np.array(signal)
    signal = signal * max / 100
    return signal

def add_generated_signal(kinvent_path, generated_signal_path, max_force):
    df_kinvent = pd.read_csv(kinvent_path, skiprows=2)

    generated_signal = read_my_txt_file(generated_signal_path)
    generated_signal = signal_from_min_to_max(generated_signal,max_force)



    generated_signal = generated_signal[155:845]
    for i in range(len(generated_signal)):
        if generated_signal[i] == 24.3:
            generated_signal[i] = 23.3
    df_kinvent_no_zeros, index = isolate_Target(df_kinvent)
    # Probably you should erase this after correcting the game with kinvent
    df_kinvent

    print(df_kinvent_no_zeros)
    print(len(df_kinvent_no_zeros['Target']))
    print(len(generated_signal))
    df_kinvent_no_zeros['Signal'] = generated_signal
    # df_kinvent_no_zeros['Signal'] = generated_signal[2:-3]
    # df_kinvent_no_zeros['Signal'] = generated_signal[1:]

    return df_kinvent_no_zeros


