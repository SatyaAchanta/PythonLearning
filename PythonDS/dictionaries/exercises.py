import sys

# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

try:
    filename = input('Enter File Name:')
    fileHandler = open(filename)
    allSenders = dict()
    maxValue = 0
    maxSender = ''
    for line in fileHandler:
        line = line.rstrip()
        currentListOfWords = line.split()
        if line.startswith('From '):
            if not currentListOfWords[1] in allSenders:
                allSenders[currentListOfWords[1]] = 1
            else:
                allSenders[currentListOfWords[1]] = allSenders[currentListOfWords[1]] + 1

    # greatestSender = max(allSenders, key = allSenders.get)
    # print(greatestSender, allSenders[greatestSender])
    for sender in allSenders:
        if allSenders[sender] > maxValue:
            maxSender = sender
            maxValue = allSenders[sender]
    print(maxSender, maxValue)
except:
    print('File Not Found')