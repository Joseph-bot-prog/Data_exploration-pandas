import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('593 salaries-by-college-major.csv')

# 1. Viewing the DataFrame
print("First few rows of the DataFrame:")
print(df.head())
print("\n")

# 2. Getting Basic Information
print("Basic information about the DataFrame:")
df.info()
print("\n")

# 3. Descriptive Statistics
print("Descriptive statistics for numeric columns:")
print(df.describe())
print("\n")

# 4. Accessing Columns
selected_column = df['ColumnName']
print(f"Selected column:\n{selected_column.head()}")
print("\n")

filtered_df = df[df['ColumnName'] > threshold_value]
print(f"Filtered DataFrame:\n{filtered_df.head()}")
print("\n")

grouped_data = df.groupby('ColumnName').mean()
print(f"Grouped data:\n{grouped_data.head()}")
print("\n")

df['NumericColumn'].plot(kind='hist', bins=20, edgecolor='black')
plt.title('Histogram of NumericColumn')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()
