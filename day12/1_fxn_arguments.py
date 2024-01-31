# There are 3 different types of arguments in python functions
# 1. Positional Arguments
# 2. Default Arguments
# 3. Arbitrary Arguments


# Positional Arguments
# These are the mandatory arguments in a function. They must be passed from the function call

def addition(a, b):  # function definition
    return a + b


result = addition(2, 3)  # function call
print(result)


# Default Arguments
# These are not the mandatory arguments in a function

def addition(a, b, c=0):  # function definition. Here "c" is the default argument
    return a + b + c


result = addition(2, 3)  # function call
print(result)
result = addition(2, 3, 4)
print(result)  # 9


# Variations of keyword arguments in function calls
result = addition(a=2, b=3, c=4)
print(result)  # 9

result = addition(b=3, a=2, c=4)
print(result)  # 9

result = addition(4, 5, c=3)
print(result)  # 12

# Positional arguments should always occur initially than the keyword arguments in function call
# Positional arguments should always occur initially than the default arguments in function definition
