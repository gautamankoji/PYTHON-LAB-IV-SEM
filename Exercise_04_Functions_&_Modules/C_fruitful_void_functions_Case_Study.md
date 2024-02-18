<!-- EXERCISE 04
    4.(c) Understand the usage of else statement in loops with a case study.
 -->

# Understanding Fruitful and Void Functions: A Case Study

## Introduction

Functions in Python can be categorized as fruitful or void based on their return value.

## Case Study: Calculating the Square of a Number

### Approach

1. **Fruitful Function**: Calculates and returns the square of a number.
2. **Void Function**: Prints the square of a number without returning anything.

### Implementation

```python
def calculateSquare(num):
    return num ** 2

def printSquare(num):
    print("The square of", num, "is:", num ** 2)

number = 5
result1 = calculateSquare(number)  # Fruitful function
print("Result from calculateSquare function:", result1)

printSquare(number)  # Void function
```

```output
Result from calculateSquare function: 25
The square of 5 is: 25
```

### Conclusion

- Fruitful functions return a value using `return`, suitable for computations where the result is needed.
- Void functions perform an action directly, such as printing, without returning anything. They're useful for tasks with side effects but no direct return value needed.
