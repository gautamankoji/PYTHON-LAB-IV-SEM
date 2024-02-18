""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:42:50 
"""

""" EXERCISE 08
    8.(c) Understand public and private members.
"""

class MyClass:
    def __init__(self, publicValue, _privateValue):
        self.publicValue = publicValue
        self._privateValue = _privateValue

    def publicMethod(self):
        print("This is a public method")

    def _privateMethod(self):
        print("This is a private method")

obj = MyClass(10, 20)
print("Public value:", obj.publicValue)
obj.publicMethod()
print("Private value:", obj._privateValue)
obj._privateMethod()



""" --------------[OUTPUT]--------------------

Public value: 10
This is a public method
Private value: 20
This is a private method

--------------[END-OF-OUTPUT]-------------- """
