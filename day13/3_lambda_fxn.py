# Lambda functions are the short and elegant functions with one-liner statement
# They are mostly used in the cases where we do not need to call the function rather we just need to pass
# the reference
# They are also called "anonymous function" as they don't have their name


def is_even(num):
    return num % 2 == 0


x = lambda y: y % 2 == 0
print(x(4))


# map()
data = [2, 3, 4, 5, 6]
result = map(lambda e: e ** 2, data)
print(list(result))   # [4, 9, 16, 25, 36]


# 2. filter(func, iterable)
# filter() function takes function as the first parameter and iterable as the second parameter
# It picks / selects the elements from data in the iterable to according to the function definition
# Count of the elements in the iterable may not be same initially and after filtering

data = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

vowel_data = filter(lambda element: element in ["a", "e", "i", "o", "u"], data)
print(list(vowel_data))  # ["a", "e", "i"]


# reduce(func, iterable)
# reduce() function takes function as the first parameter and iterable as the second parameter
# It reduces the entire iterable to a single data
# Result is a single item (not an iterable)


from functools import reduce

data = [1, 2, 3, 4, 5]
result = reduce(lambda el1, el2: el1 * el2, data)
print(result)  # 120
