import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)

print("Mean:", np.mean(a))
print("Shape:", a.shape)

print("First:", a[0])
print("Slice:", a[1:])

print("Reshape:\n", a.reshape(3, 1))
print("Zeros:\n", np.zeros((2, 2)))