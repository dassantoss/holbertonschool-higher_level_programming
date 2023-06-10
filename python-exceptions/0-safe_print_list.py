#!/usr/bin/python6
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
        print("\n", end="")
    except Exception as ex:
        print("\n", end="")
        return (i)
    else:
        return (i + 1)
