""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:42:05 
"""

""" EXERCISE 06
    6.(b) Practice basic list operations, methods.
"""

myList = [1, 2, 3, 4, 5]
print("Original list:", myList)

print("Length of the list:", len(myList))  # Length of the list

# Accessing elements of a list
print("First element:", myList[0])  # Accessing the first element
print("Last element:", myList[-1])  # Accessing the last element
print("Second to fourth elements:", myList[1:4])  # Accessing a slice of elements
print("Every other element:", myList[::2])  # Accessing every other element

# List methods
myList.append(6)
print("After appending 6:", myList)

myList.extend([7, 8, 9])
print("After extending with [7, 8, 9]:", myList)

myList.insert(3, 10)
print("After inserting 10 at index 3:", myList)

myList.remove(3)
print("After removing the first occurrence of 3:", myList)

poppedElement = myList.pop()
print("Popped element:", poppedElement)
print("List after popping:", myList)

myList.reverse()
print("Reversed list:", myList)

sortedList = sorted(myList)
print("Sorted list:", sortedList)

cnt2 = myList.count(2)
print("Number of occurrences of 2:", cnt2)

myList.clear()
print("After clearing the list:", myList)


""" --------------[OUTPUT]--------------------

Original list: [1, 2, 3, 4, 5]
Length of the list: 5
First element: 1
Last element: 5
Second to fourth elements: [2, 3, 4]
Every other element: [1, 3, 5]
After appending 6: [1, 2, 3, 4, 5, 6]
After extending with [7, 8, 9]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
After inserting 10 at index 3: [1, 2, 3, 10, 4, 5, 6, 7, 8, 9]
After removing the first occurrence of 3: [1, 2, 10, 4, 5, 6, 7, 8, 9]
Popped element: 9
List after popping: [1, 2, 10, 4, 5, 6, 7, 8]
Reversed list: [8, 7, 6, 5, 4, 10, 2, 1]
Sorted list: [1, 2, 4, 5, 6, 7, 8, 10]
Number of occurrences of 2: 1
After clearing the list: []

--------------[END-OF-OUTPUT]-------------- """
