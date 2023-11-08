#!/usr/bin/python3
def uniq_add(my_list=[]):
    _set = set(my_list)
    res = 0
    for i in _set:
        res += i
    return res
