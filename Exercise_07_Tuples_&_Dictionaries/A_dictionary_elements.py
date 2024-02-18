""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:42:15 
"""

""" EXERCISE 07
    7.(a) Write programs to define a dictionary and write programs to modify values, adding new keys.
"""

myDict = {
    'name': 'Aruna',
    'age': 30,
    'city': 'New Delhi'
}

print("Original dictionary:", myDict)

myDict['age'] = 31 # Modify value
print("Dictionary after modifying 'age':", myDict)

myDict['gender'] = 'Female' # Adding new keys
print("Dictionary after adding 'gender':", myDict)


""" --------------[OUTPUT]--------------------

Original dictionary: {'name': 'Aruna', 'age': 30, 'city': 'New Delhi'}
Dictionary after modifying 'age': {'name': 'Aruna', 'age': 31, 'city': 'New Delhi'}
Dictionary after adding 'gender': {'name': 'Aruna', 'age': 31, 'city': 'New Delhi', 'gender': 'Female'}

--------------[END-OF-OUTPUT]-------------- """
