prime_numbers=[]

for num in range(2, 101):
    is_prime=True
    for i in range(2, num):
        if num % i == 0:
            is_prime=False
            break
    if is_prime:
        prime_numbers.append(num)


print("Prime numbers from 2 to 100 are:", prime_numbers)
print(f"Their  sum is {sum(prime_numbers)}")