import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import glob
import statistics
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import lib

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 16

directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Strength data'
files = glob.glob(os.path.join(directory_path, "*"))

SaEn_80_list_T1 = []
SaEn_60_list_T1 = []
SaEn_40_list_T1 = []
SaEn_20_list_T1 = []
SaEn_05_list_T1 = []
SaEn_80_list_T2 = []
SaEn_60_list_T2 = []
SaEn_40_list_T2 = []
SaEn_20_list_T2 = []
SaEn_05_list_T2 = []
SaEn_80_list_Average = []
SaEn_60_list_Average = []
SaEn_40_list_Average = []
SaEn_20_list_Average = []
SaEn_05_list_Average = []

std_80_list_T1 = []
std_60_list_T1 = []
std_40_list_T1 = []
std_20_list_T1 = []
std_05_list_T1 = []
std_80_list_T2 = []
std_60_list_T2 = []
std_40_list_T2 = []
std_20_list_T2 = []
std_05_list_T2 = []
std_80_list_Average = []
std_60_list_Average = []
std_40_list_Average = []
std_20_list_Average = []
std_05_list_Average = []

CoV_80_list_T1 = []
CoV_60_list_T1 = []
CoV_40_list_T1 = []
CoV_20_list_T1 = []
CoV_05_list_T1 = []
CoV_80_list_T2 = []
CoV_60_list_T2 = []
CoV_40_list_T2 = []
CoV_20_list_T2 = []
CoV_05_list_T2 = []
CoV_80_list_Average = []
CoV_60_list_Average = []
CoV_40_list_Average = []
CoV_20_list_Average = []
CoV_05_list_Average = []

Isometric_80_T1_freq_90_list = []
Isometric_60_T1_freq_90_list = []
Isometric_40_T1_freq_90_list = []
Isometric_20_T1_freq_90_list = []
Isometric_05_T1_freq_90_list = []
Isometric_80_T2_freq_90_list = []
Isometric_60_T2_freq_90_list = []
Isometric_40_T2_freq_90_list = []
Isometric_20_T2_freq_90_list = []
Isometric_05_T2_freq_90_list = []
Isometric_80_freq_90_list_Average = []
Isometric_60_freq_90_list_Average = []
Isometric_40_freq_90_list_Average = []
Isometric_20_freq_90_list_Average = []
Isometric_05_freq_90_list_Average = []



Isometric_80_T1_freq_95_list = []
Isometric_60_T1_freq_95_list = []
Isometric_40_T1_freq_95_list = []
Isometric_20_T1_freq_95_list = []
Isometric_05_T1_freq_95_list = []
Isometric_80_T2_freq_95_list = []
Isometric_60_T2_freq_95_list = []
Isometric_40_T2_freq_95_list = []
Isometric_20_T2_freq_95_list = []
Isometric_05_T2_freq_95_list = []
Isometric_80_freq_95_list_Average = []
Isometric_60_freq_95_list_Average = []
Isometric_40_freq_95_list_Average = []
Isometric_20_freq_95_list_Average = []
Isometric_05_freq_95_list_Average = []

Isometric_80_T1_freq_99_list = []
Isometric_60_T1_freq_99_list = []
Isometric_40_T1_freq_99_list = []
Isometric_20_T1_freq_99_list = []
Isometric_05_T1_freq_99_list = []
Isometric_80_T2_freq_99_list = []
Isometric_60_T2_freq_99_list = []
Isometric_40_T2_freq_99_list = []
Isometric_20_T2_freq_99_list = []
Isometric_05_T2_freq_99_list = []
Isometric_80_freq_99_list_Average = []
Isometric_60_freq_99_list_Average = []
Isometric_40_freq_99_list_Average = []
Isometric_20_freq_99_list_Average = []
Isometric_05_freq_99_list_Average = []

Adaptation_down_T1_list = []
Adaptation_down_T2_list = []
Adaptation_down_list_Average = []
Adaptation_up_T1_list = []
Adaptation_up_T2_list = []
Adaptation_up_list_Average = []

sd = 2
consecutive_values = 37

ID_list = []

