# Create a decorator function which changes a lower case input in a function to upper case

def to_upper(func):
    def inner_func(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return inner_func


# @to_upper
def get_message(msg):
    return msg


print(get_message("hello world"))


@to_upper
def another_messg(msg):
    return msg


print(another_messg("another message"))
