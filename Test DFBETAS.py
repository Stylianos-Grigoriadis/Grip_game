import pandas as pd
from fathon import fathonUtils as fu
import fathon
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import Lib_grip as lb
from scipy.stats import t
import math

def calculate_DFBETAS(log_n, log_F, cutoff):
    """
    Calculate DFBETAS for each box size.
    """
    m = len(log_n)
    slopes = np.zeros(m)
    std_devs = np.zeros(m)

    # Calculate the slope and standard deviation for each subset
    for i in range(m):
        indices = np.delete(np.arange(m), i)  # Exclude the i-th point
        slope, intercept = np.polyfit(log_n[indices], log_F[indices], 1)
        slopes[i] = slope

        residuals = log_F[indices] - (slope * log_n[indices] + intercept)
        std_dev = np.sqrt(np.sum(residuals ** 2) / (len(indices) - 2))
        std_devs[i] = std_dev / np.sqrt(np.sum((log_n[indices] - np.mean(log_n[indices])) ** 2))

    # Calculate DFBETAS
    full_slope, _ = np.polyfit(log_n, log_F, 1)
    dfbetas = (full_slope - slopes) / std_devs

    return dfbetas


def identify_stable_box_sizes(log_n, log_F, alpha=0.05):
    """
    Identify stable box sizes based on DFBETAS.
    """
    m = len(log_n)
    cutoff = t.ppf(1 - alpha / 2, df=m - 2) / np.sqrt(m)  # Cutoff for DFBETAS
    stable_indices = np.arange(m)

    while True:
        dfbetas = calculate_DFBETAS(log_n[stable_indices], log_F[stable_indices], cutoff)
        if max(np.abs(dfbetas[0]), np.abs(dfbetas[-1])) > cutoff:
            if np.abs(dfbetas[0]) > cutoff:
                stable_indices = stable_indices[1:]  # Remove smallest box size
            if np.abs(dfbetas[-1]) > cutoff:
                stable_indices = stable_indices[:-1]  # Remove largest box size
        else:
            break

    return stable_indices









def DFBETAS3(variable, initial_window_size, s):
    start = initial_window_size[0]
    end = initial_window_size[1]
    winSizes = fu.linRangeByStep(start=start, end=end)
    α_exponent_initial = DFA_for_DFBETAS(variable, winSizes)[0]

    t_value = t.ppf(0.95, df=len(winSizes) - 2)  # Two-tailed critical value at 95% confidence
    sqrt_m = math.sqrt(len(winSizes))
    C = t_value / sqrt_m

    right_DFBETA = True
    i = 0
    removing_first_window_DFBETAS_list = []
    removing_final_window_DFBETAS_list = []
    std_removing_first_window_list = []
    std_removing_final_window_list = []
    while right_DFBETA:
        print(rf'start = {start}')
        print(rf'end = {end}')

        winSizes = fu.linRangeByStep(start=start, end=end)



        removing_first_window_α_exponent = DFA_for_DFBETAS(variable, winSizes[1:])
        log_n = np.log(winSizes[1:])
        slope = removing_first_window_α_exponent[0]
        intercept = removing_first_window_α_exponent[1]
        log_F = np.log(removing_first_window_α_exponent[2])
        std_removing_first_window = calculate_std_slope(log_n, log_F, slope, intercept)
        removing_first_window_DFBETAS = abs(
            (α_exponent_initial - slope) / std_removing_first_window)
        removing_first_window_DFBETAS_list.append(removing_first_window_DFBETAS)
        std_removing_first_window_list.append(std_removing_first_window)



        removing_final_window_α_exponent = DFA_for_DFBETAS(variable, winSizes[:-1])
        log_n = np.log(winSizes[:-1])
        slope = removing_final_window_α_exponent[0]
        intercept = removing_final_window_α_exponent[1]
        log_F = np.log(removing_final_window_α_exponent[2])
        std_removing_final_window = calculate_std_slope(log_n, log_F, slope, intercept)
        removing_final_window_DFBETAS = abs(
            (α_exponent_initial - slope) / std_removing_final_window)
        removing_final_window_DFBETAS_list.append(removing_final_window_DFBETAS)
        std_removing_final_window_list.append(std_removing_final_window)




        if (removing_first_window_DFBETAS > C) and (removing_final_window_DFBETAS > C):
            start += 1
            end -= 1
            print('both')
        elif removing_first_window_DFBETAS > C:
            start +=1
            print('start')
        elif removing_final_window_DFBETAS > C:
            end -=1
            print('end')
        else:
            right_DFBETA = False
        i +=1
        print(rf'DFBETAS without start = {removing_first_window_DFBETAS}')
        print(rf'DFBETAS without end = {removing_final_window_DFBETAS}')
        print(rf'i = {i}')

    plt.plot(std_removing_first_window_list, label='std_removing_first_window_list')
    plt.plot(std_removing_final_window_list, label='std_removing_final_window_list')
    plt.legend()
    plt.show()


    plt.axhline(y=C, label='C_list')
    plt.plot(removing_first_window_DFBETAS_list, label='removing_first_window_DFBETAS_list')
    plt.plot(removing_final_window_DFBETAS_list, label='removing_final_window_DFBETAS_list')
    plt.legend()
    plt.show()
    return start, end



