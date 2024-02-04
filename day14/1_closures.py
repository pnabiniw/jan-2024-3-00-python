# Closure is one of the functional approaches of solving a problem in python
# There are few criteria to be consider a function as closure in Python

# 1. A function must have another nested function
# 2. The function must take at least one argument as an input and this argument should be used inside the nested
# function
# 3. The main function should return the nested function


def closure_fxn(msg):  # main
    def inner_fxn():  # nested
        return msg
    return inner_fxn


result = closure_fxn("Hello. I am learning closure")
print(result())
