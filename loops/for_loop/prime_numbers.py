'''Create a list of prime numbers from 2 to 100 (inclusive) using a for loop.   
A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. 
The first few prime numbers are 2, 3, 5, 7, 11, and 13.
'''


prime_numbers=[]

for num in range(2, 101):
    is_prime=True
    for i in range(2, num):
        if num % i == 0:
            is_prime=False
            break
    if is_prime:
        prime_numbers.append(num)

print(prime_numbers)