# Sample list of numbers
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# List comprehension to filter prime numbers
primes = [num for num in numbers if all(num % i != 0 for i in range(2, num)) and num > 1]

print(primes)

# Output: [2, 3, 5, 7, 11]
