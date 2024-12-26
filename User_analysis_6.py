import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
from scipy.signal import decimate
import lib
import glob


directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Strength data\Old.1'
os.chdir(directory_path)
ID = os.path.basename(directory_path)
print(ID)

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

index = pd.read_excel('index.xlsx')


iso_80_T1_75Hz = Isometric_80_T1_75Hz['Performance'][index['T1_iso_80_75Hz'][0]:index['T1_iso_80_75Hz'][1]].to_numpy()
iso_80_T2_75Hz = Isometric_80_T2_75Hz['Performance'][index['T2_iso_80_75Hz'][0]:index['T2_iso_80_75Hz'][1]].to_numpy()
iso_60_T1_75Hz = Isometric_60_T1_75Hz['Performance'][index['T1_iso_60_75Hz'][0]:index['T1_iso_60_75Hz'][1]].to_numpy()
iso_60_T2_75Hz = Isometric_60_T2_75Hz['Performance'][index['T2_iso_60_75Hz'][0]:index['T2_iso_60_75Hz'][1]].to_numpy()
iso_40_T1_75Hz = Isometric_40_T1_75Hz['Performance'][index['T1_iso_40_75Hz'][0]:index['T1_iso_40_75Hz'][1]].to_numpy()
iso_40_T2_75Hz = Isometric_40_T2_75Hz['Performance'][index['T2_iso_40_75Hz'][0]:index['T2_iso_40_75Hz'][1]].to_numpy()
iso_20_T1_75Hz = Isometric_20_T1_75Hz['Performance'][index['T1_iso_20_75Hz'][0]:index['T1_iso_20_75Hz'][1]].to_numpy()
iso_20_T2_75Hz = Isometric_20_T2_75Hz['Performance'][index['T2_iso_20_75Hz'][0]:index['T2_iso_20_75Hz'][1]].to_numpy()
iso_05_T1_75Hz = Isometric_05_T1_75Hz['Performance'][index['T1_iso_05_75Hz'][0]:index['T1_iso_05_75Hz'][1]].to_numpy()
iso_05_T2_75Hz = Isometric_05_T2_75Hz['Performance'][index['T2_iso_05_75Hz'][0]:index['T2_iso_05_75Hz'][1]].to_numpy()



def index_to_500(array):

    excess_length_array = len(array) - 500
    if excess_length_array > 0:
        remove_each_side = excess_length_array//2
        array = array[remove_each_side : len(array)-remove_each_side]

    elif excess_length_array == 0:
        pass
    else:
        raise ValueError("Length is less than 500 points")

    return array

iso_80_T1_75Hz = index_to_500(iso_80_T1_75Hz)
iso_80_T2_75Hz = index_to_500(iso_80_T2_75Hz)
iso_60_T1_75Hz = index_to_500(iso_60_T1_75Hz)
iso_60_T2_75Hz = index_to_500(iso_60_T2_75Hz)
iso_40_T1_75Hz = index_to_500(iso_40_T1_75Hz)
iso_40_T2_75Hz = index_to_500(iso_40_T2_75Hz)
iso_20_T1_75Hz = index_to_500(iso_20_T1_75Hz)
iso_20_T2_75Hz = index_to_500(iso_20_T2_75Hz)
iso_05_T1_75Hz = index_to_500(iso_05_T1_75Hz)
iso_05_T2_75Hz = index_to_500(iso_05_T2_75Hz)

print(f'iso_80_T1_75Hz: {len(iso_80_T1_75Hz)}')
print(f'iso_80_T1_75Hz: {len(iso_80_T1_75Hz)}')
print(f'iso_60_T1_75Hz: {len(iso_60_T1_75Hz)}')
print(f'iso_60_T1_75Hz: {len(iso_60_T1_75Hz)}')
print(f'iso_40_T1_75Hz: {len(iso_40_T1_75Hz)}')
print(f'iso_40_T1_75Hz: {len(iso_40_T1_75Hz)}')
print(f'iso_20_T1_75Hz: {len(iso_20_T1_75Hz)}')
print(f'iso_20_T1_75Hz: {len(iso_20_T1_75Hz)}')
print(f'iso_05_T1_75Hz: {len(iso_05_T1_75Hz)}')
print(f'iso_05_T1_75Hz: {len(iso_05_T1_75Hz)}')




plt.plot(iso_80_T1_75Hz, label='iso_80_T1')
plt.plot(iso_80_T2_75Hz, label='iso_80_T2')
plt.plot(iso_60_T1_75Hz, label='iso_60_T1')
plt.plot(iso_60_T2_75Hz, label='iso_60_T2')
plt.plot(iso_40_T1_75Hz, label='iso_40_T1')
plt.plot(iso_40_T2_75Hz, label='iso_40_T2')
plt.plot(iso_20_T1_75Hz, label='iso_20_T1')
plt.plot(iso_20_T2_75Hz, label='iso_20_T2')
plt.plot(iso_05_T1_75Hz, label='iso_05_T1')
plt.plot(iso_05_T2_75Hz, label='iso_05_T2')
plt.legend()
plt.show()


