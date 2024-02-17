""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:16:09 
"""

""" EXERCISE 01
    1.(g) Use Input statement, type conversion.
"""

age_str = input("Enter your age: ")
age = int(age_str) # Convert input to integer

isAdult = age >= 18
if isAdult:
    print("You are an adult.")
else:
    print("You are not an adult yet.")


""" --------------[OUTPUT]--------------------

Enter your age: 20
You are an adult.

--------------[END-OF-OUTPUT]-------------- """
