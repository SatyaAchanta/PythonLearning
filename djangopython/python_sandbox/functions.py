# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

def invite_user():
    """
    prints Welcome to django-python
    """
    print('Welcome to django-python')

# function with default parameter value
def welcome_user(name = 'Satya'):
    print('Welcome ' + name)

def get_sum(num1, num2):
    total = num1 + num2
    return total

invite_user()
welcome_user()
welcome_user('Achanta')
print(get_sum(11,12))


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

lambda_get_sum = lambda num1, num2 : num1 + num2
print(lambda_get_sum(2,12))
