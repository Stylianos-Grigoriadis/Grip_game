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
import glob

directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Strength data\Old.18'
os.chdir(directory)
files = glob.glob(os.path.join(directory, "*"))
for file in files:
    signal = pd.read_csv(file, skiprows=2)
    plt.plot(signal['Performance'])
    plt.show()
