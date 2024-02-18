""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:43:33 
"""

""" EXERCISE 10
    10.(c) Demonstrate raising and re-raising exceptions.
"""

def example_function(x):
    try:
        if x < 0:
            raise ValueError("x should be a non-negative number")
        elif x == 0:
            raise ZeroDivisionError("x should not be zero")
        else:
            print("Square root of x:", x ** 0.5)

    except ValueError as ve:
        print("ValueError occurred:", ve)
        # Re-raise the exception with a different message
        raise ValueError("An error occurred while processing x") from ve

    except ZeroDivisionError as zde:
        print("ZeroDivisionError occurred:", zde)
        # Re-raise the exception with a different message
        raise ZeroDivisionError("An error occurred while processing x") from zde


# Calling the function with different values
try:
    example_function(-1)
except Exception as e:
    print("Outer Exception:", e)
print()

try:
    example_function(0)
except Exception as e:
    print("Outer Exception:", e)
print()

try:
    example_function(4)
except Exception as e:
    print("Outer Exception:", e)


""" --------------[OUTPUT]--------------------

ValueError occurred: x should be a non-negative number
Outer Exception: An error occurred while processing x

ZeroDivisionError occurred: x should not be zero
Outer Exception: An error occurred while processing x

Square root of x: 2.0

--------------[END-OF-OUTPUT]-------------- """
