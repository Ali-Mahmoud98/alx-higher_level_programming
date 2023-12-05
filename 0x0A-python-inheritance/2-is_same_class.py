#!/usr/bin/python3
"""Defines Function that Checks the type of object"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object is exactly
    an instance of the specified class;
    otherwise False.
    Args:
        obj (any): object to check.
        a_class (type): type to compare.
    """
    # if isinstance(obj, a_class):
    #     return True
    if type(obj) is a_class:
        return True
    return False
