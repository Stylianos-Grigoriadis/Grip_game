import numpy as np
import matplotlib.pyplot as plt
import lib
import colorednoise as cn
from fathon import fathonUtils as fu
import fathon

# plt.rcParams.update({'axes.facecolor':'black'})

def fgn_sim(n=1000, H=0.7,mean=0,std=1):
    """Create Fractional Gaussian Noise
     Inputs:
            n: Number of data points of the time series. Default is 1000 data points.
            H: Hurst parameter of the time series. Default is 0.7.
            mean: Average of generated time series
            std: Standard Deviation of generated time series
     Outputs:
            An array of n data points with variability H
    # =============================================================================
                                ------ EXAMPLE ------

          - Create time series of 1000 datapoints to have an H of 0.7
          n = 1000
          H = 0.7
          dat = fgn_sim(n, H)

          - If you would like to plot the timeseries:
          import matplotlib.pyplot as plt
          plt.plot(dat)
          plt.title(f"Fractional Gaussian Noise (H = {H})")
          plt.xlabel("Time")
          plt.ylabel("Value")
          plt.show()
    # =============================================================================
    """



    # Generate Sequence:
    z = np.random.normal(size=2*n)

    zr = z[:n]
    zi = z[n:]
    zic = -zi
    zi[0] = 0
    zr[0] = zr[0] * np.sqrt(2)
    zi[n - 1] = 0
    zr[n - 1] = zr[n - 1] * np.sqrt(2)
    zr = np.concatenate([zr[:n], zr[n - 2::-1]])
    zi = np.concatenate([zi[:n], zic[n - 2::-1]])
    z = zr + 1j * zi
    k = np.arange(n)
    gammak = (np.abs(k - 1) ** (2 * H) - 2 * np.abs(k) ** (2 * H) + np.abs(k + 1) ** (2 * H)) / 2
    ind = np.concatenate([np.arange(n - 1), [n - 1], np.arange(n - 2, 0, -1)])
    gammak = gammak[ind]  # Circular shift of gammak to match n
    gkFGN0 = np.fft.ifft(gammak)
    gksqrt = np.real(gkFGN0)

    if np.all(gksqrt > 0):
        gksqrt = np.sqrt(gksqrt)
        z = z[:len(gksqrt)] * gksqrt
        z = np.fft.ifft(z)
        z = 0.5 * (n - 1) ** (-0.5) * z
        z = np.real(z[:n])
    else:
        gksqrt = np.zeros_like(gksqrt)
        raise ValueError("Re(gk)-vector not positive")

    # Standardize: (z - np.mean(z)) / np.sqrt(np.var(z))

    ans = 100000*std * z + mean
    return ans

def pink_noise_generator2(number_of_sets,targets_per_set,mean,time_per_set,std,H):

    # input values
    # the expon ent: 0=white noite; 1=pink noise;  2=red noise (also "brownian noise")
    # samples = 500  # number of samples to generate (time series extension)
    beta=1
    total_number_targets=number_of_sets*targets_per_set
    found_time_series = False
    signal = cn.powerlaw_psd_gaussian(beta, total_number_targets)
    DFA_a = DFA(signal)
    signal = [i + mean for i in signal]
    signal = [i * std for i in signal]
    mean_post = np.mean(signal)
    signal = [i + (mean - mean_post) for i in signal]
    i = 0

    # the mean value is 70% of 1RM therefore we want our signal to be between 50% and 90% of 1RM
    max = (mean*90)/70
    print("max")
    print(max)
    print("signal max")
    print(np.max(signal))
    print()
    min = (mean*50)/70
    print("min")
    print(min)
    print("signal min")
    print(np.min(signal))

    while not found_time_series:
        signal = cn.powerlaw_psd_gaussian(beta, total_number_targets)
        signal = [i + mean for i in signal]
        signal = [i * std for i in signal]
        mean_post = np.mean(signal)
        signal = [i + (mean - mean_post) for i in signal]
        DFA_a = DFA(signal)
        print(i)
        i += 1
        if DFA_a > (H - 0.02) and DFA_a < (H + 0.02) and np.max(signal)<max and np.min(signal)>min:
            print(f"to ferame {i} akous prodoti")
            found_time_series = True
    total_time = number_of_sets * time_per_set
    step_for_time = total_time / (number_of_sets * targets_per_set)
    Time = np.arange(0, total_time, step_for_time)
    return signal,Time

