""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:40:55 
"""

""" EXERCISE 03
    3.(b) Use Break, continue, pass statements in programs.
"""

#? Using `break` Statement:
numbers = [1, 3, 5, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print("The first even number is:", num)
        break
    
#? Using `continue` Statement:
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num, end=' ')

#? Using `pass` Statement:
for i in range(5):
    pass  # do nothing



""" --------------[OUTPUT]--------------------

The first even number is: 8
1 3 5 7 9

--------------[END-OF-OUTPUT]-------------- """
