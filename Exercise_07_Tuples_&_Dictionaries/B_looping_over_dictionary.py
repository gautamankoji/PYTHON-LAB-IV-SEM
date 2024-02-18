""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:42:20 
"""

""" EXERCISE 07
    7.(b) Apply looping over a dictionary.
"""

myDict = {
    'name': 'Aruna',
    'age': 30,
    'city': 'New Delhi'
}

print("Looping over the dictionary:")
for key, value in myDict.items():
    print(key + ":", value)


""" --------------[OUTPUT]--------------------

Looping over the dictionary:
name: Aruna
age: 30
city: New Delhi

--------------[END-OF-OUTPUT]-------------- """
