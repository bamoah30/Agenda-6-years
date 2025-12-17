def output(list, index):
    return list[index]


list = [i for i in range(1,11)]

index = int(input("Please enter your index: "))

try:
    value = output(list, index)
    print(f' The value at {index} index is {value}')

except IndexError as e:
    print("You have", e)
