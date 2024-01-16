import unittest
from main import vowels

class Test(unittest.TestCase):
    def test_vowels(self):
        self.assertEqual(5, vowels('aeiou'))
    def test2(self):
        self.assertEqual(5, vowels('AEIOU'))
    def test3(self):
        self.assertEqual(4, vowels('aaaa'))
    def test4(self):
        self.assertEqual(0, vowels('BQWRtpsdfgbnbnbn   cmxbvcbx'))
    def test5(self):
        self.assertEqual(4, vowels('Why do you ask?'))
    def test6(self):
        self.assertEqual(3, vowels('Hi There!'))
    def test7(self):
        self.assertEqual(0, vowels('Why?'))


#print(vowels('123aea'))
