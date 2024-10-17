import Lib_grip as lb
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
from scipy.signal import decimate
import lib

directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Malvina 10-7-2024\Raw'
os.chdir(directory_path)

Isometric_80_T1_1000Hz = pd.read_csv(r'Isometric_80_T1.csv', skiprows=2)
Isometric_80_T2_1000Hz = pd.read_csv(r'Isometric_80_T2.csv', skiprows=2)
Isometric_80_T3_1000Hz = pd.read_csv(r'Isometric_80_T3.csv', skiprows=2)
Isometric_60_T1_1000Hz = pd.read_csv(r'Isometric_60_T1.csv', skiprows=2)
Isometric_60_T2_1000Hz = pd.read_csv(r'Isometric_60_T2.csv', skiprows=2)
Isometric_60_T3_1000Hz = pd.read_csv(r'Isometric_60_T3.csv', skiprows=2)
Isometric_40_T1_1000Hz = pd.read_csv(r'Isometric_40_T1.csv', skiprows=2)
Isometric_40_T2_1000Hz = pd.read_csv(r'Isometric_40_T2.csv', skiprows=2)
Isometric_40_T3_1000Hz = pd.read_csv(r'Isometric_40_T3.csv', skiprows=2)
Isometric_20_T1_1000Hz = pd.read_csv(r'Isometric_20_T1.csv', skiprows=2)
Isometric_20_T2_1000Hz = pd.read_csv(r'Isometric_20_T2.csv', skiprows=2)
Isometric_20_T3_1000Hz = pd.read_csv(r'Isometric_20_T2.csv', skiprows=2)
Isometric_5_T1_1000Hz = pd.read_csv(r'Isometric_5_T1.csv', skiprows=2)
Isometric_5_T2_1000Hz = pd.read_csv(r'Isometric_5_T2.csv', skiprows=2)
Isometric_5_T3_1000Hz = pd.read_csv(r'Isometric_5_T3.csv', skiprows=2)

list_of_names_1000Hz = [Isometric_80_T3_1000Hz, Isometric_60_T3_1000Hz, Isometric_40_T3_1000Hz, Isometric_20_T3_1000Hz, Isometric_5_T3_1000Hz]

directory_path_100Hz = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 8\Data\Stylianos 10-17-2024'
os.chdir(directory_path)
Isometric_80_T1_100Hz = pd.read_csv(r'Isometric_80_T1.csv', skiprows=2)
Isometric_60_T1_100Hz = pd.read_csv(r'Isometric_60_T1.csv', skiprows=2)
Isometric_40_T1_100Hz = pd.read_csv(r'Isometric_40_T1.csv', skiprows=2)
Isometric_20_T1_100Hz = pd.read_csv(r'Isometric_20_T1.csv', skiprows=2)
Isometric_5_T1_100Hz = pd.read_csv(r'Isometric_5_T1.csv', skiprows=2)
list_of_names_100Hz = [Isometric_80_T1_100Hz, Isometric_60_T1_100Hz, Isometric_40_T1_100Hz, Isometric_20_T1_100Hz, Isometric_5_T1_100Hz]



# SaEn_no_filter = []
# SaEn_with_filter = []

