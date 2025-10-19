user_input = input("Please type something: ")

print("Length of your text:", len(user_input))

print("Uppercase:", user_input.upper())

print("Lowercase:", user_input.lower())

print("Does it start with 'Hi'? ", user_input.startswith("Hi"))

print("Does it end with 'bye'? ", user_input.endswith("bye"))

new_text = user_input.replace("hello", "hi")