std_iso_80_T1_75Hz = np.std(iso_80_T1_75Hz)
std_iso_80_T2_75Hz = np.std(iso_80_T2_75Hz)
std_iso_60_T1_75Hz = np.std(iso_60_T1_75Hz)
std_iso_60_T2_75Hz = np.std(iso_60_T2_75Hz)
std_iso_40_T1_75Hz = np.std(iso_40_T1_75Hz)
std_iso_40_T2_75Hz = np.std(iso_40_T2_75Hz)
std_iso_20_T1_75Hz = np.std(iso_20_T1_75Hz)
std_iso_20_T2_75Hz = np.std(iso_20_T2_75Hz)
std_iso_05_T1_75Hz = np.std(iso_05_T1_75Hz)
std_iso_05_T2_75Hz = np.std(iso_05_T2_75Hz)

CoV_iso_80_T1_75Hz = (np.std(iso_80_T1_75Hz)/np.mean(iso_80_T1_75Hz))*100
CoV_iso_80_T2_75Hz = (np.std(iso_80_T2_75Hz)/np.mean(iso_80_T2_75Hz))*100
CoV_iso_60_T1_75Hz = (np.std(iso_60_T1_75Hz)/np.mean(iso_60_T1_75Hz))*100
CoV_iso_60_T2_75Hz = (np.std(iso_60_T2_75Hz)/np.mean(iso_60_T2_75Hz))*100
CoV_iso_40_T1_75Hz = (np.std(iso_40_T1_75Hz)/np.mean(iso_40_T1_75Hz))*100
CoV_iso_40_T2_75Hz = (np.std(iso_40_T2_75Hz)/np.mean(iso_40_T2_75Hz))*100
CoV_iso_20_T1_75Hz = (np.std(iso_20_T1_75Hz)/np.mean(iso_20_T1_75Hz))*100
CoV_iso_20_T2_75Hz = (np.std(iso_20_T2_75Hz)/np.mean(iso_20_T2_75Hz))*100
CoV_iso_05_T1_75Hz = (np.std(iso_05_T1_75Hz)/np.mean(iso_05_T1_75Hz))*100
CoV_iso_05_T2_75Hz = (np.std(iso_05_T2_75Hz)/np.mean(iso_05_T2_75Hz))*100

SaEn_iso_80_T1_75Hz = lb.Ent_Samp(iso_80_T1_75Hz, 2, 0.2)
SaEn_iso_80_T2_75Hz = lb.Ent_Samp(iso_80_T2_75Hz, 2, 0.2)
SaEn_iso_60_T1_75Hz = lb.Ent_Samp(iso_60_T1_75Hz, 2, 0.2)
SaEn_iso_60_T2_75Hz = lb.Ent_Samp(iso_60_T2_75Hz, 2, 0.2)
SaEn_iso_40_T1_75Hz = lb.Ent_Samp(iso_40_T1_75Hz, 2, 0.2)
SaEn_iso_40_T2_75Hz = lb.Ent_Samp(iso_40_T2_75Hz, 2, 0.2)
SaEn_iso_20_T1_75Hz = lb.Ent_Samp(iso_20_T1_75Hz, 2, 0.2)
SaEn_iso_20_T2_75Hz = lb.Ent_Samp(iso_20_T2_75Hz, 2, 0.2)
SaEn_iso_05_T1_75Hz = lb.Ent_Samp(iso_05_T1_75Hz, 2, 0.2)
SaEn_iso_05_T2_75Hz = lb.Ent_Samp(iso_05_T2_75Hz, 2, 0.2)

DFA_iso_80_T1_75Hz = lb.DFA(iso_80_T1_75Hz)
DFA_iso_80_T2_75Hz = lb.DFA(iso_80_T2_75Hz)
DFA_iso_60_T1_75Hz = lb.DFA(iso_60_T1_75Hz)
DFA_iso_60_T2_75Hz = lb.DFA(iso_60_T2_75Hz)
DFA_iso_40_T1_75Hz = lb.DFA(iso_40_T1_75Hz)
DFA_iso_40_T2_75Hz = lb.DFA(iso_40_T2_75Hz)
DFA_iso_20_T1_75Hz = lb.DFA(iso_20_T1_75Hz)
DFA_iso_20_T2_75Hz = lb.DFA(iso_20_T2_75Hz)
DFA_iso_05_T1_75Hz = lb.DFA(iso_05_T1_75Hz)
DFA_iso_05_T2_75Hz = lb.DFA(iso_05_T2_75Hz)

SaEn_T1 = [SaEn_iso_80_T1_75Hz, SaEn_iso_60_T1_75Hz, SaEn_iso_40_T1_75Hz, SaEn_iso_20_T1_75Hz, SaEn_iso_05_T1_75Hz]
SaEn_T2 = [SaEn_iso_80_T2_75Hz, SaEn_iso_60_T2_75Hz, SaEn_iso_40_T2_75Hz, SaEn_iso_20_T2_75Hz, SaEn_iso_05_T2_75Hz]
average_SaEn = [np.mean((SaEn_iso_80_T1_75Hz, SaEn_iso_80_T2_75Hz)),
                np.mean((SaEn_iso_60_T1_75Hz, SaEn_iso_60_T2_75Hz)),
                np.mean((SaEn_iso_40_T1_75Hz, SaEn_iso_40_T2_75Hz)),
                np.mean((SaEn_iso_20_T1_75Hz, SaEn_iso_20_T2_75Hz)),
                np.mean((SaEn_iso_05_T1_75Hz, SaEn_iso_05_T2_75Hz))]

