credentials = ['kikiwi@gmail.com', 'female', 'Kikiwi', 32]

# Accessing elements using positive and negative indexing
print(credentials[0])  # Accessing the first element (email)
print(credentials[2])  # Accessing the third element (username)
print(credentials[-1])  # Accessing the last element (age)
print(credentials[-2])  # Accessing the second last element (name)

# Output:
# kikiwi@gmail.com
# Kikiwi
# 32    
#Kikiwi





#Accessing elements using slicing
print(credentials[0:2])  # Accessing the first two elements (email and gender)
print(credentials[1:])   # Accessing elements from the second element to the end (gender, username, age)
print(credentials[:3])  # Accessing the first three elements (email, gender, username)
print(credentials[-3:]) # Accessing the last three elements (gender, username, age) 


# Output:
# # ['kikiwi@gmail.com', 'female']
# ['female', 'Kikiwi', 32]
# ['kikiwi@gmail.com', 'female', 'Kikiwi']
# ['female', 'Kikiwi', 32]      