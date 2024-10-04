import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import lib


Isometric_90 = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-7-2024\Isometric 90.csv', skiprows=2)
Isometric_70 = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-7-2024\Isometric 70.csv', skiprows=2)
Isometric_50 = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-7-2024\Isometric 50.csv', skiprows=2)
Isometric_40 = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-7-2024\Isometric 40.csv', skiprows=2)
Isometric_30 = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-7-2024\Isometric 30.csv', skiprows=2)
Isometric_15 = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-7-2024\Isometric 15.csv', skiprows=2)
Isometric_5 = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-7-2024\Isometric 5.csv', skiprows=2)
Isometric_2_half = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-7-2024\Isometric 2,5.csv', skiprows=2)
Perturbation_80 = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-7-2024\Perturbation 80.csv', skiprows=2)
Perturbation_65 = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-7-2024\Perturbation 65.csv', skiprows=2)
Perturbation_35 = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-7-2024\Perturbation 35.csv', skiprows=2)
Perturbation_20 = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-7-2024\Perturbation 20.csv', skiprows=2)
print(len(Isometric_90['Time']))
force_90 = np.array(list(Isometric_90['Performance'][375:825]))
force_70 = np.array(list(Isometric_70['Performance'][375:]))
force_50 = np.array(list(Isometric_50['Performance'][375:]))
force_40 = np.array(list(Isometric_40['Performance'][375:]))
force_30 = np.array(list(Isometric_30['Performance'][375:]))
force_15 = np.array(list(Isometric_15['Performance'][375:]))
force_5 = np.array(list(Isometric_5['Performance'][375:]))
force_2_half = np.array(list(Isometric_2_half['Performance'][375:]))

force_90_sd = np.std(force_90)
force_70_sd = np.std(force_70)
force_50_sd = np.std(force_50)
force_40_sd = np.std(force_40)
force_30_sd = np.std(force_30)
force_15_sd = np.std(force_15)
force_5_sd = np.std(force_5)
force_2_half_sd = np.std(force_2_half)

sd_list = [force_90_sd, force_70_sd, force_50_sd, force_40_sd, force_30_sd, force_15_sd, force_5_sd, force_2_half_sd]
print(sd_list)
plt.plot(sd_list)
plt.show()

force_90_Sa_Ent = lb.Ent_Samp(force_90, 2, 0.2)
force_70_Sa_Ent = lb.Ent_Samp(force_70, 2, 0.2)
force_50_Sa_Ent = lb.Ent_Samp(force_50, 2, 0.2)
force_40_Sa_Ent = lb.Ent_Samp(force_40, 2, 0.2)
force_30_Sa_Ent = lb.Ent_Samp(force_30, 2, 0.2)
force_15_Sa_Ent = lb.Ent_Samp(force_15, 2, 0.2)
force_5_Sa_Ent = lb.Ent_Samp(force_5, 2, 0.2)
force_2_half_Sa_Ent = lb.Ent_Samp(force_2_half, 2, 0.2)

Sa_Ent_list = [force_90_Sa_Ent, force_70_Sa_Ent, force_50_Sa_Ent, force_40_Sa_Ent, force_30_Sa_Ent, force_15_Sa_Ent, force_5_Sa_Ent, force_2_half_Sa_Ent]
print(Sa_Ent_list)
plt.plot(Sa_Ent_list)
plt.show()

force_90_Ap_Ent = lb.Ent_Ap(force_90, 2, 0.2)
force_70_Ap_Ent = lb.Ent_Ap(force_70, 2, 0.2)
force_50_Ap_Ent = lb.Ent_Ap(force_50, 2, 0.2)
force_40_Ap_Ent = lb.Ent_Ap(force_40, 2, 0.2)
force_30_Ap_Ent = lb.Ent_Ap(force_30, 2, 0.2)
force_15_Ap_Ent = lb.Ent_Ap(force_15, 2, 0.2)
force_5_Ap_Ent = lb.Ent_Ap(force_5, 2, 0.2)
force_2_half_Ap_Ent = lb.Ent_Ap(force_2_half, 2, 0.2)

Ap_Ent_list = [force_90_Ap_Ent, force_70_Ap_Ent, force_50_Ap_Ent, force_40_Ap_Ent, force_30_Ap_Ent, force_15_Ap_Ent, force_5_Ap_Ent, force_2_half_Ap_Ent]
print(Ap_Ent_list)
plt.plot(Sa_Ent_list)
plt.plot(Ap_Ent_list)
plt.show()
lb.isometric_min_max(49.8)



