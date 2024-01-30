"""
Create a new list of repeated items from a provided list:
nums = [3, 4, 2, 2, 1, 3, 3, 3]
Output = [3, 2]

"""

nums = [3, 4, 2, 2, 1, 3, 3, 3]
result = []
for i in nums:
    if nums.count(i) > 1 and i not in result:
        result.append(i)  # [3, 2]
print(result)
