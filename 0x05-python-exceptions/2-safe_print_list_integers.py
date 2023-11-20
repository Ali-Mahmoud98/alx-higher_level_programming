#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers.

    safe_print_list_integers:
        my_list (list): The integer should be printed followed by a new line.
        x (int): The integer should be printed followed by a new line.

    Returns:
        Returns True if value has been correctly printed
        (it means the value is an integer) Otherwise, returns False.
    """
    ret = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return ret
