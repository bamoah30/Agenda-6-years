# Get number of rows from user
rows = int(input("Enter the number of rows: "))

# Print header
print("Multiplication Table:")
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        print(f"{i * j:4}", end='')  # Format each number with 4 spaces
    print()  # Newline after each row


# Example output for rows = 5:
# Multiplication Table:
#    1   2   3   4   5
#    2   4   6   8  10   
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25
# Each number is right-aligned within a width of 4 characters for better readability.