""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:43:16 
"""

""" EXERCISE 09
    9.(c) Create abstract classes.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

rectangle = Rectangle(5, 4)
circle = Circle(3)
print("Rectangle Area:", rectangle.area())      # Output: 20
print("Rectangle Perimeter:", rectangle.perimeter())  # Output: 18
print("Circle Area:", circle.area())          # Output: 28.26 (approx)
print("Circle Perimeter:", circle.perimeter())     # Output: 18.84 (approx)


""" --------------[OUTPUT]--------------------

Rectangle Area: 20
Rectangle Perimeter: 18
Circle Area: 28.259999999999998
Circle Perimeter: 18.84

--------------[END-OF-OUTPUT]-------------- """
