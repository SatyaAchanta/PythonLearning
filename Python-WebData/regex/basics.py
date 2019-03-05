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


# Combining searching and extracting
# here ([0-9.]+) indicates that "we need only floating point numbers from the string found"
# if we remove paranthesis around the [0-9.]+, we get the whole string
fileName = open('mbox-short.txt')
for line in fileName:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)

# extract time of a day from each mail message that starts with 'From '
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
currentFile = open('mbox-short.txt')
for currentLine in currentFile:
    currentLine = currentLine.rstrip()
    if currentLine.startswith('From '):
        y = re.findall('([0-9][0-9]:[0-9][0-9]:[0-9][0-9])', currentLine)
        if len(y) > 0:
            print(y)

''' 
^ Matches the beginning of the line.

$ Matches the end of the line.

. Matches any character (a wildcard).

\s Matches a whitespace character.

\S Matches a non-whitespace character (opposite of \s).

* Applies to the immediately preceding character(s) and indicates to match zero or more times.

*? Applies to the immediately preceding character(s) and indicates to match zero or more times in "non-greedy mode".

+ Applies to the immediately preceding character(s) and indicates to match one or more times.

+? Applies to the immediately preceding character(s) and indicates to match one or more times in "non-greedy mode".

? Applies to the immediately preceding character(s) and indicates to match zero or one time.

?? Applies to the immediately preceding character(s) and indicates to match zero or one time in "non-greedy mode".

[aeiou] Matches a single character as long as that character is in the specified set. In this example, it would match "a", "e", "i", "o", or "u", but no other characters.

[a-z0-9] You can specify ranges of characters using the minus sign. This example is a single character that must be a lowercase letter or a digit.

[^A-Za-z] When the first character in the set notation is a caret, it inverts the logic. This example matches a single character that is anything other than an uppercase or lowercase letter.

( ) When parentheses are added to a regular expression, they are ignored for the purpose of matching, but allow you to extract a particular subset of the matched string rather than the whole string when using findall().

\b Matches the empty string, but only at the start or end of a word.

\B Matches the empty string, but not at the start or end of a word.

\d Matches any decimal digit; equivalent to the set [0-9].

\D Matches any non-digit character; equivalent to the set [^0-9]. '''