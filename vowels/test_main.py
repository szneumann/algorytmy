import unittest
from inspect import isfunction
from main import vowels

class Test(unittest.TestCase):

    #Vowels is a function
    def test_vovels_function(self):
        self.assertEqual(True, isfunction(vowels))

    #returns the number of vowels used
    def test_vowels(self):
        self.assertEqual(5, vowels('aeiou'))

    #returns the number of vowels used when they are capitalized
    def test2(self):
        self.assertEqual(5, vowels('AEIOU'))

    #returns the number of vowels used
    def test3(self):
        self.assertEqual(5, vowels('abcdefghijklmnopqrstuvwxyz'))

    #returns the number of vowels used
    def test4(self):
        self.assertEqual(0, vowels('bcdfghjkl'))


