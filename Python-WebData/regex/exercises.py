import re

# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.
# when you test your program on sample-data.txt file, result should be = 445833
# when tested on actual-data.txt, result should be ending with 685

fileName = input('Enter file name:')
fileHandler = open(fileName)
numbers = []
for line in fileHandler:
    if len(line) > 0:
        allNumbers = re.findall('([0-9]+)', line)
        for number in allNumbers:
            numbers.append(int(number))
print(sum(numbers))

