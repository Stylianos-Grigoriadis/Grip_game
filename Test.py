import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
import numpy as np

# Dummy data for demonstration (replace these with your actual dataframes)
Isometric_05_T1_100Hz = {'Performance': np.random.randn(10000)}
Isometric_05_T2_100Hz = {'Performance': np.random.randn(10000)}
Isometric_05_T3_100Hz = {'Performance': np.random.randn(10000)}

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Plotting each dataset
axs[0].plot(Isometric_05_T1_100Hz['Performance'])
axs[0].set_title('Isometric_5_T1')

axs[1].plot(Isometric_05_T2_100Hz['Performance'])
axs[1].set_title('Isometric_5_T2')

axs[2].plot(Isometric_05_T3_100Hz['Performance'])
axs[2].set_title('Isometric_5_T3')

# Define the callback function for span selection (locked at 500 points)
def onselect(xmin, xmax):
    # Calculate the midpoint of the selected range
    mid = (xmin + xmax) / 2
    # Recalculate xmin and xmax to lock the span at 500 points
    xmin_fixed = mid - 250
    xmax_fixed = mid + 250
    for ax in axs:
        ax.axvspan(xmin_fixed, xmax_fixed, color='yellow', alpha=0.3)  # Highlight the selected span
    plt.draw()

# Create SpanSelector for each subplot with 'interactive=True'
span_selector_1 = SpanSelector(axs[0], onselect, 'horizontal', useblit=True, interactive=True, minspan=500)
span_selector_2 = SpanSelector(axs[1], onselect, 'horizontal', useblit=True, interactive=True, minspan=500)
span_selector_3 = SpanSelector(axs[2], onselect, 'horizontal', useblit=True, interactive=True, minspan=500)

plt.show()
