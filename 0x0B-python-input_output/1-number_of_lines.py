#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding="UTF8") as myfile:

        lines = 0
        while True:
            numlines = myfile.readline()
            if not numlines:
                break
            lines += 1
        return line
