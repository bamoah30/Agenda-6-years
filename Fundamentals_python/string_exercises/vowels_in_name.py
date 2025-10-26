name = "Bernard Amoah"
vowels = ["a","e", "i", "o", "u"]
name_lower = name.lower()
vowels_in_name =[]
for letter in name_lower:
    if letter in vowels and letter not in vowels_in_name:
        vowels_in_name.append(letter)

print(vowels_in_name)
print(f"The vowels in the name {name} are: {', '.join(vowels_in_name)}")
# Output: The vowels in the name Bernard Amoah are: e, a, o
