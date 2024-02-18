""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:43:05 
"""

""" EXERCISE 09
    9.(a) Demonstrate different inheritance types.
    * Multiple Inheritance
"""

class Animal:
    def sound(self):
        print("Some sound")

class Mammal:
    def feedMilk(self):
        print("Feeding milk")

class Dog(Animal, Mammal):
    def bark(self):
        print("Woof woof!")

dog = Dog()
dog.sound()       # Output: Some sound
dog.feedMilk()  # Output: Feeding milk
dog.bark()       # Output: Woof woof!


""" --------------[OUTPUT]--------------------

Some sound
Feeding milk
Woof woof!

--------------[END-OF-OUTPUT]-------------- """
