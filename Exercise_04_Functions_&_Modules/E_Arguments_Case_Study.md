<!-- EXERCISE 04
    4.(e) Understand different kinds of arguments through a case study.
 -->

# Understanding Different Kinds of Arguments: A Case Study

## Introduction

In Python, functions can accept different kinds of arguments, including positional, keyword, default, and variable-length arguments. Let's explore these types through a case study.

## Case Study: Creating a Function to Greet Users

### Problem Statement

We want to create a function that greets users with a customizable message.

### Approach

We'll define a function `greetUser` with various types of arguments:

- **Positional Arguments**: Name and message.
- **Keyword Arguments**: Name and message with default values.
- **Variable-Length Arguments**: Greeting multiple users at once.

### Implementation

```python
def greetUser(name, message):
    print(f"Hello, {name}! {message}")

def greetUserDefault(name="Guest", message="Welcome!"):
    print(f"Hello, {name}! {message}")

def greetUsers(*names, message="Welcome!"):
    for name in names:
        print(f"Hello, {name}! {message}")

greetUser("Akash", "Good morning!")  
greetUserDefault()  
greetUsers("Varun", "Rajesh", message="Have a nice day!")
```

```output
Hello, Akash! Good morning!
Hello, Guest! Welcome!
Hello, Varun! Have a nice day!
Hello, Rajesh! Have a nice day!
```

### Explanation

- **Positional Arguments**: `greetUser` function takes `name` and `message` as positional arguments. They're passed in the order defined by the function.
- **Keyword Arguments with Default Values**: `greetUserDefault` function accepts `name` and `message` as keyword arguments with default values. They can be overridden during function call.
- **Variable-Length Arguments**: `greetUsers` function accepts a variable number of `names` using `*names` syntax. It also takes a keyword argument `message` with a default value.

### Conclusion

Understanding different kinds of arguments in Python allows us to create versatile and flexible functions. Positional, keyword, default, and variable-length arguments provide various ways to pass data to functions, enhancing code readability and usability.
