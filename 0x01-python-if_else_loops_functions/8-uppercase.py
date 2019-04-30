#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        if str[i].islower():
            num = ord(str[i]) - 32
        else:
            num = ord(str[i])
        if i != len(str) -1:
            print("{}".format(chr(num)), end='')
        else:
            print("{}".format(chr(num)))
        i += 1
