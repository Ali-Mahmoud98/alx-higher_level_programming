#!/usr/bin/python3

def no_c(my_string):
    return ''.join(s for s in my_string if s != 'C' and s != 'c')
