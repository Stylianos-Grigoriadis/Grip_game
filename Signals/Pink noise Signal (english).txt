import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Input Values
number_of_sets = 5                      # Total set each player will play
time_for_each_set =30                   # Total time of each set (seconds)
RM = 100                                # That is the Maximum force during the maximum force assessment (kg)
max_percentage= 90                      # That refers to the maximum value that the signal will have and is expressed as a percentage of the maximum force.
min_percentage = 50                     # That refers to the minimum value that the signal will have and is expressed as a percentage of the maximum force.
df = pd.read_excel(r"File Path\Pink Noise Signal.xlsx") # Import the file with pink training

# The following 11 lines alter our data to a format where they are expressed from the minimum to the maximum value we selected above (min_percentage, max_percentage)

diff_perc = max_percentage-min_percentage
for i in range(len(df[0])):
    df[0][i] = (df[0][i] * diff_perc / 100)
for i in range(len(df[0])):
    df[0][i] = df[0][i] + min_percentage
for i in range(len(df[0])):
    df[0][i] = df[0][i] *RM/100

plt.plot(df[0])
plt.show()

# The following 13 rows result in our data being expressed as percentages from 0 to 100%

min = np.min(df[0])
for i in range(len(df[0])):
    df[0][i] = df[0][i] *100/RM
max = np.max(df[0])
for i in range(len(df[0])):
    df[0][i] = df[0][i]- min_percentage

for i in range(len(df[0])):
    df[0][i] = (df[0][i] * 100 / diff_perc)

plt.plot(df[0])
plt.show()
