import random


numbers = random.sample(range(1, 11), 3)
print("Original list:", numbers)

if 2 in numbers:
    numbers = numbers * 2
    print("Duplicated list:", numbers)
else:
    del numbers
    print("List deleted.")