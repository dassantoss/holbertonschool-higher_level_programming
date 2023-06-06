#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = (None, None)
    lenght = len(sentence)
    if lenght == 0:
        my_tuple = (lenght, None)
    else:
        first = sentence[0]
        my_tuple = (lenght, first)
    return (my_tuple)
