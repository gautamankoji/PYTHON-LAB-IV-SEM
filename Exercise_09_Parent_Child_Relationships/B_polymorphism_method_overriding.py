""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:43:09 
"""

""" EXERCISE 09
    9.(b) Apply polymorphism and method overriding.
"""

class Animal:
    def makeSound(self):
        print("Some generic sound")

class Dog(Animal):
    def makeSound(self):
        print("Woof woof!")

class Cat(Animal):
    def makeSound(self):
        print("Meow meow!")

# Polymorphism: A list of animals of different types
animals = [Dog(), Cat()]

# Method overriding: Each animal makes its own sound
for animal in animals:
    animal.makeSound()


""" --------------[OUTPUT]--------------------

Woof woof!
Meow meow!

--------------[END-OF-OUTPUT]-------------- """
