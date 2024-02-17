""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:15:58 
"""

""" EXERCISE 01
    1.(f) Write programs for writing multiple statements in a single line.
"""

# Multiple statements on a single line
x = 5; y = 10; z = x + y
print("x:", x, ", y:", y, ", z:", z)

# Conditionals on a single line
a = 7; b = 3
max_value = a if a > b else b
print("Max value:", max_value)

# Loops on a single line
for i in range(5): print(i, end=' '); print("Hello")


""" --------------[OUTPUT]--------------------

x: 5 , y: 10 , z: 15
Max value: 7
0 Hello
1 Hello
2 Hello
3 Hello
4 Hello

--------------[END-OF-OUTPUT]-------------- """
