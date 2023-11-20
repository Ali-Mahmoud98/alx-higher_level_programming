#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
"""
sys.exc_info(): This function from the sys module returns a
tuple representing the current exception being handled.
The tuple contains three values: the exception type,
the exception value, and the traceback object. In this case,
[1] is used to access the second element of the tuple, which
is the exception value.
file=sys.stderr: to print output in stderr
"""
