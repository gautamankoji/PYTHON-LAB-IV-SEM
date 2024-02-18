""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:42:46 
"""

""" EXERCISE 08
    8.(b) Defining constructors and using Self.
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculateArea(self):
        return self.length * self.width

# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
length = 10
width = 30

rectangle = Rectangle(length, width)
area = rectangle.calculateArea()
print("The area of the rectangle is:", area)


""" --------------[OUTPUT]--------------------

The area of the rectangle is: 300

--------------[END-OF-OUTPUT]-------------- """
