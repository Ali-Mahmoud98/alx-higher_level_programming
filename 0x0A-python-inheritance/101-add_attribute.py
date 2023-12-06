#!/usr/bin/python3
"""Defines Function add_attribute"""


def add_attribute(obj, attr, value):
    """
    Add a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute will be added.
        attr: The name of the new attribute.
        value: The value of the new attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
