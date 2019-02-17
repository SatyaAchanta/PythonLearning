import sys

# file open
# if not found , throws FileNotFoundError
# \n - new line character is considered as single character, so in string it's length is 1

try:
    fHand = open('sample-short.txt')
    # reading file
    fileContent = fHand.read()
    print(len(fileContent))
    print(fHand)
except ValueError:
    print('File not found', )


# searching through file
# iterating through the file and printing lines those start with From:

# rstrip() - strips all the whitespace on the rght side of the string
'''fileHandler = open('sample-short.txt')
for line in fileHandler:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# find string inside string

try:
    fileName = input('Enter File Name:')
    fileHandler = open(fileName)
    for line in fileHandler:
        line = line.rstrip()
        if line.find('@uct.ac.za') == -1: continue
        print(line)
except:
    print('File not found')'''


# writing files
# to write to a file, "w" should be used as second parameter for open method
# If the file already exists, opening it in write mode clears out the old data and starts fresh,
# so be careful! If the file doesn't exist, a new one is created.
# file object keeps track of where the control is left off
# so when file object is called again, the new data is appended at the end
newFile = open('sample-short-2.txt', 'w')
newFile.write('this is sample-short-2 file\n')
newFile.write('This is data appended at the end\n')
newFile.close()
newFileHandler = open('sample-short-2.txt')
for newLine in newFileHandler:
    newLine = newLine.rstrip()
    print(newLine)
    # print(repr(newLine)) - repr method prints line as a string, which contains all special characters as well
    # so to debug a file, repr method is useful to see where \n \t characters are existing