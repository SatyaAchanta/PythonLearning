import sys
import math

# Write a program which repeatedly reads numbers until the user enters "done". 
# Once "done" is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
'''currentValue = 0
currentTotal = 0
currentCount = 0
currentAverage = 0
while True:
    currentInput = input('Enter Your Number: ')
    try:
        if currentInput == 'done':
            break
        else:
            currentTotal = int(currentInput) + currentTotal
            currentCount = currentCount + 1
            currentAverage = currentTotal/currentCount
    except Exception as e:
        print('Invalid input')
print(currentTotal, currentCount, currentAverage)

# Write another program that prompts for a list of numbers as above and 
# at the end prints out both the maximum and minimum of the numbers instead of the average.
# TODO

# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.'''
allNumbers = []
while True:
    currentInput = input('Enter Your Number: ')
    try:
        if currentInput == 'done':
            break
        else:
            allNumbers.append(int(currentInput))
    except Exception as e:
        print('Invalid input')
print('Maximum is',max(allNumbers))
print('Minimum is', min(allNumbers))