import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




def read_kinvent(path):
    df = pd.read_csv(path, header=None, delimiter=';')
    index = []
    for i, string in enumerate(df[0]):
        if 'Repetition: ' in string:
            index.append(i)
    print(index)


    df_set_1 = pd.read_csv(path, skiprows=2, nrows=index[1]-index[0] - 3)
    df_set_2 = pd.read_csv(path, skiprows=index[1]+2, nrows=index[2]-index[1] -3)
    df_set_3 = pd.read_csv(path, skiprows=index[2]+2, nrows=index[3]-index[2] -3)
    df_set_4 = pd.read_csv(path, skiprows=index[3]+2, nrows=index[4]-index[3] -3)
    df_set_5 = pd.read_csv(path, skiprows=index[4]+2)
    return df_set_1,df_set_2,df_set_3,df_set_4,df_set_5

sets = read_kinvent(r'G:\My Drive\Εργαστήριον\Operation Doctora\Projects\Grip game\Pilot study 4\Pilot 1.csv')




for set in sets:

    target_list = []
    for i in range(len(set['Target'])):
        target_list.append(set['Target'][i])

    i = 0
    while i < len(target_list):
        if target_list[i] == '-':
            del target_list[i]
        else:
            target_list[i] = float(target_list[i])
            i += 1  # Only increment if we didn't remove an item

    fig, axs = plt.subplots(2, 1, figsize=(8, 6))
    axs[0].plot(target_list)
    axs[0].set_title('Targets')
    axs[1].plot(set['Performance'], color='red')
    axs[1].set_title('Performance')
    plt.draw()


sets = read_kinvent(r'G:\My Drive\Εργαστήριον\Operation Doctora\Projects\Grip game\Pilot study 4\Pilot 2.csv')
for set in sets:

    target_list = []
    for i in range(len(set['Target'])):
        target_list.append(set['Target'][i])

    i = 0
    while i < len(target_list):
        if target_list[i] == '-':
            del target_list[i]
        else:
            target_list[i] = float(target_list[i])
            i += 1  # Only increment if we didn't remove an item

    fig, axs = plt.subplots(2, 1, figsize=(8, 6))
    axs[0].plot(target_list)
    axs[0].set_title('Targets')
    axs[1].plot(set['Performance'], color='red')
    axs[1].set_title('Performance')
    plt.draw()
plt.show()


