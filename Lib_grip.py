import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import colorednoise as cn
import random
from scipy.optimize import curve_fit
from scipy.fft import fft, ifft

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

def index_to_500(array):

    excess_length_array = len(array) - 500
    if excess_length_array > 0:
        remove_each_side = excess_length_array//2
        array = array[remove_each_side : len(array)-remove_each_side]

    elif excess_length_array == 0:
        pass
    else:
        raise ValueError("Length is less than 500 points")

    return array

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
    df_set_1 = pd.read_csv(path, skiprows=2, nrows=index[1] - 3)
    df_set_2 = pd.read_csv(path, skiprows=index[1] + 2, nrows=index[2] - index[1] - 3)
    df_set_3 = pd.read_csv(path, skiprows=index[2] + 2, nrows=index[3] - index[2] - 3)
    df_set_4 = pd.read_csv(path, skiprows=index[3] + 2, nrows=index[4] - index[3] - 3)
    df_set_5 = pd.read_csv(path, skiprows=index[4] + 2, nrows=index[5] - index[4] - 3)
    df_set_6 = pd.read_csv(path, skiprows=index[5] + 2, nrows=index[6] - index[5] - 3)
    df_set_7 = pd.read_csv(path, skiprows=index[6] + 2, nrows=index[7] - index[6] - 3)
    df_set_8 = pd.read_csv(path, skiprows=index[7] + 2, nrows=index[8] - index[7] - 3)
    df_set_9 = pd.read_csv(path, skiprows=index[8] + 2, nrows=index[9] - index[8] - 3)
    df_set_10 = pd.read_csv(path, skiprows=index[9] + 2)

    return (df_set_1,
            df_set_2,
            df_set_3,
            df_set_4,
            df_set_5,
            df_set_6,
            df_set_7,
            df_set_8,
            df_set_9,
            df_set_10)

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

def synchronization_of_Time_and_ClosestSampleTime_Stylianos(df, Targets_N, trial_time):
    """ This function takes a dataframe and converts it so that the Time column and the ClosestSampleTime column
        are matched. This is a method to synchronize the two time stamps
    Parameters
    Input
            df          :   the Dataframe
            Target_N    :   the total number of targets
            trial_time  :   the time of the trial in seconds
    Output
            new_df      :   the new Dataframe

    """
    # Find the index of the first value where the ClosestSampleTime is equal to Time
    df['Time'] = df['Time'].round(3)
    df['ClosestSampleTime'] = df['ClosestSampleTime'].round(3)

    # Find the value of the column Time with the smallest absolute difference with the first value of ClosestSampleTime
    closest_value = df['Time'].iloc[(df['Time'] - df['ClosestSampleTime'][0]).abs().idxmin()]

    # Find the index of the column Time with the smallest absolute difference with the first value of ClosestSampleTime
    index = df.loc[df['Time'] == closest_value].index[0]

    # Create a list of ClosestSampleTime with the initial value being the value of Time with the smallest difference
    # with the first value of ClosestSampleTime. To do so you need the step with which you will have values. To
    # calculate this you need the result of trial_time/Targets_N
    step = trial_time/Targets_N
    initial_value_time = df['Time'][index]
    list_ClosestSampleTime = [initial_value_time]
    for i in range(Targets_N - 1):
        list_ClosestSampleTime.append(round(list_ClosestSampleTime[-1] + step, 3))

    # Create a list of indices of column Time, where the values of list_ClosestSampleTime are equal with the values of
    # column Time
    # UPDATE: this may not work sometime if it does not use the below methodology
    # matching_indices = df.index[df['Time'].isin(list_ClosestSampleTime)].tolist()

    # If the above does not work use this
    matching_indices = [(df['Time'] - value).abs().idxmin() for value in list_ClosestSampleTime]

    # Create the Performance, Time, and Target lists with the values at the right indices of the initial df
    Performance = [df['Performance'].iloc[i] for i in matching_indices]
    Time = [df['Time'].iloc[i] for i in matching_indices]
    Target = df['Target'].head(len(matching_indices)).tolist()

    # Delete any values from the end of the list_ClosestSampleTime so that all lists Performance, Time, Target and list_ClosestSampleTime
    # have the same length
    list_ClosestSampleTime = list_ClosestSampleTime[:len(Time)]

    # create the new_df
    dist = {'Time': Time, 'Performance': Performance, 'ClosestSampleTime': list_ClosestSampleTime, 'Target': Target}
    new_df = pd.DataFrame(dist)

    return new_df

