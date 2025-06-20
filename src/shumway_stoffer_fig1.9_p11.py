import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

# --- 1. Generate Synthetic Data (Gaussian White Noise and its Moving Average) ---
# X-axis will be numerical from 0 to 250.
num_points = 251  # For an x-axis ranging from 0 to 250 (inclusive)
x_index = np.arange(num_points)  # Numerical index from 0 to 250

np.random.seed(42)  # For reproducibility of the random data

# Series 'x': Gaussian White Noise series with MEAN = 0 and VARIANCE = 1
# This means standard deviation = sqrt(1) = 1
mean_val_x = 0
std_dev_x = 1  # Adjusted as per user request: variance = 1

data_x_series = np.random.normal(mean_val_x, std_dev_x, num_points)
series_x = pd.Series(
    data_x_series, index=x_index, name="x"
)  # This is the top plot data

# Series 'y': 3-point moving average of 'x'
# min_periods=1 allows the moving average to start calculating with fewer than 3 points
# at the very beginning of the series, avoiding initial NaN values for the plot line.
series_y = series_x.rolling(window=3, min_periods=1, center=True).mean()
series_y.name = "y"  # Ensure the name is 'y' for plotting


# Combine into a DataFrame
df = pd.DataFrame({"x": series_x, "y": series_y})


# --- 2. Plotting Setup: TWO SUBPLOTS ---
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 8))


# --- 3. Plotting Series on Respective Subplots ---

# Plot series 'x' (Gaussian White Noise) on the TOP subplot (ax1)
df["x"].plot(
    ax=ax1,
    color="#1f77b4",  # Blue
    marker="o",
    linestyle="-",
    label="x",  # Legend label
    markersize=3,
    linewidth=1,
)

# Plot series 'y' (3-point Moving Average) on the BOTTOM subplot (ax2)
df["y"].plot(
    ax=ax2,
    color="#d62728",  # Red
    marker="D",
    linestyle="-",
    label="y",  # Legend label
    markersize=3,
    linewidth=1,
)


# --- 4. Customize TOP Subplot (ax1) - Gaussian White Noise ---
ax1.set_title(
    "Gaussian white noise series (mean is 0)"
)  # Specific title for top subplot
ax1.set_ylabel("x")  # Y-axis label
ax1.legend(loc="upper left")

# Adjusted Y-axis limits for ax1 to properly show mean 0 Gaussian white noise with std dev 1
ax1.set_ylim(-5, 5)  # Values will mostly fall within +/- 3 for std dev 1
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))  # Major ticks every 1 unit
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.2))  # Minor ticks every 0.2 units

# Grid for ax1
ax1.xaxis.grid(
    True, which="major", linestyle="-", alpha=0.7, color="black", linewidth=0.7
)
ax1.yaxis.grid(
    True, which="major", linestyle="-", alpha=0.7, color="black", linewidth=0.7
)
ax1.xaxis.grid(
    True, which="minor", linestyle="-", alpha=0.3, color="dimgray", linewidth=0.5
)
ax1.yaxis.grid(
    True, which="minor", linestyle="-", alpha=0.3, color="dimgray", linewidth=0.5
)

# Hide x-axis labels on the top subplot as they are shared with the bottom
ax1.tick_params(axis="x", labelbottom=False)


# --- 5. Customize BOTTOM Subplot (ax2) - 3-point Moving Average ---
ax2.set_title("3-point moving average")  # Specific title for bottom subplot
ax2.set_ylabel("y")  # Y-axis label
ax2.set_xlabel("")  # No explicit x-label besides the numerical index
ax2.legend(loc="upper left")

# Adjusted Y-axis limits for ax2 (moving average of std dev 1 noise)
ax2.set_ylim(
    -3, 3
)  # Values will mostly fall within +/- 1.73 for 3-pt MA of std dev 1 noise
ax2.yaxis.set_major_locator(ticker.MultipleLocator(1))  # Keep major ticks consistent
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.2))  # Keep minor ticks consistent

# Grid for ax2
ax2.xaxis.grid(
    True, which="major", linestyle="-", alpha=0.7, color="black", linewidth=0.7
)
ax2.yaxis.grid(
    True, which="major", linestyle="-", alpha=0.7, color="black", linewidth=0.7
)
ax2.xaxis.grid(
    True, which="minor", linestyle="-", alpha=0.3, color="dimgray", linewidth=0.5
)
ax2.yaxis.grid(
    True, which="minor", linestyle="-", alpha=0.3, color="dimgray", linewidth=0.5
)


# --- 6. Customize Shared X-axis (only visible on ax2) ---
ax2.set_xlim(-10, 260)  # X-axis range from 0 to 250 with a buffer
ax2.xaxis.set_major_locator(ticker.MultipleLocator(50))  # Major ticks at 0, 50, 100...
ax2.xaxis.set_minor_locator(ticker.MultipleLocator(10))  # Minor ticks at 10, 20, 30...

# Explicitly set x-axis label rotation to 90 degrees (vertical), centered
plt.setp(ax2.get_xticklabels(), rotation=90, ha="center")


# --- 7. Final Layout Adjustment and Display ---
plt.tight_layout()  # Adjust plot parameters for a tight layout
plt.show()  # Display the plot
