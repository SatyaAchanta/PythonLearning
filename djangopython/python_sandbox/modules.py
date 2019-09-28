# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# core modules
import datetime
import time
from datetime import date
from time import time

# pip modules
# command : pip3 install camelcase
import camelcase

# custom module
import validator
from validator import validate_email

today = date.today()
print(today)

timeStamp = time()
print(timeStamp)

print(camelcase.__file__)

camelString = camelcase.CamelCase()
text = 'hello world'
print(camelString.hump(text))

email = 'personal4mylife@gmail.com'
if validate_email(email):
    print('valid email')
else:
    print('Invalid email')
