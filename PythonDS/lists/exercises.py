import sys

# Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.
'''try:
    fname = input("Enter file name: ")
    fh = open(fname)
    allWords = list()
    for line in fh:
        line = line.rstrip()
        currentListOfWords = line.split()
        for currentWord in currentListOfWords:
            if not currentWord in allWords:
                allWords.append(currentWord)
except:
    print('File not found')

allWords.sort()
print(allWords)'''

# exercise 2
# Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'
try:
    fileName = input('Enter file name:')
    fileHandler = open(fileName)
    allEmails = list()
    for line in fileHandler:
        line = line.rstrip()
        if line.startswith('From') and not line.startswith('From:'):
            currentLineAsList = line.split()
            allEmails.append(currentLineAsList[1])
            print(currentLineAsList[1])
    print("There were", len(allEmails), "lines in the file with From as the first word")
except:
    print('File not found')