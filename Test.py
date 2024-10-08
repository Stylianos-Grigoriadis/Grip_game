import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import Lib_grip
import Lib_grip as lb
#
#
#
#
# def read_kinvent(path):
#     df = pd.read_csv(path, header=None, delimiter=';')
#     index = []
#     for i, string in enumerate(df[0]):
#         if 'Repetition: ' in string:
#             index.append(i)
#     print(index)
#
#     df_set_1 = pd.read_csv(path, skiprows=2, nrows=index[1]-index[0] - 3)
#     df_set_2 = pd.read_csv(path, skiprows=index[1]+2, nrows=index[2]-index[1] -3)
#     df_set_3 = pd.read_csv(path, skiprows=index[2]+2, nrows=index[3]-index[2] -3)
#     df_set_4 = pd.read_csv(path, skiprows=index[3]+2, nrows=index[4]-index[3] -3)
#     df_set_5 = pd.read_csv(path, skiprows=index[4]+2)
#     return df_set_1,df_set_2,df_set_3,df_set_4,df_set_5
#
# sets = read_kinvent(r'G:\My Drive\Εργαστήριον\Operation Doctora\Projects\Grip game\Pilot study 4\Pilot 1.csv')
#
#
#
#
# for set in sets:
#
#     target_list = []
#     for i in range(len(set['Target'])):
#         target_list.append(set['Target'][i])
#
#     i = 0
#     while i < len(target_list):
#         if target_list[i] == '-':
#             del target_list[i]
#         else:
#             target_list[i] = float(target_list[i])
#             i += 1  # Only increment if we didn't remove an item
#
#     fig, axs = plt.subplots(2, 1, figsize=(8, 6))
#     axs[0].plot(target_list)
#     axs[0].set_title('Targets')
#     axs[1].plot(set['Performance'], color='red')
#     axs[1].set_title('Performance')
#     plt.draw()
#
#
# sets = read_kinvent(r'G:\My Drive\Εργαστήριον\Operation Doctora\Projects\Grip game\Pilot study 4\Pilot 2.csv')
# for set in sets:
#
#     target_list = []
#     for i in range(len(set['Target'])):
#         target_list.append(set['Target'][i])
#
#     i = 0
#     while i < len(target_list):
#         if target_list[i] == '-':
#             del target_list[i]
#         else:
#             target_list[i] = float(target_list[i])
#             i += 1  # Only increment if we didn't remove an item
#
#     fig, axs = plt.subplots(2, 1, figsize=(8, 6))
#     axs[0].plot(target_list)
#     axs[0].set_title('Targets')
#     axs[1].plot(set['Performance'], color='red')
#     axs[1].set_title('Performance')
#     plt.draw()
# plt.show()
#
#
# 50.00000667,92.07396798,95.46532329,57.05607618,12.1595113,2.053323352,36.02909493,82.84965833,99.46840349,70.60613275,22.79868472,6.6478406,23.17109801,71.00856427,99.53085956,82.51471712,35.60469985,1.92966128,12.45027657,57.49394055,95.64771628,91.83319831,49.55743687,7.688572068,4.720645109,43.38235435,88.12830262,97.81927143,63.54542875,16.81798748,0.597941627,29.79792655,77.57161077,99.99608933,76.45440007,28.59066351,0.410578324,17.82278486,64.81858074,98.19024796,87.25602958,42.06879555,4.173480454,8.410862219,50.88511159,92.54559958,95.08986566,56.17872332,11.58689739,2.31190698,36.8811355,83.51179367,99.33186942,69.79645806,22.06028059,0.011758423,23.92220116,71.80845802,99.64412528,81.83721884,34.75932635,1.693645062,13.04060986,58.36787364,96.00175912,91.34184554,48.67243597,7.223588774,5.103182921,44.26070977,88.69491972,97.55320506,62.69129911,16.16107741,0.742211221,30.610735,78.30566574,99.97650406,75.69918117,27.79415575,0.305087267,18.5052985,65.66159918,98.41870393,86.65988172,41.19613945,3.826632103,8.908712395,51.76993914,93.00389814,94.70027764,55.29943416,11.02632149,2.585435233,37.7372873,84.163427,99.17987561,68.98057952,21.33063229,0.03917565,24.68147665,72.60151739,99.74183341,81.14974332,33.91872901,1.472767223,13.64252558,59.23918439,96.3413858,90.83753696,47.7878511,6.772010869,5.499790621,45.14086379,89.24941051,97.27223635,61.83319223,15.51477188,0.901917356,31.42961972,79.03085021,99.94125703,74.93590859,27.00460692,0.215169738,19.19768204,66.49970955,98.63198633,86.05224529,40.32624232,3.494253688,9.419439872,52.65421202,93.44872001,94.29668133,54.41848425,10.47795926,2.873822393,38.59728202,84.8043541,99.01246967,68.15875278,20.60996847,0.082249737,25.44868652,73.38749383,99.8239533,80.45250601,33.08317127,1.26709698,14.25583511,60.10759973,96.66648991,90.3204306,46.90395949,6.333979871,5.91034392,46.02254057,89.79160121,96.97645334,60.97137704,14.87927342,1.077009984,32.25432408,79.74693691,99.89035926,74.16482152,26.22226445,0.140853916,19.89971849,67.3326492,98.8300283,85.43331071,39.45937679,3.176449373,9.942884596,53.53765312,93.87992582,93.87920321,53.53614967,9.941982559,3.176978084,39.46085016,85.43437412,98.82970407,67.33123542,19.89851498,0.140967186,26.22359036,74.16614103,99.89045923,79.74572542,32.25291497,1.076698789,14.88034625,60.97284754,96.97696954,89.79068852,46.02103812,5.90963305,6.334714156,46.90546383,90.32132192,96.66594872,60.10612361,14.2547812,1.267434232,33.08458963,80.45370144,99.82382673,73.38616163,25.44737351,0.08216309,20.61118785,68.1601571,99.01276779,84.80327195,38.59581451,2.87331875,10.47888253,54.41998558,94.29738041,93.44797411,52.65270691,9.418559352,3.494807303,40.32772108,86.05328963,98.63163609,66.49828674,19.19649478,0.215309596,27.00594531,74.93721499,99.94133035,79.02962303,31.42822031,0.901632317,15.51586328,61.83465664,97.2727274,89.24847673,45.13936369,5.49910339,6.77276834,47.78935686,90.83840662,96.3408198,59.2377031,13.64149091,1.473130426,33.92015617,81.15092231,99.74168027,72.60017292,24.68017694,0.039115653,21.33186716,68.98197392,99.18014753,84.16232644,37.7358261,2.584956816,11.0272657,55.3009329,94.70095297,93.00312916,51.76843285,8.907853667,3.827210446,41.19762314,86.66090665,98.4183278,65.66016779,18.50412787,0.305253669,27.7955062,75.70047406,99.97655073,78.30442327,30.60934572,0.741952425,16.16218704,62.69275697,97.55367081,88.69396515,44.2592125,5.102519543,7.224369193,48.67394267,91.34269327,96.00116848,58.36638766,13.03959475,1.694034103,34.76076186,81.83838102,99.64394563,71.8071017,23.92091517,0.011725095,22.06153056,69.79784212,99.33211507,83.51067506,36.87968108,2.311453939,11.58786225,56.180219,95.09051703,92.54480778,50.8836046,8.410025553,4.174083346,42.07028371,87.25703479,98.18984604,64.81714121,17.82163122,0.410771218,28.5920256,76.45567905,99.99610932,77.57035339,29.79654783,0.597709157,16.81911499,63.54687961,97.81971173,88.12732754,43.38086038,4.720005793,7.68937519,49.55894405,91.83402384,95.64710118,57.49245034,12.44928134,1.930076037,35.60614327,82.51586214,99.53065344,71.00719652,23.16982614,0,22.79994941,70.60750602,99.46862277,82.84852201,36.02764774,2.052895829,12.16049651,57.05756833,95.4659505,92.0731536,49.99849944,7.92523102,4.535317297,42.94542931,87.84148722,97.94626242,63.9694712,17.14921872,0.531829176,29.39525389,77.20259329,100,76.82764343,28.99008135,0.468947713,17.48644126,64.3967569,98.07076677,87.5487415,42.50458259,4.351682011,8.167640608,50.44408364,92.31224436,95.27872888,56.61616501,11.87073568,2.181182256,36.45603547,83.18315334,99.4018392,70.20070806,22.42714522,0.003944042,23.54689228,71.41071189,99.58962787,82.17607481,35.17999309,1.809363515,12.74498901,57.93270593,95.82713574,91.58831442,49.11339475,7.453621993,4.910799095,43.8227857,88.41408078,97.68765328,63.11742341,16.48710108,0.668389604,30.20493935,77.9409827,99.98822155,76.07652617,28.19019902,0.355708447,18.16395671,65.24212249,98.30675728,86.95838833,41.63065373,3.997663625,8.659015566,51.32908407,92.77720495,94.896167,55.7378063,11.30413908,2.447274067,37.31017211,83.84004553,99.25754328,69.38788904,21.69310516,0.023555986,24.3021251,72.20720801,99.69509243,81.49354418,34.33698278,1.580933315,13.34115659,58.80535757,96.17395954,91.09044218,48.22856791,6.995346268,5.300411072,44.70207793,88.97463604,97.41409965,62.26126484,15.83548581,0.820409709,31.02082825,78.6706159,99.96077765,75.31723697,27.39715151,0.258026845,18.85144904,66.08271147,98.52760928,86.35645304,40.75934768,3.658061577,9.163346075,52.213668,93.2287599,94.49953545,54.85764945,10.74966909,2.728268082,38.16828553,84.48633283,99.0978109,68.56899419,20.96793599,0.058829685,25.06541119,72.99674478,99.78498342,80.80114402,33.49888099,1.367676814,13.94881242,59.67524977,96.50631323,90.57969291,47.34429621,6.55054746,5.704031128,45.58303043,89.52297732,97.12568726,61.4012638,15.19457712,0.987841849,31.84266489,79.39126422,99.91767691,74.55001379


