# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
x = 1           # int
y = 'Satya'     # string
z = 20.5        # float
w = True        # bool

# Multiple Assignments

a, b, name, is_awesome = (1, 2.5, 'Satya', True)

# check type

print(type(a))

# type casting
x = str(x)
print(type(x))