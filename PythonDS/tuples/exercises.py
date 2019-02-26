import sys


# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Split with @
# Split with spaces
# then - uct.ac.za Sat Jan  5 09:14:16 2008
# the 4th index will be the time
# then add it as key-value pair to dictionary
# from dictionaries , get a tuple and then sort by keys

try:
    fileName = input('Enter file:')
    fileHandler = open(fileName)
    emailHours = dict()
    for line in fileHandler:
        line = line.rstrip()
        if line.startswith('From '):
            fromAddress = line.split()
            currentTime = fromAddress[5]
            currentHours = currentTime.split(':')[0]
            if not currentHours in emailHours:
                emailHours[currentHours] = 1
            else:
                emailHours[currentHours] = emailHours[currentHours] + 1
    hoursList = list(emailHours.items())
    hoursList.sort()
    for key, value in hoursList:
        print(key, value)
except:
    pass
