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