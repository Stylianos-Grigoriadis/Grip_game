import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
from scipy.signal import decimate
import lib
from matplotlib.widgets import SpanSelector

directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 10\Data\9.Young'
os.chdir(directory_path)
# Determine the MVC and the different percentages
ID = os.path.basename(directory_path)
excel_for_names = pd.read_excel(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 10\Participants.xlsx')
index = excel_for_names[excel_for_names['ID'] == ID].index[0]
max_MVC = excel_for_names['MVC'][index]
perc_05 = 0.05*max_MVC
perc_20 = 0.2*max_MVC
perc_40 = 0.4*max_MVC
perc_60 = 0.6*max_MVC
perc_80 = 0.8*max_MVC

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
    print(selected_indices[label][1]-selected_indices[label][0])


fig, axs = plt.subplots(1, 2, figsize=(15, 4))

axs[0].plot(Isometric_80_T1_75Hz['Performance'], label='Force')
axs[0].set_title('Isometric_80_T1')
axs[0].axhline(y=perc_80, color='r', linestyle='--', label='Target')
axs[0].legend()

axs[1].plot(Isometric_80_T2_75Hz['Performance'], label='Force')
axs[1].set_title('Isometric_80_T2')
axs[1].axhline(y=perc_80, color='r', linestyle='--', label='Target')
axs[1].legend()


span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1_iso_80_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)
span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2_iso_80_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)

plt.show()

fig, axs = plt.subplots(1, 2, figsize=(15, 5))

axs[0].plot(Isometric_60_T1_75Hz['Performance'], label='Force')
axs[0].set_title('Isometric_60_T1')
axs[0].axhline(y=perc_60, color='r', linestyle='--', label='Target')
axs[0].legend()

axs[1].plot(Isometric_60_T2_75Hz['Performance'], label='Force')
axs[1].set_title('Isometric_60_T2')
axs[1].axhline(y=perc_60, color='r', linestyle='--', label='Target')
axs[1].legend()


span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1_iso_60_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)
span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2_iso_60_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)

plt.show()

fig, axs = plt.subplots(1, 2, figsize=(15, 5))

axs[0].plot(Isometric_40_T1_75Hz['Performance'], label='Force')
axs[0].set_title('Isometric_40_T1')
axs[0].axhline(y=perc_40, color='r', linestyle='--', label='Target')
axs[0].legend()

axs[1].plot(Isometric_40_T2_75Hz['Performance'], label='Force')
axs[1].set_title('Isometric_40_T2')
axs[1].axhline(y=perc_40, color='r', linestyle='--', label='Target')
axs[1].legend()

span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1_iso_40_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)
span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2_iso_40_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)

plt.show()

fig, axs = plt.subplots(1, 2, figsize=(15, 5))

axs[0].plot(Isometric_20_T1_75Hz['Performance'], label='Force')
axs[0].set_title('Isometric_20_T1')
axs[0].axhline(y=perc_20, color='r', linestyle='--', label='Target')
axs[0].legend()

axs[1].plot(Isometric_20_T2_75Hz['Performance'], label='Force')
axs[1].set_title('Isometric_20_T2')
axs[1].axhline(y=perc_20, color='r', linestyle='--', label='Target')
axs[1].legend()

span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1_iso_20_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)
span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2_iso_20_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)

plt.show()

fig, axs = plt.subplots(1, 2, figsize=(15, 5))

axs[0].plot(Isometric_05_T1_75Hz['Performance'], label='Force')
axs[0].set_title('Isometric_5_T1')
axs[0].axhline(y=perc_05, color='r', linestyle='--', label='Target')
axs[0].legend()

axs[1].plot(Isometric_05_T2_75Hz['Performance'])
axs[1].set_title('Isometric_5_T2')
axs[1].axhline(y=perc_05, color='r', linestyle='--', label='Target')
axs[1].legend()

span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1_iso_05_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)
span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2_iso_05_75Hz'), 'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'), interactive=True, drag_from_anywhere=True)

plt.show()


df_index = pd.DataFrame(selected_indices)
columns = df_index.columns.tolist()

for i in df_index.columns.tolist():
    if df_index[i][1] - df_index[i][0] >= 500:
        print(f'The indices are enough for {i} (indices = {df_index[i][1] - df_index[i][0]})')
    else:
        raise ValueError(f'At the {i} the indices are not enough (indices = {df_index[i][1] - df_index[i][0]})')

df_index.to_excel('index.xlsx')



