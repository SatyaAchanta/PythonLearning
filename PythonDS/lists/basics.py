import sys

countries =  ['usa', 'india', 'pakistan', 'canada']
states = ['Arizona', 'NewDelhi', 'Islamabad', 'Toronto']
ranks = [ 1,2,3,4,5]
print(countries[1]) # prints india
print(countries[-1]) # prints canada
# negative index represents reading indices from back
# -1 indicated the last value of the list

# in operator - A in B
# checks whether element A is existing in list B
print('UK' in countries) # prints False

# traversing a list
'''for country in countries:
    print(country)

for i in range(len(countries)):
    print(countries[i])'''

# List operations
# + operator - concatenates lists
places = countries + states
print(places)

# * operator - list * n-times
# repeats items in a list n number of times
print(places*2)


# list slicing
print(places[1:6]) # means items in places list from index 1 to index 5, exclusing index 6
print(places[:4]) # if you omits 1st index, it means means from index 0 to second index - 1 position
print(places[4:]) # if you omit second index, it means from index 1 to the end of the list
print(places[:]) # if you omit both indices, it means whole list

# -------------List methods------------
# list.append(), .extend(list2), .sort()
# pop(index) - deleted element at index and returns deleted element
# remove(element) - just deletes the element and returns None
# to remove more than one element, use del with sliced indices - del places[1:3] 
# deletes elements at 1 and 2 indices

# ----------- lists and functions ------------
# len(list), max(list), sum(list)

# ------------- lists and string -------------
sampleString = 'Sample'
sampleList = list(sampleString)
print(sampleList) # prints list that has each and every character in sampleString

fruit = 'banana'
fruit[0] = 'b'
print(fruit)