# for i in range(len(list_of_names_1000Hz)):
#     data = list_of_names_1000Hz[i]['Performance']
#
#
#     # fft_values = np.fft.fft(data)  # Perform FFT
#     # n = len(data)  # Number of data points
#     # sampling_rate = 1000  # Sampling rate in Hz (you can adjust this)
#     #
#     # frequencies = np.fft.fftfreq(n, d=1/sampling_rate)
#     # magnitude = np.abs(fft_values[:n//2])
#     # positive_frequencies = frequencies[:n//2]
#     #
#     # plt.plot(positive_frequencies, magnitude)
#     # plt.title(f"Frequency Spectrum {str(i)}")
#     # plt.xlabel("Frequency (Hz)")
#     # plt.ylabel("Magnitude")
#     # plt.xlim(0, 2)
#     # plt.grid(True)
#     # plt.show()
#
#
#
#     data1 = lib.Butterworth(1000, 30, data)
#
#     fft_values = np.fft.fft(data1)  # Perform FFT
#     n = len(data1)  # Number of data points
#     sampling_rate = 1000  # Sampling rate in Hz (you can adjust this)
#
#     frequencies = np.fft.fftfreq(n, d=1 / sampling_rate)
#     magnitude = np.abs(fft_values[:n // 2])
#     positive_frequencies = frequencies[:n // 2]
#
#     # plt.plot(positive_frequencies, magnitude)
#     # plt.title(f"Frequency Spectrum {str(i)}")
#     # plt.xlabel("Frequency (Hz)")
#     # plt.ylabel("Magnitude")
#     # plt.xlim(0, 2)
#     # plt.grid(True)
#     # plt.show()
#     #
#     # plt.plot(data, label='data')
#     # plt.plot(data1, label='data1')
#     # plt.legend()
#     # plt.show()
#
#     SaEn_data = lb.Ent_Samp(data,2,0.2)
#     SaEn_data1 = lb.Ent_Samp(data1, 2, 0.2)
#     SaEn_no_filter.append(SaEn_data)
#     SaEn_with_filter.append(SaEn_data1)
# list_perc_MVC = [80,60,40,20,5]
#
# plt.plot(list_perc_MVC, SaEn_no_filter, label='SaEn_no_filter')
# plt.plot(list_perc_MVC, SaEn_with_filter, label='SaEn_with_filter')
# plt.legend()
# plt.show()

def down_sampling(data, f_out, f_in):
    factor = int(f_in/f_out)
    data = np.asarray(data)
    downsampled_data = decimate(data, factor, ftype='fir')
    return downsampled_data



Iso_80_T1_1000Hz = Isometric_80_T1_1000Hz['Performance']
Iso_80_T2_1000Hz = Isometric_80_T2_1000Hz['Performance']
Iso_80_T3_1000Hz = Isometric_80_T3_1000Hz['Performance']
Iso_60_T1_1000Hz = Isometric_60_T1_1000Hz['Performance']
Iso_60_T2_1000Hz = Isometric_60_T2_1000Hz['Performance']
Iso_60_T3_1000Hz = Isometric_60_T3_1000Hz['Performance']
Iso_40_T1_1000Hz = Isometric_40_T1_1000Hz['Performance']
Iso_40_T2_1000Hz = Isometric_40_T2_1000Hz['Performance']
Iso_40_T3_1000Hz = Isometric_40_T3_1000Hz['Performance']
Iso_20_T1_1000Hz = Isometric_20_T1_1000Hz['Performance']
Iso_20_T2_1000Hz = Isometric_20_T2_1000Hz['Performance']
Iso_20_T3_1000Hz = Isometric_20_T3_1000Hz['Performance']
Iso_5_T1_1000Hz = Isometric_5_T1_1000Hz['Performance']
Iso_5_T2_1000Hz = Isometric_5_T2_1000Hz['Performance']
Iso_5_T3_1000Hz = Isometric_5_T3_1000Hz['Performance']

Iso_80_T1_100Hz = down_sampling(Iso_80_T1_1000Hz,100, 1000)
Iso_80_T2_100Hz = down_sampling(Iso_80_T2_1000Hz,100, 1000)
Iso_80_T3_100Hz = down_sampling(Iso_80_T3_1000Hz,100, 1000)
Iso_60_T1_100Hz = down_sampling(Iso_60_T1_1000Hz,100, 1000)
Iso_60_T2_100Hz = down_sampling(Iso_60_T2_1000Hz,100, 1000)
Iso_60_T3_100Hz = down_sampling(Iso_60_T3_1000Hz,100, 1000)
Iso_40_T1_100Hz = down_sampling(Iso_40_T1_1000Hz,100, 1000)
Iso_40_T2_100Hz = down_sampling(Iso_40_T2_1000Hz,100, 1000)
Iso_40_T3_100Hz = down_sampling(Iso_40_T3_1000Hz,100, 1000)
Iso_20_T1_100Hz = down_sampling(Iso_20_T1_1000Hz,100, 1000)
Iso_20_T2_100Hz = down_sampling(Iso_20_T2_1000Hz,100, 1000)
Iso_20_T3_100Hz = down_sampling(Iso_20_T3_1000Hz,100, 1000)
Iso_5_T1_100Hz = down_sampling(Iso_5_T1_1000Hz,100, 1000)
Iso_5_T2_100Hz = down_sampling(Iso_5_T2_1000Hz,100, 1000)
Iso_5_T3_100Hz = down_sampling(Iso_5_T3_1000Hz,100, 1000)

