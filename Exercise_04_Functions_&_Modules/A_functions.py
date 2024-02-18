""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:41:04 
"""

""" EXERCISE 04
    4.(a) Write programs for defining and calling functions.
"""


# Simple function
def greet():
    print("Hello, welcome!")

greet()


# Function with parameters
def greetWithName(name):
    print("Hello,", name, "welcome!")

greetWithName("Akash")


# Function with return value
def add(a, b):
    return a + b

result = add(3, 5)
print("The sum is:", result)


# Function with default parameter
def greet_with_default(name="there"):
    print("Hello,", name, "welcome!")

greet_with_default()
greet_with_default("Varun")


# Function with variable number of arguments
def sum_all(*args):
    return sum(args)

print("Sum of all numbers:", sum_all(1, 2, 3, 4, 5))
print("Sum of all numbers:", sum_all(10, 20, 30))


""" --------------[OUTPUT]--------------------

Hello, welcome!
Hello, Akash welcome!
The sum is: 8
Hello, there welcome!
Hello, Varun welcome!
Sum of all numbers: 15
Sum of all numbers: 60

--------------[END-OF-OUTPUT]-------------- """
