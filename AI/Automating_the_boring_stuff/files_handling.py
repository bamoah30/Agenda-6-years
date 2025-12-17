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

#November 3, 2025

'''Old Style String Formatting with the % Operator
You can use the % operator to format strings in Python.
The % operator is used with a format string on the left side
and the value or values to be formatted on the right side.

NB: This old style string formatting is mostly used in Python 2.x versions.
The f-string formatting and the str.format() method are preferred in Python 3.x versions.

Example usage:'''
name = 'Alice'
age = 30
formatted_string = 'My name is %s and I am %d years old.' % (name, age)
print(formatted_string) #Output: My name is Alice and I am 30 years old


'''The .pyw File Extension
The .pyw file extension is used for Python scripts that are intended to run without a console window.
When you run a .pyw file, it does not open a command prompt or terminal window.
This is useful for GUI applications where you do not want a console window to appear.
'''

''' What Is a Batch File?
    - A file with the `.bat` or `.cmd` extension.
    - When run, it executes each command line by line in the Windows shell.
    - Think of it as a macro for repetitive command-line tasks.

Example: Simple Batch File commands
    @echo off
    echo Hello, Bernard!
    pause

- `@echo off`: Hides command echoing for cleaner output.
- `echo`: Prints text to the screen.
- `pause`: Waits for user input before closing the window.

 Common Uses
- Automating software builds or deployments
- Running scripts or programs in sequence
- Setting environment variables
- Backing up files or folders
- Launching applications with specific parameters

 How to Create One
1. Open Notepad.
2. Write your commands.
3. Save the file with a `.bat` extension (e.g., `startup.bat`).
4. Double-click to run it.

 Limitations
- Only works on Windows.
- Limited logic and error handling compared to full scripting languages like PowerShell or Python.
'''

#paperclip Module


#Organizing Files:
'''The shutil module (shell utilities) 
can be used to copy, move, rename, and delete files and folders.

shutil.copy(source,destination):copy the file at the source path to the destination path.
If the destination path is a folder, the file will be copied into that folder using the
same filename as the source file. If the destination path is a file, the source file will be copied
to the destination path with the new name.

shutil.copytree(source, destination): Copies the folder at the source path to the destination path,
including all the files and folders it contains. The destination path must not already exist.

shutil.move(source, destination): Moves the file or folder at the source path to the destination path.
This can also be used to rename a file or folder by moving it to the same path with a different name.
When moving  files or folders to a destination that does not exist, shutil.move() will rasie an error if the path directory does not exist.

NB 1: Both shutil.copy() and shutil.copytree() will overwrite existing files and folders without warning.
NB 2: Always make sure you import the shutil module before using it.



Example usage:
'''
import shutil
shutil.copy('bacon.txt', 'bacon_copy.txt') #Copies the bacon.txt file to bacon_copy.txt in the cwd

shutil.copytree('Automating_the_boring_stuff', 'Automating_the_boring_stuff_backup')
#Copies the Automating_the_boring_stuff folder to a new folder named Automating_the_boring_stuff_backup in the cwd

#Creates the new folder waffles inside walnut folder inside delicious folder in the C: drive
os.makedirs('C:\\delicious\\walnut\\waffles') 

shutil.move('bacon_copy.txt', 'C:\\delicious\\walnut\\waffles\\bacon.txt')
#Moves the bacon.txt file to the waffles folder inside walnut folder inside delicious folder in the C: drive



'''Permanently Deleting Files and Folders.
You can permanently delete files and folders with the os and shutil modules.
You can also safely delete files and folders with the send2trash module.

The os module provides functions for deleting files and  empty folders.
To delete non-empty folders, you need to use the shutil module.
The shutil module, when used to delete folders, deletes all the contents of the folder permanently.

To prevent accidental data loss, 
it is recommended to use the send2trash module, which moves files and folders to the recycle bin or trash
instead of permanently deleting them.

Commands:
os.umlink(path): Deletes the file at the path.
os.rmdir(path): Deletes the folder at the path. The folder must be empty before deletion.
shutil.rmtree(path): Deletes the folder at the path and all its contents. Use with caution!
senda2trash.send2trash(path): Moves the file or folder at the path to the recycle bin or trash.

NB: send2trash module is not included in the standard library. You need to install it using pip:
pip install send2trash

Example usage:
'''
import os
import shutil
import send2trash


#Deletes the files_handling.py file permanently from the path specified.
os.unlink('D:\\Tech and AI\\Python_2025\\Agenda-6-years\\Automating_the_boring_stuff_backup\\files_handling.py') 


#Deletes the waffles folder permanently. The folder must be empty before deletion.
#os.rmdir('C:\\delicious\\walnut\\waffles') 

shutil.rmtree('C:\\delicious') #Deletes the delicious folder and all its contents permanently.

#Moves the bacon.txt file to the recycle bin or trash instead of permanently deleting it.
send2trash.send2trash('D:\\Tech and AI\\Python_2025\\Agenda-6-years\\Automating_the_boring_stuff_backup\\regexes.py')

#Moves the Automating_the_boring_stuff_backup folder to the recycle bin or trash instead of permanently deleting it.
send2trash.send2trash('D:\\Tech and AI\\Python_2025\\Agenda-6-years\\Automating_the_boring_stuff_backup') 

#November 4, 2025


'''os.walk() Function
The os.walk() function generates the file names in a directory tree by walking the tree either top-down or bottom-up.
For each directory in the tree rooted at the directory top (including top itself), it produces a 3-tuple (dirpath, dirnames, filenames).
- dirpath: A string, the path to the directory.
- dirnames: A list of the names of the subdirectories in dirpath (excluding '.' and '..').
- filenames: A list of the names of the non-directory files in dirpath.'''


'''Reading ZIP Files
To read the content of a zip files, you must create a ZipFile object.
First you must import zipfile
Then create the object by calling the ZipFile() function form the zipfile module.
Afterwards call the namelist() method on the object to see the content of the zip file.

Example Usage:

'''
import zipfile
#examplezip =zipfile.ZipFile('example.zip') #Creates the ZipFile object for the example.zip file
#print(examplezip.namelist()) #Prints the list of files and folders in the zip file

'''Extracting from Zip FIles using the extractall() method and extract() method
There are two methods for extracting files from a zip file:

 extract() Method:
- Purpose:Extracts a single file from the ZIP archive.

- Usage: examplezip.extract(member, path=None)
NB: The examplezip in the above usage refers to the ZipFile object.

  - member: The name of the file to extract.
  - path: Optional destination folder.

extractall() Method
- Purpose: Extracts all files from the ZIP archive.
- Usage: examplezip.extractall(path=None, members=None)

NB: The zip in the above usages refers to the ZipFile object.
- path: Optional destination folder.
- members: Optional list of specific files to extract.

When to Use What
- Use extract() if you only need one specific file.
- Use extractall() if you want to unpack the entire archive.
'''