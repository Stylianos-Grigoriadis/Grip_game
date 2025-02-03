import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
from matplotlib.lines import Line2D


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 16


directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Pilot Study 10\Data\Results\Isometric'
os.chdir(directory)
Resuls_all = pd.read_excel(r'Results Isometrics all Lowpass 50.xlsx')
print(Resuls_all.columns)
print(Resuls_all)
SaEn_Iso_80 = Resuls_all['SaEn_80_Average'].to_numpy()
SaEn_Iso_60 = Resuls_all['SaEn_60_Average'].to_numpy()
SaEn_Iso_40 = Resuls_all['SaEn_40_Average'].to_numpy()
SaEn_Iso_20 = Resuls_all['SaEn_20_Average'].to_numpy()
SaEn_Iso_05 = Resuls_all['SaEn_05_Average'].to_numpy()
sd_Iso_80 = Resuls_all['sd_80_Average'].to_numpy()
sd_Iso_60 = Resuls_all['sd_60_Average'].to_numpy()
sd_Iso_40 = Resuls_all['sd_40_Average'].to_numpy()
sd_Iso_20 = Resuls_all['sd_20_Average'].to_numpy()
sd_Iso_05 = Resuls_all['sd_05_Average'].to_numpy()
CoV_Iso_80 = Resuls_all['CoV_80_Average'].to_numpy()
CoV_Iso_60 = Resuls_all['CoV_60_Average'].to_numpy()
CoV_Iso_40 = Resuls_all['CoV_40_Average'].to_numpy()
CoV_Iso_20 = Resuls_all['CoV_20_Average'].to_numpy()
CoV_Iso_05 = Resuls_all['CoV_05_Average'].to_numpy()
up_adaptation = Resuls_all['Adaptation_up_average'].to_numpy()
down_adaptation = Resuls_all['Adaptation_down_average'].to_numpy()
ID = Resuls_all['ID_no_numbers'].to_numpy()
colors = ['red' if age == "Old" else 'blue' for age in ID]
plt.scatter(up_adaptation, SaEn_Iso_20, c=colors, label="Old (red) / Young (blue)")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Scatter Plot with Age Group Colors")
legend_elements = [Line2D([0], [0], marker='o', color='w', label='Old', markersize=8, markerfacecolor='red'),
                   Line2D([0], [0], marker='o', color='w', label='Young', markersize=8, markerfacecolor='blue')]
plt.legend(handles=legend_elements)
plt.show()


