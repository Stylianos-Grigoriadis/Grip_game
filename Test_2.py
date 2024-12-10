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
directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game Paper 1\Pilot Study 10\Data\Strength data\Old.6'
signal = pd.read_excel(directory+'\Time.xlsx')
closervalues = pd.read_excel(directory+'\closervalues.xlsx')
print(signal['Time'])
print(closervalues['closervalues'])
closervalues = closervalues['closervalues'].to_list()
indices = [(signal['Time'] - value).abs().idxmin() for value in closervalues]
print(indices)
index_list = range(0,500)
fd = pd.DataFrame({'indices': indices,
                   'index_list': index_list,
                   'closervalues': closervalues})
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
print(fd)
plt.plot(indices)
plt.show()

