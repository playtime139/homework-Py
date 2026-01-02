import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password = ""

for i in range(8):
    password += random.choice(letters)

print("Your password is:", password)
 