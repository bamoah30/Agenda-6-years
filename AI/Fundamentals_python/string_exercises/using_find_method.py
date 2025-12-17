quote = input("Please enter your favorite quote: ")
sub_string = input("Enter a substring to search for: ") 
if quote.find(sub_string) != -1:
    print(f"Substring found at index {quote.find(sub_string)}")
else:
    print("Substring not found")
