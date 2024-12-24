import os
import pandas as pd

# Define the path to the raw data folder and the output file
raw_data_folder = "data/raw"
output_file = "data/ucb-data.csv"

# List of CSV files to be combined
csv_files = [
    "data.csv",
]

# Number of rows to read from each file
num_rows = 1800

# Starting row number (0-indexed)
start_row = 10000

# Initialize an empty DataFrame to hold the combined data
combined_data = pd.DataFrame()

# Loop through each file and extract the specified rows
for i, file in enumerate(csv_files):
    file_path = os.path.join(raw_data_folder, file)
    data = pd.read_csv(file_path, skiprows=start_row, nrows=num_rows)
    data.columns = [
        f"data{j+1:02d}" for j in range(data.shape[1])
    ]  # Rename columns to data01, data02, ..., data08
    combined_data = pd.concat([combined_data, data], axis=0)

# Save the combined data to a new CSV file
combined_data.to_csv(output_file, index=False)
