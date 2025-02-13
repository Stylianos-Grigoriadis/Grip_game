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

SaEn_80_list = []
SaEn_60_list = []
SaEn_40_list = []
SaEn_20_list = []
SaEn_05_list = []

std_80_list = []
std_60_list = []
std_40_list = []
std_20_list = []
std_05_list = []

CoV_80_list = []
CoV_60_list = []
CoV_40_list = []
CoV_20_list = []
CoV_05_list = []

Isometric_80_freq_90_list = []
Isometric_60_freq_90_list = []
Isometric_40_freq_90_list = []
Isometric_20_freq_90_list = []
Isometric_05_freq_90_list = []

Isometric_80_freq_95_list = []
Isometric_60_freq_95_list = []
Isometric_40_freq_95_list = []
Isometric_20_freq_95_list = []
Isometric_05_freq_95_list = []

Isometric_80_freq_99_list = []
Isometric_60_freq_99_list = []
Isometric_40_freq_99_list = []
Isometric_20_freq_99_list = []
Isometric_05_freq_99_list = []

Adaptation_down_min_list = []
Adaptation_up_min_list = []
Adaptation_down_max_list = []
Adaptation_up_max_list = []
Adaptation_down_T1_list = []
Adaptation_up_T1_list = []
Adaptation_down_T2_list = []
Adaptation_up_T2_list = []

SaEn_Adaptation_down_min_list = []
SaEn_Adaptation_up_min_list = []
SaEn_Adaptation_down_max_list = []
SaEn_Adaptation_up_max_list = []
SaEn_Adaptation_down_T1_list = []
SaEn_Adaptation_up_T1_list = []
SaEn_Adaptation_down_T2_list = []
SaEn_Adaptation_up_T2_list = []

sd = 2
consecutive_values = 37

