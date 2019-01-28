import math
import random

# function example - no arguments
def printName():
    print('Karthik here')

printName()

# function with one argument
def welcomeUser(name):
    print('Hello', name, 'welcome to the world of Python')

welcomeUser('Karthik')

# void functions return a special value called 'None' which of type 'NoneType'

# method with return values
def assignUserId(name, userId):
    return name + userId

newUser = assignUserId('Karthik', '1991')
print('Welcome', newUser)
