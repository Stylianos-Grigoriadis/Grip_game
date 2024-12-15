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

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 16


directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip training\Pilot study 1\Signals'
os.chdir(directory)

set = np.arange(0, 651, 65)
midpoints = (set[:-1] + set[1:]) / 2
labels = [f"set {i+1}" for i in range(len(midpoints))]

sine_wave = lb.read_my_txt_file(r'Sine signal N650 freq0.2 Max100.txt')
pink_noise = lb.read_my_txt_file(r'pink_noise_final_650.txt')
plt.plot(sine_wave, label='sine_wave', c='green', lw=10)
plt.plot(pink_noise, label='pink_noise', c='pink', lw=10)
plt.legend()
for i in set:
    plt.axvline(x=i, color='k', linestyle='--', lw=1.5)
plt.title('Signals for both pink noise game and sine wave game')
plt.xticks(midpoints, labels)
plt.ylabel('Percentage of screen height')
plt.tight_layout()
plt.show()

