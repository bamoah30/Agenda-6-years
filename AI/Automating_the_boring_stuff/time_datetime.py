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


#December 4, 2025
'''The time.sleep() Function:
The time.sleep() function pauses the program for the given number of seconds.

Example Usage:
'''
import time
# for i in range(5):
#     print('Tick')
#     time.sleep(15) #Pause for 1 second
#     print('Tock')
#     time.sleep(15) #Pause for 1 second


#December 12, 2025
'''Rounding Numbers:
The time module usually produces a lot of numbers after the decimal.
To solve that we use python in built round() function.
The in built round() fuction accept thw areguments:
One argument for the number, the other argument for the precision.
Example usage:
'''
import time
now = time.time()
print(now)   #Output >> 1765494185.3331032
print(round(now, 2)) #Output >> 1765494185.33
print(round(now, 4)) #Output >> 1765494185.3331

#NB: Using round() without specifying the precision for the round will produce whole number.
print(round(now)) #Output >> 1765494185


'''The Datetime Module:
The time module is useful for getting a Unix epoch timestamp to work with. 
But if you want to display a date in a more convenient format, or 
do arithmetic with dates (for example, figuring out what date was 205 days ago or 
what date is 123 days from now), you should use the datetime module.

NB:The datetime module has its own datetime data type. datetime values 
represent a specific moment in time.

Example Usage: '''

import datetime
print(datetime.datetime.now()) #Output >> 2025-12-11 23:38:29.897664 (NB: Depending on your timezone, this is subject to change)
print(datetime.datetime(2015, 2, 27, 11, 10, 49, 55, )) #Output >> 2015-02-27 11:10:49.000055
dt = datetime.datetime(2015, 10, 21, 16, 29, 0)

print(dt.year, "year") #Output >> 2015
print(dt.month ,'month') #Output >> 10
print(dt.day, 'day' )  #Output >> 21
print(dt.hour, 'hour') #Output >> 16
print(dt.minute, 'minute') #Output >> 29
print(dt.second , 'seconds') #Output >> 0

'''
A Unix epoch timestamp can be converted to a datetime object with the 
datetime.datetime.fromtimestamp() function.

Example:
'''
print(datetime.datetime.fromtimestamp(1000000)) #Output >> 1970-01-12 13:46:40 (NB: This is the number of 1000000 seconds after Unix Epoch

print(datetime.datetime(1970, 1, 12, 5, 46, 40)) #Output >> 1970-01-12 05:46:40

print(datetime.datetime.fromtimestamp(time.time())) #Output >> 2025-12-12 00:14:11.641036

print(datetime.datetime(2015, 2, 27, 11, 13, 0, 604980)) #Output >>2015-02-27 11:13:00.604980



'''Timedelta Data Type:
The datetime module also provides a timedelta data type, which represents a 
duration of time rather than a moment in time.

Example: '''

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days)  #Output >> 11

print(delta.seconds) #Output >>36548

print(delta.microseconds) #Output >> 0

print(delta.total_seconds()) #Output >> 986948.0

print(str(delta)) #Output >> '11 days, 10:09:08'

'''NB: The datetime.timedelta() function takes keyword arguments weeks, days, hours, 
minutes, seconds, milliseconds, and microseconds. 
There is no month or year keyword argument because “a month” or “a year” is a variable amount of time 
depending on the particular month or year.'''


'''Pausing Until a Specific Date:
Example: 
'''
import datetime
import time
Christmas2025= datetime.datetime(2025, 12, 25, 0, 0, 0)
while datetime.datetime.now() < Christmas2025:
 print('Here we go')
 time.sleep(1)


 #December 15, 2025
 '''Review of Python’s Time Functions:
•	 A Unix epoch timestamp (used by the time module) is a float or integer 
value of the number of seconds since 12 am on January 1, 1970, UTC.

•	 A datetime object (of the datetime module) has integers stored in the 
attributes year, month, day, hour, minute, and second.

•	 The time.time() function returns an epoch timestamp float value of the 
current moment.

•	 The time.sleep(seconds) function stops the program for the amount of seconds specified by the seconds argument.

•	 The datetime.datetime(year, month, day, hour, minute, second) function 
returns a datetime object of the moment specified by the arguments. If 
hour, minute, or second arguments are not provided, they default to 0.

•	 The datetime.datetime.now() function returns a datetime object of the current moment.

•	 The datetime.datetime.fromtimestamp(epoch) function returns a datetime
object of the moment represented by the epoch timestamp argument.

•	 The total_seconds() method for timedelta objects returns the number of 
seconds the timedelta object represents.

'''


