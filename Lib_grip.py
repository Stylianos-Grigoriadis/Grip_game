import numpy as np
from fathon import fathonUtils as fu
import fathon
import matplotlib.pyplot as plt
from scipy.stats import linregress


def Perc(signal):
    """This function takes a signal as a list and turns is in a 0 to 100% ratio"""

    new_signal = [i for i in signal]
    min = np.min(signal)
    if min >0:
        for i in range(len(new_signal)):
            new_signal[i] = new_signal[i] + min
    else:
        for i in range(len(new_signal)):
            new_signal[i] = new_signal[i] - min

    max = np.max(new_signal)
    for i in range(len(new_signal)):
        new_signal[i] = new_signal[i]* 100/max
    return new_signal

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