import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.animation as animation

def make_it_random(up_1, up_2, up_3, down_1, down_2, down_3):
    list1 = [up_1, up_2, up_3, down_1, down_2, down_3]
    random.shuffle(list1)
    return list1


def perturbation_both_force(up_1, up_2, up_3, down_1, down_2, down_3, step_1, step_2, step_3, data_num):
    baseline = np.zeros(data_num)
    pert_up_1 = np.full(data_num, up_1)
    pert_up_2 = np.full(data_num, up_2)
    pert_up_3 = np.full(data_num, up_3)
    pert_down_1 = np.full(data_num, down_1)
    pert_down_2 = np.full(data_num, down_2)
    pert_down_3 = np.full(data_num, down_3)
    pert_step_1 = np.full(int(data_num/10), step_1)
    pert_step_2 = np.full(int(data_num/10), step_2)
    pert_step_3 = np.full(int(data_num/10), step_3)
    pert_down_whole_1 = np.concatenate((pert_step_1, pert_down_1))
    pert_down_whole_2 = np.concatenate((pert_step_2, pert_down_2))
    pert_down_whole_3 = np.concatenate((pert_step_3, pert_down_3))

    overall_list = make_it_random(pert_up_1, pert_up_2, pert_up_3, pert_down_whole_1, pert_down_whole_2, pert_down_whole_3)

    final_pert = np.concatenate((baseline, overall_list[0], baseline, overall_list[1], baseline, overall_list[2], baseline, overall_list[3], baseline, overall_list[4],
                                 baseline, overall_list[5]))
    return final_pert




def perturbation_plus_force(a, b, c, d, data_num, num_from_base_1,num_from_base_2,num_from_base_3,num_from_base_4):
    # Create separately the signals
    baseline = np.zeros(data_num)
    pert_a = np.full(data_num, a)
    pert_b = np.full(data_num, b)
    pert_c = np.full(data_num, c)
    pert_d = np.full(data_num, d)

    base_to_1 = np.linspace(0, num_from_base_1, data_num)
    base_to_2 = np.linspace(0, num_from_base_2, data_num)
    base_to_3 = np.linspace(0, num_from_base_3, data_num)
    base_to_4 = np.linspace(0, num_from_base_4, data_num)

    # pert_a_to_baseline = np.linspace(a, 0, data_num)
    # pert_b_to_baseline = np.linspace(b, 0, data_num)
    # pert_c_to_baseline = np.linspace(c, 0, data_num)
    # pert_d_to_baseline = np.linspace(d, 0, data_num)

    # Create one signal
    final_pert = np.concatenate((baseline, base_to_1, pert_a, baseline, base_to_2, pert_b, baseline, base_to_3, pert_c, baseline, base_to_4, pert_d))
    return final_pert
size = 50
# Pert_1 = perturbation_plus_force(30,100,70,50,size,30,65,20,80)
# Pert_2 = perturbation_plus_force(70,100,30,50,size,30,65,20,80)
# Pert_3 = perturbation_plus_force(100,50,30,70,size,30,65,20,80)
# Pert_4 = perturbation_plus_force(30,50,70,100,size,30,65,20,80)

Pert_1 = perturbation_both_force(30,60,100,50,40,20,70,80,70,data_num=size)
Pert_2 = perturbation_both_force(30,60,100,50,40,20,70,80,70,data_num=size)
Pert_3 = perturbation_both_force(30,60,100,50,40,20,70,80,70,data_num=size)
Pert_4 = perturbation_both_force(30,60,100,50,40,20,70,80,70,data_num=size)
y = np.arange(0,615,1)
for i in Pert_1:
    print(i)
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
# print(len(y))
# print(len(Pert_1))
# size_scatter = 10
# ax1.scatter(y, Pert_1,s=size_scatter)
# ax1.plot(y, Pert_1, color = "pink")
# ax1.set_title('Pert_1')
#
# ax2.scatter(y, Pert_2,s=size_scatter)
# ax2.plot(y, Pert_2, color = "pink")
# ax2.set_title('Pert_2')
#
# ax3.scatter(y, Pert_3,s=size_scatter)
# ax3.plot(y, Pert_3, color = "pink")
# ax3.set_title('Pert_3')
#
# ax4.scatter(y, Pert_4,s=size_scatter)
# ax4.plot(y, Pert_4, color = "pink")
# ax4.set_title('Pert_4')
#
# plt.tight_layout()
#
#
# plt.show()

plt.scatter(y, Pert_1)
plt.ylabel("Force (% of 1RM)", fontsize=20)
plt.plot(y, Pert_1, '--')
plt.title("Example of a perturbation", fontsize = 20)

plt.show()

# fig, ax = plt.subplots()
# ax.plot(y,Pert_1)
# line, = ax.plot([], [], 'r-', lw=2)  # Initial line (will be updated)
#
# def init():
#     line.set_data([], [])
#     return line,
#
# def animate(i):
#     # Update the line to follow the y-value of the data
#     line.set_data([Pert_1[i], Pert_1[i]], [-1, 1])
#     return line,
#
# ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(Pert_1), interval=50, blit=True)
#
# plt.show()


