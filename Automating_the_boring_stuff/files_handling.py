#October 30, 2025
import os

"Folders = Directory"

#In windows root folder = C:\ = C: drive
#On OS X and Linux, the root folder is /.D
# DVD drive or USB thunmb drive appears differently on different operating systems.
# On Windows, they appear as a lettered root drives such as:
# D:\ or E:\
# On OS X, they appear as new folders under the /Volumes folder.
# On Linux, they appear as new folders under the /mnt ("mount") folder.
# Folder names and filenames are not case sensitive on Windows and OS X, they are case sensitive on Linux.

 

#Why do we need file extensions and what are the main purpose of using files extensions:
"""File extensions are used to show the file format or type and it helps the operating system
To choose which app opens or renders it"""

'''os.path.join()
To solve the issue of using backslahes on Windows and forward slashes on OS X and Linux,
we use the os.path.join()
You pass in the string values of individual files and folder names in your path
os.path.join() will return a string with the path using the correct path separator.
Example usage:'''

dir= os.path.join("usr", "bin", "spam")
print(dir) #prints usr\bin\spam. Note: I'm using Windows

'''The Current working Directory or cwd
Any filenames or paths that do not begin with the root folder 
are assunmed to be under the cwd
os.getcwd() function is used to get the current working directory as a string value.
You can alos change the cwd with the os.chdir().
Example usage:'''
print(os.getcwd()) # For me, yours might be different. Output: d:\Tech and AI\Python_2025\Agenda-6-years

'''Absolute vs. Relative Paths
Two ways to specify file path:
1.Absolute path : Begins with root folder
2.Relative path: Relative to the program's cwd

NB: There's also dot(.) and dot-dot(..) folders.
Dot(.): Shorthand for this directory
Dot-dot(..): Parent folder'''


'''Making New Folder
os.makedirs('C:\\delicious\\walnut\\waffles')
This will make the newfolder, waffles inside walnut folder inside  delicious folder
which is also inside the  C: root folder'''

#os.path Module: Offers many methods for handling files

'''Handling Absolute and Relative Paths
os.path module provides function for returning the absolute path of 
a relative path and for checking whether a given path is absoulte.

os.path.abspath(path): Used for returning the absolute path of the argument, path

os.path.isabs(path): Returns True if path is absolute and False otherwise.

os.path.relpath(path, start): Returns string of relative path from the start path to path. The default start value is cwd.

Example usage:'''

dir = os.path.abspath('.')
print(dir) #Output for my computer: d:\Tech and AI\Python_2025\Agenda-6-years

dir = os.path.abspath('.\\Scripts')
print(dir) #Output:d:\Tech and AI\Python_2025\Agenda-6-years\Scripts

dir = os.path.isabs(os.path.abspath('.'))
print(dir) #Output : True

dir = os.path.relpath('d:\\Windows') # For here make sure you start with the drive you are working in or you will get ValueError
print(dir) #Output: ..\..\..\Windows


#October 31, 2025
'''os.path.dirname(path): Returns everything that comes before the last slash in path
os.path.basename(path): returns everything that come after the last slash in path
Example:'''
path = 'C:\\Windows\\System32\\calc.exe'
dir = os.path.basename(path)
print(dir) #Output: calc.exe

dir = os.path.dirname(path)
print(dir) #Output: C:\Windows\System32

#If you want  to generate a tuple of the files and folders in a file path into a tuple sperated at backslahes:
print(dir.split(os.path.sep)) #Output: ['C:', 'Windows', 'System32']



'''Finding File Sizes and Folder Contents:
os.path.getsize(path): Returns the size in bytes of the file in the path argument.

os.listdir(path): Returnds a list of filename strings for eqch files in the path argument.

Example usage: '''
print(os.path.getsize(os.getcwd())) #Output:4096
print(os.listdir(os.getcwd())) #Output: ['.git', 'assets', 'Automating_the_boring_stuff',
#                                       'Fundamentals_python', 'Journal', 'Maths', 'README.md', 'Roadmaps']


'''Checking Path Validity:
os.path.exists(path): Returns True if the path exists or False otherwise.
os.path.isfile(path): Returns True if the path exists and is a file. False otherwise.
os.path.isdir(path): Returns True if the path exists and is a folder. False otherwise.
Example usage:'''
print(os.path.exists('d:\\Tech and AI\\Python_2025\\Agenda-6-years\\README.md'))                #Output: True
print(os.path.exists('d:\\Tech and AI\\Python_2025\\Agenda-6-years\\non_existing_file.txt'))     #Output: False
print(os.path.isfile('d:\\Tech and AI\\Python_2025\\Agenda-6-years\\README.md'))                   #Output: True
print(os.path.isdir('d:\\Tech and AI\\Python_2025\\Agenda-6-years\\Automating_the_boring_stuff')) #Output: True
print(os.path.isdir('d:\\Tech and AI\\Python_2025\\Agenda-6-years\\README.md'))                    #Output: False


#November 1, 2025


'''Opening FIles with the open() Function:
The open() method is used to create a file object in a certain mode. 
The default mode is read ('r'): Which does not allow editting the content of the file object created.
Other modes are:
1. write mode ('w'): This is used to write contents into the file object created.
This mode when used can create a file if the files does not exists and will override the content of a file when used.
The write mode does not end a string with a new line. Users must add the newline themselves.

2. The append ('a')  mode:
This mode is used when you want to add content to the existing content of the file object.
It will also create a new file when passed as the second argument of the open() function.

NB: After handling files, used the close() method on the file object.

Example usage:
'''
baconFile = open('bacon.txt', 'w') 
baconFile.write('Hello world!\n')
baconFile.close()


baconFile = open('bacon.txt', 'a') 
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()

print(content) #Output: Hello world!
#                       Bacon is not a vegetable.


#Alternatively, we can also use the readlines method to generate a list of strings contianing the content
#of the file object. Where each string represents on line of the text.
#Example:

objectFile = open('bacon.txt')
content= objectFile.readlines()
print(content) #Output: ['Hello world!\n', 'Bacon is not a vegetable.']



'''Saving Variables with the shelve Module
The shelve module enable us to save varaibles
in our python scripts to binary shelf files.
Example:
'''
import shelve
shelfFile = shelve.open('mydata') #Creates the shelf file names mydata
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats # Creates a dictionary object in the mydata file
shelfFile.close()

#To access the content of the shelf file:
shelfFile =shelve.open('mydata')
print(shelfFile['cats']) #Output: ['Zophie', 'Pooka', 'Simon']
shelfFile.close()

#Just like dictionaries, you can access the keys and values of the shelf file:

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys())) #Output: ['cats']


print(list(shelfFile.values())) #Output: [['Zophie', 'Pooka', 'Simon']]
shelfFile.close()