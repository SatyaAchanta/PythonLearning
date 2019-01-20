import sys

# variables
message = 'This is Python 3.7.x'
print(message)

#to know the type of varaible use type function
print(type(17))
print(type('Hello Python'))

# Operators and Operands
# Opeators are: + - * / // **
# ** is 'to the power of'
# // is to tell python to ignore decimal part of the remainder
# order of operations happen based on PEMDAS law
x = 10
y = 20
x = x + y
z = y//x
q = x ** 2
v = x/2
print(x)
print(z)
print(q)
print(v)


# string operations
# + Operator - concatenates two string and adds two integers
# When you multiply string with an integer 'x' the result will be string with 'x' times of same value in it
value1 = 'test'
value2 = 2
print(value1 * value2)

# Asking user for the input
# to get the user for the input, use input method
# questionAsked = input('enter today day\n')
# print('Today\'s day is', questionAsked)

# converting string to int - use int(string) method
yourFavNumber = input('Enter your fav number\n')
bffBirthday = int(yourFavNumber) + 16
print('BFF bday is',bffBirthday)

#Lists
countries = ['India', 'USA', 'NZ', 'AUS', 'Pakistan']
print(countries)
