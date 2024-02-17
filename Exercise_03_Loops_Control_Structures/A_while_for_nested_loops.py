""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:40:22 
"""

""" EXERCISE 03
    3.(a) Design and develop programs using Iterative statements-while, for, nested loops.
"""

#? While Loop:
num = 1
while num <= 5:
    print(num, end=" ")
    num += 1
print("\n")

#? For Loop:
for num in range(1, 6):
    print(num, end=" ")
print("\n")

#? Nested Loops:
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


""" --------------[OUTPUT]--------------------

1 2 3 4 5 

1 2 3 4 5

*
* *
* * *
* * * *
* * * * *

--------------[END-OF-OUTPUT]-------------- """
