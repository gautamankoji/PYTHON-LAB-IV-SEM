""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:43:05 
"""

""" EXERCISE 09
    9.(a) Demonstrate different inheritance types.
    * Single Inheritance
"""

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def bark(self):
        print("Woof woof!")

dog = Dog()
dog.sound()  # Output: Some sound
dog.bark()   # Output: Woof woof!


""" --------------[OUTPUT]--------------------

Some sound
Woof woof!

--------------[END-OF-OUTPUT]-------------- """
