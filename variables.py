

# ============================================================
# Any line that starts with "#" is a comment

# IMMUTABLE TYPES

# int (integer)
my_int = 123

# float (real number)
my_float = 3.14

# bool (boolean)
my_boolean = True

# str (string)
my_string = 'Hello!'

# tuple
# defined using brackets "()"
my_tuple = (1, 2, 3)
another_tuple = (my_int, my_float, my_string)
# or callable
yet_another_tuple = tuple([1,2,3])


# MUTABLE TYPES

# list
my_list = ['hello', 2.4]
another_list = [my_int, my_float, my_string]

# set
# define
my_set = {'one', 'two', 'two'}
# or using "set" callable
another_set = set([my_int, my_float, my_string])


# OTHER TYPES

# None value/type. There's only one value for this type (None), which indicates that there's no value.
none_type = None

# CONVERTING BETWEEN TYPES

float_to_int = int(my_float)
int_to_float = float(my_int)

tuple_from_string = tuple(my_string)  # <== notice what happens when we call tuple on a string

# converting to boolean.
# Every object has its "truthy" value.
int_to_bool = bool(my_int)
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



# EXERCISE
# Try converting between types and see what happens
# Things to try:
# - any type to bool
# - tuple to list and vice versa
# - str to list or typle
# - int or float to str


# ============================================================

# Use this function to inspect the variable type:
# show_type(my_varible)

def show_type(value):
    print('Value {} is of type {}'.format(value, type(value)))

