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
.get_highest_row() - returns the highest row number that contains data
.get_highest_column() - returns the highest column number that contains data

Example usage:
'''
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']