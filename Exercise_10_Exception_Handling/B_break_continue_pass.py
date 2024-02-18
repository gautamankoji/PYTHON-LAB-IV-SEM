""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:43:27 
"""

""" EXERCISE 10
    10.(b) Use Break, continue, pass statements in programs.
"""

print("Demonstrating 'break' statement:")
for i in range(1, 11):
    if i == 6:
        print("Exiting loop at", i)
        break
    print("Current value:", i)
print()

print("Demonstrating 'continue' statement:")
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print("Even number found:", i)
print()

print("Demonstrating 'pass' statement:")
for i in range(1, 4):
    if i == 2:
        pass
    else:
        print("Current value:", i)
print("Pass statement used for value 2.")


""" --------------[OUTPUT]--------------------

Demonstrating 'break' statement:
Current value: 1
Current value: 2
Current value: 3
Current value: 4
Current value: 5
Exiting loop at 6

Demonstrating 'continue' statement:
Even number found: 2
Even number found: 4
Even number found: 6
Even number found: 8
Even number found: 10

Demonstrating 'pass' statement:
Current value: 1
Current value: 3
Pass statement used for value 2.

--------------[END-OF-OUTPUT]-------------- """
