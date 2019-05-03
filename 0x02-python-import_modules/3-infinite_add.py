#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    suma = 0
    if len(argv) == 1:
        print("{}".format(0))
    for i in range(1, len(argv)):
        suma = suma + int(argv[i])
    print("{}".format(suma))