ID_list = []
excel_for_names = pd.read_excel(
    r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Participants.xlsx')

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
    Pert_down_T1['Performance'] = lib.Butterworth(75, 50, Pert_down_T1['Performance'])
    Pert_down_T2['Performance'] = lib.Butterworth(75, 50, Pert_down_T2['Performance'])
    Pert_up_T1['Performance'] = lib.Butterworth(75, 50, Pert_up_T1['Performance'])
    Pert_up_T2['Performance'] = lib.Butterworth(75, 50, Pert_up_T2['Performance'])

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

    # Calculation of Frequency of 90%, 95%, and 99% of total power for every rep for all percentages of MVC
    Isometric_80_freq_90, Isometric_80_freq_95, Isometric_80_freq_99 = lib.FFT(Isometric_80, 75)
    Isometric_60_freq_90, Isometric_60_freq_95, Isometric_60_freq_99 = lib.FFT(Isometric_60, 75)
    Isometric_40_freq_90, Isometric_40_freq_95, Isometric_40_freq_99 = lib.FFT(Isometric_40, 75)
    Isometric_20_freq_90, Isometric_20_freq_95, Isometric_20_freq_99 = lib.FFT(Isometric_20, 75)
    Isometric_05_freq_90, Isometric_05_freq_95, Isometric_05_freq_99 = lib.FFT(Isometric_05, 75)

    freq_90 = [Isometric_80_freq_90, Isometric_60_freq_90, Isometric_40_freq_90, Isometric_20_freq_90,
               Isometric_05_freq_90]

    freq_95 = [Isometric_80_freq_95, Isometric_60_freq_95, Isometric_40_freq_95, Isometric_20_freq_95,
               Isometric_05_freq_95]

    freq_99 = [Isometric_80_freq_99, Isometric_60_freq_99, Isometric_40_freq_99, Isometric_20_freq_99,
               Isometric_05_freq_99]

    # Calculation of standard deviation for every rep for all percentages of MVC
    std_Isometric_80 = np.std(Isometric_80)
    std_Isometric_60 = np.std(Isometric_60)
    std_Isometric_40 = np.std(Isometric_40)
    std_Isometric_20 = np.std(Isometric_20)
    std_Isometric_05 = np.std(Isometric_05)

    # Calculation of Coefficient of Variation for every rep for all percentages of MVC
    CoV_Isometric_80 = (np.std(Isometric_80) / np.mean(Isometric_80)) * 100
    CoV_Isometric_60 = (np.std(Isometric_60) / np.mean(Isometric_60)) * 100
    CoV_Isometric_40 = (np.std(Isometric_40) / np.mean(Isometric_40)) * 100
    CoV_Isometric_20 = (np.std(Isometric_20) / np.mean(Isometric_20)) * 100
    CoV_Isometric_05 = (np.std(Isometric_05) / np.mean(Isometric_05)) * 100

    # Calculation of Sample Entropy for every rep for all percentages of MVC
    SaEn_Isometric_80 = lb.Ent_Samp(Isometric_80, 2, 0.2)
    SaEn_Isometric_60 = lb.Ent_Samp(Isometric_60, 2, 0.2)
    SaEn_Isometric_40 = lb.Ent_Samp(Isometric_40, 2, 0.2)
    SaEn_Isometric_20 = lb.Ent_Samp(Isometric_20, 2, 0.2)
    SaEn_Isometric_05 = lb.Ent_Samp(Isometric_05, 2, 0.2)


    # Calculation of time to adaptation for all perturbation trials
    time_of_adaptation_down_T1 = lb.adaptation_time_using_sd(Pert_down_T1, 250, sd, 100, consecutive_values, 100, 'Pert_down_T1', plot=False)
    time_of_adaptation_down_T2 = lb.adaptation_time_using_sd(Pert_down_T2, 250, sd, 100, consecutive_values, 100, 'Pert_down_T2', plot=False)
    time_of_adaptation_up_T1 = lb.adaptation_time_using_sd(Pert_up_T1, 250, sd, 100, consecutive_values, 100, 'Pert_up_T1', plot=False)
    time_of_adaptation_up_T2 = lb.adaptation_time_using_sd(Pert_up_T2, 250, sd, 100, consecutive_values, 100, 'Pert_up_T2', plot=False)

    if not ID == 'Old.18' and not ID == 'Old.7':
        Pert_down_T1_array = Pert_down_T1['Performance'][300:1200].to_numpy()
        Pert_down_T2_array = Pert_down_T2['Performance'][300:1200].to_numpy()
        Pert_up_T1_array = Pert_up_T1['Performance'][300:1200].to_numpy()
        Pert_up_T2_array = Pert_up_T2['Performance'][300:1200].to_numpy()

    elif ID == 'Old.18':
        Pert_down_T1_array = Pert_down_T1['Performance'][300:1200].to_numpy()
        Pert_down_T2_array = Pert_down_T2['Performance'][150:600].to_numpy()
        Pert_up_T1_array = Pert_up_T1['Performance'][300:1200].to_numpy()
        Pert_up_T2_array = Pert_up_T2['Performance'][300:1200].to_numpy()

    elif ID == 'Old.7':
        Pert_down_T1_array = Pert_down_T1['Performance'][300:1200].to_numpy()
        Pert_down_T2_array = Pert_down_T2['Performance'][300:1200].to_numpy()
        Pert_up_T1_array = Pert_up_T1['Performance'][300:1200].to_numpy()
        Pert_up_T2_array = Pert_up_T2['Performance'][450:1800].to_numpy()

    if time_of_adaptation_down_T1 != None:
        time_of_adaptation_down_T1 = round(time_of_adaptation_down_T1, 3)
    else:
        time_of_adaptation_down_T1 = 0

    if time_of_adaptation_down_T2 != None:
        time_of_adaptation_down_T2 = round(time_of_adaptation_down_T2, 3)
    else:
        time_of_adaptation_down_T2 = 0

    if time_of_adaptation_up_T1 != None:
        time_of_adaptation_up_T1 = round(time_of_adaptation_up_T1, 3)
    else:
        time_of_adaptation_up_T1 = 0

    if time_of_adaptation_up_T2 != None:
        time_of_adaptation_up_T2 = round(time_of_adaptation_up_T2, 3)
    else:
        time_of_adaptation_up_T2 = 0



    if time_of_adaptation_down_T1 != 0 and time_of_adaptation_down_T2 != 0:
        time_of_adaptation_down_min = np.min((time_of_adaptation_down_T1, time_of_adaptation_down_T2))
        time_of_adaptation_down_max = np.max((time_of_adaptation_down_T1, time_of_adaptation_down_T2))

        if time_of_adaptation_down_min == time_of_adaptation_down_T1:
            Pert_down_array_min = Pert_down_T1_array
            Pert_down_array_max = Pert_down_T2_array
        elif time_of_adaptation_down_min == time_of_adaptation_down_T2:
            Pert_down_array_min = Pert_down_T2_array
            Pert_down_array_max = Pert_down_T1_array

    elif time_of_adaptation_down_T1 != 0 and time_of_adaptation_down_T2 == 0:
        time_of_adaptation_down_min = time_of_adaptation_down_T1
        time_of_adaptation_down_max = None
        Pert_down_array_min = Pert_down_T1_array
        Pert_down_array_max = None


    elif time_of_adaptation_down_T1 == 0 and time_of_adaptation_down_T2 != 0:
        time_of_adaptation_down_min = time_of_adaptation_down_T2
        time_of_adaptation_down_max = None
        Pert_down_array = Pert_down_T2_array
        Pert_down_array_max = None

    elif time_of_adaptation_down_T1 == 0 and time_of_adaptation_down_T2 == 0:
        time_of_adaptation_down_min = None
        time_of_adaptation_down_max = None
        Pert_down_array_min = None  # This is because we haven't found any adaptation in both trials thus, no array has any meaning
        Pert_down_array_max = None  # This is because we haven't found any adaptation in both trials thus, no array has any meaning
        print(f'no adaptation occurred for {ID} in down perturbation')

    if time_of_adaptation_up_T1 != 0 and time_of_adaptation_up_T2 != 0:
        time_of_adaptation_up_min = np.min((time_of_adaptation_up_T1, time_of_adaptation_up_T2))
        time_of_adaptation_up_max = np.max((time_of_adaptation_up_T1, time_of_adaptation_up_T2))

        if time_of_adaptation_up_min == time_of_adaptation_up_T1:
            Pert_up_array_min = Pert_up_T1_array
            Pert_up_array_max = Pert_up_T2_array
        elif time_of_adaptation_up_min == time_of_adaptation_up_T2:
            Pert_up_array_min = Pert_up_T2_array
            Pert_up_array_max = Pert_up_T1_array

    elif time_of_adaptation_up_T1 != 0 and time_of_adaptation_up_T2 == 0:
        time_of_adaptation_up_min = time_of_adaptation_up_T1
        time_of_adaptation_up_max = None
        Pert_up_array_min = Pert_up_T1_array
        Pert_up_array_max = None


    elif time_of_adaptation_up_T1 == 0 and time_of_adaptation_up_T2 != 0:
        time_of_adaptation_up_min = time_of_adaptation_up_T2
        time_of_adaptation_up_max = None
        Pert_up_array = Pert_up_T2_array
        Pert_up_array_max = None

    elif time_of_adaptation_up_T1 == 0 and time_of_adaptation_up_T2 == 0:
        time_of_adaptation_up_min = None
        time_of_adaptation_up_max = None
        Pert_up_array_min = None  # This is because we haven't found any adaptation in both trials thus, no array has any meaning
        Pert_up_array_max = None  # This is because we haven't found any adaptation in both trials thus, no array has any meaning
        print(f'no adaptation occurred for {ID} in up perturbation')



    # Calculate the SaEn of the perturbation trials
    if Pert_down_array_min is not None:
        SaEn_Pert_down_min = lb.Ent_Samp(Pert_down_array_min, 2, 0.2)
    else:
        SaEn_Pert_down_min = None

    if Pert_down_array_max is not None:
        SaEn_Pert_down_max = lb.Ent_Samp(Pert_down_array_max, 2, 0.2)
    else:
        SaEn_Pert_down_max = None

    SaEn_Pert_down_T1 = lb.Ent_Samp(Pert_down_T1_array, 2, 0.2)
    SaEn_Pert_down_T2 = lb.Ent_Samp(Pert_down_T2_array, 2, 0.2)

    if Pert_up_array_min is not None:
        SaEn_Pert_up_min = lb.Ent_Samp(Pert_up_array_min, 2, 0.2)
    else:
        SaEn_Pert_up_min = None

    if Pert_up_array_max is not None:
        SaEn_Pert_up_max = lb.Ent_Samp(Pert_up_array_max, 2, 0.2)
    else:
        SaEn_Pert_up_max = None

    SaEn_Pert_up_T1 = lb.Ent_Samp(Pert_up_T1_array, 2, 0.2)
    SaEn_Pert_up_T2 = lb.Ent_Samp(Pert_up_T2_array, 2, 0.2)



    # Append every value to each dedicated list
    SaEn_80_list.append(SaEn_Isometric_80)
    SaEn_60_list.append(SaEn_Isometric_60)
    SaEn_40_list.append(SaEn_Isometric_40)
    SaEn_20_list.append(SaEn_Isometric_20)
    SaEn_05_list.append(SaEn_Isometric_05)

    std_80_list.append(std_Isometric_80)
    std_60_list.append(std_Isometric_60)
    std_40_list.append(std_Isometric_40)
    std_20_list.append(std_Isometric_20)
    std_05_list.append(std_Isometric_05)

    CoV_80_list.append(CoV_Isometric_80)
    CoV_60_list.append(CoV_Isometric_60)
    CoV_40_list.append(CoV_Isometric_40)
    CoV_20_list.append(CoV_Isometric_20)
    CoV_05_list.append(CoV_Isometric_05)

    Isometric_80_freq_90_list.append(Isometric_80_freq_90)
    Isometric_60_freq_90_list.append(Isometric_60_freq_90)
    Isometric_40_freq_90_list.append(Isometric_40_freq_90)
    Isometric_20_freq_90_list.append(Isometric_20_freq_90)
    Isometric_05_freq_90_list.append(Isometric_05_freq_90)

    Isometric_80_freq_95_list.append(Isometric_80_freq_95)
    Isometric_60_freq_95_list.append(Isometric_60_freq_95)
    Isometric_40_freq_95_list.append(Isometric_40_freq_95)
    Isometric_20_freq_95_list.append(Isometric_20_freq_95)
    Isometric_05_freq_95_list.append(Isometric_05_freq_95)

    Isometric_80_freq_99_list.append(Isometric_80_freq_99)
    Isometric_60_freq_99_list.append(Isometric_60_freq_99)
    Isometric_40_freq_99_list.append(Isometric_40_freq_99)
    Isometric_20_freq_99_list.append(Isometric_20_freq_99)
    Isometric_05_freq_99_list.append(Isometric_05_freq_99)

    Adaptation_down_min_list.append(time_of_adaptation_down_min)
    Adaptation_down_max_list.append(time_of_adaptation_down_max)
    Adaptation_down_T1_list.append(time_of_adaptation_down_T1)
    Adaptation_down_T2_list.append(time_of_adaptation_down_T2)
    Adaptation_up_min_list.append(time_of_adaptation_up_min)
    Adaptation_up_max_list.append(time_of_adaptation_up_max)
    Adaptation_up_T1_list.append(time_of_adaptation_up_T1)
    Adaptation_up_T2_list.append(time_of_adaptation_up_T2)

    SaEn_Adaptation_down_min_list.append(SaEn_Pert_down_min)
    SaEn_Adaptation_down_max_list.append(SaEn_Pert_down_max)
    SaEn_Adaptation_down_T1_list.append(SaEn_Pert_down_T1)
    SaEn_Adaptation_down_T2_list.append(SaEn_Pert_down_T2)
    SaEn_Adaptation_up_min_list.append(SaEn_Pert_up_min)
    SaEn_Adaptation_up_max_list.append(SaEn_Pert_up_max)
    SaEn_Adaptation_up_T1_list.append(SaEn_Pert_up_T1)
    SaEn_Adaptation_up_T2_list.append(SaEn_Pert_up_T2)

# Creation of a dictionary with all the data for all participants
dist = {
    'ID': ID_list,
    'SaEn_80': SaEn_80_list,
    'SaEn_60': SaEn_60_list,
    'SaEn_40': SaEn_40_list,
    'SaEn_20': SaEn_20_list,
    'SaEn_05': SaEn_05_list,
    'sd_80': std_80_list,
    'sd_60': std_60_list,
    'sd_40': std_40_list,
    'sd_20': std_20_list,
    'sd_05': std_05_list,
    'CoV_80': CoV_80_list,
    'CoV_60': CoV_60_list,
    'CoV_40': CoV_40_list,
    'CoV_20': CoV_20_list,
    'CoV_05': CoV_05_list,
    'Freq_90_80': Isometric_80_freq_90_list,
    'Freq_90_60': Isometric_60_freq_90_list,
    'Freq_90_40': Isometric_40_freq_90_list,
    'Freq_90_20': Isometric_20_freq_90_list,
    'Freq_90_05': Isometric_05_freq_90_list,
    'Freq_95_80': Isometric_80_freq_95_list,
    'Freq_95_60': Isometric_60_freq_95_list,
    'Freq_95_40': Isometric_40_freq_95_list,
    'Freq_95_20': Isometric_20_freq_95_list,
    'Freq_95_05': Isometric_05_freq_95_list,
    'Freq_99_80': Isometric_80_freq_99_list,
    'Freq_99_60': Isometric_60_freq_99_list,
    'Freq_99_40': Isometric_40_freq_99_list,
    'Freq_99_20': Isometric_20_freq_99_list,
    'Freq_99_05': Isometric_05_freq_99_list,
    'Adaptation_down_min': Adaptation_down_min_list,
    'Adaptation_down_max': Adaptation_down_max_list,
    'Adaptation_down_T1': Adaptation_down_T1_list,
    'Adaptation_down_T2': Adaptation_down_T2_list,
    'Adaptation_up_min': Adaptation_up_min_list,
    'Adaptation_up_max': Adaptation_up_max_list,
    'Adaptation_up_T1': Adaptation_up_T1_list,
    'Adaptation_up_T2': Adaptation_up_T2_list,
    'SaEn_Adaptation_down_min': SaEn_Adaptation_down_min_list,
    'SaEn_Adaptation_down_max': SaEn_Adaptation_down_max_list,
    'SaEn_Adaptation_down_T1': SaEn_Adaptation_down_T1_list,
    'SaEn_Adaptation_down_T2': SaEn_Adaptation_down_T2_list,
    'SaEn_Adaptation_up_min': SaEn_Adaptation_up_min_list,
    'SaEn_Adaptation_up_max': SaEn_Adaptation_up_max_list,
    'SaEn_Adaptation_up_T1': SaEn_Adaptation_up_T1_list,
    'SaEn_Adaptation_up_T2': SaEn_Adaptation_up_T2_list,

}

new_excel = pd.DataFrame(dist)
os.chdir(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Results')
new_excel.to_excel(r'Results all Lowpass 50Hz only best iso trials all pert trials 3.xlsx')
