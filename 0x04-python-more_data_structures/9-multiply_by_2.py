#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = dict()
    for k in a_dictionary.keys():
        d = a_dictionary[k] * 2
    return d
