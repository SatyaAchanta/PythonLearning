# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 5

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

if x < y:
    print(f'{x} is less to {y}')
elif  x==y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is greater to {y}')

# Logical operators (and, or, not) - Used to combine conditional statements

if x > y and x/y==2:
    print(f'{x} is multiple of {y}')
else:
    print(f'{x} is not multiple of {y}')


if not y > x:
    print(f'{x} is greater than {y}')

# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

scores = [15, 26, 12, 77, 37, 100]

if 100 not in scores:
    print('No one scored century')
else:
    print(100 in scores)
    print('we had centurion today')


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
