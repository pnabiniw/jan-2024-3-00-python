# Order of arguments in python function is:
# 1. Positional
# 2. Default / Keyword
# 3. *args
# 4. **kwargs


def addition(a, b, c, d=2, e=3, *args, **kwargs):
    print(a)  # 10
    print(b)  # 20
    print(c)  # 5
    print(d)  # 9
    print(e)  # 12
    print(args)  # (3, 7, 8, 9, 11)
    print(kwargs)  # {"x": 14, "y" 13}


addition(10, 20, 5, 9, 12, 3, 7, 8, 9, 11, x=14, y=13)
