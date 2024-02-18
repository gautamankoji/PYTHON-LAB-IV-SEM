""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:42:26 
"""

""" EXERCISE 07
    7.(c) Use built in dictionary methods, functions.
"""

myDict = {
    'name': 'Aruna',
    'age': 30,
    'city': 'New Delhi'
}

print("Original dictionary:", myDict)

# Dictionary methods and functions
print("Keys in the dictionary:", myDict.keys())      # Get keys
print("Values in the dictionary:", myDict.values())  # Get values
print("Items in the dictionary:", myDict.items())    # Get key-value pairs

# Accessing values
print("Value of 'name':", myDict.get('name'))        # Using get() method
print("Value of 'occupation':", myDict.get('occupation', 'Unknown'))  # Handling key not found

# Modifying dictionary
myDict['age'] = 31  # Update value
print("Dictionary after updating 'age':", myDict)

myDict.update({'gender': 'Female'})  # Update or add multiple key-value pairs
print("Dictionary after updating with gender:", myDict)

# Removing items
removed_value = myDict.pop('city')  # Remove item by key and get its value
print("Removed value of 'city':", removed_value)
print("Dictionary after removing 'city':", myDict)

myDict.clear()  # Clear the dictionary
print("Dictionary after clearing:", myDict)


""" --------------[OUTPUT]--------------------

Original dictionary: {'name': 'Aruna', 'age': 30, 'city': 'New Delhi'}
Keys in the dictionary: dict_keys(['name', 'age', 'city'])
Values in the dictionary: dict_values(['Aruna', 30, 'New Delhi'])
Items in the dictionary: dict_items([('name', 'Aruna'), ('age', 30), ('city', 'New Delhi')])
Value of 'name': Aruna
Value of 'occupation': Unknown
Dictionary after updating 'age': {'name': 'Aruna', 'age': 31, 'city': 'New Delhi'}
Dictionary after updating with gender: {'name': 'Aruna', 'age': 31, 'city': 'New Delhi', 'gender': 'Female'}
Removed value of 'city': New Delhi
Dictionary after removing 'city': {'name': 'Aruna', 'age': 31, 'gender': 'Female'}
Dictionary after clearing: {}

--------------[END-OF-OUTPUT]-------------- """
