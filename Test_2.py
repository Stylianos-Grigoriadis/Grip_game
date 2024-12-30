import os
import numpy as np
from fathon import fathonUtils as fu
import fathon
import matplotlib.pyplot as plt
from scipy.stats import linregress
import pandas as pd
import colorednoise as cn
import random
from scipy.optimize import curve_fit
from scipy.signal import decimate
import Lib_grip as lb
from scipy.stats import t


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


# Example usage:
log_n = np.log(np.array([4, 8, 16, 32, 64, 128, 256]))  # Example box sizes
log_F = np.log(np.random.rand(len(log_n)))  # Example fluctuation values

stable_indices = identify_stable_box_sizes(log_n, log_F)
stable_log_n = log_n[stable_indices]
print("Stable box sizes (log-scale):", stable_log_n)
