import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import glob
import matplotlib.patches as mpatches
import matplotlib.lines as mlines


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 16

directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Data collection\Results'
os.chdir(directory)
results = pd.read_excel(r'Results all Lowpass 50Hz only best iso trials all pert trials.xlsx')

SaEn_80_Old = results[results['ID_group'] == 'Old']['SaEn_80'].to_numpy()
SaEn_60_Old = results[results['ID_group'] == 'Old']['SaEn_60'].to_numpy()
SaEn_40_Old = results[results['ID_group'] == 'Old']['SaEn_40'].to_numpy()
SaEn_20_Old = results[results['ID_group'] == 'Old']['SaEn_20'].to_numpy()
SaEn_05_Old = results[results['ID_group'] == 'Old']['SaEn_05'].to_numpy()

SaEn_80_Young = results[results['ID_group'] == 'Young']['SaEn_80'].to_numpy()
SaEn_60_Young = results[results['ID_group'] == 'Young']['SaEn_60'].to_numpy()
SaEn_40_Young = results[results['ID_group'] == 'Young']['SaEn_40'].to_numpy()
SaEn_20_Young = results[results['ID_group'] == 'Young']['SaEn_20'].to_numpy()
SaEn_05_Young = results[results['ID_group'] == 'Young']['SaEn_05'].to_numpy()

sd_80_Old = results[results['ID_group'] == 'Old']['sd_80'].dropna().to_numpy()
sd_60_Old = results[results['ID_group'] == 'Old']['sd_60'].dropna().to_numpy()
sd_40_Old = results[results['ID_group'] == 'Old']['sd_40'].to_numpy()
sd_20_Old = results[results['ID_group'] == 'Old']['sd_20'].to_numpy()
sd_05_Old = results[results['ID_group'] == 'Old']['sd_05'].to_numpy()

sd_80_Young = results[results['ID_group'] == 'Young']['sd_80'].to_numpy()
sd_60_Young = results[results['ID_group'] == 'Young']['sd_60'].to_numpy()
sd_40_Young = results[results['ID_group'] == 'Young']['sd_40'].to_numpy()
sd_20_Young = results[results['ID_group'] == 'Young']['sd_20'].to_numpy()
sd_05_Young = results[results['ID_group'] == 'Young']['sd_05'].to_numpy()

Pert_down_Old = results[results['ID_group'] == 'Old']['Adaptation_down_min'].to_numpy()
Pert_up_Old = results[results['ID_group'] == 'Old']['Adaptation_up_min'].to_numpy()

Pert_down_Young = results[results['ID_group'] == 'Young']['Adaptation_down_min'].to_numpy()
Pert_up_Young = results[results['ID_group'] == 'Young']['Adaptation_up_min'].to_numpy()


old_SaEn = [SaEn_05_Old, SaEn_20_Old, SaEn_40_Old, SaEn_60_Old, SaEn_80_Old]
young_SaEn = [SaEn_05_Young, SaEn_20_Young, SaEn_40_Young, SaEn_60_Young, SaEn_80_Young]

old_sd = [sd_05_Old, sd_20_Old, sd_40_Old, sd_60_Old, sd_80_Old]
young_sd = [sd_05_Young, sd_20_Young, sd_40_Young, sd_60_Young, sd_80_Young]

old_time_of_adaptation = [Pert_down_Old, Pert_up_Old]
young_time_of_adaptation = [Pert_down_Young, Pert_up_Young]



def _add_jittered_points(ax, data, positions, color, jitter, alpha, marker):
    for pos, group in zip(positions, data):
        x = np.random.normal(loc=pos, scale=jitter, size=len(group))
        ax.scatter(x, group, color=color, alpha=alpha, s=30, marker=marker, zorder=3)


def plot_sample_entropy(young_SaEn, old_SaEn, show_points=False, jitter=0.05, alpha=0.6, marker='o', ylim=(0, 0.35), show_mean=True):
    fig, ax = plt.subplots(figsize=(8, 6))

    young_positions = [1, 4, 7, 10, 13]
    plus_factor = 0.6
    old_positions = [x + plus_factor for x in young_positions]

    ax.boxplot(young_SaEn, positions=young_positions, patch_artist=True,
               showmeans=show_mean, showfliers=False,
               boxprops=dict(facecolor='lightblue', color='blue', zorder=1),
               meanprops=dict(marker='o', markeredgecolor='blue', markerfacecolor='blue'),
               medianprops=dict(color='none'))

    ax.boxplot(old_SaEn, positions=old_positions, patch_artist=True,
               showmeans=show_mean, showfliers=False,
               boxprops=dict(facecolor='lightcoral', color='red', zorder=1),
               meanprops=dict(marker='o', markeredgecolor='red', markerfacecolor='red'),
               medianprops=dict(color='none'))

    if show_points:
        _add_jittered_points(ax, young_SaEn, young_positions, 'blue', jitter, alpha, marker)
        _add_jittered_points(ax, old_SaEn, old_positions, 'red', jitter, alpha, marker)

    legend_elements = [
        mpatches.Patch(color='lightblue', label='Young adults'),
        mpatches.Patch(color='lightcoral', label='Older adults'),
    ]

    if show_mean:
        young_means = [np.mean(data) for data in young_SaEn]
        old_means = [np.mean(data) for data in old_SaEn]

        ax.plot(young_positions, young_means, color='blue', linestyle='--', zorder=2)
        ax.plot(old_positions, old_means, color='red', linestyle='--', zorder=2)

        legend_elements += [
            mlines.Line2D([], [], color='blue', marker='o', linestyle='None', label='Young mean'),
            mlines.Line2D([], [], color='red', marker='o', linestyle='None', label='Older mean'),
        ]

    ax.legend(handles=legend_elements, loc='upper left', frameon=False)

    ax.set_title('Sample Entropy Curve between Young and Older adults')
    ax.set_xticks([(x + y) / 2 for x, y in zip(young_positions, old_positions)])
    ax.set_xticklabels(['5%', '20%', '40%', '60%', '80%'])
    ax.set_ylabel('Sample Entropy')
    ax.set_xlabel('Percentage of MVC')
    ax.set_ylim(ylim)

    plt.show()


