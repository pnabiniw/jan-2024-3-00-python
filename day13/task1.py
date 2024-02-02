# WAP to calculate the factorial of 7 using python reduce() function with lambda
# 7*6*...*1
from functools import reduce
result = reduce(lambda el1, el2: el1 * el2, range(1, 8))
print(result)  # 5040
