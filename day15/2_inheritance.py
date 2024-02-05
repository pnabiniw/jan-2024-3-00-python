# Inheritance is the process of accessing attributes in the children classes from parent classes

class A:
    x = 1


class B(A):  # Inheritance. B is inheriting A
    y = 2


obj = B()
print(obj.y)  # 2
print(obj.x)  # 1


# Types of Inheritance in Python
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance


# Single Inheritance
class A:
    x = 1


class B(A):  # Inheritance. B is inheriting A
    y = 2


print(B().x)  # 1



# Multiple Inheritance

class A:
    x = 1

class B:
    y = 2


class C(A, B):
    z = 3


obj = C()
print(obj.z)
print(obj.y)
print(obj.x)



# Multilevel Inheritance
class A:
    x = 1


class B(A):
    y = 2


class C(B):
    z = 3

obj = C()
print(obj.x)



# Hierarchical Inheritance

class A:
    x = 1


class B(A):
    y = 2

class C(A):
    z = 3


obj = C()
print(obj.z)


# Hybrid Inheritance
# It is the combination of multiple and hierarchical inheritance

class A:
    z = 1

class B(A):
    x = 2

class C(A):
    z = 3


class D(B, C):
    y = 4

class E(D):
    q = 5


obj = E()
print(obj.z)

# MRO (Method Resolution Order) is the process by which the attributes are searched by an object
print(E.mro())
