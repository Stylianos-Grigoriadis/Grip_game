import pandas as pd
from fathon import fathonUtils as fu
import fathon
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import Lib_grip as lb

for i in range(1,19):
    try:
        directory = rf'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Strength data\Old.{i}'
        os.chdir(directory)

        Isometric_80_T1 = pd.read_csv(r'Isometric_80_T1.csv', skiprows=2)
        Isometric_80_T2 = pd.read_csv(r'Isometric_80_T2.csv', skiprows=2)
        Isometric_60_T1 = pd.read_csv(r'Isometric_60_T1.csv', skiprows=2)
        Isometric_60_T2 = pd.read_csv(r'Isometric_60_T2.csv', skiprows=2)
        Isometric_40_T1 = pd.read_csv(r'Isometric_40_T1.csv', skiprows=2)
        Isometric_40_T2 = pd.read_csv(r'Isometric_40_T2.csv', skiprows=2)
        Isometric_20_T1 = pd.read_csv(r'Isometric_20_T1.csv', skiprows=2)
        Isometric_20_T2 = pd.read_csv(r'Isometric_20_T2.csv', skiprows=2)
        Isometric_5_T1 = pd.read_csv(r'Isometric_05_T1.csv', skiprows=2)
        Isometric_5_T2 = pd.read_csv(r'Isometric_05_T2.csv', skiprows=2)

        # print(rf'Old {i}')
        # print(rf"Isometric_80_T1: {len(Isometric_80_T1['Performance'])}")
        # print(rf"Isometric_80_T2: {len(Isometric_80_T2['Performance'])}")
        # print(rf"Isometric_60_T1: {len(Isometric_60_T1['Performance'])}")
        # print(rf"Isometric_60_T2: {len(Isometric_60_T2['Performance'])}")
        # print(rf"Isometric_40_T1: {len(Isometric_40_T1['Performance'])}")
        # print(rf"Isometric_40_T2: {len(Isometric_40_T2['Performance'])}")
        # print(rf"Isometric_20_T1: {len(Isometric_20_T1['Performance'])}")
        # print(rf"Isometric_20_T2: {len(Isometric_20_T2['Performance'])}")
        # print(rf"Isometric_5_T1: {len(Isometric_5_T1['Performance'])}")
        # print(rf"Isometric_5_T2: {len(Isometric_5_T2['Performance'])}")


        selected_indices = {}


        def on_select(min_idx, max_idx, label):
            selected_indices[label] = [int(min_idx), int(max_idx)]
            print(selected_indices[label][1] - selected_indices[label][0])


        fig, axs = plt.subplots(1, 2, figsize=(15, 4))

        axs[0].plot(Isometric_80_T1_75Hz['Performance'], label='Force')
        axs[0].set_title('Isometric_80_T1')
        axs[0].axhline(y=perc_80, color='r', linestyle='--', label='Target')
        axs[0].legend()

        axs[1].plot(Isometric_80_T2_75Hz['Performance'], label='Force')
        axs[1].set_title('Isometric_80_T2')
        axs[1].axhline(y=perc_80, color='r', linestyle='--', label='Target')
        axs[1].legend()

        span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1_iso_80_75Hz'),
                             'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'),
                             interactive=True, drag_from_anywhere=True)
        span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2_iso_80_75Hz'),
                             'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'),
                             interactive=True, drag_from_anywhere=True)

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

        span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1_iso_60_75Hz'),
                             'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'),
                             interactive=True, drag_from_anywhere=True)
        span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2_iso_60_75Hz'),
                             'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'),
                             interactive=True, drag_from_anywhere=True)

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

        span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1_iso_40_75Hz'),
                             'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'),
                             interactive=True, drag_from_anywhere=True)
        span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2_iso_40_75Hz'),
                             'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'),
                             interactive=True, drag_from_anywhere=True)

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

        span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1_iso_20_75Hz'),
                             'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'),
                             interactive=True, drag_from_anywhere=True)
        span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2_iso_20_75Hz'),
                             'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'),
                             interactive=True, drag_from_anywhere=True)

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

        span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1_iso_05_75Hz'),
                             'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'),
                             interactive=True, drag_from_anywhere=True)
        span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2_iso_05_75Hz'),
                             'horizontal', minspan=5, useblit=True, props=dict(alpha=0.5, facecolor='red'),
                             interactive=True, drag_from_anywhere=True)

        plt.show()

        df_index = pd.DataFrame(selected_indices)
        columns = df_index.columns.tolist()

        for i in df_index.columns.tolist():
            if df_index[i][1] - df_index[i][0] >= 500:
                print(f'The indices are enough for {i} (indices = {df_index[i][1] - df_index[i][0]})')
            else:
                raise ValueError(f'At the {i} the indices are not enough (indices = {df_index[i][1] - df_index[i][0]})')

        df_index.to_excel('index.xlsx')



    except:
        pass
    # directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game Paper 1\Pilot Study 10\Data\Strength data\Old.8'
# signal = pd.read_csv(directory+r'\grip_strength_Mpoura_Vasiliki__05Dec24_10_31_34.csv', skiprows=2)
# print(signal)
# signal_target = signal['Target'].dropna().loc[signal['Target'] != ''].tolist()
# print(signal_target)
# fig, ax1 = plt.subplots()
#
# ax1.plot(signal['Performance'], label='big_tablet', c='orange')
# ax2 = ax1.twiny()
# ax2.plot(signal_target, label='big_tablet_target', c='red')
# plt.show()

# directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip  game Paper 1\Pilot Study 10\Data\Strength data\Old.3'
# # os.chdir(directory)
# files = glob.glob(os.path.join(directory, "*"))
# print(files)
# for file in files:
#     big_tablet = pd.read_csv(file, skiprows=2)
#     big_tablet_target = big_tablet['Target'].dropna().loc[big_tablet['Target'] != ''].tolist()
#     max = 22.8
#     print(f'5% = {0.05*max}')
#     print(f'20% = {0.2*max}')
#     print(f'40% = {0.4*max}')
#     print(f'60% = {0.6*max}')
#     print(f'80% = {0.8*max}')
#     print(os.path.basename(file))
#
#     fig, ax1 = plt.subplots()
#     plt.title(big_tablet_target[0])
#     ax1.plot(big_tablet['Performance'], label='big_tablet', c='orange')
#
#     ax2 = ax1.twiny()
#     ax2.plot(big_tablet_target, label='big_tablet_target', c='red')
#
#     plt.show()



# fig, ax1 = plt.subplots()
#
# ax1.plot(big_tablet['Performance'], label='big_tablet', c='orange')
# ax1.plot(small_tablet['Performance'], label='small_tablet', c='lightblue')
# ax1.plot(koutlinaos_tablet['Performance'], label='koutlianos_tablet', c='black')
#
#
# ax2 = ax1.twiny()
#
# ax2.plot(big_tablet_target, label='big_tablet_target', c='red')
# ax2.plot(small_tablet_target, label='small_tablet_target', c='blue')
# ax2.plot(koutlinaos_tablet_target, label='koutlinaos_tablet_target', c='gray')
#
#
# plt.show()

