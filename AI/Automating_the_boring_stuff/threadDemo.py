#December 15, 2025
'''Multithreading:
A single threaded program has only one finger. But a multithreaded program has multiple fingers. 
Each finger still moves to the next line of code as defined by 
the flow control statements, but the fingers can be at different places in the 
program, executing different lines of code at the same time

Example Usage:
'''
import threading, time
print('Start of program.')

def takeANap(): #A function that we want to use in a new thread
 time.sleep(5)
 print('Wake up!')

threadObj = threading.Thread(target=takeANap) # Creating a thread object
'''Notice that the keyword argument is target=takeANap, 
not target=takeANap(). This is because you want to pass the takeANap() function itself as the argument, 
not call takeANap() and pass its return value.'''

threadObj.start() #start executing the target function in the new thread.

print('End of program.')

'''Output:
Start of program.
End of program.
Wake up!

Explanation:
The reason Wake up! comes after it is that when threadObj.start() is called, 
the target function for threadObj is run in a new thread of execution. 

Think of it as a second finger appearing at the start of the takeANap() function. 

The main thread continues to print('End of program.'). 

Meanwhile, the new thread that has been executing the time.sleep(5) call, pauses for 5 seconds. 

After it wakes from its 5-second nap, it prints 'Wake up!' and then returns from the takeANap() function. 

Chronologically, 'Wake up!' is the last thing printed by the program.


Summary:
threadObj.start() creates a new environment aside the original environment in which the target is executed.
'''

#Passing argument to thread's target fuction:
import threading
threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})

threadObj.start()


'''Concurrency Issues
You can easily create several new threads and have them all running at the 
same time. 

But multiple threads can also cause problems called concurrency 
issues. 

These issues happen when threads read and write variables at the 
same time, causing the threads to trip over each other. 

Concurrency issues can be hard to reproduce consistently, making them hard to debug.

To avoid concurrency issues, never let multiple threads read or write the same variables.

When you create a new Thread object, make sure its target function uses only 
local variables in that function. This will avoid hard-to-debug concurrency issues in your programs.'''