Iso_80_T1_50Hz = down_sampling(Iso_80_T1_1000Hz,50, 1000)
Iso_80_T2_50Hz = down_sampling(Iso_80_T2_1000Hz,50, 1000)
Iso_80_T3_50Hz = down_sampling(Iso_80_T3_1000Hz,50, 1000)
Iso_60_T1_50Hz = down_sampling(Iso_60_T1_1000Hz,50, 1000)
Iso_60_T2_50Hz = down_sampling(Iso_60_T2_1000Hz,50, 1000)
Iso_60_T3_50Hz = down_sampling(Iso_60_T3_1000Hz,50, 1000)
Iso_40_T1_50Hz = down_sampling(Iso_40_T1_1000Hz,50, 1000)
Iso_40_T2_50Hz = down_sampling(Iso_40_T2_1000Hz,50, 1000)
Iso_40_T3_50Hz = down_sampling(Iso_40_T3_1000Hz,50, 1000)
Iso_20_T1_50Hz = down_sampling(Iso_20_T1_1000Hz,50, 1000)
Iso_20_T2_50Hz = down_sampling(Iso_20_T2_1000Hz,50, 1000)
Iso_20_T3_50Hz = down_sampling(Iso_20_T3_1000Hz,50, 1000)
Iso_5_T1_50Hz = down_sampling(Iso_5_T1_1000Hz,50, 1000)
Iso_5_T2_50Hz = down_sampling(Iso_5_T2_1000Hz,50, 1000)
Iso_5_T3_50Hz = down_sampling(Iso_5_T3_1000Hz,50, 1000)



# Create time vectors based on the number of points
time_1000 = np.linspace(0, 10, len(Iso_80_T1_1000Hz))  # 10 seconds for 1000 points
time_10000 = np.linspace(0, 10, len(Iso_80_T1_100Hz))  # 10 seconds for 10000 points
time_5000 = np.linspace(0, 10, len(Iso_80_T1_50Hz))   # 10 seconds for 5000 points

# Create a figure and axis for the first dataset
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot the first dataset on the primary x-axis
line1, = ax1.plot(time_1000, Iso_80_T1_1000Hz, 'b-', label='Iso_80_T1_1000Hz')
ax1.set_xlabel('Time (s) - 1000 Points')
ax1.set_ylabel('Amplitude', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Create a secondary x-axis for the second dataset
ax2 = ax1.twiny()  # twiny() creates a new x-axis
line2, = ax2.plot(time_10000, Iso_80_T1_100Hz, 'r-', label='Iso_80_T1_100Hz')
ax2.spines['top'].set_position(('outward', 40))  # Move the secondary x-axis outward for better visibility
ax2.tick_params(axis='x', colors='none')  # Hide ticks of the second x-axis

# Create a third x-axis for the third dataset
ax3 = ax1.twiny()  # Another twiny() for the third x-axis
line3, = ax3.plot(time_5000, Iso_80_T1_50Hz, 'g-', label='Iso_80_T1_50Hz')
ax3.spines['top'].set_position(('outward', 80))  # Move this x-axis further outward
ax3.tick_params(axis='x', colors='none')  # Hide ticks of the third x-axis

# Hide the second and third x-axes completely (only the first axis will be visible)
ax2.xaxis.set_visible(False)
ax3.xaxis.set_visible(False)

lines = [line1, line2, line3]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='upper right')

# Set the title and show the plot
plt.title("Three Datasets with Different X-Axes (Only Primary Visible)")
plt.grid(True)
plt.show()




