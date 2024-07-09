import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({'font.size':16})

def sine(Number_of_targets,frequency, Total_Time):

    x = np.arange(0, Number_of_targets)
    y = np.sin(x)
    y = y*frequency
    y = y - np.min(y)
    y = y*100/np.max(y)
    time = np.arange(0, Total_Time, Total_Time/Number_of_targets)
    plt.scatter(time,y)
    plt.plot(time, y, c = 'red', ls='--')
    plt.ylabel('% of 1 RM')
    plt.xlabel('Time')
    plt.show()
    y = list(y)
    print(type(y))
    return time,y

signal = sine(Number_of_targets=500,
     frequency=1,
     Total_Time=60)

df = pd.DataFrame(signal[1])
df.rename(columns={0: 'Signal'}, inplace=True)

print(df)
df.to_excel('Sine Signal.xlsx', index=False)