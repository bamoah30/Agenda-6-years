# November 14, 2025
'''openpyxl module:
This module allows you to read and write Excel files (with .xlsx extension) using Python.
Some of the key functions and methods include:
.load_workbook() - opens an existing Excel file
.get_sheet_names() - lists all sheet names in the workbook
.get_sheet_by_name() - accesses a specific sheet by name
.workbook.active - gets the active sheet
.title - gets or sets the title of the sheet
.cell(row, column) - accesses a specific cell
NB: For the cell() method, the arguments are integers and both row and column indices start at 1, not 0.
.value - gets or sets the value of a cell
.save() - saves the workbook to a file
.max_row() - returns the highest row number that contains data
.max_column() - returns the highest column number that contains data

Example usage:
'''
import openpyxl
wb = openpyxl.Workbook().save('example.xlsx')  # Create a new workbook and save it
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet'] # Access sheet by name
print(sheet.title)  # Output >>> Sheet
cell = sheet.cell(row=1, column=2) # Access cell B1
print(cell.value)  # Output >>> 42 Depending on the content of cell B1
sheet.cell(row=2, column=2, value='Hello')  # Set cell
wb.save('example_modified.xlsx')  # Save the workbook with changes
print(sheet.max_row)  # Output >>> Maximum row number that contains data
print(sheet.max_column)  # Output >>> Maximum column number that contains data

# November 17, 2025
'''Spreadsheet Concepts Review:
1. Import the openpyxl module.
2. Call the openpyxl.load_workbook() function.
3. Get a Workbook object.
4. Call the get_active_sheet() or get_sheet_by_name() workbook method.
5. Get a Worksheet object.
6. Use indexing or the cell() sheet method with row and column keyword arguments.
7. Get a Cell object.
8. Read the Cell object’s value attribute.

Note:Whenever you edit a spreadsheet you’ve loaded from a file, you should 
always save the new, edited spreadsheet to a different filename than the 
original. That way, you’ll still have the original spreadsheet file to work with 
in case a bug in your code caused the new, saved file to have incorrect or 
corrupt data
Pravtical Examples  and Formulas:
'''
import openpyxl
wb = openpyxl.Workbook() # Create a new workbook
sheet = wb.active if wb.active else wb.create_sheet() # Get the active sheet, or create one if none exists
sheet['A0'] = 200 # Set cell A1 to 200
sheet['A1'] = 300 # Set cell A2 to 300

sheet['A2'] = '=SUM(A0:A1)' # Set cell A3 to the formula that sums A1 and A2
wb.save('writeFormula.xlsx')

# To read the value of a formula cell, you need to set data_only=True when loading the workbook or else you'll get the formula itself
wbFormulas = openpyxl.load_workbook('writeFormula.xlsx')
sheet = wbFormulas.active if wbFormulas.active else wbFormulas.worksheets[0] # Get the active sheet or first sheet
print(sheet['A2'].value) # Output >>> '=SUM(A0:A1)'

wbDataOnly = openpyxl.load_workbook('writeFormula.xlsx', data_only=True) # Load workbook with data_only=True
sheet = wbDataOnly.active if wbDataOnly.active else wbDataOnly.worksheets[0] # Get the active sheet

print(sheet['A2'].value) # Output >>> 500 # Now it shows the calculated value of the formula
