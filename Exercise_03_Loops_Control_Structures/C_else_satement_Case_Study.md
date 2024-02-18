<!-- EXERCISE 03
    3.(c) Understand the usage of else statement in loops with a case study
 -->

# Case Study: Finding Prime Numbers

## Introduction

In this case study, we will discuss a Python program designed to find all prime numbers within a specified range. The program utilizes a nested loop structure to efficiently identify prime numbers.

## Problem Statement

Given a range of numbers, we aim to identify and list all prime numbers within that range.

## Approach

To solve this problem, we employ a nested loop structure:

1. **Outer Loop**: Iterates over each number in the specified range.
2. **Inner Loop**: Checks if the current number is divisible by any number between 2 and itself minus 1. If a divisor is found, the loop terminates.
3. If no divisors are found, indicating that the number is prime, we add it to the list of prime numbers.

## Implementation

```python
start = 10
end = 20
primeNumbers = []
for num in range(start, end + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primeNumbers.append(num)
print("Prime numbers between", start, "and", end, "are:", primeNumbers)
```

```output
Prime numbers between 10 and 20 are: [11, 13, 17, 19]
```

## Explanation

- The outer loop iterates over each number in the specified range.
- The inner loop checks if the current number is divisible by any number between 2 and itself minus 1. If a divisor is found, the inner loop is terminated with `break`.
- If no divisors are found, indicating that the number is prime, the `else` block associated with the inner loop is executed, adding the number to the list of prime numbers.
- The `else` block of the inner loop is only executed if the loop completes all iterations without encountering a `break` statement, i.e., if the number is not divisible by any number other than 1 and itself.

## Conclusion

The provided Python program efficiently identifies prime numbers within a specified range using a nested loop structure. It demonstrates a practical application of nested loops and conditional statements in solving mathematical problems.
 