std_T1 = [std_iso_80_T1_75Hz, std_iso_60_T1_75Hz, std_iso_40_T1_75Hz, std_iso_20_T1_75Hz, std_iso_05_T1_75Hz]
std_T2 = [std_iso_80_T2_75Hz, std_iso_60_T2_75Hz, std_iso_40_T2_75Hz, std_iso_20_T2_75Hz, std_iso_05_T2_75Hz]

average_std = [np.mean((std_iso_80_T1_75Hz, std_iso_80_T2_75Hz)),
                np.mean((std_iso_60_T1_75Hz, std_iso_60_T2_75Hz)),
                np.mean((std_iso_40_T1_75Hz, std_iso_40_T2_75Hz)),
                np.mean((std_iso_20_T1_75Hz, std_iso_20_T2_75Hz)),
                np.mean((std_iso_05_T1_75Hz, std_iso_05_T2_75Hz))]

CoV_T1 = [CoV_iso_80_T1_75Hz, CoV_iso_60_T1_75Hz, CoV_iso_40_T1_75Hz, CoV_iso_20_T1_75Hz, CoV_iso_05_T1_75Hz]
CoV_T2 = [CoV_iso_80_T2_75Hz, CoV_iso_60_T2_75Hz, CoV_iso_40_T2_75Hz, CoV_iso_20_T2_75Hz, CoV_iso_05_T2_75Hz]

average_CoV = [np.mean((CoV_iso_80_T1_75Hz, CoV_iso_80_T2_75Hz)),
                np.mean((CoV_iso_60_T1_75Hz, CoV_iso_60_T2_75Hz)),
                np.mean((CoV_iso_40_T1_75Hz, CoV_iso_40_T2_75Hz)),
                np.mean((CoV_iso_20_T1_75Hz, CoV_iso_20_T2_75Hz)),
                np.mean((CoV_iso_05_T1_75Hz, CoV_iso_05_T2_75Hz))]

DFA_T1 = [DFA_iso_80_T1_75Hz, DFA_iso_60_T1_75Hz, DFA_iso_40_T1_75Hz, DFA_iso_20_T1_75Hz, DFA_iso_05_T1_75Hz]
DFA_T2 = [DFA_iso_80_T2_75Hz, DFA_iso_60_T2_75Hz, DFA_iso_40_T2_75Hz, DFA_iso_20_T2_75Hz, DFA_iso_05_T2_75Hz]

average_DFA = [np.mean((DFA_iso_80_T1_75Hz, DFA_iso_80_T2_75Hz)),
                np.mean((DFA_iso_60_T1_75Hz, DFA_iso_60_T2_75Hz)),
                np.mean((DFA_iso_40_T1_75Hz, DFA_iso_40_T2_75Hz)),
                np.mean((DFA_iso_20_T1_75Hz, DFA_iso_20_T2_75Hz)),
                np.mean((DFA_iso_05_T1_75Hz, DFA_iso_05_T2_75Hz))]


Percentage_iso = [80,60,40,20,5]


plt.plot(Percentage_iso, SaEn_T1, label='T1')
plt.plot(Percentage_iso, SaEn_T2, label='T2')
plt.plot(Percentage_iso, average_SaEn, label='average_SaEn', lw=4)
plt.legend()
plt.show()

plt.plot(Percentage_iso, std_T1, label='T1')
plt.plot(Percentage_iso, std_T2, label='T2')
plt.plot(Percentage_iso, average_std, label='average_std', lw=4)
plt.legend()
plt.show()

plt.plot(Percentage_iso, CoV_T1, label='T1')
plt.plot(Percentage_iso, CoV_T2, label='T2')
plt.plot(Percentage_iso, average_CoV, label='average_CoV', lw=4)
plt.legend()
plt.show()

plt.plot(Percentage_iso, DFA_T1, label='T1')
plt.plot(Percentage_iso, DFA_T2, label='T2')
plt.plot(Percentage_iso, average_DFA, label='average_DFA', lw=4)
plt.legend()
plt.show()


excel = {'Isometrics': (80, 60, 40, 20, 5),
            'SaEn_T1': SaEn_T1,
            'SaEn_T2': SaEn_T2,
            'SaEn_Average': average_SaEn,
            'std_T1': std_T1,
            'std_T2': std_T2,
            'std_Average': average_std,
            'CoV_T1': CoV_T1,
            'CoV_T2': CoV_T2,
            'CoV_Average': average_CoV,
            'DFA_T1': DFA_T1,
            'DFA_T2': DFA_T2,
            'DFA_Average': average_DFA
         }

df_excel = pd.DataFrame(excel)
print(df_excel)
df_excel.to_excel(rf'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Results\Isometric\{ID}.xlsx')