#
# import numpy as np
#
# # Example: Create a numpy array with 500 values ranging from 0 to 100
# np.random.seed(42)  # For reproducibility
# array = np.random.rand(500) * 100
#
# # Step 1: Find the minimum and maximum values of the original array
# min_val = array.min()
# max_val = array.max()
# plt.plot(array)
# plt.show()
# # Step 2: Normalize the array values to a 0-1 range
# normalized_array = (array - min_val) / (max_val - min_val)
# plt.plot(normalized_array)
# plt.show()
# # Step 3: Loop through values from 1 to 20 and scale the array
# for min_target in range(10, 21):
#     max_target = 80
#     new_range = max_target - min_target
#
#     # Step 4: Scale the normalized values to the new desired range (min_target to max_target)
#     scaled_array = normalized_array * new_range + min_target
#     plt.plot(scaled_array)
#     plt.show()
#     print(f"Scaled array with min_target = {min_target}:\n", scaled_array, "\n")
#
#
# # Create some data
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
#
# # Create the plot
# plt.plot(x, y, label='sin(x)')
#
# # Fill the area between the plot and the x-axis
# # plt.fill_between(x, y, color='skyblue', alpha=0.4)
#
# # Add labels and title
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Filling Between Plot and X-Axis')
# plt.legend()
#
# # Show the plot
# plt.show()


