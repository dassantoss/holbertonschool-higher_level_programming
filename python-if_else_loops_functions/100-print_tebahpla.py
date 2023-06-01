#!/usr/bin/python3
for c in reversed(range(65, 91)):
    if c % 2 != 0:
        print(chr(c), end="")
    else:
        print(chr(c + 32), end="")
