""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:43:23 
"""

""" EXERCISE 10
    10.(a) Write a program for catching multiple exceptions.
"""

try:
    x = int(input("Enter a number: ")) # x = 10
    y = 0
    result = x / y

except (ValueError, ZeroDivisionError) as e:
    print("An error occurred:", e)


""" --------------[OUTPUT]--------------------

Enter a number: 10
An error occurred: division by zero

--------------[END-OF-OUTPUT]-------------- """
