#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="UTF8") as myfile:
        numlines = 0
        while nb_lines <= 0 or nb_lines > numlines:
            lines = myfile.readline()
            if not lines:
                break
            numlines += 1
            print(lines, end='')
