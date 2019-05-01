#!/usr/bin/python3
def remove_char_at(str, n):
    firstPart = str[:n]
    lastPart = str[n+1:]
    final = firstPart + lastPart
    print(final)
