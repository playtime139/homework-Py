import pandas as pd

# Create sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Score": [85, 90, 95, 80]
}

df = pd.DataFrame(data)

# View data
print("Dataset:")
print(df)

# Filter rows (Age > 30)
filtered = df[df["Age"] > 30]
print("\nFiltered Data (Age > 30):")
print(filtered)

# Add new column
df["Passed"] = df["Score"] >= 85
print("\nWith New Column:")
print(df)

# Summary statistics
print("\nStatistics:")
print(df.describe())

# Sort values
sorted_df = df.sort_values(by="Score", ascending=False)
print("\nSorted by Score:")
print(sorted_df)