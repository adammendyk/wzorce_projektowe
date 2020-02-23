"""
sprawdzić metody klasy i metody statyczne
"""


# class Student:

#     def __init__(self, x):
#         self.x = x

#     @staticmethod
#     def foo():
#         return 42

#     @classmethod
#     def spam(cls):
#         pass


# jack = Student(4)
# print(jack.foo)
# print(jack.foo())

# # ---

from functools import namedtuple

Point = namedtuple('Point', ['x', 'y', 'z'])

p = Point(x=1, y=2, z=1)

print(p.x)
print(p.y)
print(p.z)

# # ---
