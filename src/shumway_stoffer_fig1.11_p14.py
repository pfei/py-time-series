import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# 1. Set seed for reproducibility (using user's chosen seed for this iteration)
np.random.seed(42)

# 2. Generate Gaussian white noise (w)
w = np.random.normal(0, 1, 200)  # 200 standard normal random numbers

# 3. Generate random walk without drift (x) starting at 0
x_raw = np.cumsum(w)
x = np.insert(x_raw, 0, 0)  # Now 'x' has 201 points, starting with 0 at index 0

# 4. Generate white noise with drift (wd) and random walk with drift (xd) starting at 0
drift_value = 0.2
wd = w + drift_value  # Add a constant drift to the white noise
xd_raw = np.cumsum(wd)
xd = np.insert(xd_raw, 0, 0)  # 'xd' also has 201 points, starting with 0.

# Define time points for plotting (now 201 points from 0 to 200)
time_points = np.arange(len(x))

# Calculate the drift line's y-values (y = 0.2t)
drift_line_y = drift_value * time_points

# Calculate dynamic Y-axis limits to ensure all curves are visible
# Get min/max from both random walk curves
min_val = min(np.min(x), np.min(xd))
max_val = max(np.max(x), np.max(xd))

# Add some padding to the min/max values (10% of the data range)
padding = (max_val - min_val) * 0.1
new_ylim_min = min_val - padding
new_ylim_max = max_val + padding

# 5. Plotting setup
plt.figure(figsize=(10, 6))

# Plot the random walk with drift (xd)
plt.plot(time_points, xd, color="blue", label="Random Walk with Drift", linewidth=1.5)

# Plot the random walk without drift (x)
# It will now be fully visible within the overall plot's dynamically set y-limits.
plt.plot(
    time_points, x, color="magenta", label="Random Walk without Drift", linewidth=1.5
)

# Plot the drift line (y = 0.2t)
plt.plot(
    time_points,
    drift_line_y,
    color="gray",
    linestyle="--",
    label="Drift Line (y = 0.2t)",
    linewidth=1.5,
)

# Add the horizontal zero line at y=0, now more visible
plt.axhline(
    y=0, color="black", linestyle=":", linewidth=2, label="Zero Line (y=0)", zorder=0
)


# Customize plot appearance
plt.title("Random Walk")
plt.xlabel("Time Index")
plt.ylabel("Value")

# Set Y-axis limits dynamically
plt.ylim(new_ylim_min, new_ylim_max)

# Set X-axis limits and ticks (now covers 0 to 200 data points)
plt.xlim(-10, 210)  # Add a small buffer for aesthetics
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(50))
plt.gca().xaxis.set_minor_locator(ticker.MultipleLocator(10))

# Add a legend
plt.legend(loc="upper left")

# Add grid lines
plt.grid(True, which="major", linestyle="-", alpha=0.7, color="black", linewidth=0.7)
plt.grid(True, which="minor", linestyle="-", alpha=0.3, color="dimgray", linewidth=0.5)

# Ensure X-axis labels are vertical (consistent with previous plots)
plt.tick_params(axis="x", rotation=90)

plt.tight_layout()  # Adjust layout to prevent labels from overlapping
plt.show()
