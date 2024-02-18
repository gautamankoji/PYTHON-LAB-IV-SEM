""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:43:42 
"""

""" EXERCISE 10
    10.(e) Demonstrate the usage of polymorphism in overloading of operators.
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    # Overloading the addition operator
    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.length + other.length, self.width + other.width)
        else:
            return Rectangle(self.length + other, self.width + other)

    # Overloading the equality operator
    def __eq__(self, other):
        return self.length == other.length and self.width == other.width

    # Overloading the string representation
    def __str__(self):
        return f"Rectangle: length={self.length}, width={self.width}"


rect1 = Rectangle(5, 4)
rect2 = Rectangle(3, 2)
rectSum = rect1 + rect2
print("Sum of rectangles:", rectSum)
rectWithScalar = rect1 + 2
print("Rectangle with scalar addition:", rectWithScalar)
print("Are rect1 and rect2 equal?", rect1 == rect2)


""" --------------[OUTPUT]--------------------

Sum of rectangles: Rectangle: length=8, width=6
Rectangle with scalar addition: Rectangle: length=7, width=6
Are rect1 and rect2 equal? False

--------------[END-OF-OUTPUT]-------------- """
