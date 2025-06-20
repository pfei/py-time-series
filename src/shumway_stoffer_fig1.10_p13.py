import matplotlib.pyplot as plt
import matplotlib.ticker as ticker  # For tick customization
import numpy as np
import pandas as pd
from scipy.signal import lfilter  # For recursive filtering (AR process)

# 1. Generate Gaussian White Noise (w)
# R equivalent: w = rnorm(300)
np.random.seed(42)  # For reproducibility (optional, but good for consistent results)
w = np.random.normal(0, 1, 300)  # mean=0, std_dev=1, 300 points

# 2. Implement the Autoregressive (AR) filter
# R equivalent: x = filter(w, filter=c(1.5,-.75), method="recursive")
# This defines an AR(2) process: x_t = 1.5 * x_{t-1} - 0.75 * x_{t-2} + w_t
#
# In scipy.signal.lfilter(b, a, x):
#   'a' are the feedback (autoregressive) coefficients in the form: [1, -phi_1, -phi_2, ...]
#   'b' are the feedforward (moving average) coefficients: [1, theta_1, ...]
#
# For an AR(2) process of the form x_t - phi_1 x_{t-1} - phi_2 x_{t-2} = w_t,
# the 'a' coefficients for lfilter are [1, -phi_1, -phi_2].
# The 'b' coefficient is [1] because w_t is the only input term (no MA part directly from w).

phi1 = 1.5
phi2 = -0.75

a_lfilter = np.array([1, -phi1, -phi2])
b_lfilter = np.array([1])

# Apply the filter to generate the AR process
x_all = lfilter(b_lfilter, a_lfilter, w)

# 3. Discard the first 50 points to avoid startup/transient problems
# R equivalent: [-(1:50)]
x_simulated = x_all[
    50:
]  # Keep points from index 50 onwards (0-indexed), resulting in 250 points

# Create a pandas Series for easy plotting, using a simple numerical index (0 to 249)
x_series = pd.Series(x_simulated, index=np.arange(len(x_simulated)))

# 4. Plotting the simulated AR(2) series
# R equivalent: tsplot(x, main="autoregression", col=4, gg=TRUE)
plt.figure(figsize=(10, 6))
plt.plot(x_series.index, x_series.values, color="blue", linewidth=1)

plt.title("Simulated Autoregressive Process (AR(2))")
plt.xlabel("Time Index")
plt.ylabel("x")

# Set X-axis limits and ticks to be consistent with your previous plots (0 to 250)
plt.xlim(-10, 260)  # Adding a small buffer
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(50))
plt.gca().xaxis.set_minor_locator(ticker.MultipleLocator(10))

# Set Y-axis limits (adjusted for the typical fluctuation range of this specific AR(2) process)
plt.ylim(
    -10, 10
)  # This range should accommodate most values for a stable AR(2) driven by std_dev=1 noise

# Add grid lines (consistent with your previous plots)
plt.grid(True, which="major", linestyle="-", alpha=0.7, color="black", linewidth=0.7)
plt.grid(True, which="minor", linestyle="-", alpha=0.3, color="dimgray", linewidth=0.5)

# Ensure X-axis labels are vertical (consistent with your previous plots)
plt.tick_params(axis="x", rotation=90)

plt.tight_layout()  # Adjust plot parameters for a tight layout
plt.show()  # Display the plot
