#December 16, 2025
'''Popen() fucntion:
The "P" in the Popen() fuction stands for  process

NB: If you want to start an external program from your Python script, pass 
the program’s filename to subprocess.Popen().

On  Windows, right-click  on the apllication icon on the desktop and select Porperties to view the directory and the  application's filename.
Copy the directory and the aplication name.

On OS X, ctrl-click the application and select show Package Contents to find the path to the executable files

NB: The launched program is not run in the same thread as your Python program.

Example Usage:
'''
import subprocess
subprocess.Popen('C:\\Program Files\\Google\\Chrome\\Application\\chrome_proxy.exe')

#WHenyou wan to open a file using Popen(), you first specify the app you wan to use and then follow it by the filename.

'''The Unix Philosophy:
It says that it’s better to write small, limited purpose programs that can interoperate, rather than large, 
feature-rich applications. The smaller programs are easier to understand, and by being interoperable, 
they can be the building blocks of much more powerful applications.'''