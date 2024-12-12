import matplotlib.pyplot as plt
import pandas as pd
import os
import glob
import numpy as np
import Lib_grip as lb
from scipy.stats import linregress


def calculation_slope_intercept(split_spatial_error):
    list_slope = []
    list_intercept = []
    for sub_array in split_spatial_error:
        print(sub_array)
        # X values (index of elements in sub-array)
        x = np.arange(len(sub_array))  # Indices of the sub-array elements (0 to 49)

        # Y values (sub-array itself)
        y = sub_array

        # Calculate linear regression
        slope, intercept, _, _, _ = linregress(x, y)
        print(slope)
        list_slope.append(slope)
        list_intercept.append(intercept)

    return list_slope, list_intercept

# directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game Paper 1\Pilot Study 10\Data\Strength data'
# files = glob.glob(os.path.join(directory_path, "*"))
directory_path = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game Paper 1\Pilot Study 10\Data\Strength data\Old.4'
os.chdir(directory_path)
pd.set_option('display.max_rows', None)  # Allow printing all rows
pd.set_option('display.max_columns', None)

warm_up_1 = pd.read_csv(r'Warm_up_1.csv', skiprows=2)
warm_up_2 = pd.read_csv(r'Warm_up_2.csv', skiprows=2)
warm_up_3 = pd.read_csv(r'Warm_up_3.csv', skiprows=2)


warm_up_1_noNaN = lb.synchronization_of_Time_and_ClosestSampleTime(warm_up_1, 500, 30)
warm_up_2_noNaN = lb.synchronization_of_Time_and_ClosestSampleTime(warm_up_2, 500, 30)
warm_up_3_noNaN = lb.synchronization_of_Time_and_ClosestSampleTime(warm_up_3, 500, 30)

spatial_error_warm_up_1 = lb.spatial_error(warm_up_1_noNaN)
spatial_error_warm_up_2 = lb.spatial_error(warm_up_2_noNaN)
spatial_error_warm_up_3 = lb.spatial_error(warm_up_3_noNaN)

array = np.arange(0, 501, 62.5)

time = np.arange(0,500,1)
plt.scatter(time, warm_up_1_noNaN['Target'], label= 'Target')
plt.legend()
plt.show()


#
# fig, ax = plt.subplots(3,2)
# ax[0, 0].plot(warm_up_1_noNaN['Performance'], label='Performance', c='red')
# ax[0, 0].plot(warm_up_1_noNaN['Target'], label='Target', c='k')
# for value in array:
#     ax[0, 0].axvline(x=value, color='b', linestyle='--')
#
# ax[1, 0].plot(warm_up_2_noNaN['Performance'], label='Performance', c='red')
# ax[1, 0].plot(warm_up_2_noNaN['Target'], label='Target', c='k')
# for value in array:
#     ax[1, 0].axvline(x=value, color='b', linestyle='--')
#
# ax[2, 0].plot(warm_up_3_noNaN['Performance'], label='Performance', c='red')
# ax[2, 0].plot(warm_up_3_noNaN['Target'], label='Target', c='k')
# for value in array:
#     ax[2, 0].axvline(x=value, color='b', linestyle='--')
#
# ax[0, 1].plot(spatial_error_warm_up_1)
# ax[1, 1].plot(spatial_error_warm_up_2)
# ax[2, 1].plot(spatial_error_warm_up_3)
#
# ax[0,0].legend()
#
# plt.tight_layout()
# plt.show()

split_spatial_error_warm_up_1 = np.array_split(spatial_error_warm_up_1, 10)
split_spatial_error_warm_up_2 = np.array_split(spatial_error_warm_up_2, 10)
split_spatial_error_warm_up_3 = np.array_split(spatial_error_warm_up_3, 10)

slope_warm_up_1, intercept_warm_up_1 = calculation_slope_intercept(split_spatial_error_warm_up_1)
slope_warm_up_2, intercept_warm_up_2 = calculation_slope_intercept(split_spatial_error_warm_up_2)
slope_warm_up_3, intercept_warm_up_3 = calculation_slope_intercept(split_spatial_error_warm_up_3)

slopwarm_up_all = slope_warm_up_1 + slope_warm_up_2 + slope_warm_up_3



plt.plot(slope_warm_up_1, label='slope_warm_up_1')
plt.plot(slope_warm_up_2, label='slope_warm_up_2')
plt.plot(slope_warm_up_3, label='slope_warm_up_3')
plt.legend()
plt.show()

plt.plot(slopwarm_up_all)
plt.show()

