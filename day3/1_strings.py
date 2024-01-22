# Strings are the sequence of characters in Python. They are also the iterables (sequence of data)
# character itself is also a string in Python
# Strings are enclosed either in double quotes ("") or single quotes ('') or triple quotes ("""""" or '''''')
# String is an immutable datatype

# Creating strings
a = ""  # empty string
b = ''  # empty string
c = """"""  # empty string
d = ''''''  # empty string

e = "Hello World"  # non-empty string
f = 'Hello World'  # non empty string
g = """
I'm learning Python.
Python is a high level language
"""
h = '''
I'm learning Python.
Python is a high level language
'''

data = "I'm learning Python"
data = 'He said, "Python is high level language"'


# Accessing string items
# String items can also be accessed using indexing and slicing


# Indexing
data = "Python is a high level language"
print(data[0])  # P
print(data[6])  # ' '
print(data[-1])  # e
print(data[-8])  # l


# Slicing
print(data[3:8])  # hon i
print(data[7:2])  # ''
print(data[:7])  # Python
print(data[9:])  # ' a high level language'
print(data[-8:-2])  # langua
print(data[-3:-7])  # ''
print(data[:-7])  # Python is a high level l
print(data[-5:])  # guage


# We cannot update string elements because string is an immutable datatype

data = "I am learning"
data[5] = "L"  # This raises error. We can't change the particular position of a string data.
del data[5]  # This is also not possible

# But we can delete the string object
del data   # It deletes the string object



# len() is a built-in function in python that gives length of an iterable
# It can give the length of strings, lists, tuple, dictionary, set and any other iterable

print(len("Hello"))  # 5

