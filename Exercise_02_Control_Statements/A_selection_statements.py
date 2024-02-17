""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:40:34 
"""

""" EXERCISE 02
    2.(a) Write programs using selection statements.
"""

#? Simple If Statement:
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")


#? If-else Statement:
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#? If-elif-else Statement:
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#? Nested If Statements:
num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")


""" --------------[OUTPUT]--------------------

Enter a number: 5
The number is positive.
Enter a number: 5
The number is odd.
Enter your marks: 95
Grade: A
Enter a number: 0
The number is zero.

--------------[END-OF-OUTPUT]-------------- """
