""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:41:08 
"""

""" EXERCISE 04
    4.(b) Understand Scope of a variable and Use global statement.
"""


globalVar = 10 # Global variable

def func():
    
    localVar = 20 # Local variable
    print("Inside func(): globalVar =", globalVar)
    print("Inside func(): localVar =", localVar)

    def innerFunc():
        innerVar = 30 # Enclosing scope
        print("Inside innerFunc(): globalVar =", globalVar)
        print("Inside innerFunc(): localVar =", localVar)
        print("Inside innerFunc(): innerVar =", innerVar)

    innerFunc()

print("Outside func(): globalVar =", globalVar) # Accessing global variable
func()
# print("Outside func(): localVar =", localVar) # Accessing local variable outside its scope


""" --------------[OUTPUT]--------------------

Outside func(): globalVar = 10
Inside func(): globalVar = 10
Inside func(): localVar = 20
Inside innerFunc(): globalVar = 10
Inside innerFunc(): localVar = 20
Inside innerFunc(): innerVar = 30

--------------[END-OF-OUTPUT]-------------- """
