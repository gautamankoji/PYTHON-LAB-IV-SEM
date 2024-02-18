""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:42:59 
"""

""" EXERCISE 08
    8.(e) Write built in functions to check, get, set and delete attributes.
"""

class MyClass:
    def __init__(self):
        self.attribute = None

obj = MyClass()

# Check if an attribute exists
print("Does 'obj' have 'attribute'?", hasattr(obj, "attribute"))
print("Does 'obj' have 'nonexistent_attribute'?", hasattr(obj, "nonexistent_attribute"))

# Get the value of an attribute
value = getattr(obj, "attribute")
print("Value of 'attribute':", value)

# Set the value of an attribute
setattr(obj, "attribute", 42)
print("Value of 'attribute' after setting:", obj.attribute)

# Delete an attribute
delattr(obj, "attribute")
print("Does 'obj' have 'attribute' after deletion?", hasattr(obj, "attribute"))


""" --------------[OUTPUT]--------------------

Does 'obj' have 'attribute'? True
Does 'obj' have 'nonexistent_attribute'? False
Value of 'attribute': None
Value of 'attribute' after setting: 42
Does 'obj' have 'attribute' after deletion? False

--------------[END-OF-OUTPUT]-------------- """
