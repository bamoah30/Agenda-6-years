import random

names = ["manny",'sousy','Gringo','zeptter']
numbers = []


#Using for loop to generate the numbers for each name in names
for name in names:
    number = f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}"
    numbers.append(number)

contact_info = dict(zip(names,numbers))


print(contact_info.items())


print(contact_info.keys())

print(contact_info.values())