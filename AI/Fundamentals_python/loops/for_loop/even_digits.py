# Get input from user
number = input("Enter a number: ")
even_digits = []
# Loop through each character in the string
for digit in number:
    if digit.isdigit() and int(digit) % 2 == 0:
        even_digits.append(int(digit))

print(f"The even digits in {number} are: {set(even_digits)}")
