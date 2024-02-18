""" AUTHOR
 * Gautam Ankoji 
 * Saturday 17-02-2024 23:42:09 
"""

""" EXERCISE 06
    6.(c) Write programs to use list as a stack and queue.
"""

def stackOperations():
    # stack (Last-In, First-Out)
    stack = []

    # Push elements onto the stack
    stack.append(1)
    stack.append(2)
    stack.append(3)

    print("Stack:", stack)

    # Pop elements from the stack
    poppedElement = stack.pop()
    print("Popped element:", poppedElement)
    print("Stack after popping:", stack)

    # Peek at the top element of the stack
    topElement = stack[-1]
    print("Top element of the stack:", topElement)

def queueOperations():
    # queue (First-In, First-Out)
    queue = []

    # Enqueue elements into the queue
    queue.append(1)
    queue.append(2)
    queue.append(3)

    print("Queue:", queue)

    # Dequeue elements from the queue
    dequeuedElement = queue.pop(0)
    print("Dequeued element:", dequeuedElement)
    print("Queue after dequeueing:", queue)

    # Peek at the front element of the queue
    frontElement = queue[0]
    print("Front element of the queue:", frontElement)

print("Stack Operations:")
stackOperations()

print("\nQueue Operations:")
queueOperations()


""" --------------[OUTPUT]--------------------

Stack Operations:
Stack: [1, 2, 3]
Popped element: 3
Stack after popping: [1, 2]
Top element of the stack: 2

Queue Operations:
Queue: [1, 2, 3]
Dequeued element: 1
Queue after dequeueing: [2, 3]
Front element of the queue: 2

--------------[END-OF-OUTPUT]-------------- """
