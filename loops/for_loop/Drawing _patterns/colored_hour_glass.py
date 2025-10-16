import time
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

rows = int(input("Enter the number of rows: "))

# Top half of hourglass
for i in range(rows, 0, -1):
    spaces = rows - i
    stars = 2 * i - 1
    print(' ' * spaces + Fore.CYAN + '*' * stars)
    time.sleep(0.3)

# Bottom half of hourglass
for i in range(2, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(' ' * spaces + Fore.GREEN + '*' * stars)
    time.sleep(0.3)


# Example output for rows = 5:
#     *****
#      ***
#       *
#      ***
#     *****
# The top half of the hourglass is printed in cyan and the bottom half in green.
# Each line is printed with a delay of 0.3 seconds to create an animation effect.
# The hourglass is centered by adding spaces before the stars.
# The number of rows determines the height of the hourglass.
# The widest part of the hourglass has (2*rows - 1) stars.
# The number of stars decreases by 2 for each row in the top half and increases by 2 for each row in the bottom half.
# The number of leading spaces increases by 1 for each row in the top half and decreases by 1 for each row in the bottom half.
# The colorama library is used to add color to the stars.
# The autoreset=True parameter ensures that the color resets after each print statement.
# The time library is used to add a delay between printing each row.