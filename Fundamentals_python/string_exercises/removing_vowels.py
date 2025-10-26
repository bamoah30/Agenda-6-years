name = "Yonatan"
vowels = ["a","e", "i", "o", "u"]
name_lower = name.lower()
name_no_vowels = ""
for letter in name_lower:
    if letter not in vowels:
        name_no_vowels += letter    
print(name_no_vowels)



# Output: yntn