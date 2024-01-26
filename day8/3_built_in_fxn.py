# all() and any()

# all() takes iterable as an input and return True / False as an output

print(all([1, 0, [1, 2], True]))  # False => because at least one of the data is Falsy i.e. 0
print(all([1, [1, 2], True]))  # True => because all the data are truthy


# any() takes iterable as an input and return True / False as an output
print(any([1, 0, [1, 2], True]))  # True => because at least one of the data is Truthy
print(any([0, [], False]))  # False => because all the elements are Falsy

