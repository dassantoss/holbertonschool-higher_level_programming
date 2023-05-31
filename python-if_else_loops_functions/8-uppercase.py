#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            upper_ch = chr(ord(ch) - 32)
        else:
            upper_ch = ch
        upper_str += upper_ch
    print("{upper_str}\n".format(upper_str=upper_str), end="")
