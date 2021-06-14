#  xlwings - Make Excel fly: Interact with Excel from Python and vice versa.

# PyPi: https://pypi.org/project/xlwings/
# Docs: https://docs.xlwings.org/en/stable/quickstart.html

# pip install xlwings


# Establish a connection to a workbook:
import xlwings as xw

wb = xw.Book()  # this will create a new workbook
wb = xw.Book('FileName.xlsx')  # connect to a file that is open or in the current working directory
wb = xw.Book(r'C:\path\to\file.xlsx')  # on Windows: use raw strings to escape backslashes


#  Jupyter Notebooks: Interact with Excel
# https://docs.xlwings.org/en/stable/jupyternotebooks.html#jupyternotebooks
