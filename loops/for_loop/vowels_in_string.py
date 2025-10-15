word = input("Enter a string: ")
vowels = "aeiou"
vowel_word = []
for char in word.lower():
    if char in vowels:
        vowel_word.append(char)



print(f"The vowels in {word} are: {set(vowel_word)}")