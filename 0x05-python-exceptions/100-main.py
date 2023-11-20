#!/usr/bin/python3
safe_print_integer_err = \
    __import__('100-safe_print_integer_err').safe_print_integer_err

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
"""
./100-main.py 2> /dev/null:
=> this command runs a Python script, and any error messages
produced by the script are suppressed (redirected to "/dev/null").

=> "2> /dev/null": Redirects the standard error (file descriptor 2)
to "/dev/null". "/dev/null" is a special file in Unix-like systems
that discards all data written to it.
"""
