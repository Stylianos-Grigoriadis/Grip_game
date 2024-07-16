import pandas as pd
import matplotlib.pyplot as plt

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

df_set_1,df_set_2,df_set_3,df_set_4,df_set_5 = read_kinvent(r"C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Data\grip_strength_Grig_Styl___16Jul24_13_35_28.csv")
print(df_set_1)
print(df_set_2)
print(df_set_3)
print(df_set_4)
print(df_set_5)

plt.plot(df_set_1['Time'], df_set_1['Performance'], label='Performance')
plt.plot(df_set_1['Time'], df_set_1['Target'], label='Target')
plt.legend()
plt.show()

plt.plot(df_set_2['Time'], df_set_2['Performance'], label='Performance')
plt.plot(df_set_2['Time'], df_set_2['Target'], label='Target')
plt.legend()
plt.show()

plt.plot(df_set_3['Time'], df_set_3['Performance'], label='Performance')
plt.plot(df_set_3['Time'], df_set_3['Target'], label='Target')
plt.legend()
plt.show()

plt.plot(df_set_4['Time'], df_set_4['Performance'], label='Performance')
plt.plot(df_set_4['Time'], df_set_4['Target'], label='Target')
plt.legend()
plt.show()

plt.plot(df_set_5['Time'], df_set_5['Performance'], label='Performance')
plt.plot(df_set_5['Time'], df_set_5['Target'], label='Target')
plt.legend()
plt.show()


# for i in range(0,1,2,3,4):
#     plt.plot(df[i]['Time'], df[i]['Performance'], label='Performance')
#     plt.plot(df[i]['Time'], df[i]['Target'], label='Target')
#     plt.legend()
#     plt.show()