force_90_fft_90, force_90_fft_95, force_90_fft_99 = lib.FFT(force_90, 75)
force_70_fft_90, force_70_fft_95, force_70_fft_99 = lib.FFT(force_70, 75)
force_50_fft_90, force_50_fft_95, force_50_fft_99 = lib.FFT(force_50, 75)
force_40_fft_90, force_40_fft_95, force_40_fft_99 = lib.FFT(force_40, 75)
force_30_fft_90, force_30_fft_95, force_30_fft_99 = lib.FFT(force_30, 75)
force_15_fft_90, force_15_fft_95, force_15_fft_99 = lib.FFT(force_15, 75)
force_5_fft_90, force_5_fft_95, force_5_fft_99 = lib.FFT(force_5, 75)
force_2_half_Ap_E90, force_2_half_fft_90, f5rce_2_half_fft_99 = lib.FFT(force_2_half, 75)
print(force_90_fft_90, force_90_fft_95, force_90_fft_99)
print(force_70_fft_90, force_70_fft_95, force_70_fft_99)
print(force_50_fft_90, force_50_fft_95, force_50_fft_99)
print(force_40_fft_90, force_40_fft_95, force_40_fft_99)
print(force_30_fft_90, force_30_fft_95, force_30_fft_99)
print(force_15_fft_90, force_15_fft_95, force_15_fft_99)
print(force_5_fft_90, force_5_fft_95, force_5_fft_99)
print(force_2_half_Ap_E90, force_2_half_fft_90, f5rce_2_half_fft_99)



# plt.plot(Isometric_90['Time'],Isometric_90['Performance'], label = '90')
# plt.scatter(Isometric_90['Time'], Isometric_90['Target'], c='red')
# plt.legend()
# plt.show()

# plt.plot(Isometric_70['Time'],Isometric_70['Performance'], label = '70')
# plt.scatter(Isometric_70['Time'], Isometric_70['Target'], c='red')
# plt.legend()
# plt.show()
#
# plt.plot(Isometric_50['Time'],Isometric_50['Performance'], label = '50')
# plt.scatter(Isometric_50['Time'], Isometric_50['Target'], c='red')
# plt.legend()
# plt.show()
#
# plt.plot(Isometric_40['Time'],Isometric_40['Performance'], label = '40')
# plt.scatter(Isometric_40['Time'], Isometric_40['Target'], c='red')
# plt.legend()
# plt.show()
#
# plt.plot(Isometric_30['Time'],Isometric_30['Performance'], label = '30')
# plt.scatter(Isometric_30['Time'], Isometric_30['Target'], c='red')
# plt.legend()
# plt.show()
#
# plt.plot(Isometric_15['Time'],Isometric_15['Performance'], label = '15')
# plt.scatter(Isometric_15['Time'], Isometric_15['Target'], c='red')
# plt.legend()
# plt.show()
#
# plt.plot(Isometric_5['Time'],Isometric_5['Performance'], label = '5')
# plt.scatter(Isometric_5['Time'], Isometric_5['Target'], c='red')
# plt.legend()
# plt.show()
#
# plt.plot(Isometric_2_half['Time'],Isometric_2_half['Performance'], label = '2.5')
# plt.scatter(Isometric_2_half['Time'], Isometric_2_half['Target'], c='red')
# plt.legend()
# plt.show()
#
# plt.plot(Perturbation_80['Time'],Perturbation_80['Performance'], label = 'P80')
# plt.scatter(Perturbation_80['Time'], Perturbation_80['Target'], c='red')
# plt.legend()
# plt.show()
#
# plt.plot(Perturbation_65['Time'],Perturbation_65['Performance'], label = 'P65')
# plt.scatter(Perturbation_65['Time'], Perturbation_65['Target'], c='red')
# plt.legend()
# plt.show()
#
# plt.plot(Perturbation_35['Time'],Perturbation_35['Performance'], label = 'P35')
# plt.scatter(Perturbation_35['Time'], Perturbation_35['Target'], c='red')
# plt.legend()
# plt.show()
#
# plt.plot(Perturbation_20['Time'],Perturbation_20['Performance'], label = 'P20')
# plt.scatter(Perturbation_20['Time'], Perturbation_20['Target'], c='red')
# plt.legend()
# plt.show()



