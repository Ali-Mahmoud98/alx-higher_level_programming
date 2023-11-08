#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    res = 0
    d = 0
    for i in my_list:
        res += i[0] * i[1]
        d += i[1]
    return res / d
