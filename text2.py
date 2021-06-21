# The string is enclosed in double quotes if the string contains a single quote and no double quotes, otherwise it is enclosed in single quotes.print('"Isn\'t," she said.')
print '"Isn\'t," she said.'

# \n means newline
s = 'First line.\nSecond line.'  
print(s)  # without print, \n is included in the output

# If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote
