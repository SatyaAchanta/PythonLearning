import sys
import re
# regex in python, "have to" import re


testString = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# ^ - matches the beginning of the line
if re.search('^From', testString):
    print('From found')

# . - matches any character ( period character )
if re.search('^F..m', testString):
    print('From found in dot notation regex')

# wild card characters * or +
# * indicates zero or more times
# + indicates one or more times
if re.search('^From.+@', testString):
    print(testString) 


# findall() and \S non-white space character
# find every email from the below string
emailContent = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
emailAddresses = re.findall('\S+@\S', emailContent)
print(emailAddresses) 
