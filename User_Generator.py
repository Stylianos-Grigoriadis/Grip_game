import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import Lib_grip as lb




# Create a pink signal
# pink_signal = lb.pink_signal_generator(350 ,100,0)
# plt.plot(pink_signal)
# plt.show()
# lb.create_txt_file(pink_signal,'Pink signal N350 Max100 Min0', r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Signals')


# Create a sine signal
# sine_signal = lb.sine_signal_generator(350 ,0.5 ,60 ,40)
# lb.create_txt_file(sine_signal,'Sine signal 3 N350 freq0.5 Max60 Min40', r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Signals')


# Create an isometric signal
# isom_signal = lb.isometric_generator(400,50)
# lb.create_txt_file(isom_signal,'Isom signal 1 N40 0 V50', r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Signals')

# Create a perturbation signal
pert = lb.perturbation_both_force(60,80,40,50,20,35,70,50,45, 120)
print(len(pert))
plt.plot(pert)
plt.show()
# lb.create_txt_file(pert,'Perturbation N117', r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Signals')
