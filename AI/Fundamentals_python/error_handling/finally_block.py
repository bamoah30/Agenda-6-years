list = [i for i in range(1,11)]
try:
    average= sum(list)/ len(list)
    print(f'The average of the list is {average}')
except ValueError as e:
    print("You have", e)
finally:
    print("Your list is:", list, "and the number of elements of the list is:", len(list), "The sum of the list is:", sum(list))
    print("Execution completed.")
    