SaEn_1000Hz_T1 = []
SaEn_1000Hz_T1.append(lb.Ent_Samp(Iso_80_T1_1000Hz[2000:8000], 2, 0.2))
SaEn_1000Hz_T1.append(lb.Ent_Samp(Iso_60_T1_1000Hz[2000:8000], 2, 0.2))
SaEn_1000Hz_T1.append(lb.Ent_Samp(Iso_40_T1_1000Hz[2000:8000], 2, 0.2))
SaEn_1000Hz_T1.append(lb.Ent_Samp(Iso_20_T1_1000Hz[2000:8000], 2, 0.2))
SaEn_1000Hz_T1.append(lb.Ent_Samp(Iso_5_T1_1000Hz[2000:8000], 2, 0.2))
SaEn_1000Hz_T2 = []
SaEn_1000Hz_T2.append(lb.Ent_Samp(Iso_80_T2_1000Hz[2000:8000], 2, 0.2))
SaEn_1000Hz_T2.append(lb.Ent_Samp(Iso_60_T2_1000Hz[2000:8000], 2, 0.2))
SaEn_1000Hz_T2.append(lb.Ent_Samp(Iso_40_T2_1000Hz[2000:8000], 2, 0.2))
SaEn_1000Hz_T2.append(lb.Ent_Samp(Iso_20_T2_1000Hz[2000:8000], 2, 0.2))
SaEn_1000Hz_T2.append(lb.Ent_Samp(Iso_5_T2_1000Hz[2000:8000], 2, 0.2))
SaEn_1000Hz_T3 = []
SaEn_1000Hz_T3.append(lb.Ent_Samp(Iso_80_T3_1000Hz[2000:8000], 2, 0.2))
SaEn_1000Hz_T3.append(lb.Ent_Samp(Iso_60_T3_1000Hz[2000:8000], 2, 0.2))
SaEn_1000Hz_T3.append(lb.Ent_Samp(Iso_40_T3_1000Hz[2000:8000], 2, 0.2))
SaEn_1000Hz_T3.append(lb.Ent_Samp(Iso_20_T3_1000Hz[2000:8000], 2, 0.2))
SaEn_1000Hz_T3.append(lb.Ent_Samp(Iso_5_T3_1000Hz[2000:8000], 2, 0.2))

SaEn_100Hz_T1 = []
SaEn_100Hz_T1.append(lb.Ent_Samp(Iso_80_T1_100Hz[200:800], 2, 0.2))
SaEn_100Hz_T1.append(lb.Ent_Samp(Iso_60_T1_100Hz[200:800], 2, 0.2))
SaEn_100Hz_T1.append(lb.Ent_Samp(Iso_40_T1_100Hz[200:800], 2, 0.2))
SaEn_100Hz_T1.append(lb.Ent_Samp(Iso_20_T1_100Hz[200:800], 2, 0.2))
SaEn_100Hz_T1.append(lb.Ent_Samp(Iso_5_T1_100Hz[200:800], 2, 0.2))
SaEn_100Hz_T2 = []
SaEn_100Hz_T2.append(lb.Ent_Samp(Iso_80_T2_100Hz[200:800], 2, 0.2))
SaEn_100Hz_T2.append(lb.Ent_Samp(Iso_60_T2_100Hz[200:800], 2, 0.2))
SaEn_100Hz_T2.append(lb.Ent_Samp(Iso_40_T2_100Hz[200:800], 2, 0.2))
SaEn_100Hz_T2.append(lb.Ent_Samp(Iso_20_T2_100Hz[200:800], 2, 0.2))
SaEn_100Hz_T2.append(lb.Ent_Samp(Iso_5_T2_100Hz[200:800], 2, 0.2))
SaEn_100Hz_T3 = []
SaEn_100Hz_T3.append(lb.Ent_Samp(Iso_80_T3_100Hz[200:800], 2, 0.2))
SaEn_100Hz_T3.append(lb.Ent_Samp(Iso_60_T3_100Hz[200:800], 2, 0.2))
SaEn_100Hz_T3.append(lb.Ent_Samp(Iso_40_T3_100Hz[200:800], 2, 0.2))
SaEn_100Hz_T3.append(lb.Ent_Samp(Iso_20_T3_100Hz[200:800], 2, 0.2))
SaEn_100Hz_T3.append(lb.Ent_Samp(Iso_5_T3_100Hz[200:800], 2, 0.2))

