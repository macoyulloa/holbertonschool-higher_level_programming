#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        if str[i].islower():
            num = ord(str[i]) - 32
        else:
            num = ord(str[i])
        if i != len(str):
            print("{}".format(chr(num)), end='')
        i += 1
    print("")
