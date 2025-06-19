from typing import cast

import matplotlib.pyplot as plt
import pandas as pd

# --- File Path Configuration ---
json_file_path: str = "data/raw/jj_data.json"

# --- Data Loading and Initial Inspection ---
# Load the JSON file into a pandas DataFrame.
# The explicit typ='frame' and type: ignore are used to help type checkers
# like MyPy and Pylance with complex pandas DataFrame inference.
df_jj: pd.DataFrame = cast(
    pd.DataFrame,
    pd.read_json(json_file_path, typ="frame"),  # type: ignore
)

print("--- Initial DataFrame Head ---")
print(df_jj.head())
print("\n--- Initial DataFrame Info ---")
# The 'None' output after df_jj.info() is normal, as info() prints directly and returns nothing.
print(df_jj.info())

# --- Date Column Construction and Indexing ---
# The original JSON data has 'Year' and 'Quarter' columns, not a single 'Date' column.
# We construct a 'Date' column from 'Year' and 'Quarter' to create a proper time series index.

# Step 1: Create a string representation of the quarter (e.g., '1960Q1')
df_jj["Date"] = df_jj["Year"].astype(str) + "Q" + df_jj["Quarter"].astype(str)

# Step 2: Convert the string 'Date' column into a pandas DatetimeIndex.
# pd.PeriodIndex converts 'YYYYQ Q' strings into Period objects,
# and .to_timestamp() converts these periods to the start of their respective timestamps.
df_jj["Date"] = pd.PeriodIndex(df_jj["Date"], freq="Q").to_timestamp()

# Step 3: Set the newly created 'Date' column as the DataFrame's index.
# The 'Value' column will be extracted into a pandas Series.
# The type: ignore is kept here if type checkers like MyPy/Pylance struggle with
# inferring the exact type of the Series after chaining set_index and column selection.
jj_series: "pd.Series[float]" = df_jj.set_index("Date")["Value"]  # type: ignore

print("\n--- Pandas Series with DatetimeIndex (Head) ---")
print(jj_series.head())
print("\n--- Pandas Series Index ---")
# # noqa comments are used to suppress specific Pylance warnings on this line if they appear.
print(jj_series.index)  # noqa: reportUnknownMemberType, reportUnknownArgumentType

# --- Time Series Plotting (Equivalent to R's tsplot) ---

# Create a figure and a set of subplots.
# mfrow=2:1 in R is equivalent to (2, 1) in plt.subplots().
fig, axes = plt.subplots(2, 1, figsize=(10, 8))  # figsize=(width, height) in inches

# --- Plot 1: Linear Scale ---
jj_series.plot(
    ax=axes[0],  # Plot on the first subplot
    color="blue",  # Line color (similar to R's col=4)
    marker="o",  # Add markers for each point (similar to R's type="o")
    linestyle="-",  # Connect markers with a line
    title="Johnson & Johnson Quarterly Earnings per Share",
    ylabel="USD",
)
axes[0].grid(True, linestyle=":", alpha=0.6)  # Add a grid for better readability

# --- Plot 2: Logarithmic Scale ---
jj_series.plot(
    ax=axes[1],  # Plot on the second subplot
    color="blue",  # Line color
    marker="o",  # Add markers
    linestyle="-",
    title="Johnson & Johnson Quarterly Earnings per Share (Log Scale)",  # Descriptive title
    ylabel="USD (log scale)",
    logy=True,  # Set y-axis to logarithmic scale (equivalent to R's log="y")
)
axes[1].grid(True, linestyle=":", alpha=0.6)  # Add a grid

# Adjust subplot parameters for a tight layout, preventing labels/titles from overlapping
plt.tight_layout()

# Display the plots
plt.show()
