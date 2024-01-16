from unittest import TestCase
from main import Stack

class TestStack(TestCase):

    #stack can add and remove items
    def test_push(self):
        s = Stack()
        s.push(1)
        self.assertEqual(s.pop(), 1)
        s.push(2)
        self.assertEqual(s.pop(), 2)

    #stack can follow first in, last out
    def test_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    #peek returns the first element but doesnt pop it
    def test_peek(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.peek(), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.pop(), 1)
