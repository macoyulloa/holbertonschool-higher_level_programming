#!/usr/bin/python3
for alph in range(97, 122):
    if alph == 101 or alph == 113:
        continue
    print("{:s}".format(chr(alph)), end='')
