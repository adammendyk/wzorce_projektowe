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

# from functools import namedtuple

# Point = namedtuple('Point', ['x', 'y', 'z'])

# # p = Point(x=1, y=2, z=1) lub
# p = Point(1, 2, 1)


# print(p.x)
# print(p.y)
# print(p.z)

# # ---

# import abc
# from abc import ABCMeta, abstractmethod


# class Shape(metaclass=abc.ABCMeta):

#     @abstractmethod
#     def area(self):
#         raise NotImplementedError  # pass

#     # # @property
#     # @abc.abstractmethod
#     # def property(self):
#     #     raise NotImplementedError  # pass

#         def foo():
#             pass


# class Square(Shape):
#     def __init__(self, value):
#         self.value = value

#     def area(self):
#         return self.value ** 2


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius  # or self.r_adius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2


# if __name__ == "__main__":
#     circle = Circle(1)
#     assert circle.area() == 3.14
#     # assert circle.area() == 3.15

#     print(circle.area())

#     square = Square(5)
#     assert square.area() == 25

#     print(square.area())

# # --- Builder pattern

# import abc
# from abc import ABCMeta, abstractmethod


# class Building:

#     def __init__(self, flors=6, windows=24, walls=5):  # some might have deoult values
#         self.flors = flors
#         self.windows = windows
#         self.walls = walls
#         self.doors = None
#         self.roof = None

#     def __str__(self):
#         return f'Building: flors -> {self.flors}, windows -> {self.windows},\
# walls -> {self.walls}, doors -> {self.doors}, roof -> {self.roof}'


# class Builder(metaclass=abc.ABCMeta):

#     @abstractmethod
#     def set_flors(self, value):
#         raise NotImplementedError

#     @abstractmethod
#     def set_windows(self, value):
#         raise NotImplementedError

#     @abstractmethod
#     def set_walls(self, value):
#         raise NotImplementedError

#     @abstractmethod
#     def set_doors(self, value):
#         raise NotImplementedError

#     @abstractmethod
#     def set_roof(self, value):
#         raise NotImplementedError


# class BuildingBuilder(Builder):

#     def __init__(self):
#         self.building = Building()

#     def set_flors(self, value):
#         self.building.flors = value
#         return self

#     def set_windows(self, value):
#         self.building.windows = value
#         return self

#     def set_doors(self, value):
#         self.building.doors = value
#         return self

#     def set_walls(self, value):
#         self.building.walls = value
#         return self

#     def set_roof(self, value):
#         self.building.roof = value
#         return self

#     def get_result(self):
#         return self.building


# class BuildingBuilderDirector:

#     @staticmethod
#     def construct():
#         builder = BuildingBuilder()
#         house = builder.set_flors(6).set_walls(4).set_windows(
#             12).set_doors(4).set_roof("one_slope")
#         return house.get_result()


# def main():
#     building = BuildingBuilderDirector.construct()
#     print(building)


# if __name__ == '__main__':
#     main()

# # --- Strategy pattern

# from abc import ABCMeta, abstractmethod


# class Provider(metaclass=ABCMeta):

#     @abstractmethod
#     def calculate_cost(self):
#         raise NotImplementedError


# class Fedex(Provider):

#     def __init__(self, weight, rate):
#         self.rate = rate
#         self.weight = weight

#     def calculate_cost(self):
#         return self.rate * self.weight


# class Inpost(Provider):

#     def __init__(self, weight, rate):
#         self.rate = rate
#         self.weight = weight

#     def calculate_cost(self):
#         return self.rate * self.weight


# class Calculator:

#     def __init__(self, provider):
#         self.provider = provider

#     def calculate(self, provider):
#         if provider == None:
#             raise Exception('No provider set')
#         else:
#             return self.provider.calculate_cost()

#     def set_provider(self, new_provider):
#         self.new_provider = new_provider

#     def __str__(self):
#         return f'Weight: {self.weight}, cost: {self.provider.cost}'


# def main():
#     fedex = Fedex(2, 6.23)
#     calculator = Calculator(fedex)

#     cost = calculator.calculate(fedex)
#     print(f' Shipping will cost: {cost}')


# if __name__ == "__main__":
#     main()

# # ---

# def Beer() -> 'Beer':  # type annotation
#     pass

# # ---
