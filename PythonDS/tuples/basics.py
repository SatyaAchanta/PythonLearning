import sys


# Tuples

# tuples can contains any type of values in it
# main difference is tuples are immutable
# we cannot modify the elements in the tuple, but
# we can replace whole tuple with another tuple
# a tuple is a comma separated list of values 
# ex: t = 'a','b','c','d','e','f' or t = ('a','b','c','d','e','f')

# Tuple declaration - without comma in declaration, python understands it as string
coffeeStores = ('sb',) # type of tuple
coffeeShops = tuple()

# coffeeStores = ('sb') - is type of string

# --------- Comparing Tuples -------------
# you can compare two tuples with < operator
# python starts with first element from each sequence, but not subsequent elements

(1,3,4) < (2,5,10) # compares corresponding indexed elements of 1,3,4 with 2,5,10
# prints False


# ------- Tuple Assignment --------
m = [ 'good morning', 'good afternoon', 'good evening', 'good night']
a,b,c,d = m
print(a) # prints good morning
print(b) # good afternoon
print(c) # good evening
print(d) # good night

# one of the best feature of the tuples is that tuples allow us to swap values of two variables in just one statement
favCoffee = 'Snickers'
favCandy = 'Decaf'
favCoffee, favCandy = favCandy, favCoffee
print(favCoffee)
print(favCandy)


# --------- Dictionaries and Tuples ------------
# Dictionaries allows us to get all items from a dictionary in the form of tuples
# the result value is list of tuples with first elements of each tuple as key and second element in value
myAddress = { 'street': 'Gold Side', 'County': 'washtenaw', 'zip code': 48197 }
print(list(myAddress.items()))

print((6,0,0) > (5,3,3))
