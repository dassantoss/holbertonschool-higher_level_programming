#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_by_keys = sorted(a_dictionary.keys())
    for key in sorted_by_keys:
        print("{}: {}".format(key, a_dictionary[key]))
