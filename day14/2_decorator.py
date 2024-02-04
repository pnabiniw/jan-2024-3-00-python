# Decorators are the design patterns in python to solve problems in functional approach
# They are build on the basis of closures in python


# Criteria to create a decorator:
# 1. A function must have a nested function
# 2. The main function must take a function as an input
# 3. The nested function must use the function sent to the main function
# 4. The main function must return the inner / nested function


def decorator_fxn(func):
    def inner_fxn():
        print("Hello I am learning decorator")
        return func()
    return inner_fxn


@decorator_fxn
def message():
    print("This is main function")


# addition(2, 3)
# message = decorator_fxn(message)
message()
