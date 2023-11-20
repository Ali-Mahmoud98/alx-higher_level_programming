#!/usr/bin/python3
def safe_print_integer(value):
    """prints an integer with "{:d}".format().

    safe_print_integer:
        value (int): The integer should be printed followed by a new line.

    Returns:
        Returns True if value has been correctly printed
        (it means the value is an integer) Otherwise, returns False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
