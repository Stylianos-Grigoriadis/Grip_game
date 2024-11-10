import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import colorednoise as cn
import Lib_grip as lb



def outputs(white, pink, sine):
    white_average = np.mean(white)
    pink_average = np.mean(pink)
    sine_average = np.mean(sine)
    list_average = [white_average, pink_average, sine_average]

    white_std = np.std(white)
    pink_std = np.std(pink)
    sine_std = np.std(sine)
    list_std = [white_std, pink_std, sine_std]

    white_total_load = np.cumsum(white)[-1]
    pink_total_load = np.cumsum(pink)[-1]
    sine_total_load = np.cumsum(sine)[-1]
    list_total_load = [white_total_load, pink_total_load, sine_total_load]

    dist = {'Signals': ['White', 'Pink', 'Sine'],
            'Average' : list_average,
            'std' : list_std,
            'Total_load' : list_total_load}
    df = pd.DataFrame(dist)
    print(df)



num_points = 1000
frequency = 0.5  # frequency of sine wave in Hz
sampling_rate = 100  # sampling rate in Hz
t = np.linspace(0, num_points / sampling_rate, num_points)  # time vector


white_noise = np.random.normal(0, 1, num_points)
pink_noise  = cn.powerlaw_psd_gaussian(1, num_points)
sine_wave = np.sin(2 * np.pi * frequency * t)

white_noise_0_1 = lb.Perc(white_noise,1,0)
pink_noise_0_1 = lb.Perc(pink_noise,1,0)
sine_wave_0_1 = lb.Perc(sine_wave,1,0)



std_white = np.std(white_noise_0_1)
std_pink = np.std(pink_noise_0_1)
std_sine = np.std(sine_wave_0_1)
desired_std = 2
white_noise_0_1_std = white_noise_0_1 * desired_std/std_white
pink_noise_0_1_std = pink_noise_0_1 * desired_std/std_pink
sine_wave_0_1_std = sine_wave_0_1 * desired_std/std_sine

average_white = np.mean(white_noise_0_1_std)
average_pink = np.mean(pink_noise_0_1_std)
average_sine = np.mean(sine_wave_0_1_std)

white_noise_0_1_std2 = white_noise_0_1_std + 10 - average_white
pink_noise_0_1_std2 = pink_noise_0_1_std + 10 - average_pink
sine_wave_0_1_std2 = sine_wave_0_1_std + 10 - average_sine


print('***Before conversion')
outputs(white_noise_0_1, pink_noise_0_1, sine_wave_0_1)
print('***After conversion')
outputs(white_noise_0_1_std2, pink_noise_0_1_std2, sine_wave_0_1_std2)

plt.plot(white_noise_0_1_std2, label='white_noise', c='grey')
plt.plot(pink_noise_0_1_std2, label='pink_noise', c='pink')
plt.plot(sine_wave_0_1_std2, label='sine_wave', c='red')
plt.legend()
plt.show()






