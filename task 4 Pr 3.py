import math
from abc import ABC, abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle (Shape):
    def __init__ (self, width, height):
      self.widgh = width
      self.height = height

    def area(self):
        return self.widgh * self.height

circle = Circle(5)
print("Коло з радіусом 5:", circle.area())
 
rectangle = Rectangle(4,6)
print("Площа трикутника зі сторонами 4 i 6:", rectangle.area())

