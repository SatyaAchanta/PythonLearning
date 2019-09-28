# Python has functions for creating, reading, updating, and deleting files.

myFile = open('practice.txt', 'w')

print('File Nameis:', myFile.name)

myFile.write('This is python django learning course')
myFile.write('I like this course so far')
myFile.close()

myFile = open('practice.txt', 'r+')
print(myFile.read(100))
