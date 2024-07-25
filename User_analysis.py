import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import Lib_grip as lb



path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data'
df1 = pd.read_csv(rf'{path}\Isometric Test of constant 40%.csv', skiprows=2 )
df2 = pd.read_csv(rf'{path}\Isometric Test of constant 40% 2.csv', skiprows=2 )
df3 = pd.read_csv(rf'{path}\Isometric Test of constant 40% 3.csv', skiprows=2 )
df4 = pd.read_csv(rf'{path}\Isometric Test of constant 40% 4.csv', skiprows=2)
df5 = pd.read_csv(rf'{path}\Isometric Test of constant 40% 5.csv', skiprows=2)
df6 = pd.read_csv(rf'{path}\Isometric Test of constant 40% 6.csv', skiprows=2)




my_signal = lb.read_my_txt_file(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Signals\Isometric Test of constant 40%.txt')
my_signal = my_signal + 0.1
my_signal = my_signal*10/100

my_signal_time = np.arange(0, len(my_signal), 1)
removed_0_df1 = lb.isolate_Target(df1)
removed_0_df2 = lb.isolate_Target(df2)
removed_0_df3 = lb.isolate_Target(df3)
removed_0_df4 = lb.isolate_Target(df4)
removed_0_df5 = lb.isolate_Target(df5)
removed_0_df6 = lb.isolate_Target(df6)

np_time1 = np.arange(0, len(removed_0_df1['Target']), 1)
np_time2 = np.arange(0, len(removed_0_df2['Target']), 1)
np_time3 = np.arange(0, len(removed_0_df3['Target']), 1)
np_time4 = np.arange(0, len(removed_0_df4['Target']), 1)
np_time5 = np.arange(0, len(removed_0_df5['Target']), 1)
np_time6 = np.arange(0, len(removed_0_df6['Target']), 1)


plt.scatter(np_time1, removed_0_df1['Target'], label='1', lw=3)
plt.scatter(np_time2, removed_0_df2['Target'], c='red', label='2', lw=3)
plt.scatter(np_time3, removed_0_df3['Target'], c='k', label='3', lw=3)
plt.scatter(np_time4, removed_0_df4['Target'], c='yellow', label='4')
plt.scatter(np_time5, removed_0_df5['Target'], c='purple', label='5')
plt.scatter(np_time6, removed_0_df6['Target'], c='green', label='6')
plt.scatter(my_signal_time, my_signal, c='pink', label='my_signal')
plt.legend()
plt.show()
