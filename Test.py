import pandas as pd
from fathon import fathonUtils as fu
import fathon
import numpy as np
import matplotlib.pyplot as plt
import os
import Lib_grip as lb


directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 10\Data to test the new tablets'
os.chdir(directory)

big_tablet = pd.read_csv(r'Big tablet sine wave.csv', skiprows=2)
small_tablet = pd.read_csv(r'Small tablet sine wave.csv', skiprows=2)

print(big_tablet)
print(small_tablet)
print()
print(len(big_tablet['Performance']))
print(len(small_tablet['Performance']))

for index,i in enumerate(big_tablet['Target']):
    print(index)
    print(i)
print()
print()
print()
print()
print()
print()
print()

big_tablet_target = big_tablet['Target'].dropna().loc[big_tablet['Target'] != ''].tolist()
small_tablet_target = small_tablet['Target'].dropna().loc[small_tablet['Target'] != ''].tolist()



for index,i in enumerate(small_tablet['Target']):
    print(index)
    print(i)



fig, ax1 = plt.subplots()

ax1.plot(big_tablet['Performance'], label='big_tablet', c='orange')
ax1.plot(small_tablet['Performance'], label='small_tablet', c='lightblue')

ax2 = ax1.twiny()

ax2.plot(big_tablet_target, label='big_tablet_target', c='red')
ax2.plot(small_tablet_target, label='big_tablet_target', c='blue')

plt.show()