#!/usr/bin/python3

"""
This Module Contains the lookup function that returns attributes
of an object
"""


def lookup(obj):
    """
    Returns the Object's all available attributes

    Args:
        obj (<class object>); python object
    """
    return dir(obj)
