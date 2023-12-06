#!/usr/bin/python3
"""Defines a function that creates an Object from a JSON file."""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file.

    Args:
        filename (str): JSON file name.
    """
    with open(filename) as f:
        return json.load(f)
