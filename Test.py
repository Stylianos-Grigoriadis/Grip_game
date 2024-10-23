import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector

# Sample data creation for demonstration purposes
Isometric_05_T1_100Hz = {'Performance': np.random.rand(1000)}
Isometric_05_T2_100Hz = {'Performance': np.random.rand(1000)}
Isometric_05_T3_100Hz = {'Performance': np.random.rand(1000)}

# Dictionary to store selected indices for each subplot
selected_indices = {
    'T1': [],
    'T2': [],
    'T3': []
}

# Function to be called when a span is selected
def on_select(min_idx, max_idx, label):
    selected_indices[label] = np.arange(int(min_idx), int(max_idx), 1)
    print(f"Selected Indices for {label}: {selected_indices[label]}")  # Optional: print the selected indices

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Plot data series
axs[0].plot(Isometric_05_T1_100Hz['Performance'])
axs[0].set_title('Isometric_5_T1')

axs[1].plot(Isometric_05_T2_100Hz['Performance'])
axs[1].set_title('Isometric_5_T2')

axs[2].plot(Isometric_05_T3_100Hz['Performance'])
axs[2].set_title('Isometric_5_T3')

# Add SpanSelector to each subplot with a specific label
span1 = SpanSelector(axs[0], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T1'),
                    'horizontal', minspan=5, useblit=True,
                    props=dict(alpha=0.5, facecolor='red'), interactive=True,
                    drag_from_anywhere=True)
span2 = SpanSelector(axs[1], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T2'),
                    'horizontal', minspan=5, useblit=True,
                    props=dict(alpha=0.5, facecolor='red'), interactive=True,
                    drag_from_anywhere=True)
span3 = SpanSelector(axs[2], lambda min_idx, max_idx: on_select(min_idx, max_idx, 'T3'),
                    'horizontal', minspan=5, useblit=True,
                    props=dict(alpha=0.5, facecolor='red'), interactive=True,
                    drag_from_anywhere=True)

# Show the plot
plt.tight_layout()
plt.show()