def DFA(variable):
    a = fu.toAggregated(variable)
        #b = fu.toAggregated(b)

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

def Pink_targets_generator(number_of_sets, targets_per_set, H, mean, std, time_per_set):
    total_number_targets = number_of_sets*targets_per_set
    found_time_series = False
    dat = fgn_sim(total_number_targets,H,mean,std)
    DFA_a = DFA(dat)
    i =0
    while not found_time_series:
        dat = fgn_sim(total_number_targets,H,mean,std)
        DFA_a = DFA(dat)
        i +=1
        # print(DFA_a)
        if DFA_a > (H-0.02) and DFA_a<(H+0.02):
            # print(i)
            # print(DFA_a)
            found_time_series= True
    total_time = number_of_sets * time_per_set
    step_for_time = total_time / (number_of_sets * targets_per_set)
    Time = np.arange(0, total_time, step_for_time)

    return dat, DFA_a, Time

def Rigid_targets_generator (amplitude,number_of_sets,targets_per_set,mean,time_per_set):
    """Generation of rigid signal"""
    total_time = number_of_sets*time_per_set
    step_for_time = total_time / (number_of_sets * targets_per_set)
    Time = np.arange(0,total_time,step_for_time)
    total_number_of_targets = number_of_sets * targets_per_set
    targets = np.arange(0, total_number_of_targets, 1)
    sine_wave = amplitude*np.sin(targets) + mean
    return sine_wave,targets,Time

def Total_force_output(data_series,number_of_sets,time_per_set,targets_per_set):
    total_force_output = 0
    for i in range(len(data_series)):
        total_force_output = total_force_output + data_series[i]
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

def Comparison_of_given_std_and_calculated_std():
    """This function shows the difference of std given to the
    pink signal generator algorithm with the std calculated after"""
    std_calculated = []
    std_given = []
    for i in range(1, 200):
        pink_noise = pink_noise_generator2(number_of_sets=5,targets_per_set=20,time_per_set=100,mean=60,std=i)
        stadev = np.std(pink_noise[0])
        std_calculated.append(stadev)
        std_given.append(i)
    plt.plot(std_given, label="std_given")
    plt.plot(std_calculated, label="std_calculated")
    plt.legend()
    plt.show()


pink_signal = pink_noise_generator2(number_of_sets=5,targets_per_set=20,time_per_set=30,mean=40,std=5,H=1)
rigid_signal = Rigid_targets_generator(amplitude=10, number_of_sets=5, targets_per_set=20, mean=40,time_per_set=30)
# Normalize mean of pink_signal to rigid_signal
# mean_difference = np.mean(rigid_signal[0])-np.mean(pink_signal[0])
# for i in range(len(pink_signal[0])):
#     pink_signal[0][i]+=(mean_difference)

# a = Comparison_of_given_std_and_calculated_std()
total_force_rigid = Total_force_output(rigid_signal[0],number_of_sets=5,time_per_set=30,targets_per_set=20)
total_force_pink = Total_force_output(pink_signal[0],number_of_sets=5,time_per_set=30,targets_per_set=20)
print("total_force_rigid")
print(total_force_rigid)
print("total_force_pink")
print(total_force_pink)
print("Std_rigid")
print(np.std(rigid_signal[0]))
print("Std_pink")
print(np.std(pink_signal[0]))
print("Average_rigid")
print(np.mean(rigid_signal[0]))
print("Average_pink")
print(np.mean(pink_signal[0]))
#
# number_of_sets = 5
# time_per_set = 120
# targets_per_set = 20
# total_time = number_of_sets*time_per_set
# step_for_time = total_time / (number_of_sets * targets_per_set)
# Time = np.arange(0,total_time,step_for_time)
# for i in range(1,number_of_sets+1):
#     plt.axvline(x=i*Time[-1]/number_of_sets,color='blue', label="set" + str(i))
# # plt.style.use('dark_background')
# plt.scatter(pink_noise[2], pink_noise[0],color="red",lw=4)
# plt.plot(rigid_signal[2], rigid_signal[0],color="white", label="Rigid Signal")
# plt.plot(pink_noise[2],pink_noise[0],color="red", label="Pink Signal")
# plt.xlabel("Time (s)")
# plt.ylabel("Amplitude")
# plt.legend(labelcolor='linecolor')
# plt.show()
#
# a = Total_force_output(pink_noise[0],number_of_sets=5,time_per_set=120,targets_per_set=20)
# print(a[1])
# a = Total_force_output(rigid_signal[0],number_of_sets=5,time_per_set=120,targets_per_set=20)
# print(a[1])

