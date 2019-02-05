import sys

# string slices
# a segment of a string is a slice
'''laptopName = "MacBook Air 2014"

print(laptopName[4]) # prints character at 4th index in the string

# prints chars from including 0 to 4 ( excluding 5 )
print(laptopName[0:5]) # prints Macbo

print(laptopName[:5]) # same output as line 8
print(laptopName[6:]) # prints everything from index 6 to last

# ---- STRINGS IN PYTHON ARE IMMUTABLE ----

# in operator
# it takes two strings and checks whether 2nd string contains first string
print('seed' in 'banana')

# string methods

currentMonth = 'January'
type(currentMonth) # gives the type of the currentMonth
dir(currentMonth) # gives all the method avaiable in currentMonth

# upper case and lowe case conversions
print(laptopName.upper())
print(laptopName.lower())'''

# parsing strings
stringToParse = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
delimiterValueIndex = stringToParse.find('@')
firstSpaceIndexFromDelimiterValue = stringToParse.find(' ', delimiterValueIndex)
parsedString = stringToParse[delimiterValueIndex+1 : firstSpaceIndexFromDelimiterValue]
print(parsedString)

# format operator
# lets you to replace values inside strings
# %d - for interger , %s - for string, %g - floating point
monthName = 'February'
year = 2019
date = 3
portinOfTheYear = 2/10
print('we are in %d year %s month %d date and %g way through' % (year, monthName, date, portinOfTheYear))