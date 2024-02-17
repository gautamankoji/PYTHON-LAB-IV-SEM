""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:40:47 
"""

""" EXERCISE 02
    2.(b) Implement programs on and conditional branching statements.
"""

#? Using `and` Operator:
num = int(input("Enter a number: "))
if num > 10 and num < 20:
    print("The number is between 10 and 20.")
else:
    print("The number is not between 10 and 20.")


#? Conditional Branching:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("The largest number is:", largest)


""" --------------[OUTPUT]--------------------

Enter a number: 11
The number is between 10 and 20.
Enter first number: 2
Enter second number: 3
Enter third number: 4
The largest number is: 4

--------------[END-OF-OUTPUT]-------------- """
