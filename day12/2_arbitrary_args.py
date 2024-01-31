# Arbitrary arguments are like an expandable bucket which can accept any number of parameters.
# *args and **kwargs are the arbitrary arguments in Python

# *args
def addition(*args):
    print(args)  # it gives tuple
    return sum(args)


print(addition(1, 2))  # 3
print(addition(1, 2, 3))  # (1, 2, 3)
print(addition(1, 2, 3, 4))  # (1, 2, 3, 4)
print(addition(1, 2, 3, 4, 5))  # (1, 2, 3, 4, 5)


# **kwargs
def subtract(**kwargs):
    print(kwargs)  # it gives dictionary  {"a": 10, "b": 2, "c": 1}
    return kwargs["a"] - kwargs['b']


subtract(a=2, b=1)  # 1
subtract(a=10, b=2, c=1)  # 8
subtract(a=7, b=3, c=2, d=1)  # 4


def addition(**kwargs):
    print(kwargs)  # it gives dictionary  {"a": 10, "b": 2, "c": 1}
    return sum(kwargs.values())


addition(a=2, b=1)  # 3
addition(a=10, b=2, c=1)  # 13
addition(a=7, b=3, c=2, d=1)  # 11
