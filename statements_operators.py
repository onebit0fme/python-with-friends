
# STATEMENTS AND OPERATORS

# "if" statement

# All types' values have a "truth" value. For example 0 is False, but 1, 2, 3, etc are True
# This is used when using "if" statements
if True:
    print('I am True')
if 1:
    print('1 is True')
if 'some text':
    print('some text is True')
# note that empty string is falsy
if not '': # note that "if not" negates the condition, so "if not True" evaluates not False
    print('empty string is not True, therefore it\'s False')

# "if elif else" statments
my_name = 'Rachel'

if my_name is 'Monica':
    print('my name is Monica')
elif my_name is 'Phoebe':
    print('my name is Phoebe')
else:
    print('my name is not Rachel nor Phoebe')

# arithmetic operators
# +, -, *, **, /, //, %
start = 1000

print('Substraction operator')
print(start - 123)
print('Addition operator')
print(start + 500)
print('Multiply operator')
print(start * 2)
print('Power operator')
print(start ** 2)
print('Division operator')
print(999 / 2)
print('Whole division oparator')
print(999 // 2)
print('Modulo operator')
print(999 % 10)

# Comparison operators. See https://docs.python.org/3/reference/expressions.html#comparisons for more details
# value comparison:
# ==, >, <, >=, <=, !=
my_value = 3
if my_value > 1:
    print('{} is greater than 1'.format(my_value))

if my_value == 3:
    print('{} equals to 3'.format(my_value))

if my_value < 100:
    print('{} is less than a 100'.format(my_value))

if my_value != 5:
    print('{} is not equal to 5'.format(my_value))


# "is" and "is not" identity test oparators
# This is different from "==" operator, where "is" operator checks if variables point to the same object, where "==" checks if variables have the same value.
x = [1,2,3]
y = [1,2,3]

# This is True
print(x == y)

# but this is False
print(x is y)

# membershipt "in" and "not in" operators
print('1 is in x')
print(1 in x)

print('10 is in y')
print(10 in y)

print('100 is not in x')
print(100 not in x)

