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
import seaborn as sns

plt.rcParams['font.family'] = 'serif'
# plt.rcParams['font.size'] = 16

directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\Education\Classes\BMKI 9000 GRANT WRITING FOR THE BIOMEDICAL SCIENCES\Final Assignament\Proposal\Figures'
os.chdir(directory)
results = pd.read_excel(r'Results Perturbation 2sd 37values after change the sd calculation.xlsx')
data = [
    results['Adaptation down Old'].to_list(),  # Older Adults Downward
    results['Adaptation down Young'].to_list(),  # Older Adults Upward
    results['Adaptation up Old'].to_list(),  # Young Adults Downward
    results['Adaptation up Young'].to_list(),  # Young Adults Upward
]
box = plt.boxplot(data, patch_artist=True, labels=[
    "Old Downward",
    "Young Downward",
    "Old Upward",
    "Young Upward",
])

colors = ["skyblue", "blue", "lightcoral", "red"]

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for median in box['medians']:
    median.set_visible(False)  # Make the median line invisible
plt.xticks(rotation=30, fontsize=16)
plt.title("Adaptation time between Young and Older adults", fontsize=16)
plt.ylabel("Time of adaptation (sec)", fontsize=16)
plt.ylim(0, 10)
# plt.grid(axis='y', linestyle='--', alpha=0.6)  # Optional: Add gridlines for better readability

# Show the plot
plt.tight_layout()
plt.show()





