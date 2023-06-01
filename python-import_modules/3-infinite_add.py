#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for arg in sys.argv[1:]:
        if arg.isdigit():
            result += int(arg)
    print(result)
