# Get number of rows from user
rows = int(input("Enter the number of rows: "))

# Loop through each row
for i in range(rows):
    # Print spaces to center the stars
    print(' ' * (rows - i - 1), end='')
    # Print stars: (2 * i + 1) gives the correct number of stars per row
    print('*' * (2 * i + 1))