def plot_standard_deviation(young_sd, old_sd, show_points=False, jitter=0.05, alpha=0.6, marker='o', ylim=(0, 2.7), show_mean=True):
    fig, ax = plt.subplots(figsize=(8, 6))

    young_positions = [1, 4, 7, 10, 13]
    plus_factor = 0.6
    old_positions = [x + plus_factor for x in young_positions]

    ax.boxplot(young_sd, positions=young_positions, patch_artist=True,
               showmeans=show_mean, showfliers=False,
               boxprops=dict(facecolor='lightblue', color='blue', zorder=1),
               meanprops=dict(marker='o', markeredgecolor='blue', markerfacecolor='blue'),
               medianprops=dict(color='none'))

    ax.boxplot(old_sd, positions=old_positions, patch_artist=True,
               showmeans=show_mean, showfliers=False,
               boxprops=dict(facecolor='lightcoral', color='red', zorder=1),
               meanprops=dict(marker='o', markeredgecolor='red', markerfacecolor='red'),
               medianprops=dict(color='none'))

    if show_points:
        _add_jittered_points(ax, young_sd, young_positions, 'blue', jitter, alpha, marker)
        _add_jittered_points(ax, old_sd, old_positions, 'red', jitter, alpha, marker)

    legend_elements = [
        mpatches.Patch(color='lightblue', label='Young adults'),
        mpatches.Patch(color='lightcoral', label='Older adults'),
    ]

    if show_mean:
        young_means = [np.mean(data) for data in young_sd]
        old_means = [np.mean(data) for data in old_sd]

        ax.plot(young_positions, young_means, color='blue', linestyle='--', zorder=2)
        ax.plot(old_positions, old_means, color='red', linestyle='--', zorder=2)

        legend_elements += [
            mlines.Line2D([], [], color='blue', marker='o', linestyle='None', label='Young mean'),
            mlines.Line2D([], [], color='red', marker='o', linestyle='None', label='Older mean'),
        ]

    ax.legend(handles=legend_elements, loc='upper left', frameon=False)

    ax.set_title('Standard Deviation curve between Young and Older adults')
    ax.set_xticks([(x + y) / 2 for x, y in zip(young_positions, old_positions)])
    ax.set_xticklabels(['5%', '20%', '40%', '60%', '80%'])
    ax.set_ylabel('Standard Deviation')
    ax.set_xlabel('Percentage of MVC')
    ax.set_ylim(ylim)

    plt.show()


def plot_time_of_adaptation(young_time, old_time, show_points=False, jitter=0.05, alpha=0.6, marker='o', ylim=(0, 7), show_mean=True):
    fig, ax = plt.subplots(figsize=(8, 6))

    young_positions = [1, 4]
    plus_factor = 0.6
    old_positions = [x + plus_factor for x in young_positions]

    ax.boxplot(young_time, positions=young_positions, patch_artist=True,
               showmeans=show_mean, showfliers=False,
               boxprops=dict(facecolor='lightblue', color='blue', zorder=1),
               meanprops=dict(marker='o', markeredgecolor='blue', markerfacecolor='blue'),
               medianprops=dict(color='none'))

    ax.boxplot(old_time, positions=old_positions, patch_artist=True,
               showmeans=show_mean, showfliers=False,
               boxprops=dict(facecolor='lightcoral', color='red', zorder=1),
               meanprops=dict(marker='o', markeredgecolor='red', markerfacecolor='red'),
               medianprops=dict(color='none'))

    if show_points:
        _add_jittered_points(ax, young_time, young_positions, 'blue', jitter, alpha, marker)
        _add_jittered_points(ax, old_time, old_positions, 'red', jitter, alpha, marker)

    legend_elements = [
        mpatches.Patch(color='lightblue', label='Young adults'),
        mpatches.Patch(color='lightcoral', label='Older adults'),
    ]

    if show_mean:
        young_means = [np.mean(data) for data in young_time]
        old_means = [np.mean(data) for data in old_time]

        ax.plot(young_positions, young_means, color='blue', linestyle='--', zorder=2)
        ax.plot(old_positions, old_means, color='red', linestyle='--', zorder=2)

        legend_elements += [
            mlines.Line2D([], [], color='blue', marker='o', linestyle='None', label='Young mean'),
            mlines.Line2D([], [], color='red', marker='o', linestyle='None', label='Older mean'),
        ]

    ax.legend(handles=legend_elements, loc='upper right', frameon=False)

    ax.set_title('Time to adapt curve between Young and Older adults')
    ax.set_xticks([(x + y) / 2 for x, y in zip(young_positions, old_positions)])
    ax.set_xticklabels(['Perturbation\ndownwards', 'Perturbation\nupwards'])
    ax.set_ylabel('Time to adapt')
    ax.set_ylim(ylim)

    plt.show()

plot_sample_entropy(young_SaEn, old_SaEn, show_points=True, jitter=0.05, ylim=(0, 0.35), show_mean=True, alpha=0.3, marker='D')
plot_standard_deviation(young_sd, old_sd, show_points=True, jitter=0.05, ylim=(0, 4), show_mean=True, alpha=0.3, marker='D')
plot_time_of_adaptation(young_time_of_adaptation, old_time_of_adaptation, show_points=True, jitter=0.05, ylim=(0, 7), show_mean=True, alpha=0.3, marker='D')

