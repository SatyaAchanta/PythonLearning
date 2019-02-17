import sys
# Write a program that prompts for a file name, then opens that file and reads through the file, 
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.

'''fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    line = line.upper()
    print(line)'''

# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and 
# compute the average of those values and 
# produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
delimiterValue = ':'
currentSpamValue = 0.0
totalLines = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        totalLines = totalLines + 1
        # print(line.split(delimiterValue)[1].strip())
        currentSpamValue = currentSpamValue + float(line.split(delimiterValue)[1].strip())
print('Average spam confidence:', currentSpamValue/totalLines)