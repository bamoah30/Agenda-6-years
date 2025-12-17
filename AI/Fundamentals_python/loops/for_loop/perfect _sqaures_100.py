"""
Create a list of perfect squares from 0 to 100 (inclusive) using a for loop."""


perfect_squares = []
for i in range(0, 101): 
    perfect_squares.append(i * i)
print(perfect_squares)