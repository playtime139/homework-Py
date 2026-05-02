import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(1, 6)
y = [10, 20, 15, 25, 30]

# Line Plot
plt.figure()
plt.plot(x, y)
plt.title("Line Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# Bar Chart
plt.figure()
plt.bar(x, y)
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Histogram
data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=20)
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()