def DFBETAS2(variable, initial_window_size, s):
    start = initial_window_size[0]
    end = initial_window_size[1]
    winSizes = fu.linRangeByStep(start=start, end=end)
    α_exponent_initial = DFA_for_DFBETAS(variable, winSizes)
    α = α_exponent_initial[0]
    number_of_boxes = len(winSizes)
    t_value = t.ppf(0.975, df=number_of_boxes - 2)  # Two-tailed critical value at 95% confidence
    sqrt_m = math.sqrt(number_of_boxes)
    C = t_value / sqrt_m
    DFBETAS = calculatation_of_DFBETAS(variable, winSizes, α)
    i = 0

    while DFBETAS[0] > C or DFBETAS[-1] > C or not np.all(DFBETAS < C):
        i += 1
        print(i)

        if DFBETAS[0] > C:
            print('DFBETAS[0] > C')
            start = start + 1
            plt.plot(winSizes, DFBETAS, label=f'DFBETAS {s} ')
            plt.axhline(y=C, label=f'Cut off value {s}', c='red')
            plt.title(rf'DFBETAS[0] > C')
            plt.legend()
            plt.show()

        elif DFBETAS[-1] > C:
            print('DFBETAS[-1] > C')
            end = end - 1
            plt.plot(winSizes, DFBETAS, label=f'DFBETAS {s} ')
            plt.axhline(y=C, label=f'Cut off value {s}', c='red')
            plt.title(rf'DFBETAS[-1] > C')
            plt.legend()
            plt.show()

        elif DFBETAS[0] > C and DFBETAS[-1] > C:
            print('DFBETAS[0] > C and DFBETAS[-1] > C')
            start = start + 1
            end = end - 1
        elif not np.all(DFBETAS < C):
            print('not np.all(DFBETAS < C)')
            number_of_windows_to_keep = []
            for i in range(len(winSizes)):
                if DFBETAS[i] < C:
                    number_of_windows_to_keep.append(winSizes[i])
                else:
                    number_of_windows_to_keep = []
            start = number_of_windows_to_keep[0]
            end = number_of_windows_to_keep[-1]
            plt.plot(winSizes, DFBETAS, label=f'DFBETAS {s} ')
            plt.axhline(y=C, label=f'Cut off value {s}', c='red')
            plt.title(rf'DFBETAS[-1] > C')
            plt.legend()
            plt.show()

        winSizes = fu.linRangeByStep(start=start, end=end)
        α_exponent_initial = DFA_for_DFBETAS(variable, winSizes)
        α = α_exponent_initial[0]
        number_of_boxes = len(winSizes)
        t_value = t.ppf(0.975, df=number_of_boxes - 2)  # Two-tailed critical value at 95% confidence
        sqrt_m = math.sqrt(number_of_boxes)
        C = t_value / sqrt_m
        DFBETAS = calculatation_of_DFBETAS(variable, winSizes, α)
        print(rf'start = {start}, end = {end}')



    plt.plot(winSizes, DFBETAS, label=f'DFBETAS {s} ')
    plt.axhline(y=C, label=f'Cut off value {s}', c='red')
    plt.title(rf'Keep windows from')
    plt.legend()
    return start, end