for file in files:
    directory = file
    os.chdir(directory)
    ID = os.path.basename(file)

    ID_list.append(ID)
    index = pd.read_excel(fr'index_{ID}.xlsx', index_col=None)
    print(ID)


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

    Pert_down_T1 = pd.read_csv(r'Pert_down_T1.csv', skiprows=2)
    Pert_down_T2 = pd.read_csv(r'Pert_down_T2.csv', skiprows=2)
    Pert_up_T1 = pd.read_csv(r'Pert_up_T1.csv', skiprows=2)
    Pert_up_T2 = pd.read_csv(r'Pert_up_T2.csv', skiprows=2)


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
    #
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
    Pert_down_T1['Performance'] = lib.Butterworth(75, 50, Pert_down_T1['Performance'])
    Pert_down_T2['Performance'] = lib.Butterworth(75, 50, Pert_down_T2['Performance'])
    Pert_up_T1['Performance'] = lib.Butterworth(75, 50, Pert_up_T1['Performance'])
    Pert_up_T2['Performance'] = lib.Butterworth(75, 50, Pert_up_T2['Performance'])


    # Calculation of Frequency of 90%, 95%, and 99% of total power for every rep for all percentages of MVC
    Isometric_80_T1_freq_90, Isometric_80_T1_freq_95, Isometric_80_T1_freq_99 = lib.FFT(Isometric_80_T1, 75)
    Isometric_80_T2_freq_90, Isometric_80_T2_freq_95, Isometric_80_T2_freq_99 = lib.FFT(Isometric_80_T2, 75)
    Isometric_60_T1_freq_90, Isometric_60_T1_freq_95, Isometric_60_T1_freq_99 = lib.FFT(Isometric_60_T1, 75)
    Isometric_60_T2_freq_90, Isometric_60_T2_freq_95, Isometric_60_T2_freq_99 = lib.FFT(Isometric_60_T2, 75)
    Isometric_40_T1_freq_90, Isometric_40_T1_freq_95, Isometric_40_T1_freq_99 = lib.FFT(Isometric_40_T1, 75)
    Isometric_40_T2_freq_90, Isometric_40_T2_freq_95, Isometric_40_T2_freq_99 = lib.FFT(Isometric_40_T2, 75)
    Isometric_20_T1_freq_90, Isometric_20_T1_freq_95, Isometric_20_T1_freq_99 = lib.FFT(Isometric_20_T1, 75)
    Isometric_20_T2_freq_90, Isometric_20_T2_freq_95, Isometric_20_T2_freq_99 = lib.FFT(Isometric_20_T2, 75)
    Isometric_05_T1_freq_90, Isometric_05_T1_freq_95, Isometric_05_T1_freq_99 = lib.FFT(Isometric_05_T1, 75)
    Isometric_05_T2_freq_90, Isometric_05_T2_freq_95, Isometric_05_T2_freq_99 = lib.FFT(Isometric_05_T2, 75)

    freq_T1_90 = [Isometric_80_T1_freq_90, Isometric_60_T1_freq_90, Isometric_40_T1_freq_90, Isometric_20_T1_freq_90,
                  Isometric_05_T1_freq_90]
    freq_T2_90 = [Isometric_80_T2_freq_90, Isometric_60_T2_freq_90, Isometric_40_T2_freq_90, Isometric_20_T2_freq_90,
                  Isometric_05_T2_freq_90]
    freq_T1_95 = [Isometric_80_T1_freq_95, Isometric_60_T1_freq_95, Isometric_40_T1_freq_95, Isometric_20_T1_freq_95,
                  Isometric_05_T1_freq_95]
    freq_T2_95 = [Isometric_80_T2_freq_95, Isometric_60_T2_freq_95, Isometric_40_T2_freq_95, Isometric_20_T2_freq_95,
                  Isometric_05_T2_freq_95]
    freq_T1_99 = [Isometric_80_T1_freq_99, Isometric_60_T1_freq_99, Isometric_40_T1_freq_99, Isometric_20_T1_freq_99,
                  Isometric_05_T1_freq_99]
    freq_T2_99 = [Isometric_80_T2_freq_99, Isometric_60_T2_freq_99, Isometric_40_T2_freq_99, Isometric_20_T2_freq_99,
                  Isometric_05_T2_freq_99]

    average_freq_90 = [np.mean((Isometric_80_T1_freq_90, Isometric_80_T2_freq_90)),
                    np.mean((Isometric_60_T1_freq_90, Isometric_60_T2_freq_90)),
                    np.mean((Isometric_40_T1_freq_90, Isometric_40_T2_freq_90)),
                    np.mean((Isometric_20_T1_freq_90, Isometric_20_T2_freq_90)),
                    np.mean((Isometric_05_T1_freq_90, Isometric_05_T2_freq_90))]
    average_freq_95 = [np.mean((Isometric_80_T1_freq_95, Isometric_80_T2_freq_95)),
                    np.mean((Isometric_60_T1_freq_95, Isometric_60_T2_freq_95)),
                    np.mean((Isometric_40_T1_freq_95, Isometric_40_T2_freq_95)),
                    np.mean((Isometric_20_T1_freq_95, Isometric_20_T2_freq_95)),
                    np.mean((Isometric_05_T1_freq_95, Isometric_05_T2_freq_95))]
    average_freq_99 = [np.mean((Isometric_80_T1_freq_99, Isometric_80_T2_freq_99)),
                    np.mean((Isometric_60_T1_freq_99, Isometric_60_T2_freq_99)),
                    np.mean((Isometric_40_T1_freq_99, Isometric_40_T2_freq_99)),
                    np.mean((Isometric_20_T1_freq_99, Isometric_20_T2_freq_99)),
                    np.mean((Isometric_05_T1_freq_99, Isometric_05_T2_freq_99))]


    # Calculation of standard deviation for every rep for all percentages of MVC
    std_Isometric_80_T1 = np.std(Isometric_80_T1)
    std_Isometric_80_T2 = np.std(Isometric_80_T2)
    std_Isometric_60_T1 = np.std(Isometric_60_T1)
    std_Isometric_60_T2 = np.std(Isometric_60_T2)
    std_Isometric_40_T1 = np.std(Isometric_40_T1)
    std_Isometric_40_T2 = np.std(Isometric_40_T2)
    std_Isometric_20_T1 = np.std(Isometric_20_T1)
    std_Isometric_20_T2 = np.std(Isometric_20_T2)
    std_Isometric_05_T1 = np.std(Isometric_05_T1)
    std_Isometric_05_T2 = np.std(Isometric_05_T2)

    std_T1 = [std_Isometric_80_T1, std_Isometric_60_T1, std_Isometric_40_T1, std_Isometric_20_T1, std_Isometric_05_T1]
    std_T2 = [std_Isometric_80_T2, std_Isometric_60_T2, std_Isometric_40_T2, std_Isometric_20_T2, std_Isometric_05_T2]
    average_std = [np.mean((std_Isometric_80_T1, std_Isometric_80_T2)),
                   np.mean((std_Isometric_60_T1, std_Isometric_60_T2)),
                   np.mean((std_Isometric_40_T1, std_Isometric_40_T2)),
                   np.mean((std_Isometric_20_T1, std_Isometric_05_T1)),
                   np.mean((std_Isometric_05_T1, std_Isometric_05_T2))]

    # Calculation of Coefficient of Variation for every rep for all percentages of MVC
    CoV_Isometric_80_T1 = (np.std(Isometric_80_T1) / np.mean(Isometric_80_T1)) * 100
    CoV_Isometric_80_T2 = (np.std(Isometric_80_T2) / np.mean(Isometric_80_T2)) * 100
    CoV_Isometric_60_T1 = (np.std(Isometric_60_T1) / np.mean(Isometric_60_T1)) * 100
    CoV_Isometric_60_T2 = (np.std(Isometric_60_T2) / np.mean(Isometric_60_T2)) * 100
    CoV_Isometric_40_T1 = (np.std(Isometric_40_T1) / np.mean(Isometric_40_T1)) * 100
    CoV_Isometric_40_T2 = (np.std(Isometric_40_T2) / np.mean(Isometric_40_T2)) * 100
    CoV_Isometric_20_T1 = (np.std(Isometric_20_T1) / np.mean(Isometric_20_T1)) * 100
    CoV_Isometric_20_T2 = (np.std(Isometric_20_T2) / np.mean(Isometric_20_T2)) * 100
    CoV_Isometric_05_T1 = (np.std(Isometric_05_T1) / np.mean(Isometric_05_T1)) * 100
    CoV_Isometric_05_T2 = (np.std(Isometric_05_T2) / np.mean(Isometric_05_T2)) * 100

    CoV_T1 = [CoV_Isometric_80_T1, CoV_Isometric_60_T1, CoV_Isometric_40_T1, CoV_Isometric_20_T1, CoV_Isometric_05_T1]
    CoV_T2 = [CoV_Isometric_80_T2, CoV_Isometric_60_T2, CoV_Isometric_40_T2, CoV_Isometric_20_T2, CoV_Isometric_05_T2]
    average_CoV = [np.mean((CoV_Isometric_80_T1, CoV_Isometric_80_T2)),
                   np.mean((CoV_Isometric_60_T1, CoV_Isometric_60_T2)),
                   np.mean((CoV_Isometric_40_T1, CoV_Isometric_40_T2)),
                   np.mean((CoV_Isometric_20_T1, CoV_Isometric_20_T2)),
                   np.mean((CoV_Isometric_05_T1, CoV_Isometric_05_T2))]

    # Calculation of Sample Entropy for every rep for all percentages of MVC
    SaEn_Isometric_80_T1 = lb.Ent_Samp(Isometric_80_T1, 2, 0.2)
    SaEn_Isometric_80_T2 = lb.Ent_Samp(Isometric_80_T2, 2, 0.2)
    SaEn_Isometric_60_T1 = lb.Ent_Samp(Isometric_60_T1, 2, 0.2)
    SaEn_Isometric_60_T2 = lb.Ent_Samp(Isometric_60_T2, 2, 0.2)
    SaEn_Isometric_40_T1 = lb.Ent_Samp(Isometric_40_T1, 2, 0.2)
    SaEn_Isometric_40_T2 = lb.Ent_Samp(Isometric_40_T2, 2, 0.2)
    SaEn_Isometric_20_T1 = lb.Ent_Samp(Isometric_20_T1, 2, 0.2)
    SaEn_Isometric_20_T2 = lb.Ent_Samp(Isometric_20_T2, 2, 0.2)
    SaEn_Isometric_05_T1 = lb.Ent_Samp(Isometric_05_T1, 2, 0.2)
    SaEn_Isometric_05_T2 = lb.Ent_Samp(Isometric_05_T2, 2, 0.2)

    SaEn_T1 = [SaEn_Isometric_80_T1, SaEn_Isometric_60_T1, SaEn_Isometric_40_T1, SaEn_Isometric_20_T1, SaEn_Isometric_05_T1]
    SaEn_T2 = [SaEn_Isometric_80_T2, SaEn_Isometric_60_T2, SaEn_Isometric_40_T2, SaEn_Isometric_20_T2, SaEn_Isometric_05_T2]

    average_SaEn = [np.mean((SaEn_Isometric_80_T1, SaEn_Isometric_80_T2)),
                    np.mean((SaEn_Isometric_60_T1, SaEn_Isometric_60_T2)),
                    np.mean((SaEn_Isometric_40_T1, SaEn_Isometric_40_T2)),
                    np.mean((SaEn_Isometric_20_T1, SaEn_Isometric_20_T2)),
                    np.mean((SaEn_Isometric_05_T1, SaEn_Isometric_05_T2))]

    # Calculation of time to adaptation for all perturbation trials
    time_of_adaptation_down_T1 = lb.adaptation_time_using_sd(Pert_down_T1, 250, sd, 100, consecutive_values, 100, 500,'Pert_down_T1', 20, plot=False)
    time_of_adaptation_down_T2 = lb.adaptation_time_using_sd(Pert_down_T2, 250, sd, 100, consecutive_values, 100, 500,'Pert_down_T2', 20, plot=False)
    time_of_adaptation_up_T1 = lb.adaptation_time_using_sd(Pert_up_T1, 250, sd, 100, consecutive_values, 100, 500,'Pert_up_T1', 20, plot=False)
    time_of_adaptation_up_T2 = lb.adaptation_time_using_sd(Pert_up_T2, 250, sd, 100, consecutive_values, 100, 500,'Pert_up_T2', 20, plot=False)

    if time_of_adaptation_down_T1 != None:
        time_of_adaptation_down_T1 = round(time_of_adaptation_down_T1, 3)

    if time_of_adaptation_down_T2 != None:
        time_of_adaptation_down_T2 = round(time_of_adaptation_down_T2, 3)

    if time_of_adaptation_up_T1 != None:
        time_of_adaptation_up_T1 = round(time_of_adaptation_up_T1, 3)

    if time_of_adaptation_up_T2 != None:
        time_of_adaptation_up_T2 = round(time_of_adaptation_up_T2, 3)

    if time_of_adaptation_down_T1 != None and time_of_adaptation_down_T2 != None:
        time_of_adaptation_down_average = np.mean((time_of_adaptation_down_T1, time_of_adaptation_down_T2))

    elif time_of_adaptation_down_T1 != None and time_of_adaptation_down_T2 == None:
        time_of_adaptation_down_average = time_of_adaptation_down_T1

    elif time_of_adaptation_down_T1 == None and time_of_adaptation_down_T2 != None:
        time_of_adaptation_down_average = time_of_adaptation_down_T2

    elif time_of_adaptation_down_T1 == None and time_of_adaptation_down_T2 == None:
        time_of_adaptation_down_average = None
        print(f'no adaptation occurred for {ID} in down perturbation')

    if time_of_adaptation_up_T1 != None and time_of_adaptation_up_T2 != None:
        time_of_adaptation_up_average = np.mean((time_of_adaptation_up_T1, time_of_adaptation_up_T2))

    elif time_of_adaptation_up_T1 != None and time_of_adaptation_up_T2 == None:
        time_of_adaptation_up_average = time_of_adaptation_up_T1

    elif time_of_adaptation_up_T1 == None and time_of_adaptation_up_T2 != None:
        time_of_adaptation_up_average = time_of_adaptation_up_T2

    elif time_of_adaptation_up_T1 == None and time_of_adaptation_up_T2 == None:
        time_of_adaptation_up_average = None
        print(f'no adaptation occurred for {ID} in up perturbation')



    # Append every value to each dedicated list
    SaEn_80_list_T1.append(SaEn_Isometric_80_T1)
    SaEn_60_list_T1.append(SaEn_Isometric_60_T1)
    SaEn_40_list_T1.append(SaEn_Isometric_40_T1)
    SaEn_20_list_T1.append(SaEn_Isometric_20_T1)
    SaEn_05_list_T1.append(SaEn_Isometric_05_T1)
    SaEn_80_list_T2.append(SaEn_Isometric_80_T2)
    SaEn_60_list_T2.append(SaEn_Isometric_60_T2)
    SaEn_40_list_T2.append(SaEn_Isometric_40_T2)
    SaEn_20_list_T2.append(SaEn_Isometric_20_T2)
    SaEn_05_list_T2.append(SaEn_Isometric_05_T2)
    SaEn_80_list_Average.append(average_SaEn[0])
    SaEn_60_list_Average.append(average_SaEn[1])
    SaEn_40_list_Average.append(average_SaEn[2])
    SaEn_20_list_Average.append(average_SaEn[3])
    SaEn_05_list_Average.append(average_SaEn[4])

    std_80_list_T1.append(std_Isometric_80_T1)
    std_60_list_T1.append(std_Isometric_60_T1)
    std_40_list_T1.append(std_Isometric_40_T1)
    std_20_list_T1.append(std_Isometric_20_T1)
    std_05_list_T1.append(std_Isometric_05_T1)
    std_80_list_T2.append(std_Isometric_80_T2)
    std_60_list_T2.append(std_Isometric_60_T2)
    std_40_list_T2.append(std_Isometric_40_T2)
    std_20_list_T2.append(std_Isometric_20_T2)
    std_05_list_T2.append(std_Isometric_05_T2)
    std_80_list_Average.append(average_std[0])
    std_60_list_Average.append(average_std[1])
    std_40_list_Average.append(average_std[2])
    std_20_list_Average.append(average_std[3])
    std_05_list_Average.append(average_std[4])

    CoV_80_list_T1.append(CoV_Isometric_80_T1)
    CoV_60_list_T1.append(CoV_Isometric_60_T1)
    CoV_40_list_T1.append(CoV_Isometric_40_T1)
    CoV_20_list_T1.append(CoV_Isometric_20_T1)
    CoV_05_list_T1.append(CoV_Isometric_05_T1)
    CoV_80_list_T2.append(CoV_Isometric_80_T2)
    CoV_60_list_T2.append(CoV_Isometric_60_T2)
    CoV_40_list_T2.append(CoV_Isometric_40_T2)
    CoV_20_list_T2.append(CoV_Isometric_20_T2)
    CoV_05_list_T2.append(CoV_Isometric_05_T2)
    CoV_80_list_Average.append(average_CoV[0])
    CoV_60_list_Average.append(average_CoV[1])
    CoV_40_list_Average.append(average_CoV[2])
    CoV_20_list_Average.append(average_CoV[3])
    CoV_05_list_Average.append(average_CoV[4])

    Isometric_80_T1_freq_90_list.append(Isometric_80_T1_freq_90)
    Isometric_60_T1_freq_90_list.append(Isometric_60_T1_freq_90)
    Isometric_40_T1_freq_90_list.append(Isometric_40_T1_freq_90)
    Isometric_20_T1_freq_90_list.append(Isometric_20_T1_freq_90)
    Isometric_05_T1_freq_90_list.append(Isometric_05_T1_freq_90)
    Isometric_80_T2_freq_90_list.append(Isometric_80_T2_freq_90)
    Isometric_60_T2_freq_90_list.append(Isometric_60_T2_freq_90)
    Isometric_40_T2_freq_90_list.append(Isometric_40_T2_freq_90)
    Isometric_20_T2_freq_90_list.append(Isometric_20_T2_freq_90)
    Isometric_05_T2_freq_90_list.append(Isometric_05_T2_freq_90)
    Isometric_80_freq_90_list_Average.append(average_freq_90[0])
    Isometric_60_freq_90_list_Average.append(average_freq_90[1])
    Isometric_40_freq_90_list_Average.append(average_freq_90[2])
    Isometric_20_freq_90_list_Average.append(average_freq_90[3])
    Isometric_05_freq_90_list_Average.append(average_freq_90[4])

    Isometric_80_T1_freq_95_list.append(Isometric_80_T1_freq_95)
    Isometric_60_T1_freq_95_list.append(Isometric_60_T1_freq_95)
    Isometric_40_T1_freq_95_list.append(Isometric_40_T1_freq_95)
    Isometric_20_T1_freq_95_list.append(Isometric_20_T1_freq_95)
    Isometric_05_T1_freq_95_list.append(Isometric_05_T1_freq_95)
    Isometric_80_T2_freq_95_list.append(Isometric_80_T2_freq_95)
    Isometric_60_T2_freq_95_list.append(Isometric_60_T2_freq_95)
    Isometric_40_T2_freq_95_list.append(Isometric_40_T2_freq_95)
    Isometric_20_T2_freq_95_list.append(Isometric_20_T2_freq_95)
    Isometric_05_T2_freq_95_list.append(Isometric_05_T2_freq_95)
    Isometric_80_freq_95_list_Average.append(average_freq_95[0])
    Isometric_60_freq_95_list_Average.append(average_freq_95[1])
    Isometric_40_freq_95_list_Average.append(average_freq_95[2])
    Isometric_20_freq_95_list_Average.append(average_freq_95[3])
    Isometric_05_freq_95_list_Average.append(average_freq_95[4])

    Isometric_80_T1_freq_99_list.append(Isometric_80_T1_freq_99)
    Isometric_60_T1_freq_99_list.append(Isometric_60_T1_freq_99)
    Isometric_40_T1_freq_99_list.append(Isometric_40_T1_freq_99)
    Isometric_20_T1_freq_99_list.append(Isometric_20_T1_freq_99)
    Isometric_05_T1_freq_99_list.append(Isometric_05_T1_freq_99)
    Isometric_80_T2_freq_99_list.append(Isometric_80_T2_freq_99)
    Isometric_60_T2_freq_99_list.append(Isometric_60_T2_freq_99)
    Isometric_40_T2_freq_99_list.append(Isometric_40_T2_freq_99)
    Isometric_20_T2_freq_99_list.append(Isometric_20_T2_freq_99)
    Isometric_05_T2_freq_99_list.append(Isometric_05_T2_freq_99)
    Isometric_80_freq_99_list_Average.append(average_freq_99[0])
    Isometric_60_freq_99_list_Average.append(average_freq_99[1])
    Isometric_40_freq_99_list_Average.append(average_freq_99[2])
    Isometric_20_freq_99_list_Average.append(average_freq_99[3])
    Isometric_05_freq_99_list_Average.append(average_freq_99[4])

    Adaptation_down_T1_list.append(time_of_adaptation_down_T1)
    Adaptation_down_T2_list.append(time_of_adaptation_down_T2)
    Adaptation_down_list_Average.append(time_of_adaptation_down_average)
    Adaptation_up_T1_list.append(time_of_adaptation_up_T1)
    Adaptation_up_T2_list.append(time_of_adaptation_up_T2)
    Adaptation_up_list_Average.append(time_of_adaptation_up_average)