# path_sine = (r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Data\Sine signal 3 N350 freq0.5 Max60 Min40.csv')
# # set_1_sine,set_2_sine,set_3_sine,set_4_sine,set_5_sine = lb.read_kinvent(path_sine)
# df= lb.read_kinvent(path_sine)
# print(df)
#
# Lib_grip.isometric_min_max(49.6)
data_5perc_1,data_5perc_2,data_5perc_3 = lb.read_kinvent(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-9-2024\Raw data\Isometric_5%.csv')
data_5perc_1_targets, index_1 = lb.isolate_Target(data_5perc_1)
data_5perc_2_targets, index_2 = lb.isolate_Target(data_5perc_2)
data_5perc_3_targets, index_3 = lb.isolate_Target(data_5perc_3)
plt.plot(data_5perc_1_targets['Target'], label='Target 1')
plt.plot(data_5perc_2_targets['Target'], label='Target 2')
plt.plot(data_5perc_3_targets['Target'], label='Target 3')
plt.title('5% of MVC')
plt.legend()
plt.show()

data_20perc_1,data_20perc_2,data_20perc_3 = lb.read_kinvent(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-9-2024\Raw data\Isometric_20%.csv')
data_20perc_1_targets, index_1 = lb.isolate_Target(data_20perc_1)
data_20perc_2_targets, index_2 = lb.isolate_Target(data_20perc_2)
data_20perc_3_targets, index_3 = lb.isolate_Target(data_20perc_3)
plt.plot(data_20perc_1_targets['Target'], label='Target 1')
plt.plot(data_20perc_2_targets['Target'], label='Target 2')
plt.plot(data_20perc_3_targets['Target'], label='Target 3')
plt.title('20% of MVC')
plt.legend()
plt.show()

data_40perc_1,data_40perc_2,data_40perc_3 = lb.read_kinvent(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-9-2024\Raw data\Isometric_40%.csv')
data_40perc_1_targets, index_1 = lb.isolate_Target(data_40perc_1)
data_40perc_2_targets, index_2 = lb.isolate_Target(data_40perc_2)
data_40perc_3_targets, index_3 = lb.isolate_Target(data_40perc_3)
plt.plot(data_40perc_1_targets['Target'], label='Target 1')
plt.plot(data_40perc_2_targets['Target'], label='Target 2')
plt.plot(data_40perc_3_targets['Target'], label='Target 3')
plt.title('40% of MVC')
plt.legend()
plt.show()

data_60perc_1,data_60perc_2,data_60perc_3 = lb.read_kinvent(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-9-2024\Raw data\Isometric_60%.csv')
data_60perc_1_targets, index_1 = lb.isolate_Target(data_60perc_1)
data_60perc_2_targets, index_2 = lb.isolate_Target(data_60perc_2)
data_60perc_3_targets, index_3 = lb.isolate_Target(data_60perc_3)
plt.plot(data_60perc_1_targets['Target'], label='Target 1')
plt.plot(data_60perc_2_targets['Target'], label='Target 2')
plt.plot(data_60perc_3_targets['Target'], label='Target 3')
plt.title('60% of MVC')
plt.legend()
plt.show()

data_80perc_1,data_80perc_2,data_80perc_3 = lb.read_kinvent(r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Data\Stylianos 30-9-2024\Raw data\Isometric_80%.csv')
data_80perc_1_targets, index_1 = lb.isolate_Target(data_80perc_1)
data_80perc_2_targets, index_2 = lb.isolate_Target(data_80perc_2)
data_80perc_3_targets, index_3 = lb.isolate_Target(data_80perc_3)
plt.plot(data_80perc_1_targets['Target'], label='Target 1')
plt.plot(data_80perc_2_targets['Target'], label='Target 2')
plt.plot(data_80perc_3_targets['Target'], label='Target 3')
plt.title('80% of MVC')
plt.legend()
plt.show()