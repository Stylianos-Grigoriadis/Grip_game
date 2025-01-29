import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import glob
import statistics
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

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
    'CoV_05_Average': CoV_05_list_Average
}

new_excel = pd.DataFrame(dist)
os.chdir(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Results\Isometric')
new_excel.to_excel(r'results Isometrics all 2.xlsx')
