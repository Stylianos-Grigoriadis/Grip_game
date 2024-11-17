import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
from scipy.signal import decimate
import lib
from matplotlib.widgets import SpanSelector

directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 10\Data\3.Young'
os.chdir(directory_path)

Isometric_80_T1_75Hz = pd.read_csv(r'Isometric_80_T1.csv', skiprows=2)
Isometric_80_T2_75Hz = pd.read_csv(r'Isometric_80_T2.csv', skiprows=2)
Isometric_60_T1_75Hz = pd.read_csv(r'Isometric_60_T1.csv', skiprows=2)
Isometric_60_T2_75Hz = pd.read_csv(r'Isometric_60_T2.csv', skiprows=2)
Isometric_40_T1_75Hz = pd.read_csv(r'Isometric_40_T1.csv', skiprows=2)
Isometric_40_T2_75Hz = pd.read_csv(r'Isometric_40_T2.csv', skiprows=2)
Isometric_20_T1_75Hz = pd.read_csv(r'Isometric_20_T1.csv', skiprows=2)
Isometric_20_T2_75Hz = pd.read_csv(r'Isometric_20_T2.csv', skiprows=2)
Isometric_05_T1_75Hz = pd.read_csv(r'Isometric_05_T1.csv', skiprows=2)
Isometric_05_T2_75Hz = pd.read_csv(r'Isometric_05_T2.csv', skiprows=2)




# THE FOLLOWING PART KEEPS ONLY THE WANTED INDEX FROM EACH ISOMETRIC TRIAL
selected_indices = {}
def on_select(min_idx, max_idx, label):
    selected_indices[label] = [int(min_idx), int(max_idx)]


fig, axs = plt.subplots(1, 2, figsize=(15, 5))

axs[0].plot(Isometric_80_T1_75Hz['Performance'])
axs[0].set_title('Isometric_80_T1')

axs[1].plot(Isometric_80_T2_75Hz['Performance'])
axs[1].set_title('Isometric_80_T2')

span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1_iso_80_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)
span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2_iso_80_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)

plt.show()

fig, axs = plt.subplots(1, 2, figsize=(15, 5))

axs[0].plot(Isometric_60_T1_75Hz['Performance'])
axs[0].set_title('Isometric_60_T1')

axs[1].plot(Isometric_60_T2_75Hz['Performance'])
axs[1].set_title('Isometric_60_T2')

span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1_iso_60_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)
span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2_iso_60_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)

plt.show()

fig, axs = plt.subplots(1, 2, figsize=(15, 5))

axs[0].plot(Isometric_40_T1_75Hz['Performance'])
axs[0].set_title('Isometric_40_T1')

axs[1].plot(Isometric_40_T2_75Hz['Performance'])
axs[1].set_title('Isometric_40_T2')

span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1_iso_40_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)
span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2_iso_40_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)

plt.show()

fig, axs = plt.subplots(1, 2, figsize=(15, 5))

axs[0].plot(Isometric_20_T1_75Hz['Performance'])
axs[0].set_title('Isometric_20_T1')

axs[1].plot(Isometric_20_T2_75Hz['Performance'])
axs[1].set_title('Isometric_20_T2')

span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1_iso_20_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)
span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2_iso_20_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)

plt.show()

fig, axs = plt.subplots(1, 2, figsize=(15, 5))

axs[0].plot(Isometric_05_T1_75Hz['Performance'])
axs[0].set_title('Isometric_5_T1')

axs[1].plot(Isometric_05_T2_75Hz['Performance'])
axs[1].set_title('Isometric_5_T2')

span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1_iso_05_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)
span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2_iso_05_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)

plt.show()


print(selected_indices)
df_index = pd.DataFrame(selected_indices)
df_index.to_excel('index.xlsx')



