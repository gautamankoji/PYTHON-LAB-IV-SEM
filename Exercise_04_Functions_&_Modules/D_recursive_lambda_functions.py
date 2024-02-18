""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:41:20 
"""

""" EXERCISE 04
    4.(d) Apply recursive and Lambda functions.
"""


# Recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# Recursive lambda function
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Lambda function to add two numbers
add = lambda x, y: x + y

print("Factorial of 4:", factorial(4))
print("Sum of 3 and 5:", add(3, 5))


""" --------------[OUTPUT]--------------------

Factorial of 5: 120
Factorial of 4: 24
Sum of 3 and 5: 8

--------------[END-OF-OUTPUT]-------------- """
