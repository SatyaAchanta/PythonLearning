# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# simple dictionary
person = {
    'fname': 'Satya',
    'lname': 'Achanta',
    'age': 28
}

print(person)

# another way to create dictionaries
favorites = dict(sports='Cricket', music='Country', food='Indian')
print(favorites)

# access value from dictionaries
print(favorites['sports'])
print(favorites.get('food'))

person['mobile'] = '734-734-7343'

print(person)

print(person.keys())
print(person.items())

# remove item from dict
del person['mobile']
print(person)

# list of dict

people = [
    person,
    favorites
]

print(people[0]['fname'])