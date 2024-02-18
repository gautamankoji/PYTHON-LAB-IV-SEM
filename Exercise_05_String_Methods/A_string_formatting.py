""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:41:33 
"""

""" EXERCISE 05
    5.(a) Apply string formatting operator.
"""

# Example of using the string formatting operator %

# Variables
name = "Akash"
age = 30
height = 5.6

# String formatting
formattedString1 = "Name: %s, Age: %d, Height: %.2f feet" % (name, age, height) # Using `%` operator
formattedString2 = f"Name: {name}, Age: {age}, Height: {height:.2f} feet" # str.format()

print(formattedString1)
print(formattedString2)


""" --------------[OUTPUT]--------------------

Name: Akash, Age: 30, Height: 5.60 feet
Name: Akash, Age: 30, Height: 5.60 feet

--------------[END-OF-OUTPUT]-------------- """
