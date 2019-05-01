#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    else:
        firstPart = str[:n]
        lastPart = str[n+1:]
        return firstPart + lastPart
