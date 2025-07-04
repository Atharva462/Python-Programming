import pandas as pd
# Step 1: Read data from a CSV file
file_path = 'data.csv' # Replace with the path to your CSV file
df = pd.read_csv(file_path)

# Step 2: Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Step 3: Display information about the DataFrame
print("\nInformation about the DataFrame:")
print(df.info())

# Step 4: Display basic statistics of the DataFrame
print("\nBasic statistics of the DataFrame:")
print(df.describe())

# Optional: Modify the DataFrame (example: adding a new column)
df['NewColumn'] = df['ExistingColumn'] * 2 # Replace 'ExistingColumn' with an actual 
column name

# Step 5: Save the modified DataFrame to a new CSV file
output_file_path = 'modified_data.csv' # Path for the new CSV file
df.to_csv(output_file_path, index=False)
print(f"\nModified DataFrame saved to {output_file_path}")