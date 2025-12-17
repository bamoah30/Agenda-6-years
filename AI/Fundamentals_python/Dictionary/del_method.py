import random

names = ["manny",'sousy','Gringo','zeptter','Abel']
numbers = []


#Using for loop to generate the numbers for each name in names
for name in names:
    number = f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}"
    numbers.append(number)

contact_info = dict(zip(names,numbers))


print("The old dictionary is :" ,contact_info)


del contact_info["Abel"]

print("The new dictionar is: ", contact_info)