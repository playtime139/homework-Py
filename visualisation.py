import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
df = sns.load_dataset("tips")

# Create a scatter plot
sns.scatterplot(x="total_bill", y="tip", data=df)

plt.show()