def synchronization_of_Time_and_ClosestSampleTime_Anestis(df):
    """ This function creates a new dataframe by synchronizing the Time column to the ClosestSampleTime column and then returns a new dataframe with the correct values"""

    time_index = []
    for i in range(len(df)):
        # Calculate the difference of the element i of the column ClosestSampleTime with every value of the column Time
        closest_index = (df['Time'] - df['ClosestSampleTime'].iloc[i]).abs()
        # Drop the None values of the closest_index so that in the next step the .empty attribute if it has only None values it would show False
        closest_index = closest_index.dropna()

        if not closest_index.empty:
            # Find the index of the minimum difference
            closest_index = closest_index.idxmin()
            # Keep only the index of minimum difference
            time_index.append(closest_index)
    # Create all other columns
    time = df.loc[time_index, 'Time'].to_numpy()
    performance = df.loc[time_index, 'Performance'].to_numpy()
    targets = df['Target'].dropna().to_numpy()
    time_close_to_target = df['ClosestSampleTime'].dropna().to_numpy()

    # Create the dataframe which will be returned afterward.
    dist = {'Indices': time_index,
            'Time': time,
            'Performance': performance,
            'ClosestSampleTime': time_close_to_target,
            'Target': targets}
    new_df = pd.DataFrame(dist)

    return new_df

def isolate_Target(df):

    new_Time = []
    ClosestSampleTime = df['ClosestSampleTime'].dropna().to_list()
    Performance = []
    Target = []
    index_list = []

    Time = df['Time'].to_list()
    # Time = [round(value, 3) for value in Time]
    df['Time'] = df['Time'].round(3)
    print(df['Time'])

    for i in ClosestSampleTime:
        if i in df['Time'].values:
            index = df.index[df['Time'] == i].tolist()[0]
            print(index)
            Performance.append(df['Performance'][index])
            Target.append(df['Target'][index])
            index_list.append(index)
            new_Time.append(i)
    df_targets = pd.DataFrame({'Time': new_Time, 'Performance': Performance, 'ClosestSampleTime': ClosestSampleTime, 'Target': Target})

    return df_targets

def spatial_error(df):
    """ Calculate the spatial error of the Performance and Target
    Parameters
    Input
            df              :   the Dataframe
    Output
            spatial_error   :   the spatial_error between the Performance and Target
    """

    spatial_error = []
    for i in range(len(df['Time'])):
        spatial_error.append((abs(df['Performance'][i]-df['Target'][i])))
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

