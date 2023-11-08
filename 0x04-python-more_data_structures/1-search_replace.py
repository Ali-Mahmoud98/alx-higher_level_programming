#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = list()
    for i in my_list:
        if i == search:
            newList += [replace]
            continue
        newList += [i]
    # return [replace if i == search else i for i in my_list]
    return newList     
