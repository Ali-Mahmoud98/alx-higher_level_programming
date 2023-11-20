#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as _except:
        print("Exception: {}".format(_except), file=sys.stderr)
        return None
    return res
