""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:41:46 
"""

""" EXERCISE 05
    5.(c) Define a list and write programs to access and modify elements of a list.
"""

myList = [1, 2, 3, 4, 5]

# Accessing elements of a list
print("Original list:", myList)
print("First element:", myList[0])  # Accessing the first element
print("Last element:", myList[-1])  # Accessing the last element
print("Second to fourth elements:", myList[1:4])  # Accessing a slice of elements
print("Every other element:", myList[::2])  # Accessing every other element
print()

# Modifying elements of a list
myList[2] = 10
print("After updating element at index 2:", myList)

myList.append(6)
print("After appending 6:", myList)

myList.insert(3, 7)
print("After inserting 7 at index 3:", myList)

myList.remove(4)
print("After removing 4:", myList)

del myList[0]
print("After deleting first element:", myList)

popped_element = myList.pop()
print("Popped element:", popped_element)
print("List after popping:", myList)

myList.clear()
print("After clearing the list:", myList)


""" --------------[OUTPUT]--------------------

Original list: [1, 2, 3, 4, 5]
First element: 1
Last element: 5
Second to fourth elements: [2, 3, 4]
Every other element: [1, 3, 5]

After updating element at index 2: [1, 2, 10, 4, 5]
After appending 6: [1, 2, 10, 4, 5, 6]
After inserting 7 at index 3: [1, 2, 10, 7, 4, 5, 6]
After removing 4: [1, 2, 10, 7, 5, 6]
After deleting first element: [2, 10, 7, 5, 6]
Popped element: 6
List after popping: [2, 10, 7, 5]
After clearing the list: []

--------------[END-OF-OUTPUT]-------------- """
