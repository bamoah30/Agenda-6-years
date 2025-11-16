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
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
print(sheet.title)  # Output >>> Sheet1
cell = sheet.cell(row=1, column=2) # Access cell B1
print(cell.value)  # Output >>> 42 Depending on the content of cell B1
sheet.cell(row=2, column=2, value='Hello')  # Set cell
wb.save('example_modified.xlsx')  # Save the workbook with changes
print(sheet.max_row)  # Output >>> Maximum row number that contains data
print(sheet.max_column)  # Output >>> Maximum column number that contains data
