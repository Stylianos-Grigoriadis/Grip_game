from fathon import fathonUtils as fu
import fathon
import numpy as np
import matplotlib.pyplot as plt


# The following is the way Rudisch et al., 2024 Force Fluctuations During Role-Differentiated Bimanual
# Movements Reflect Cognitive Impairments in Older Adults: A Cohort Sequential Study
# https://doi.org/10.1093/gerona/glae137
# calculate the windows for the DFA algorithm. They had 20 seconds of 120Hz trials with the first 6 seconds being erased.
# Therefor, their remaining data points were 1680 in total, while I only have 500 data points
winSizes = fu.linRangeByStep(start=10, end=200)
print(winSizes)

data = np.arange(10, 201)

# Generate 30 exponential indices
a = 1  # Starting multiplier
r = 1.2  # Growth factor
n = 30  # Number of points


#
# # Generate exponential values and round them to nearest integer indices
# exponential_indices = np.round(a * (r ** np.arange(n))).astype(int)
# # Ensure indices are within the bounds of the list
# exponential_indices = np.clip(exponential_indices, 0, len(data) - 1)
# # Use indices to pick values from the list
# selected_values = data[exponential_indices]
# print(selected_values)
# plt.plot(selected_values)
# plt.title(r)
# plt.show()

log_windows = np.log10(data)
plt.plot(log_windows)
plt.show()
print(np.log10(122))