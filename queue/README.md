Queue Class

The Queue class is a fundamental implementation of a queue data structure. It provides the following methods:

__init__(self): Initializes an empty queue.

add(self, element): Adds an element to the end of the queue.

remove(self): Removes and returns the element from the front of the queue. If the queue is empty, it returns None.





test_main.py

TestQueue Class

The TestQueue class includes unit tests to ensure the correct functionality of the Queue class.

test_isClass(self): Verifies that an instance of the Queue class is created successfully.

test_add(self): Checks that elements can be added to the queue without any exceptions.

test_remove(self): Ensures that elements can be removed from the queue without any exceptions.

test_order(self): Validates that the order of elements in the queue is maintained.
