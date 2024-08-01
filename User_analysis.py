import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import Lib_grip as lb



# path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data'
# df1 = pd.read_csv(rf'{path}\Isometric Test of constant 40%.csv', skiprows=2 )
# df2 = pd.read_csv(rf'{path}\Isometric Test of constant 40% 2.csv', skiprows=2 )
# df3 = pd.read_csv(rf'{path}\Isometric Test of constant 40% 3.csv', skiprows=2 )
# df4 = pd.read_csv(rf'{path}\Isometric Test of constant 40% 4.csv', skiprows=2)
# df5 = pd.read_csv(rf'{path}\Isometric Test of constant 40% 5.csv', skiprows=2)
# df6 = pd.read_csv(rf'{path}\Isometric Test of constant 40% 6.csv', skiprows=2)
#
#
#
#
# my_signal = lb.read_my_txt_file(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Signals\Isometric Test of constant 40%.txt')
# my_signal = my_signal + 0.1
# my_signal = my_signal*10/100
#
# my_signal_time = np.arange(0, len(my_signal), 1)
# removed_0_df1 = lb.isolate_Target(df1)
# removed_0_df2 = lb.isolate_Target(df2)
# removed_0_df3 = lb.isolate_Target(df3)
# removed_0_df4 = lb.isolate_Target(df4)
# removed_0_df5 = lb.isolate_Target(df5)
# removed_0_df6 = lb.isolate_Target(df6)
#
# np_time1 = np.arange(0, len(removed_0_df1['Target']), 1)
# np_time2 = np.arange(0, len(removed_0_df2['Target']), 1)
# np_time3 = np.arange(0, len(removed_0_df3['Target']), 1)
# np_time4 = np.arange(0, len(removed_0_df4['Target']), 1)
# np_time5 = np.arange(0, len(removed_0_df5['Target']), 1)
# np_time6 = np.arange(0, len(removed_0_df6['Target']), 1)
#
#
# plt.scatter(np_time1, removed_0_df1['Target'], label='1', lw=3)
# plt.scatter(np_time2, removed_0_df2['Target'], c='red', label='2', lw=3)
# plt.scatter(np_time3, removed_0_df3['Target'], c='k', label='3', lw=3)
# plt.scatter(np_time4, removed_0_df4['Target'], c='yellow', label='4')
# plt.scatter(np_time5, removed_0_df5['Target'], c='purple', label='5')
# plt.scatter(np_time6, removed_0_df6['Target'], c='green', label='6')
# plt.scatter(my_signal_time, my_signal, c='pink', label='my_signal')
# plt.legend()
# plt.show()

# df = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-7-2024\Perturbation 20.csv', skiprows=2)
# print(df)
# plt.plot(df['Time'], df['Performance'])
# plt.scatter(df['Time'], df['Target'])
# plt.show()

# df_no_zeros = lb.isolate_Target(df)
# plt.plot(df_no_zeros['Time'], df_no_zeros['Performance'])
# plt.scatter(df_no_zeros['Time'], df_no_zeros['Target'])
# plt.show()

# my_signal = lb.read_my_txt_file(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Signals\Perturbation N200 B50 P20.txt')
# print(my_signal)
# my_signal = lb.Perc(my_signal,26.5,12.7)
# print(len(my_signal))
# print(len(df_no_zeros['Time'][:-1]))
# df_no_zeros = lb.isolate_Target(df)
# plt.plot(df_no_zeros['Time'], df_no_zeros['Performance'])
# plt.scatter(df_no_zeros['Time'], df_no_zeros['Target'], lw=5)
# plt.scatter(df_no_zeros['Time'], my_signal[1:], c='red')
# plt.show()
kinvent_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Loizides 1-8-2024\Perturbation 20.csv'
signal_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Signals\Perturbation N200 B50 P20.txt'
# Vasilis max = 50.3
# Loizides max = 47.8
df1 = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Loizides 1-8-2024\Perturbation 20.csv', skiprows=2)
df2 = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-7-2024\Perturbation 20.csv', skiprows=2)
df3 = pd.read_csv(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Vasilis 1-8-2024\Perturbation 20.csv', skiprows=2)
print(len(df1['Time']))
print(len(df2['Time']))
print(len(df3['Time']))

index1 = lb.isolate_Target(df1)
index2 = lb.isolate_Target(df2)
index3 = lb.isolate_Target(df3)
print(index1[1])
print(index2[1])
print(index3[1])

# df_with_my_signal = lb.add_generated_signal(kinvent_path, signal_path, 19.5, 0.2*47.8)
#
# plt.plot(df_with_my_signal['Time'], df_with_my_signal['Performance'])
# plt.scatter(df_with_my_signal['Time'], df_with_my_signal['Target'], lw=5)
# plt.scatter(df_with_my_signal['Time'], df_with_my_signal['Signal'], c='red')
#
# plt.show()

# spatial_error = lb.spatial_error(df_with_my_signal)
# plt.plot(spatial_error)
# plt.axvline(x=99)
# plt.axvline(x=99+18)
# plt.show()
# max_spatial_error = max(spatial_error)
# max_index = spatial_error.index(max_spatial_error)
# plt.plot(spatial_error[99:])
#
# plt.show()
# mean_baseline = np.mean(spatial_error[50:98])
# sd_baseline = np.std(spatial_error[50:98])
# asymptotes = lb.asymptotes(df_with_my_signal)
# print(asymptotes)