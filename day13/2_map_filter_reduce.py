# map(), filter() and reduce() are the higher order functions

# 1. map(func, iterable)
# map() function takes function as the first parameter and iterable as the second parameter
# It changes the current form of the data in the iterable to a new form
# Count of the elements in the iterable is same initially and after mapping

data = [2, 3, 4, 5, 6]


def to_squared(e):
    return e ** 2


result = map(to_squared, data)
print(list(result))   # [4, 9, 16, 25, 36]


# 2. filter(func, iterable)
# filter() function takes function as the first parameter and iterable as the second parameter
# It picks / selects the elements from data in the iterable to according to the function definition
# Count of the elements in the iterable may not be same initially and after filtering

data = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]


def pick_vowel(element):
    return element in ["a", "e", "i", "o", "u"]


vowel_data = filter(pick_vowel, data)
print(list(vowel_data))  # ["a", "e", "i"]


# reduce(func, iterable)
# reduce() function takes function as the first parameter and iterable as the second parameter
# It reduces the entire iterable to a single data
# Result is a single item (not an iterable)


from functools import reduce

data = [1, 2, 3, 4, 5]


def multiply_all_elements(element1, element2):
    return element1 * element2


result = reduce(multiply_all_elements, data)
print(result)  # 120
