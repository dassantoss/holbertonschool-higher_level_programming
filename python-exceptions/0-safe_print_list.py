#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            print("\n", end="")
        except Exception as ex:
            print("\n", end="")
            return (i)
        else:
            return (i + 1)
