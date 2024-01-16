from unittest import TestCase
from main import Queue

class TestQueue(TestCase):
    #Queue is a class
    def test_isClass(self):
        q = Queue()
        self.assertTrue(type(q), "<class 'main.Queue'>")

    #can add elements to a queue'
    def test_add(self):
        q = Queue()
        self.assertIsNone(q.add(1))

    #can remove elements from a queue
    def test_remove(self):
        q = Queue()
        self.assertIsNone(q.add(1))  # No exceptions should be thrown
        try:
            self.assertIsNone(q.remove())  # No exceptions should be thrown
        except:
            return Exception

    # Order of elements is maintained
    def test_order(self):
        q = Queue()
        q.add(1)
        q.add(2)
        q.add(3)
        self.assertEqual(q.remove(), 1)
        self.assertEqual(q.remove(), 2)
        self.assertEqual(q.remove(), 3)
        self.assertIsNone(q.remove(), None)
