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
sine_signal = lb.sine_signal_generator(650,0.2,100,0)
plt.plot(sine_signal)
plt.show()
lb.create_txt_file(sine_signal,'Sine signal N650 freq0.2 Max100', r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip training\Pilot study 1\Signals')


# Create an isometric signal
# isom_signal = lb.isometric_generator_single_rep(1000,50)
# plt.plot(isom_signal)
# plt.show()
# lb.create_txt_file(isom_signal,'Isom signal 1 N1000 F50', r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Signals')

# Create a perturbation signal
# pert = lb.perturbation_both_force(60,80,40,50,20,35,70,50,45, 120)
# print(len(pert))
# plt.plot(pert)
# plt.show()
# lb.create_txt_file(pert,'Perturbation N117', r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 5\Signals')

# Create a single perturbation 30-45
# pert = lb.single_perturbation_generator(50, 75,800)
# plt.plot(pert)
# plt.ylim(0, 100)
# plt.show()
# lb.create_txt_file(pert,'Single Perturbation N800 bas30 pert45', r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Signals\Final used')

# Create a single perturbation 30-15
# pert = lb.single_perturbation_generator(50, 25, 1000)
# plt.plot(pert)
# plt.ylim(0, 100)
# plt.show()
# lb.create_txt_file(pert,'Single Perturbation N1000 bas30 pert15,', r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip game\Pilot Study 6\Signals\Final used')
