""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:40:59 
"""

""" EXERCISE 03
    3.(c) Understand the usage of else statement in loops with a case study
"""

start, end = 10, 20
primeNumbers = []
for num in range(start, end + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primeNumbers.append(num)
print("Prime numbers between", start, "and", end, "are:", primeNumbers)

""" --------------[OUTPUT]--------------------

Prime numbers between 10 and 20 are: [11, 13, 17, 19]

--------------[END-OF-OUTPUT]-------------- """
