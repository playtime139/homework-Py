age = int(input("Enter your age: "))

if age < 0:
    print("Age cannot be negative.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
