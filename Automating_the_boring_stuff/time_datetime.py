#December 1. 2025
'''The time Module:
The computer's system clock is set to a specific date, time and time zone.
The built-in time module allows you to access and manipulate the system clock.
The time.time() and the time.sleep() functions are the most useful functions in the time module.

The time.time() Function:
The Unix epoch is a time reference commonly used in programming : 12 :00 am January 1, 1970, Coordinated Universal Time (UTC).
The time.time() function returns the number of seconds that have passed since the epoch as a float value
The number is called a timestamp.

Example:
'''
import time
print(time.time()) #Output: 1764618306.8946157 (example output, will vary) The output is the number of seconds since the epoch to the time the code is run.

#Example of using time.time() to measure how long a program takes to run:
import time
def calcProd():
    # Calculate the product of the first 30 numbers
    product = 1
    for i in range(1, 30):
        product = product * i
    return product

startTime = time.time() #Get the start time
prod = calcProd()
endTime = time.time() #Get the end time
print(f'The result is {prod}.' ) # Output: 8841761993739701954543616000000
print('Took %s seconds to calculate.' % (endTime - startTime)) #Print the time taken to calculate