# for i in range(0,10):
#     pink_signal = pink_noise_generator2(number_of_sets=5,targets_per_set=20,time_per_set=30,mean=60,std=10,H=1)
#     plt.plot(pink_signal[1],pink_signal[0])
# pink_signal = pink_noise_generator2(number_of_sets=5,targets_per_set=20,time_per_set=30,mean=60,std=5,H=1)
plt.plot(pink_signal[1],pink_signal[0])
plt.show()
# a = Comparison_of_given_std_and_calculated_std()

def DFA_check_for_windows(variable, start_win, end_win):
    """Damouras et al. (2010) suggested a way to calculate the appropriate range of boxes for DFA
        This requires the calculation of DFBETAS which is:
        DFBETAS = (α - α(i))/std(α(i))
        where   α           : The α exponent when using a range of boxes
                α(i)        : The α exponent when using the same range of boxes but excluding the ith box
                std(α(i))   : The standard deviation of the fluctuation of each box to the regression model’s slope
        DFBETAS is the standardized difference in the scaling exponent before and after removing the ith box size. Under standard linear regression assumptions,
        the DFBETAS are distributed as t(m-2)/sqrt(m), wheret (m-2) is the t-distribution with m-2 degrees of freedom and m is the number of box sizes. Even though
        the regression assumptions are not strictly applicable to DFA (e.g. mean fluctuations are not independent), we still use the result as an approximation.
        We identify box sizes leading to significant changes in a by checking whether or not their absolute DFBETAS are above a specific cutoff value C.
        We set the cutoff value to
        C = t(975)(m-2)/sqrt(m), at the usual 5% significance level

        Input Values
        variable    : the data series you need to find the boxes for
        start_win   : the window from which the algorithm will start
        end_win     : the window at which the algorithm will stop

        Output Values
        """
    α_exponents = []
    index = []
    residuals_all = []
    for i in range(start_win - 1, end_win + 1):
        print("start_win")
        print(start_win - 1)
        print("end_win")
        print(end_win + 1)
        a = fu.toAggregated(variable)
        pydfa = fathon.DFA(a)

        """Compute the box range"""
        winSizes = []
        for j in range(start_win, end_win + 1):
            if not i == j:
                winSizes.append(j)
        winSizes = np.array(winSizes, dtype=np.int64)


        """Calculate α exponent"""
        revSeg = True
        polOrd = 1

        n, F = pydfa.computeFlucVec(winSizes, revSeg=revSeg, polOrd=polOrd)
        H, H_intercept = pydfa.fitFlucVec()

        """Calculate the standard deviation of the regression model’s slope"""
        fitted_values = H_intercept + H * np.log(n)
        residuals = np.log(n) - fitted_values
        residual_std = np.std(residuals)

        """Append the values to list """
        α_exponents.append(H)
        index.append(i)
        residuals_all.append(residual_std)

        """Plot DFA"""
        # plt.plot(np.log(n), np.log(F), 'ro')
        # plt.plot(np.log(n), H_intercept + H * np.log(n),  label='H = {:.2f}'.format(H))
        # plt.xlabel('ln(n)', fontsize=14)
        # plt.ylabel('ln(F(n))', fontsize=14)
        # plt.title('DFA without ' + str(i) + "th window", fontsize=14)
        # plt.legend(loc=0, fontsize=14)
        # plt.show()
    DFBETAS = []

    for i in range(1, len(α_exponents)):
        print("i")
        print(i)
        print(abs((α_exponents[0] - α_exponents[i]) / residuals_all[i]))
        DFBETAS.append(abs((α_exponents[0] - α_exponents[i]) / residuals_all[i]))
    plt.plot(range(start_win, end_win + 1), DFBETAS)
    plt.show()

    return α_exponents, index, residuals_all, DFBETAS[1:]

