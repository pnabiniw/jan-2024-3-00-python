# Namespaces define the scopes of variables and functions (objects) in Python
# There are broadly four namespaces
# 1. Local scope
# 2. Enclosed Scope
# 3. Global Scope
# 4. Built-in Scope

# This is sometimes also referred as LEGB rule

# Built-in scopes
# All those objects which can be easily accessed in any of the python module. Actuall inbuilt python modules
# come in this scope

import csv
import json
from functools import reduce



# Global Scope
def addition(a, b):
    return a + b

name = "Python"
print(name)  # Python



# Local scope
def summ(x, y):
    return x+y  # Here x and y have local scope

summ(2, 3)
# print(x)


# Enclosed Scope
a = 1

def func(x):
    global a
    a = 2
    print(x)  # 23
    print(a)  # 2


func(23)
print(a)  # 1
