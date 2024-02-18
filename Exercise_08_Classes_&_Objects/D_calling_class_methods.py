""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:42:54 
"""

""" EXERCISE 08
    8.(d) Practice calling class methods from another class.
"""

class Dog:
    def bark(self):
        print("Woof woof!")

class Cat:
    def meow(self):
        print("Meow meow!")

class PetShop:
    @staticmethod
    def sellDog():
        dog = Dog()
        dog.bark()

    @staticmethod
    def sellCat():
        cat = Cat()
        cat.meow()

PetShop.sellDog()  # Output: Woof woof!
PetShop.sellCat()  # Output: Meow meow!


""" --------------[OUTPUT]--------------------

Woof woof!
Meow meow!

--------------[END-OF-OUTPUT]-------------- """
