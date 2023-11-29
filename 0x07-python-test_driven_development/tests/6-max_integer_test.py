#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def Test_ListOfINT(self):
        self.assertEqual(max_integer([1 , 2, 3, 4]), 4)
        self.assertEqual(max_integer([1 , 5, 3, 4]), 5)
        self.assertEqual(max_integer([7 , 5, 3, 4]), 7)
        self.assertEqual(max_integer([4 , 3, 2, 1]), 4)

    def Test_EmptyList(self):
        self.assertEqual(max_integer([]), None)

    def Test_OneElementList(self):
        self.assertEqual(max_integer([5]), 5)

    def Test_FloatList(self):
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)
    
    def Test_floatIntList(self):
        self.assertEqual(max_integer([1.53, 15.5, -9, 15, 6]), 15.5)

    def Test_stringList(self):
        self.assertEqual(max_integer(["Brennan", "is", "my", "name"]), "name")
    
    def Test_string(self):
        self.assertEqual(max_integer("ABcZt"), 't')
    
    def Test_EmptyStr(self):
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
