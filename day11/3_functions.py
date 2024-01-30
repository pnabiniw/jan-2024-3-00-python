# Functions are the modules which takes input as parameters and returns output
# We can make user-defined functions in python
# We use "def" keyword to create a function in python


# Functions can be break down into two different parts
# 1. Function definition
# 2. Function Call

def addition(a, b):  # Function Definition
    """
    here a and b are the input numbers to the function. The function returns the sum of provided numbers
    . 'a' and 'b' are the parameters of this function
    """
    return a + b


result = addition(2, 3)  # function call. Here 2 and 3 are the arguments of the addition function
print(result)  # 10
