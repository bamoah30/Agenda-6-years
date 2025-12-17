# November 25, 2025

'''CSV & JSON Intro:
CSV stands for “comma-separated values,” and CSV files are simplified 
spreadsheets stored as plaintext files. Python’s csv module makes it easy to 
parse CSV files.

JSON  is a for￾mat that stores information as JavaScript source code in plaintext files. 
JSON is short for JavaScript Object Notation. You don’t need to know the JavaScript programming language to use JSON files,
but the JSON format is useful to know because it’s used in many web applications.'''

'''CSV Module:
NB:Each line in a CSV file represents a row in the spreadsheet, and commas 
separate the cells in the row.
CSV are very different for spreadsheet because csv:
•	 Don’t have types for their values—everything is a string
•	 Don’t have settings for font size or color
•	 Don’t have multiple worksheets
•	 Can’t specify cell widths and heights
•	 Can’t have merged cells
•	 Can’t have images or charts embedded in them'''

'''Reader Objects
To read data from a CSV file with the csv module, you need to create a Reader
object. A Reader object lets you iterate over lines in the CSV file. 

Example:'''
import csv
exampleFile = open('.\\Automating_the_boring_stuff\\example.csv') #Make sure you have example.csv file the the specified directory
exampleReader = csv.reader(exampleFile) #Creates a reader object
exampleData = list(exampleReader)
print(exampleData)

#The csv module it preinstall with python, you don't have to pip install it

#Now you can acess the me,bers of the list using list indexing. For example:
print(exampleData[0][0]) #Output :4/5/2015 13:34

print(exampleData[6][1]) # Output : Strawberries

'''Writer Objects
A Writer object lets you write data to a CSV file. To create a Writer object, you 
use the csv.writer() function.

Example Usage:'''

import csv

outputFile = open('output.csv', 'w', newline='') # the newline='' ensures that when writing rows (especially with the csv module), Python doesn’t insert extra blank lines between them.
outputWriter = csv.writer(outputFile) 
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham']) # Values for row 1
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham']) # Values for row 2
outputWriter.writerow([1, 2, 3.141592, 4]) #Values for row 3

outputFile.close()

#November 26, 2025
'''Delimiter and Lineterminator keyword Argument:

Delimiter are used to specify the seperator between cells of the same row.
Lineterminator are used to specify the separator between rows:

Example Usage:
'''
import csv
csvFile = open('example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
csvFile.close()


# November 27, 2025
'''JSON and APIs:
JSON is the native way that JavaScript programs 
write their data structures and usually resembles what Python’s print()
function would produce.

An example of data foramtted in JSON:
{"name": "Zophie", "isCat": true, 
 "miceCaught": 0, "napsTaken": 37.5, 
 "felineIQ": null} 
 
JSON is useful to know, because many websites offer JSON content as a way 
for programs to interact with the website. This is known as providing an application programming interface (API). 
Accessing an API is the same as accessing any other web page via a URL. 
The difference is that the data returned by an API is formatted (with JSON, for example) for machines; 
APIs aren’t easy for people to read.

Some Uses APIs:
•	 Scrape raw data from websites. (Accessing APIs is often more convenient 
than downloading web pages and parsing HTML with Beautiful Soup.)

•	 Automatically download new posts from one of your social network 
accounts and post them to another account. For example, you could 
take your Tumblr posts and post them to Facebook.

•	 Create a “movie encyclopedia” for your personal movie collection by 
pulling data from IMDb, Rotten Tomatoes, and Wikipedia and putting 
it into a single text file on your computer.

The JSON Module:
Python’s json module handles all the details of translating between a string 
with JSON data and Python values for the json.loads() and json.dumps() functions. 
JSON can’t store every kind of Python value. It can contain values 
of only the following data types: 
strings, integers, floats, Booleans, lists, 
dictionaries, and NoneType. 

JSON cannot represent Python-specific objects, 
such as File objects, CSV Reader or Writer objects, Regex objects, or Selenium 
WebElement objects.'''

'''Reading JSON with the loads() Function:
To translate a string containing JSON data into a Python value, pass it to the json.loads() function. 

NB:The name means “load string,” not “loads.”

Example Usage:'''

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue) # Output:{'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

'''Warning:
After you import the json module, you can call loads() and pass it a string of JSON data. 

NB: JSON strings always use double quotes. It will return that data as a Python dictionary. 
Python dictionaries are not ordered, so the key-value pairs may appear in a different order when you 
print jsonDataAsPythonValue'''

'''Writing JSON with the dumps() Function:
The json.dumps() function (which means “dump string,” not “dumps”) will 
translate a Python value into a string of JSON-formatted data

Example Usage:
'''
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
import json
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)#Output >>>{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }