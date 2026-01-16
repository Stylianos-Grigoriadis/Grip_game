import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from matplotlib.patches import Patch
import seaborn as sns


def plot_saen_by_mvc_group(
    results,
    box_width=0.25,
    show_points=True
):
    """
    Boxplots of Sample Entropy (SaEn) across MVC levels,
    with separate boxplots for Young and Older adults.

    Parameters
    ----------
    results : pandas.DataFrame
        DataFrame containing SaEn time-delay averages.

    box_width : float
        Width of each boxplot.

    show_points : bool
        Whether to show individual datapoints.
    """

    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from matplotlib.patches import Patch

    sns.set_style("whitegrid")
    sns.set_context("talk")

    # -------------------------------
    # MVC levels and corresponding columns
    # -------------------------------
    mvc_levels = [5, 20, 40, 60, 80]

    column_map = {
        5:  'SaEn_time_delay_average_05',
        20: 'SaEn_time_delay_average_20',
        40: 'SaEn_time_delay_average_40',
        60: 'SaEn_time_delay_average_60',
        80: 'SaEn_time_delay_average_80'
    }

    # -------------------------------
    # Groups
    # -------------------------------
    group_order = ['Young', 'Old']

    colors = {
        'Young': 'Blue',
        'Old': 'red'
    }

    # -------------------------------
    # X positions
    # -------------------------------
    base_positions = np.arange(len(mvc_levels))
    offsets = [-box_width / 2, box_width / 2]

    plt.figure(figsize=(10, 6))
    ax = plt.gca()

    # -------------------------------
    # Draw boxplots (+ optional datapoints)
    # -------------------------------
    for gi, group in enumerate(group_order):
        for mi, mvc in enumerate(mvc_levels):

            col = column_map[mvc]

            data = results.loc[
                results['Group'] == group,
                col
            ].dropna()

            if data.empty:
                continue

            pos = base_positions[mi] + offsets[gi]

            bp = ax.boxplot(
                data,
                positions=[pos],
                widths=box_width,
                patch_artist=True,
                showfliers=False
            )

            for patch in bp['boxes']:
                patch.set_facecolor(colors[group])
                patch.set_edgecolor('black')
                patch.set_alpha(0.9)

            for element in ['whiskers', 'caps', 'medians']:
                for item in bp[element]:
                    item.set_color('black')
                    item.set_linewidth(1.2)

            # ---- Raw datapoints (ONLY CHANGE)
            if show_points:
                x_jitter = np.random.normal(pos, box_width * 0.15, size=len(data))
                ax.scatter(
                    x_jitter,
                    data,
                    s=35,
                    facecolor=colors[group],
                    edgecolor='black',
                    linewidth=0.8,
                    alpha=0.75,
                    zorder=3
                )

    # -------------------------------
    # Axes formatting
    # -------------------------------
    ax.set_xticks(base_positions)
    ax.set_xticklabels([f'{m}%' for m in mvc_levels])
    ax.set_xlabel('% MVC')
    ax.set_ylabel('Sample Entropy (SaEn)')
    ax.set_title('Sample Entropy Across MVC Levels')

    ax.set_xlim(
        base_positions[0] - 0.6,
        base_positions[-1] + 0.6
    )

    # -------------------------------
    # Legend
    # -------------------------------
    legend_handles = [
        Patch(facecolor=colors['Young'], edgecolor='black', label='Young'),
        Patch(facecolor=colors['Old'], edgecolor='black', label='Older')
    ]

    ax.legend(
        handles=legend_handles,
        title='Group',
        loc='upper right',
        frameon=False
    )

    sns.despine(trim=True)
    plt.tight_layout()
    plt.show()




directory = r'C:\Users\Stylianos\OneDrive - Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης\My Files\PhD\Projects\Grip perturbation\Data collection\Results'
os.chdir(directory)
results = pd.read_excel('Results Isometric SaEn Time delay.xlsx')
print(results.columns)
print(results['Group'])

plot_saen_by_mvc_group(results)