import lib
import Lib_grip as lb
import numpy as np
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Data collection\Data\Strength data'
files = glob.glob(os.path.join(directory_path, "*"))

ID_list = []
excel_for_names = pd.read_excel(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Data collection\Participants.xlsx')

for file in files:
    directory = file
    os.chdir(directory)
    ID = os.path.basename(file)
    ID_list.append(ID)
    print(ID)

    index = pd.read_excel(fr'index_{ID}.xlsx', index_col=None)

    index_for_excel = excel_for_names[excel_for_names['ID'] == ID].index[0]
    max_MVC = excel_for_names['MVC'][index_for_excel]

    percentage_05 = 0.05 * max_MVC
    percentage_20 = 0.2 * max_MVC
    percentage_40 = 0.4 * max_MVC
    percentage_60 = 0.6 * max_MVC
    percentage_80 = 0.8 * max_MVC

    Isometric_80_T1 = pd.read_csv(r'Isometric_80_T1.csv', skiprows=2)
    Isometric_80_T2 = pd.read_csv(r'Isometric_80_T2.csv', skiprows=2)
    Isometric_60_T1 = pd.read_csv(r'Isometric_60_T1.csv', skiprows=2)
    Isometric_60_T2 = pd.read_csv(r'Isometric_60_T2.csv', skiprows=2)
    Isometric_40_T1 = pd.read_csv(r'Isometric_40_T1.csv', skiprows=2)
    Isometric_40_T2 = pd.read_csv(r'Isometric_40_T2.csv', skiprows=2)
    Isometric_20_T1 = pd.read_csv(r'Isometric_20_T1.csv', skiprows=2)
    Isometric_20_T2 = pd.read_csv(r'Isometric_20_T2.csv', skiprows=2)
    Isometric_05_T1 = pd.read_csv(r'Isometric_05_T1.csv', skiprows=2)
    Isometric_05_T2 = pd.read_csv(r'Isometric_05_T2.csv', skiprows=2)

    Isometric_80_T1 = Isometric_80_T1['Performance'][index['T2_iso_80_75Hz'][0]:index['T2_iso_80_75Hz'][1]].to_numpy()
    Isometric_80_T2 = Isometric_80_T2['Performance'][index['T2_iso_80_75Hz'][0]:index['T2_iso_80_75Hz'][1]].to_numpy()
    Isometric_60_T1 = Isometric_60_T1['Performance'][index['T1_iso_60_75Hz'][0]:index['T1_iso_60_75Hz'][1]].to_numpy()
    Isometric_60_T2 = Isometric_60_T2['Performance'][index['T2_iso_60_75Hz'][0]:index['T2_iso_60_75Hz'][1]].to_numpy()
    Isometric_40_T1 = Isometric_40_T1['Performance'][index['T1_iso_40_75Hz'][0]:index['T1_iso_40_75Hz'][1]].to_numpy()
    Isometric_40_T2 = Isometric_40_T2['Performance'][index['T2_iso_40_75Hz'][0]:index['T2_iso_40_75Hz'][1]].to_numpy()
    Isometric_20_T1 = Isometric_20_T1['Performance'][index['T1_iso_20_75Hz'][0]:index['T1_iso_20_75Hz'][1]].to_numpy()
    Isometric_20_T2 = Isometric_20_T2['Performance'][index['T2_iso_20_75Hz'][0]:index['T2_iso_20_75Hz'][1]].to_numpy()
    Isometric_05_T1 = Isometric_05_T1['Performance'][index['T1_iso_05_75Hz'][0]:index['T1_iso_05_75Hz'][1]].to_numpy()
    Isometric_05_T2 = Isometric_05_T2['Performance'][index['T2_iso_05_75Hz'][0]:index['T2_iso_05_75Hz'][1]].to_numpy()

    Isometric_80_T1 = lb.index_to_500(Isometric_80_T1)
    Isometric_80_T2 = lb.index_to_500(Isometric_80_T2)
    Isometric_60_T1 = lb.index_to_500(Isometric_60_T1)
    Isometric_60_T2 = lb.index_to_500(Isometric_60_T2)
    Isometric_40_T1 = lb.index_to_500(Isometric_40_T1)
    Isometric_40_T2 = lb.index_to_500(Isometric_40_T2)
    Isometric_20_T1 = lb.index_to_500(Isometric_20_T1)
    Isometric_20_T2 = lb.index_to_500(Isometric_20_T2)
    Isometric_05_T1 = lb.index_to_500(Isometric_05_T1)
    Isometric_05_T2 = lb.index_to_500(Isometric_05_T2)

    # Butterworth filtering at 50Hz
    Isometric_80_T1 = lib.Butterworth(75, 50, Isometric_80_T1)
    Isometric_80_T2 = lib.Butterworth(75, 50, Isometric_80_T2)
    Isometric_60_T1 = lib.Butterworth(75, 50, Isometric_60_T1)
    Isometric_60_T2 = lib.Butterworth(75, 50, Isometric_60_T2)
    Isometric_40_T1 = lib.Butterworth(75, 50, Isometric_40_T1)
    Isometric_40_T2 = lib.Butterworth(75, 50, Isometric_40_T2)
    Isometric_20_T1 = lib.Butterworth(75, 50, Isometric_20_T1)
    Isometric_20_T2 = lib.Butterworth(75, 50, Isometric_20_T2)
    Isometric_05_T1 = lib.Butterworth(75, 50, Isometric_05_T1)
    Isometric_05_T2 = lib.Butterworth(75, 50, Isometric_05_T2)

    # Average of spatial error so that we can determine which Isometric trial to use for each percentage
    # for further analysis

    Spatial_error_Isometric_80_T1 = np.mean(np.abs(Isometric_80_T1 - percentage_80))
    Spatial_error_Isometric_80_T2 = np.mean(np.abs(Isometric_80_T2 - percentage_80))
    Spatial_error_Isometric_60_T1 = np.mean(np.abs(Isometric_60_T1 - percentage_60))
    Spatial_error_Isometric_60_T2 = np.mean(np.abs(Isometric_60_T2 - percentage_60))
    Spatial_error_Isometric_40_T1 = np.mean(np.abs(Isometric_40_T1 - percentage_40))
    Spatial_error_Isometric_40_T2 = np.mean(np.abs(Isometric_40_T2 - percentage_40))
    Spatial_error_Isometric_20_T1 = np.mean(np.abs(Isometric_20_T1 - percentage_20))
    Spatial_error_Isometric_20_T2 = np.mean(np.abs(Isometric_20_T2 - percentage_20))
    Spatial_error_Isometric_05_T1 = np.mean(np.abs(Isometric_05_T1 - percentage_05))
    Spatial_error_Isometric_05_T2 = np.mean(np.abs(Isometric_05_T2 - percentage_05))

    if Spatial_error_Isometric_80_T1 >= Spatial_error_Isometric_80_T2:
        Isometric_80 = Isometric_80_T1
    else:
        Isometric_80 = Isometric_80_T2

    if Spatial_error_Isometric_60_T1 >= Spatial_error_Isometric_60_T2:
        Isometric_60 = Isometric_60_T1
    else:
        Isometric_60 = Isometric_60_T2

    if Spatial_error_Isometric_40_T1 >= Spatial_error_Isometric_40_T2:
        Isometric_40 = Isometric_40_T1
    else:
        Isometric_40 = Isometric_40_T2

    if Spatial_error_Isometric_20_T1 >= Spatial_error_Isometric_20_T2:
        Isometric_20 = Isometric_20_T1
    else:
        Isometric_20 = Isometric_20_T2

    if Spatial_error_Isometric_05_T1 >= Spatial_error_Isometric_05_T2:
        Isometric_05 = Isometric_05_T1
    else:
        Isometric_05 = Isometric_05_T2

    Isometric_80_surrogate_signals_list = []
    Isometric_60_surrogate_signals_list = []
    Isometric_40_surrogate_signals_list = []
    Isometric_20_surrogate_signals_list = []
    Isometric_05_surrogate_signals_list = []

    SaEn_Isometric_80_surrogate_signals_list = []
    SaEn_Isometric_60_surrogate_signals_list = []
    SaEn_Isometric_40_surrogate_signals_list = []
    SaEn_Isometric_20_surrogate_signals_list = []
    SaEn_Isometric_05_surrogate_signals_list = []

    SaEn_Isometric_80 = lb.Ent_Samp(Isometric_80, 2, 0.2)
    SaEn_Isometric_60 = lb.Ent_Samp(Isometric_60, 2, 0.2)
    SaEn_Isometric_40 = lb.Ent_Samp(Isometric_40, 2, 0.2)
    SaEn_Isometric_20 = lb.Ent_Samp(Isometric_20, 2, 0.2)
    SaEn_Isometric_05 = lb.Ent_Samp(Isometric_05, 2, 0.2)

    for i in range(19):
        Isometric_80_surrogate_signal = lb.Surr_Theiler(Isometric_80, 0)
        Isometric_60_surrogate_signal = lb.Surr_Theiler(Isometric_60, 0)
        Isometric_40_surrogate_signal = lb.Surr_Theiler(Isometric_40, 0)
        Isometric_20_surrogate_signal = lb.Surr_Theiler(Isometric_20, 0)
        Isometric_05_surrogate_signal = lb.Surr_Theiler(Isometric_05, 0)

        SaEn_Isometric_80_surrogate_signal = lb.Ent_Samp(Isometric_80_surrogate_signal, 2, 0.2)
        SaEn_Isometric_60_surrogate_signal = lb.Ent_Samp(Isometric_60_surrogate_signal, 2, 0.2)
        SaEn_Isometric_40_surrogate_signal = lb.Ent_Samp(Isometric_40_surrogate_signal, 2, 0.2)
        SaEn_Isometric_20_surrogate_signal = lb.Ent_Samp(Isometric_20_surrogate_signal, 2, 0.2)
        SaEn_Isometric_05_surrogate_signal = lb.Ent_Samp(Isometric_05_surrogate_signal, 2, 0.2)

        Isometric_80_surrogate_signals_list.append(Isometric_80_surrogate_signal)
        Isometric_60_surrogate_signals_list.append(Isometric_60_surrogate_signal)
        Isometric_40_surrogate_signals_list.append(Isometric_40_surrogate_signal)
        Isometric_20_surrogate_signals_list.append(Isometric_20_surrogate_signal)
        Isometric_05_surrogate_signals_list.append(Isometric_05_surrogate_signal)

        SaEn_Isometric_80_surrogate_signals_list.append(SaEn_Isometric_80_surrogate_signal)
        SaEn_Isometric_60_surrogate_signals_list.append(SaEn_Isometric_60_surrogate_signal)
        SaEn_Isometric_40_surrogate_signals_list.append(SaEn_Isometric_40_surrogate_signal)
        SaEn_Isometric_20_surrogate_signals_list.append(SaEn_Isometric_20_surrogate_signal)
        SaEn_Isometric_05_surrogate_signals_list.append(SaEn_Isometric_05_surrogate_signal)


    time_original = 0
    time_surrogation = np.linspace(1,19,19)
    plt.scatter(time_original, SaEn_Isometric_80, c='red')
    plt.scatter(time_surrogation, SaEn_Isometric_80_surrogate_signals_list, c='blue')
    plt.show()