# Creation of a dictionary with all the data for all participants
dist = {
    'ID': ID_list,
    'SaEn_80_T1': SaEn_80_list_T1,
    'SaEn_60_T1': SaEn_60_list_T1,
    'SaEn_40_T1': SaEn_40_list_T1,
    'SaEn_20_T1': SaEn_20_list_T1,
    'SaEn_05_T1': SaEn_05_list_T1,
    'SaEn_80_T2': SaEn_80_list_T2,
    'SaEn_60_T2': SaEn_60_list_T2,
    'SaEn_40_T2': SaEn_40_list_T2,
    'SaEn_20_T2': SaEn_20_list_T2,
    'SaEn_05_T2': SaEn_05_list_T2,
    'SaEn_80_Average': SaEn_80_list_Average,
    'SaEn_60_Average': SaEn_60_list_Average,
    'SaEn_40_Average': SaEn_40_list_Average,
    'SaEn_20_Average': SaEn_20_list_Average,
    'SaEn_05_Average': SaEn_05_list_Average,
    'sd_80_T1': std_80_list_T1,
    'sd_60_T1': std_60_list_T1,
    'sd_40_T1': std_40_list_T1,
    'sd_20_T1': std_20_list_T1,
    'sd_05_T1': std_05_list_T1,
    'sd_80_T2': std_80_list_T2,
    'sd_60_T2': std_60_list_T2,
    'sd_40_T2': std_40_list_T2,
    'sd_20_T2': std_20_list_T2,
    'sd_05_T2': std_05_list_T2,
    'sd_80_Average': std_80_list_Average,
    'sd_60_Average': std_60_list_Average,
    'sd_40_Average': std_40_list_Average,
    'sd_20_Average': std_20_list_Average,
    'sd_05_Average': std_05_list_Average,
    'CoV_80_T1': CoV_80_list_T1,
    'CoV_60_T1': CoV_60_list_T1,
    'CoV_40_T1': CoV_40_list_T1,
    'CoV_20_T1': CoV_20_list_T1,
    'CoV_05_T1': CoV_05_list_T1,
    'CoV_80_T2': CoV_80_list_T2,
    'CoV_60_T2': CoV_60_list_T2,
    'CoV_40_T2': CoV_40_list_T2,
    'CoV_20_T2': CoV_20_list_T2,
    'CoV_05_T2': CoV_05_list_T2,
    'CoV_80_Average': CoV_80_list_Average,
    'CoV_60_Average': CoV_60_list_Average,
    'CoV_40_Average': CoV_40_list_Average,
    'CoV_20_Average': CoV_20_list_Average,
    'CoV_05_Average': CoV_05_list_Average,
    'Freq_90_T1_80': Isometric_80_T1_freq_90_list,
    'Freq_90_T1_60': Isometric_60_T1_freq_90_list,
    'Freq_90_T1_40': Isometric_40_T1_freq_90_list,
    'Freq_90_T1_20': Isometric_20_T1_freq_90_list,
    'Freq_90_T1_05': Isometric_05_T1_freq_90_list,
    'Freq_90_T2_80': Isometric_80_T2_freq_90_list,
    'Freq_90_T2_60': Isometric_60_T2_freq_90_list,
    'Freq_90_T2_40': Isometric_40_T2_freq_90_list,
    'Freq_90_T2_20': Isometric_20_T2_freq_90_list,
    'Freq_90_T2_05': Isometric_05_T2_freq_90_list,
    'Freq_90_Average_80': Isometric_80_freq_90_list_Average,
    'Freq_90_Average_60': Isometric_60_freq_90_list_Average,
    'Freq_90_Average_40': Isometric_40_freq_90_list_Average,
    'Freq_90_Average_20': Isometric_20_freq_90_list_Average,
    'Freq_90_Average_05': Isometric_05_freq_90_list_Average,
    'Freq_95_T1_80': Isometric_80_T1_freq_95_list,
    'Freq_95_T1_60': Isometric_60_T1_freq_95_list,
    'Freq_95_T1_40': Isometric_40_T1_freq_95_list,
    'Freq_95_T1_20': Isometric_20_T1_freq_95_list,
    'Freq_95_T1_05': Isometric_05_T1_freq_95_list,
    'Freq_95_T2_80': Isometric_80_T2_freq_95_list,
    'Freq_95_T2_60': Isometric_60_T2_freq_95_list,
    'Freq_95_T2_40': Isometric_40_T2_freq_95_list,
    'Freq_95_T2_20': Isometric_20_T2_freq_95_list,
    'Freq_95_T2_05': Isometric_05_T2_freq_95_list,
    'Freq_95_Average_80': Isometric_80_freq_95_list_Average,
    'Freq_95_Average_60': Isometric_60_freq_95_list_Average,
    'Freq_95_Average_40': Isometric_40_freq_95_list_Average,
    'Freq_95_Average_20': Isometric_20_freq_95_list_Average,
    'Freq_95_Average_05': Isometric_05_freq_95_list_Average,
    'Freq_99_T1_80': Isometric_80_T1_freq_99_list,
    'Freq_99_T1_60': Isometric_60_T1_freq_99_list,
    'Freq_99_T1_40': Isometric_40_T1_freq_99_list,
    'Freq_99_T1_20': Isometric_20_T1_freq_99_list,
    'Freq_99_T1_05': Isometric_05_T1_freq_99_list,
    'Freq_99_T2_80': Isometric_80_T2_freq_99_list,
    'Freq_99_T2_60': Isometric_60_T2_freq_99_list,
    'Freq_99_T2_40': Isometric_40_T2_freq_99_list,
    'Freq_99_T2_20': Isometric_20_T2_freq_99_list,
    'Freq_99_T2_05': Isometric_05_T2_freq_99_list,
    'Freq_99_Average_80': Isometric_80_freq_99_list_Average,
    'Freq_99_Average_60': Isometric_60_freq_99_list_Average,
    'Freq_99_Average_40': Isometric_40_freq_99_list_Average,
    'Freq_99_Average_20': Isometric_20_freq_99_list_Average,
    'Freq_99_Average_05': Isometric_05_freq_99_list_Average,
    'time_of_adaptation_down_T1': Adaptation_down_T1_list,
    'time_of_adaptation_down_T2': Adaptation_down_T2_list,
    'time_of_adaptation_down_average': Adaptation_down_list_Average,
    'time_of_adaptation_up_T1': Adaptation_up_T1_list,
    'time_of_adaptation_up_T2': Adaptation_up_T2_list,
    'time_of_adaptation_up_average': Adaptation_up_list_Average,

}



new_excel = pd.DataFrame(dist)
os.chdir(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Results\Isometric')
new_excel.to_excel(r'Results all Lowpass 50Hz.xlsx')
