#!/usr/bin/python3
"""Defines a function that append a string to a text file."""


def write_file(filename="", text=""):
    """Function append a string to the end of a text file (UTF8).

    Args:
        filename (str, optional): File name. Defaults to "".
        text (str, optional): text to be appended in file. Defaults to "".
    Return:
        number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
