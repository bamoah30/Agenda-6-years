import random

# Create a list of 5 random integers between 1 and 20 (inclusive)
numbers = [random.randint(1, 20) for _ in range(5)]
print('Original list:', numbers)

# Remove duplicates while preserving order
seen = set()
unique_numbers = []
for n in numbers:
    if n not in seen:
        unique_numbers.append(n)
        seen.add(n)

if len(unique_numbers) != len(numbers):
    print('Duplicates found and removed ->', unique_numbers)
else:
    print('No duplicates ->', unique_numbers)

# Compute sum and decide whether to print max or min
total = sum(unique_numbers)
if total % 2 == 0:
    print('Sum is even (', total, ') -> max =', max(unique_numbers))
else:
    print('Sum is odd (', total, ') -> min =', min(unique_numbers))
