# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

employees = ['Satya', 'Achanta', 'Venkata', 'Subramanya', 'Karthik']

for employee in employees:
    print('Current Employee: ', employee)

# break

for emploee in employees:
    if emploee == 'Achanta':
        print('End here')
        break
    print(emploee)


# continue
for emp in employees:
    if emp == 'Satya':
        continue
    print(emp)

# range

for i in range(len(employees)):
    print('Curr Employee is:', employees[i])

# While loops execute a set of statements as long as a condition is true.

rank = 1
while rank <= 10:
    print('Rank: ', rank)
    rank += 1
