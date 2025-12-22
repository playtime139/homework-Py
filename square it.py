start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

squares = []
for i in range(start, end + 1):
    squares.append(i ** 2)

even_squares = []
odd_squares = []

for sq in squares:
    if sq % 2 == 0:
        even_squares.append(sq)
    else:
        odd_squares.append(sq)

print("All squares:", squares)
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)
