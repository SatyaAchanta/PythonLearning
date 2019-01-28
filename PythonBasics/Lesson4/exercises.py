import sys

# exercises

# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

print('Enter your total hours ')
totalHours = input()
print('Enter your rate ')
netRate = input()

try:
    if int(totalHours) > 40:
        print(int(totalHours) * 1.5 * int(netRate))
    else:
        print(int(totalHours) * int(netRate))
except Exception as e:
    print('Please Enter Number')

# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
# < 0.6     F
print('Enter your grade')
acquiredGrade = input()

try:
    if float(acquiredGrade) >= 0.9:
        print('A')
    elif float(acquiredGrade) >= 0.8:
        print('B')
    elif float(acquiredGrade) >= 0.7:
        print('C')
    elif float(acquiredGrade) >= 0.6:
        print('D')
    else:
        print('F')

except Exception as e:
    print('Please Enter Number')