def adaptation_time_using_sd(df, perturbation_index, sd_factor, first_values, consecutive_values, values_for_sd, name, plot=False):
    """
    This function returns the time after the perturbation which was needed to adapt to the perturbation
    Parameters
    Input
            df                  :   The Dataframe
            perturbation_index  :   The index where the perturbation occurred
            sd_factor           :   This will be multiplied with the sd of the error before the perturbation
                                    and if the error after the is less than the mean + sd*sd_factor and more than
                                    the mean - sd*sd_factor, the algorithm will consider that the adaptation of the
                                    perturbation occurred
            first_values        :   At first the error will be too much so to calculate the mean and sd before the perturbation
                                    right, we erase some values from the beginning
            consecutive_values  :   This is how many values the algorithm needs to consider so that it decides that the adaptation occurred.
            total targets       :   The total number of targets
            Plot                :   Plot the spatial error and the time of adaptation (default value False)

    Output
            time_of_adaptation  :   The time it took the df['Performance'] to steadily reach df['Target']. This
                                    number corresponds to the first value of time at which for the next X consecutive_values
                                    the spatial error was lower than the average +- (sd * sd_factor)
    """
    # First synchronize the Time and ClosestSampleTime columns and create a new df with
    # only the synchronized values
    df = synchronization_of_Time_and_ClosestSampleTime_Anestis(df)

    # Calculate the spatial error and the average and sd of the spatial error
    # after the first_values
    spatial_er = spatial_error(df)

    # The following 2 lines calculate the mean and sd of the 'first_values' before the perturbation
    # to use for calculating the adaptation time
    mean = np.mean(spatial_er[first_values:perturbation_index])
    sd_before_perturbation = np.std(spatial_er[first_values:perturbation_index])

    # The following line calculate the lowest sd for 'values_for_sd' in overlapping window and
    # the lowest sd is the sd used for further analysis
    list_for_mean_and_sd = spatial_er[perturbation_index:]
    list_of_sd = []
    list_of_means = []
    for i in range(len(list_for_mean_and_sd) - values_for_sd):
        average = np.mean(list_for_mean_and_sd[i:i+values_for_sd])
        sd = np.std(list_for_mean_and_sd[i:i+values_for_sd])
        list_of_means.append(average)
        list_of_sd.append(sd)
    min_sd = min(list_of_sd)
    min_sd_index = list_of_sd.index(min_sd)
    average_at_min_sd = list_of_means[min_sd_index]
    # plt.plot(list_of_sd)
    # plt.show()

    # Create an array with consecutive_values equal number
    consecutive_values_list = np.arange(0,consecutive_values,1)

    # Iterate the spatial error after the perturbation_index to calculate the time of adaptation
    for i in range(len(spatial_er) - consecutive_values+1):
        if i >= perturbation_index:

            if (all(spatial_er[i + j] < average_at_min_sd + min_sd * sd_factor for j in consecutive_values_list) and
                all(spatial_er[i + j] > average_at_min_sd - min_sd * sd_factor for j in consecutive_values_list)
            ):
                time_of_adaptation = df['Time'][i] - df['Time'][perturbation_index]
                break

    if plot == True:
        try:
            time_of_adaptation
            plt.plot(df['Time'], spatial_er, label='Spatial Error')
            plt.axhline(y=average_at_min_sd, c='k', label = 'Average')
            plt.axhline(y=average_at_min_sd + min_sd*sd_factor, c='k', ls=":", label=f'{sd_factor}*std')
            plt.axhline(y=average_at_min_sd - min_sd*sd_factor, c='k', ls=":")
            plt.axvline(x=df['Time'][perturbation_index] + time_of_adaptation, lw=3, c='red', label='Adaptation instance')
            plt.axvline(x=df['Time'][perturbation_index], linestyle='--', c='gray', label='Perturbation instance')

            plt.legend()
            plt.ylabel('Force difference (kg)')
            plt.xlabel('Time (sec)')
            plt.title(f'{name}\ntime for adaptation: {round(time_of_adaptation,3)} sec')
            plt.show()
        except NameError:
            print(f"No adaptation was evident for {name}")

    try:
        time_of_adaptation
        return time_of_adaptation
    except:
        time_of_adaptation = None
        return time_of_adaptation

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
    ''' Where:
                signal: is the signal I want to change
                max:    is the max force I inserted into Kinvent app
                '''
    signal = np.array(signal)
    signal = signal * max / 100
    return signal

def add_generated_signal(kinvent_path, generated_signal_path, max_force):
    df_kinvent = pd.read_csv(kinvent_path, skiprows=2)
    df_kinvent_no_zeros = isolate_Target(df_kinvent)
    length_kinvent = len(df_kinvent_no_zeros['Target'])

    generated_signal = read_my_txt_file(generated_signal_path)
    print(generated_signal)
    generated_signal = signal_from_min_to_max(generated_signal, max_force)

    length_generated_signal = len(generated_signal)
    length_erase = length_generated_signal - length_kinvent

    length_generated_signal_erase = length_erase//2 +1
    length_generated_signal_start = length_generated_signal_erase
    print(f'reminder {length_erase % 2}')
    length_generated_signal_end = length_generated_signal - length_generated_signal_erase + length_erase % 2




    print(rf"length_generated_signal_start: {length_generated_signal_start}")
    print(rf"length_generated_signal_end: {length_generated_signal_end}")

    print(rf"length_kinvent: {length_kinvent}")
    print(rf"length_generated_signal_before: {length_generated_signal}")
    print(rf"length_erase: {length_erase}")

    generated_signal = generated_signal[length_generated_signal_start:length_generated_signal_end]
    print(rf"generated_signal: {len(generated_signal)}")

    df_kinvent_no_zeros['Generated_Signal'] = generated_signal

    return df_kinvent_no_zeros

