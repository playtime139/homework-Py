test_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 1
}

value = 1
frequency = list(test_dict.values()).count(value)

print("Frequency of", value, "is:", frequency)
