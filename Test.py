import pandas as pd
from fathon import fathonUtils as fu
import fathon
import numpy as np
import matplotlib.pyplot as plt
import os
import Lib_grip as lb


directory = r'C:\Users\Stylianos\Desktop\pilot grip training'
os.chdir(directory)


set_1, set_2, set_3, set_4, set_5, set_6, set_7, set_8, set_9, set_10 = lb.read_kinvent(r'grip_Damianou__Anestis___28Νοε24_13_29_45.csv')

print(set_1)

sync_set_1 = lb.synchronization_of_Time_and_ClosestSampleTime(set_1, 65)
sync_set_2 = lb.synchronization_of_Time_and_ClosestSampleTime(set_2, 65)
sync_set_3 = lb.synchronization_of_Time_and_ClosestSampleTime(set_3, 65)
sync_set_4 = lb.synchronization_of_Time_and_ClosestSampleTime(set_4, 65)
sync_set_5 = lb.synchronization_of_Time_and_ClosestSampleTime(set_5, 65)
sync_set_6 = lb.synchronization_of_Time_and_ClosestSampleTime(set_6, 65)
sync_set_7 = lb.synchronization_of_Time_and_ClosestSampleTime(set_7, 65)
sync_set_8 = lb.synchronization_of_Time_and_ClosestSampleTime(set_8, 65)
sync_set_9 = lb.synchronization_of_Time_and_ClosestSampleTime(set_9, 65)
print(sync_set_1)
list_sets = [sync_set_1, sync_set_2, sync_set_3, sync_set_4, sync_set_5, sync_set_6, sync_set_7, sync_set_8, sync_set_9]
for list in list_sets:
    plt.plot(list['Performance'], label='Performance')
    plt.plot(list['Target'], label='Target')
    plt.legend()
    plt.show()
