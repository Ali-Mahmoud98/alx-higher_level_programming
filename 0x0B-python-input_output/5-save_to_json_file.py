#!/usr/bin/python3
"""Defines a function writes an Object to a text file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation.

    Args:
        my_obj (Any): The object to be serialized to JSON.
        filename (str): the file name.
    """
    with open(filename, mode="w") as f:
        json.dumps(my_obj, f)
