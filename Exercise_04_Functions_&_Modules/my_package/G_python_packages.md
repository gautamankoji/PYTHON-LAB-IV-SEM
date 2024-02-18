<!-- EXERCISE 04
    4.(g) Use python packages.
 -->

# Creating and Using a Python Package: A Quick Example

## Introduction

Python packages organize code into reusable modules. Let's create a simple package for math operations and use it in a Python script.

## Example: Math Operations Package

### Approach

1. Create a package structure with two files: `__init__.py` and `math_operations.py`.
2. Define math-related functions in `math_operations.py`.

### Implementation

```python
# my_package/__init__.py (empty)

# my_package/math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"
```

```output

```

### Usage

```python
# Using the math operations package
from my_package import math_operations

# Example usage
print("Sum:", math_operations.add(5, 3))         # Output: 8
print("Difference:", math_operations.subtract(5, 3))  # Output: 2
print("Product:", math_operations.multiply(5, 3))     # Output: 15
print("Quotient:", math_operations.divide(5, 3))      # Output: 1.6666666666666667
```

## Conclusion

Creating Python packages allows for modular and reusable code organization. This quick example demonstrates how to create a package for math operations and utilize it in Python scripts with ease.
