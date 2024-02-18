""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:42:35 
"""

""" EXERCISE 07
    7.(e) Use basic tuple operations and comparisons.
"""

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# Concatenation
concatenatedTuple = tuple1 + tuple2
print("Concatenated tuple:", concatenatedTuple)

# Repetition
repeatedTuple = tuple1 * 3
print("Repeated tuple:", repeatedTuple)

# Membership
print("Is 'b' in tuple2?", "b" in tuple2)

# Length
print("Length of tuple1:", len(tuple1))

# Comparison
print("Is tuple1 equal to tuple2?", tuple1 == tuple2)
print("Is tuple1 not equal to tuple2?", tuple1 != tuple2)
print("Is tuple1 less than tuple2?", tuple1 < tuple2)
print("Is tuple1 greater than tuple2?", tuple1 > tuple2)


""" --------------[OUTPUT]--------------------

Tuple 1: (1, 2, 3)
Tuple 2: (4, 5, 6)
Concatenated tuple: (1, 2, 3, 4, 5, 6)
Repeated tuple: (1, 2, 3, 1, 2, 3, 1, 2, 3)
Is 'b' in tuple2? False
Length of tuple1: 3
Is tuple1 equal to tuple2? False
Is tuple1 not equal to tuple2? True
Is tuple1 less than tuple2? True
Is tuple1 greater than tuple2? False

--------------[END-OF-OUTPUT]-------------- """
