import sys

# argumentList = sys.argv
# print(argumentList)



# print(sys.argv[0])

# print(sys.argv[1])

print(type(sys.argv))


print("The command line arguments are: ")
for i in sys.argv:
    print(i)

'''
The aboveline of code is used to access the commnad or the code on the 
command line interface when the code is executed

'''
#Another line of code for sys module
print(f"System version is: {sys.version}")


print(f"Version Information is: {sys.version_info}")
