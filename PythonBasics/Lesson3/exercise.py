import sys

# Write a program that uses input to prompt a user for their name and then welcomes them.
 print('Enter your name ')
userName = input()
print('Hello ' + userName)

# Write a program to prompt the user for hours and rate per hour to compute gross pay.
print('Enter your hours ')
totalHours = input()
print('Enter your rate ')
netRate = input()
grossPay = int(totalHours) * int(netRate)
print('Pay:', grossPay)

width = 17
height = 12.0
print(width//2)
print(width/2.0) # in this case the answer is 8.5 but not 8.0
print(height/3)
print(1+2 * 5)

# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
print("Enter temperature in Celsius")
celsiusTemparature = input()
farnheitTemparature = ( int(celsiusTemparature) * 9/5 ) + 32
print('Farnheit Temparature is ', farnheitTemparature)
