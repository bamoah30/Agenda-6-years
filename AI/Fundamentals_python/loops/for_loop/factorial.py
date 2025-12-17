number = int(input("Enter a number to calculate its factorial: "))

factorial = 1
for i in range(number):
    if i == 0:
        factorial = 1
    else:
        factorial *= (i + 1)

        
print(f"The factorial of {number} is {factorial}")