SaEn_50Hz_T1 = []
SaEn_50Hz_T1.append(lb.Ent_Samp(Iso_80_T1_50Hz[100:400], 2, 0.2))
SaEn_50Hz_T1.append(lb.Ent_Samp(Iso_60_T1_50Hz[100:400], 2, 0.2))
SaEn_50Hz_T1.append(lb.Ent_Samp(Iso_40_T1_50Hz[100:400], 2, 0.2))
SaEn_50Hz_T1.append(lb.Ent_Samp(Iso_20_T1_50Hz[100:400], 2, 0.2))
SaEn_50Hz_T1.append(lb.Ent_Samp(Iso_5_T1_50Hz[100:400], 2, 0.2))
SaEn_50Hz_T2 = []
SaEn_50Hz_T2.append(lb.Ent_Samp(Iso_80_T2_50Hz[100:400], 2, 0.2))
SaEn_50Hz_T2.append(lb.Ent_Samp(Iso_60_T2_50Hz[100:400], 2, 0.2))
SaEn_50Hz_T2.append(lb.Ent_Samp(Iso_40_T2_50Hz[100:400], 2, 0.2))
SaEn_50Hz_T2.append(lb.Ent_Samp(Iso_20_T2_50Hz[100:400], 2, 0.2))
SaEn_50Hz_T2.append(lb.Ent_Samp(Iso_5_T2_50Hz[100:400], 2, 0.2))
SaEn_50Hz_T3 = []
SaEn_50Hz_T3.append(lb.Ent_Samp(Iso_80_T3_50Hz[100:400], 2, 0.2))
SaEn_50Hz_T3.append(lb.Ent_Samp(Iso_60_T3_50Hz[100:400], 2, 0.2))
SaEn_50Hz_T3.append(lb.Ent_Samp(Iso_40_T3_50Hz[100:400], 2, 0.2))
SaEn_50Hz_T3.append(lb.Ent_Samp(Iso_20_T3_50Hz[100:400], 2, 0.2))
SaEn_50Hz_T3.append(lb.Ent_Samp(Iso_5_T3_50Hz[100:400], 2, 0.2))

list_perc_MVC = [80,60,40,20,5]
plt.plot(list_perc_MVC, SaEn_1000Hz_T1, label='SaEn_1000Hz_T1')
plt.plot(list_perc_MVC, SaEn_1000Hz_T2, label='SaEn_1000Hz_T2')
plt.plot(list_perc_MVC, SaEn_1000Hz_T3, label='SaEn_1000Hz_T3')
plt.plot(list_perc_MVC, SaEn_100Hz_T1, label='SaEn_100Hz_T1')
plt.plot(list_perc_MVC, SaEn_100Hz_T2, label='SaEn_100Hz_T2')
plt.plot(list_perc_MVC, SaEn_100Hz_T3, label='SaEn_100Hz_T3')
plt.plot(list_perc_MVC, SaEn_50Hz_T1, label='SaEn_50Hz_T1')
plt.plot(list_perc_MVC, SaEn_50Hz_T2, label='SaEn_50Hz_T2')
plt.plot(list_perc_MVC, SaEn_50Hz_T3, label='SaEn_50Hz_T3')
plt.legend()
plt.show()

SeEn_average_1000Hz = [(a + b + c) / 3 for a, b, c in zip(SaEn_1000Hz_T1, SaEn_1000Hz_T2, SaEn_1000Hz_T3)]
SeEn_average_100Hz = [(a + b + c) / 3 for a, b, c in zip(SaEn_100Hz_T1, SaEn_100Hz_T2, SaEn_100Hz_T3)]
SeEn_average_50Hz = [(a + b + c) / 3 for a, b, c in zip(SaEn_50Hz_T1, SaEn_50Hz_T2, SaEn_50Hz_T3)]
plt.plot(list_perc_MVC, SeEn_average_1000Hz, label='SeEn_average_1000Hz')
plt.plot(list_perc_MVC, SeEn_average_100Hz, label='SeEn_average_100Hz')
plt.plot(list_perc_MVC, SeEn_average_50Hz, label='SeEn_average_50Hz')
plt.legend()
plt.show()