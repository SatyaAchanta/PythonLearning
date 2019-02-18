import sys

# dictionaries

# creating new dictionary
# the order of items in dictionary is unpredictable
# items might not retrieved in the same order we inserted
allStatesAndZipCodes = dict()
allAreasAndZipCodes = { 'Washtenaw': 48197, 'Ann Arbor': 48105, 'Ypsilanti': 48198 }
# print(allAreasAndZipCodes['Washtenaw'])

len(allAreasAndZipCodes) # gives the length of the dictionary

# in operator - searches for key in dictionary
print('washtenaw' in allAreasAndZipCodes) # should print False becuase of case-sensitive nature

# to read all the values from dictionary
print(allAreasAndZipCodes.values())

stuff = dict()
print(stuff.get('candy',-1))