def down_sampling(df, f_out, f_in):
    """
    Parameters
    In
                df:     the dataframe to be downsampled
                f_out:  the frequency I want
                f_in:   the frequency the df has
    Out
                df_downsampled:     the df with downsampled the 'Time' and 'Performance' columns
                                    while 'ClosestSampleTime' and 'Target' were left intact

    """
    factor = int(f_in/f_out)

    df_downsampled_first_two_cols = df[['Time', 'Performance']].iloc[::factor].reset_index(drop=True)
    df_remaining_cols = df[['ClosestSampleTime', 'Target']]
    df_downsampled = pd.concat([df_downsampled_first_two_cols, df_remaining_cols], axis=1)

    return df_downsampled

def FFT(signal, sampling_frequency):
    # Compute FFT
    fft_values = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(signal), d=1 / sampling_frequency)  # Frequency bins

    # Compute power spectrum (magnitude of FFT)
    power_spectrum = np.abs(fft_values)

    # Plot
    plt.figure(figsize=(8, 4))
    plt.plot(frequencies[:len(frequencies) // 2],
             power_spectrum[:len(frequencies) // 2])
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power")
    plt.title("FFT Spectrum")
    plt.grid()
    plt.show()

def Surr_Theiler(y, algorithm):
    """
    z=Surr_Theiler20200723(y,algorithm)
    inputs  - y, time series to be surrogated
                 algorithm - the type of algorithm to be completed
    outputs - z, surrogated time series
    Remarks
    - This code creates a surrogate time series according to Algorithm 0,
      Algorithm 1 or Algorithm 2.
    Future Work
    - None.
    References
    - Theiler, J., Eubank, S., Longtin, A., Galdrikian, B., & Doyne
      Farmer, J. (1992). Testing for nonlinearity in time series: the
      method of surrogate data. Physica D: Nonlinear Phenomena, 58(1–4),
      77–94. https://doi.org/10.1016/0167-2789(92)90102-S
    Jun 2015 - Modified by Ben Senderling
             - Added function help section and plot commands for user
               feedback
             - The code was originally created as two algorithms. It was
               modified so one code included both functions.
    Jul 2020 - Modified by Ben Senderling, bmchnonan@unomaha.edu
             - Changed file and function name.
             - Added reference.
    """
    if algorithm == 0:
        z = np.random.randn(*np.shape(y))
        idx = np.argsort(z)
        z = y[idx]
    elif algorithm == 1:
        z = surr1(y, algorithm)
    elif algorithm == 2:
        z = surr1(y, algorithm)

    return z

def surr1(x, algorithm):
    """
    z = surr1(x,algorithm)
    Inputs: x, The input to be surrogated.
            algorithm, The selected algorithm to use.
    Output: z, The surrogated time series.
    """

    x = np.array(x, ndmin=2).T.copy()

    r, c = np.shape(x)

    y = np.zeros((r, c))

    if abs(algorithm) == 2:
        ra = np.random.randn(r, c)
        sr = np.sort(ra, axis=0)
        xi = np.argsort(x, axis=0)
        sx = np.sort(x, axis=0)
        xii = np.argsort(xi, axis=0)
        for i in range(c):
            y[:, i] = sr[xii[:, i]].flatten()
    else:
        y = x
    m = np.mean(y)

    y = y - m

    fy = fft(y, axis=0)

    # randomizing phase
    phase = np.random.rand(r, 1)
    # repeat the random values for each column in the input
    if c > 1:
        phase = np.tile(phase, c)

    rot = np.exp(1) ** (2 * np.pi * np.sqrt(-1 + 0j) * phase)

    fyy = np.multiply(fy, rot)

    yy = np.real(ifft(fyy)) + m

    z = np.ones(np.shape(sx))

    if abs(algorithm) == 2:
        yyi = np.argsort(yy, axis=0)
        yyii = np.argsort(yyi, axis=0)
        for k in range(c):
            z[:, k] = sx[yyii[:, k]].flatten()
    else:
        z = yy

    return z




