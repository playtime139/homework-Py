import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset (replace with your own if needed)
df = sns.load_dataset("tips")

# 1. Pairplot
sns.pairplot(df)
plt.show()

# 2. Heatmap
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.show()

# 3. Boxplot
sns.boxplot(x="day", y="total_bill", data=df)
plt.show()

# 4. Violin plot
sns.violinplot(x="day", y="total_bill", data=df)
plt.show()

# 5. Bar plot
sns.barplot(x="day", y="total_bill", data=df)
plt.show()