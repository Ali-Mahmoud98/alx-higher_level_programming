#!/usr/bin/python3
"""Defines a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Function to reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str, optional): File name. Defaults to "".
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
