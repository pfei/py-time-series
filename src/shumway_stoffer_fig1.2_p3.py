from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# --- File Path Configuration ---
land_file_path = Path("data/raw/gtemp_land_data.json")
ocean_file_path = Path("data/raw/gtemp_ocean_data.json")

# --- Data Loading and Time Series Reconstruction ---
gtemp_land_values = pd.read_json(land_file_path).iloc[:, 0]
gtemp_ocean_values = pd.read_json(ocean_file_path).iloc[:, 0]

# Reconstruct the DatetimeIndex
# Data is Yearly average from 1850 to 2023, 174 points total.
start_year = 1850
frequency = "YS"  # 'YS' for Year Start, as the data is yearly

# Create a date range as a pandas DatetimeIndex
date_range = pd.date_range(
    start=f"{start_year}-01-01",
    periods=len(gtemp_land_values),
    freq=frequency,
)

# Create pandas Series with the correct DatetimeIndex
gtemp_land_series = pd.Series(
    gtemp_land_values.values, index=date_range, name="Land Surface"
)
gtemp_ocean_series = pd.Series(
    gtemp_ocean_values.values, index=date_range, name="Sea Surface"
)

# Combine into a single DataFrame for plotting
gtemp_df = pd.DataFrame(
    {"Land Surface": gtemp_land_series, "Sea Surface": gtemp_ocean_series}
)

# --- Time Series Plotting ---

plt.figure(figsize=(12, 6))  # Reverted to original figure creation
ax = plt.gca()  # Reverted to getting current axes

colors = ["#1f77b4B3", "#d62728B3"]
markers = ["o", "D"]
linestyles = ["-", "-"]

gtemp_df["Land Surface"].plot(
    ax=ax,  # Use ax for plotting
    color=colors[0],
    marker=markers[0],
    linestyle=linestyles[0],
    label="Land Surface",
)
gtemp_df["Sea Surface"].plot(
    ax=ax,  # Use ax for plotting
    color=colors[1],
    marker=markers[1],
    linestyle=linestyles[0],
    label="Sea Surface",
)

ax.set_title("Global Surface Temperature Anomalies")  # Use ax.set_title
ax.set_ylabel("°C")  # Use ax.set_ylabel
ax.grid(True, linestyle=":", alpha=0.6)  # Reverted to simpler grid call
ax.legend(loc="upper left")

# Add horizontal margins (padding) to the x-axis
margin_factor = 0.05
total_span_days = (gtemp_df.index.max() - gtemp_df.index.min()).days
margin_in_days = margin_factor * total_span_days
ax.set_xlim(  # Use ax.set_xlim
    gtemp_df.index.min() - pd.Timedelta(days=margin_in_days),
    gtemp_df.index.max() + pd.Timedelta(days=margin_in_days),
)

# Adjust layout to prevent labels from overlapping
plt.tight_layout()

# Display the plot
plt.show()
