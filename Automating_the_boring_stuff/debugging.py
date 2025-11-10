#November 5, 2025

'''Traceback:
A treasure of trove error information produced by pythin whe it encounters an error.
Traceback includes:
1.Error message
2.The line number of the line that caused the error
3.The sequence of the function calls that led to the error.
NB: The sequence of calls is known as the call stack
'''


'''Assertion:
An assertion is a sanity check to make sure the code isn't doing something obviously wrong.
These sanity checks are performed by assert statements.
If the sanity checks fails, then an AssertionError is raised.
An assert statement consists of the following:
1.The assert keyword
2.A condition that evaluaters to True or False
3.A comma
4. A string to display when the condition is false.
Example Usage:
'''
def kelvin_to_celsius(kelvin: float) -> float:
    assert kelvin >= 0, "Kelvin temperature cannot be negative"
    celsius = kelvin - 273.15
    return celsius  

print(kelvin_to_celsius(300))  # Valid input
#print(kelvin_to_celsius(-5))  # This will raise an AssertionError



#November 10, 2025

'''Using the Logging Module:
If you'v ever used the print() function to help you see the outcome of of a code befoere deploying,
You've had experience with hoe the logging module behaves.
However,it is advisable to use the logging module instead of the print function because of how easy
it is to disable the it.
We do have about 5 logging levels:
1.DEBUG:Detailed information,typically of interest only when diagnosing problems. Called using logging.debug()
2.INFO:Confirmation that things are working as expected. Called using logging.info()    
3.WARNING:An indication that something unexpected happened,or indicative of some problem in the near future(such as 'disk space low').Called using logging.warning()
4.ERROR:Used to log an error that caused the program to fail.Called using logging.error()
5.CRITICAL:A serious error,indicating that the program itself may be unable to continue running.Called using logging.critical()

NB: 1.You can  specify the logging level when you configure the logging module using logging.basicConfig()
2.Specifying a logging level of INFO will disable all the logging messages at the DEBUG level. 
3.Specifying a logging level of WARNING will disable all the logging messages at the DEBUG and INFO levels.
4.Specifying a logging level of ERROR will disable all the logging messages at the DEBUG,INFO,and WARNING levels.
5.Specifying a logging level of CRITICAL will disable all the logging messages at the DEBUG,INFO,WARNING,and ERROR levels.
6.You can disable all logging messages by calling logging.disable(logging.CRITICAL)


Example Usage:'''

import logging
from typing import *
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s') #Basic Configuration of the logging module
#logging.disable(logging.CRITICAL) #This is used to disable the logging module

logging.debug('Start of program') 
def new_factorial(n: int) -> Optional[str] :
    logging.debug('Start of factorial(%d)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%d)' % (n))
    return f"The factorial of {n} is {total}"


print(new_factorial(5))

logging.debug('End of program')
