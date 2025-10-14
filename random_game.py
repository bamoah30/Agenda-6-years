import random

your_num = int(input("Enter your number: "))
comp_num = random.randint(1, 10)
if your_num == comp_num:
    print(f"You win! The winning number is {comp_num}")
else:
    print(f"You lose! Your number is {your_num}, the computer  number is {comp_num}")
