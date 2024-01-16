Stack Class

The Stack class represents a basic implementation of a stack. It provides the following methods:


__init__(self): Initializes an empty stack.

push(self, item): Adds an item to the top of the stack.

pop(self): Removes and returns the item from the top of the stack. If the stack is empty, it returns None.

peek(self): Returns the item from the top of the stack without removing it.

is_empty(self): Checks if the stack is empty.



TestStack Class


The TestStack class includes unit tests to ensure the correct functionality of the Stack class.

test_push(self): Verifies that the stack can add and remove items following the Last In, First Out (LIFO) principle.

test_pop(self): Ensures that the stack follows the LIFO principle, where the last item added is the first to be removed.

test_peek(self): Validates that the peek method returns the top element without removing it.
