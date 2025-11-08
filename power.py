base = int(input("Enter a number: "))
exponent = int(input("Enter the power: "))

result = 1

for i in range(exponent):
    result = result * base

print(base, "to the power of", exponent, "is", result)
