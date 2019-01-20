import sys

# Conditionals

# Boolean operators are: ==, > , < , >=, <=
# two new other operators are 'is', and 'is not'
beer = 'Angry Orchard'
wine = 'Red Wine'
hardCider = 'Angry Orchard'
print('Is beer Wine ?', beer is wine)
print('Is beer not wine ?', beer is not wine)
print('Is hard cider a beer ?', hardCider is beer)

# Logical Operators: and , or , not
# The 'not' operator is quite different from 'is not'
# not operator checks the negation of the condition
# not operator is similar to ! in java

# In python any non-zero number is interpreted as True, for example
print(17 and True) # result is True
print(0 and True) # result is 0, but not false

# Conditional Execution
# if else condition
print('Enter number for positive check')
checkNumber = input()
if int(checkNumber) < 0:
    pass # pass keyword lets python know not to do anything but just pass to next statement
if int(checkNumber) > 0:
    print(checkNumber, 'is positive')
else:
    print('Negative number')

# if elif else
print('Enter Age ')
currentAge = input()
if int(currentAge) > 21:
    print('Adult')
elif int(currentAge) > 12:
    print('Teen')
else:
    print('Kid')

# try and except
print('Enter tire pressure')
tirePressure = input()
try:
    print('required tire pressure ', int(tirePressure) + 5)
except:
    print('Please Enter Number')