def DFBETAS(variable, initial_window_size, s):
    winSizes = fu.linRangeByStep(start=initial_window_size[0], end=initial_window_size[1])
    α_exponent_initial = DFA_for_DFBETAS(variable, winSizes)
    α = α_exponent_initial[0]
    DFBETAS = []
    α_list = []
    std_for_each_excluded_window = []

    for i in range(len(winSizes)):
        winSizes_without_i = np.delete(winSizes, i)

        log_n = np.log(winSizes_without_i)
        results_form_DFA_for_DFBETAS = DFA_for_DFBETAS(variable,winSizes_without_i)
        slope = results_form_DFA_for_DFBETAS[0]
        intercept = results_form_DFA_for_DFBETAS[1]
        log_F = np.log(results_form_DFA_for_DFBETAS[2])
        std = calculate_std_slope(log_n, log_F, slope, intercept)

        DFA = DFA_for_DFBETAS(variable,winSizes_without_i)
        α_i = DFA[0]
        α_list.append(α_i)

        std_for_each_excluded_window.append(std)

        DFBETAS.append(abs((α - α_i)/std))
        # DFBETAS.append(abs((round(α, 3) - round(α_i, 3)) / round(std, 3)))



    number_of_boxes = len(winSizes)
    t_value = t.ppf(0.95, df=number_of_boxes - 2)  # Two-tailed critical value at 95% confidence
    sqrt_m = math.sqrt(number_of_boxes)
    C = t_value / sqrt_m

    number_of_windows_to_keep = []
    for i in range(len(winSizes)):
        if DFBETAS[i] < C:
            number_of_windows_to_keep.append(winSizes[i])
        else:
            number_of_windows_to_keep = []



    plt.plot(winSizes, DFBETAS, label=f'DFBETAS {s} w={number_of_windows_to_keep[0]}')
    plt.axhline(y=C, label=f'Cut off value {s}', c='red')
    plt.title(rf'Keep windows from {number_of_windows_to_keep[0]} until {number_of_windows_to_keep[-1]}')
    plt.legend()
    print(number_of_windows_to_keep)
    print(C)

def calculatation_of_DFBETAS(variable, winSizes, α):
    α_list = []
    std_for_each_excluded_window = []
    DFBETAS = []
    for i in range(len(winSizes)):
        winSizes_without_i = np.delete(winSizes, i)

        log_n = np.log(winSizes_without_i)
        results_form_DFA_for_DFBETAS = DFA_for_DFBETAS(variable,winSizes_without_i)
        slope = results_form_DFA_for_DFBETAS[0]
        intercept = results_form_DFA_for_DFBETAS[1]
        log_F = np.log(results_form_DFA_for_DFBETAS[2])
        std = calculate_std_slope(log_n, log_F, slope, intercept)
        α_i = slope
        α_list.append(α_i)

        std_for_each_excluded_window.append(std)

        DFBETAS.append(abs((α - α_i)/std))
    DFBETAS = np.array(DFBETAS)
    return DFBETAS

def calculate_std_slope(log_n, log_F, slope, intercept):
    # Compute residuals
    residuals = log_F - (slope * log_n + intercept)

    # Variance of residuals
    var_residuals = np.sum(residuals ** 2) / (len(log_n) - 2)

    # Variance of log_n
    var_log_n = np.sum((log_n - np.mean(log_n)) ** 2)

    # Standard deviation of the slope
    std_slope = np.sqrt(var_residuals / var_log_n)
    return std_slope


def DFA_for_DFBETAS(variable, winSizes):
    a = fu.toAggregated(variable)

    pydfa = fathon.DFA(a)

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
    return H, H_intercept, F
