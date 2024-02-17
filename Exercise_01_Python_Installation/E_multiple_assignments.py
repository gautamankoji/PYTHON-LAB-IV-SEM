""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:15:53 
"""

""" EXERCISE 01
    1.(e) write programs to do multiple assignments at a time.
"""

# Multiple assignments at once
x, y, z = 10, 20, 30
print("x:", x)  # Output: 10
print("y:", y)  # Output: 20
print("z:", z)  # Output: 30

# Swapping values of variables
a, b = 5, 10
print("Before swapping: a =", a, ", b =", b)
a, b = b, a
print("After swapping: a =", a, ", b =", b)

# Multiple assignments with a single value
x = y = z = 50
print("x:", x)  # Output: 50
print("y:", y)  # Output: 50
print("z:", z)  # Output: 50


""" --------------[OUTPUT]--------------------

x: 10
y: 20
z: 30
Before swapping: a = 5 , b = 10
After swapping: a = 10 , b = 5
x: 50
y: 50
z: 50

--------------[END-OF-OUTPUT]-------------- """
