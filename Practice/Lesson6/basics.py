import math
import sys

# Loops and iterations

# while Loops
totalDays = 10
while totalDays > 0:
    print(totalDays)
    totalDays = totalDays - 1
print('All Days printed')

# for Loop
friends = ['Bobby', 'Crazy', 'Seema Bidda', 'Hemanth']
for friend in friends:
    print('Hey Buddy', friend, 'Welcome to 4808 Warriors')
print('Welcomed All')

# here it is 0 inclusive and 10 exclusive
for x in range(0, 10):
    print(x)
print('Finisged range for loop')

# find average of scores
scores =[10,20,30,40,50]
print(scores)
totalScore = 0
for score in scores:
    totalScore = totalScore + score
print(totalScore/len(scores))
# len(list) gives the size of the list
