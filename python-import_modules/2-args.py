#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    num_args = len(args) - 1
    msg = ""

    if num_args == 0:
        msg = "arguments."
    elif num_args == 1:
        msg = "argument:"
    else:
        msg = "arguments:"

    print("{} {}".format(num_args, msg))

    for i in range(1, num_args + 1):
        print("{}: {}".format(i, args[i]))
