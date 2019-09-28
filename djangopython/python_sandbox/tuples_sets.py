# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
sports_tuples = ('Cricket', 'vball', 'tennis')
print(sports_tuples[1])

'''
tuples with only one value should be ending with trailin comma, otherwise
the value inside the tuple is considered as string
'''

cricket_tuples = ('Fielding')

'''
the below line causes the error because tuples cannot be changed
tuples are immutable
'''
# cricket_tuples[0] = ('Batting')
# print(cricket_tuples)

'''
when you access cricket_tuples[0] you get 'Fielding' as otherwise it will be considered as string
'''
print(cricket_tuples[0])
print(len(cricket_tuples))

cricket_tuples_2 = ('Fielding',)
print(cricket_tuples_2[0])
print(len(cricket_tuples_2))


# A Set is a collection which is unordered and unindexed. No duplicate members.
# set is created using curly braces

coding_lang_set = {'java', 'angular', 'python', 'django'}
print(coding_lang_set)

coding_lang_set.add('c#')
print(coding_lang_set)

print('C#'.casefold() in coding_lang_set)

# remove from set
coding_lang_set.remove('c#')

print(coding_lang_set)