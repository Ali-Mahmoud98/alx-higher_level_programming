#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Function writes a string to a text file (UTF8).

    Args:
        filename (str, optional): File name. Defaults to "".
        text (str, optional): text to be written in file. Defaults to "".
    Return:
        number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