def DFBETAS4(variable, number_of_boxes):
    start = number_of_boxes[0]
    end = number_of_boxes[1]
    winSizes = fu.linRangeByStep(start=start, end=end)

    α = lb.DFA_for_DFBETAS(variable, winSizes)[0]


    α_list = []
    betas_list = []
    C_list = []
    std_list = []
    while True:

        # Caluclation of the DFBETAS when the initial value is deleted
        print(start, end)

        winSizes = fu.linRangeByStep(start=start, end=end)

        t_value = t.ppf(0.975, df=len(winSizes) - 2)
        sqrt_m = math.sqrt(len(winSizes))
        C = t_value / sqrt_m
        C_list.append(C)

        removing_first_window_α_exponent = lb.DFA_for_DFBETAS(variable, winSizes[1:])
        log_n = np.log(winSizes[1:])
        slope_first = removing_first_window_α_exponent[0]
        log_F = np.log(removing_first_window_α_exponent[2])
        std_removing_first_window = calculate_std_alpha(log_n, log_F)
        removing_first_window_DFBETAS = abs(
            (α - slope_first) / std_removing_first_window)

        # Caluclation of the DFBETAS when the final value is deleted
        winSizes = fu.linRangeByStep(start=start, end=end)
        removing_final_window_α_exponent = lb.DFA_for_DFBETAS(variable, winSizes[:-1])
        log_n = np.log(winSizes[1:])
        slope_final = removing_final_window_α_exponent[0]
        log_F = np.log(removing_final_window_α_exponent[2])
        std_removing_final_window = calculate_std_alpha(log_n, log_F)
        removing_final_window_DFBETAS = abs(
            (α - slope_final) / std_removing_final_window)
        if max(removing_first_window_DFBETAS, removing_final_window_DFBETAS) > C:
            if removing_first_window_DFBETAS > removing_final_window_DFBETAS:
                start +=1
                α_list.append(slope_first)
                betas_list.append(removing_first_window_DFBETAS)
                std_list.append(std_removing_first_window)

            else:
                end -=1
                α_list.append(slope_final)
                betas_list.append(removing_final_window_DFBETAS)
                std_list.append(std_removing_final_window)

        else:
            break

    return start, end, α_list, betas_list, α, C_list, std_list

def calculate_std_alpha(log_n, log_F):
    """
    Calculate the standard deviation of the slope alpha(i) for DFA.

    Parameters:
    log_n (array): Log-transformed box sizes.
    log_F (array): Log-transformed fluctuation values.

    Returns:
    float: Standard deviation of the slope.
    """
    # Perform linear regression
    slope, intercept = np.polyfit(log_n, log_F, 1)

    # Predicted values and residuals
    predicted = slope * log_n + intercept
    residuals = log_F - predicted

    # Variance of residuals
    residual_variance = np.sum(residuals ** 2) / (len(log_n) - 2)

    # Variance of log_n
    log_n_variance = np.sum((log_n - np.mean(log_n)) ** 2)

    # Standard deviation of the slope
    std_alpha = np.sqrt(residual_variance / log_n_variance)

    return std_alpha


directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Strength data\Young.1'
os.chdir(directory_path)
ID = os.path.basename(directory_path)

Isometric_80_T1_75Hz = pd.read_csv(r'Isometric_80_T1.csv', skiprows=2)

index = pd.read_excel('index.xlsx')

iso_80_T1_75Hz = Isometric_80_T1_75Hz['Performance'][index['T1_iso_80_75Hz'][0]:index['T1_iso_80_75Hz'][1]].to_numpy()

iso_80_T1_75Hz = lb.index_to_500(iso_80_T1_75Hz)

start = 4
end = 250




start, end, α_list, betas_list, α, C_list, std_list = DFBETAS4(iso_80_T1_75Hz, [start, end])
print(start, end)
print(C_list)
α_list = np.array(α_list)
a_diff = α - α_list

plt.axhline(y=α, label='α', c='red')
plt.plot(C_list[:100], label='C_list', c='black')
plt.plot(std_list[:100], label='std_list', c='green')
plt.plot(a_diff[:100], label='a_diff', c='orange')
plt.plot(α_list[:100], label='α_list', c='blue')
plt.plot(betas_list[:100], label='betas_list', c='gray')
plt.legend()
plt.show()


