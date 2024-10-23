import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
from scipy.signal import decimate
import lib
from matplotlib.widgets import SpanSelector

directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\4. Christos Chalitsios'
os.chdir(directory_path)

Isometric_80_T1_1000Hz = pd.read_csv(r'Isometric_80_T1.csv', skiprows=2)
Isometric_80_T2_1000Hz = pd.read_csv(r'Isometric_80_T2.csv', skiprows=2)
Isometric_80_T3_1000Hz = pd.read_csv(r'Isometric_80_T3.csv', skiprows=2)
Isometric_60_T1_1000Hz = pd.read_csv(r'Isometric_60_T1.csv', skiprows=2)
Isometric_60_T2_1000Hz = pd.read_csv(r'Isometric_60_T2.csv', skiprows=2)
Isometric_60_T3_1000Hz = pd.read_csv(r'Isometric_60_T3.csv', skiprows=2)
Isometric_40_T1_1000Hz = pd.read_csv(r'Isometric_40_T1.csv', skiprows=2)
Isometric_40_T2_1000Hz = pd.read_csv(r'Isometric_40_T2.csv', skiprows=2)
Isometric_40_T3_1000Hz = pd.read_csv(r'Isometric_40_T3.csv', skiprows=2)
Isometric_20_T1_1000Hz = pd.read_csv(r'Isometric_20_T1.csv', skiprows=2)
Isometric_20_T2_1000Hz = pd.read_csv(r'Isometric_20_T2.csv', skiprows=2)
Isometric_20_T3_1000Hz = pd.read_csv(r'Isometric_20_T2.csv', skiprows=2)
Isometric_05_T1_1000Hz = pd.read_csv(r'Isometric_05_T1.csv', skiprows=2)
Isometric_05_T2_1000Hz = pd.read_csv(r'Isometric_05_T2.csv', skiprows=2)
Isometric_05_T3_1000Hz = pd.read_csv(r'Isometric_05_T3.csv', skiprows=2)
Pert_down = pd.read_csv(r'Pert_down.csv', skiprows=2)
Pert_up = pd.read_csv(r'Pert_up.csv', skiprows=2)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# print(Isometric_5_T3_1000Hz)

Isometric_5_T3_100Hz = lb.down_sampling(Isometric_05_T3_1000Hz,100,1000)

Isometric_80_T1_100Hz = lb.down_sampling(Isometric_80_T1_1000Hz,100,1000)
Isometric_80_T2_100Hz = lb.down_sampling(Isometric_80_T2_1000Hz,100,1000)
Isometric_80_T3_100Hz = lb.down_sampling(Isometric_80_T3_1000Hz,100,1000)
Isometric_60_T1_100Hz = lb.down_sampling(Isometric_60_T1_1000Hz,100,1000)
Isometric_60_T2_100Hz = lb.down_sampling(Isometric_60_T2_1000Hz,100,1000)
Isometric_60_T3_100Hz = lb.down_sampling(Isometric_60_T3_1000Hz,100,1000)
Isometric_40_T1_100Hz = lb.down_sampling(Isometric_40_T1_1000Hz,100,1000)
Isometric_40_T2_100Hz = lb.down_sampling(Isometric_40_T2_1000Hz,100,1000)
Isometric_40_T3_100Hz = lb.down_sampling(Isometric_40_T3_1000Hz,100,1000)
Isometric_20_T1_100Hz = lb.down_sampling(Isometric_20_T1_1000Hz,100,1000)
Isometric_20_T2_100Hz = lb.down_sampling(Isometric_20_T2_1000Hz,100,1000)
Isometric_20_T3_100Hz = lb.down_sampling(Isometric_20_T3_1000Hz,100,1000)
Isometric_05_T1_100Hz = lb.down_sampling(Isometric_05_T1_1000Hz,100,1000)
Isometric_05_T2_100Hz = lb.down_sampling(Isometric_05_T2_1000Hz,100,1000)
Isometric_05_T3_100Hz = lb.down_sampling(Isometric_05_T3_1000Hz,100,1000)


def onselect(xmin, xmax):
    # Calculate the midpoint of the selected range
    mid = (xmin + xmax) / 2
    # Recalculate xmin and xmax to lock the span at 500 points
    xmin_fixed = mid - 250
    xmax_fixed = mid + 250
    for ax in axs:
        ax.axvspan(xmin_fixed, xmax_fixed, color='yellow', alpha=0.3)  # Highlight the selected span
    plt.draw()
#
# fig, axs = plt.subplots(1, 3, figsize=(15, 5))
#
# axs[0].plot(Isometric_80_T1_100Hz['Performance'])
# axs[0].set_title('Isometric_80_T1')
#
# axs[1].plot(Isometric_80_T2_100Hz['Performance'])
# axs[1].set_title('Isometric_80_T2')
#
# axs[2].plot(Isometric_80_T3_100Hz['Performance'])
# axs[2].set_title('Isometric_80_T3')
# plt.show()
#
# fig, axs = plt.subplots(1, 3, figsize=(15, 5))
#
# axs[0].plot(Isometric_60_T1_100Hz['Performance'])
# axs[0].set_title('Isometric_60_T1')
#
# axs[1].plot(Isometric_60_T2_100Hz['Performance'])
# axs[1].set_title('Isometric_60_T2')
#
# axs[2].plot(Isometric_60_T2_100Hz['Performance'])
# axs[2].set_title('Isometric_60_T3')
# plt.show()
#
# fig, axs = plt.subplots(1, 3, figsize=(15, 5))
#
# axs[0].plot(Isometric_40_T1_100Hz['Performance'])
# axs[0].set_title('Isometric_40_T1')
#
# axs[1].plot(Isometric_40_T2_100Hz['Performance'])
# axs[1].set_title('Isometric_40_T2')
#
# axs[2].plot(Isometric_40_T3_100Hz['Performance'])
# axs[2].set_title('Isometric_40_T3')
# plt.show()
#
# fig, axs = plt.subplots(1, 3, figsize=(15, 5))
#
# axs[0].plot(Isometric_20_T1_100Hz['Performance'])
# axs[0].set_title('Isometric_20_T1')
#
# axs[1].plot(Isometric_20_T2_100Hz['Performance'])
# axs[1].set_title('Isometric_20_T2')
#
# axs[2].plot(Isometric_20_T3_100Hz['Performance'])
# axs[2].set_title('Isometric_20_T3')
#
# plt.show()

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].plot(Isometric_05_T1_100Hz['Performance'])
axs[0].set_title('Isometric_5_T1')

axs[1].plot(Isometric_05_T2_100Hz['Performance'])
axs[1].set_title('Isometric_5_T2')

axs[2].plot(Isometric_05_T3_100Hz['Performance'])
axs[2].set_title('Isometric_5_T3')
plt.show()

span_selector_1 = SpanSelector(axs[0], onselect, 'horizontal', useblit=True, interactive=True, minspan=500)
span_selector_2 = SpanSelector(axs[1], onselect, 'horizontal', useblit=True, interactive=True, minspan=500)
span_selector_3 = SpanSelector(axs[2], onselect, 'horizontal', useblit=True, interactive=True, minspan=500)
