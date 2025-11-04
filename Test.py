import Lib_grip as lb
import lib
import colorednoise as cn
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 15


N=200
time = np.linspace(0,10,N)

brown = cn.powerlaw_psd_gaussian(3,N)
random = np.random.rand(N)
brown_random = brown
brown_z = lb.z_transform(brown_random,5,40)
pink = lb.fgn_sim(N,0.99)
pink_z = lb.z_transform(pink,2.5,40)

SaEn_brown = round(lb.Ent_Samp(brown_z, 2, 0.2),2)
SaEn_pink = round(lb.Ent_Samp(pink_z, 2, 0.2),2)
SD_brown = round(np.std(brown_z),2)
SD_pink = round(np.std(pink_z),2)

# plt.plot(brown_z, label=f'Signal 1, SaEn = {SaEn_brown}, SD = {SD_brown}')
# plt.plot(pink_z, label=f'Signal 2, SaEn = {SaEn_pink}, SD = {SD_pink}')
# plt.legend()
# plt.show()


plt.figure(figsize=(8, 4))
plt.plot(time, brown_z, color='red', linewidth=3, label=f'Signal 1, SaEn = {SaEn_brown}, SD = {SD_brown}')
plt.plot(time, pink_z, color='blue', linewidth=3, label=f'Signal 2, SaEn = {SaEn_pink}, SD = {SD_pink}')
plt.legend(prop={'weight': 'bold'})
# Styling
# plt.legend(
#     loc='upper right',
#     frameon=True,
#     fancybox=True,
#     shadow=True,
#     framealpha=0.9,
#     prop={'weight': 'bold'}  # <-- makes legend text bold
# )

plt.title('Signals Comparison', fontweight='bold')
plt.xlabel('Time (s)')
plt.ylabel('Force output (N)')

plt.tight_layout()
plt.show()

