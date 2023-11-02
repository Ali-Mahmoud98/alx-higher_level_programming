#!/usr/bin/python3
from add_0 import add

'''
__name__ is a built-in Python variable that is automatically set by the
Python interpreter.

When a Python script is executed, the __name__ variable is set to
'__main__' if the script is the main program being run.
This happens when you directly run the script using the Python interpreter.
'''

if __name__ == '__main__':
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
