#!/usr/bin/python3
" find peak "


def find_peak(list_of_integers):
    leng = len(list_of_integers)
    if leng == 0:
        return None
    if leng == 1:
        return list_of_integers[0]
    elif list_of_integers[leng-1] >= list_of_integers[leng-2]:
        del list_of_integers[leng-2]
    elif list_of_integers[leng-1] <= list_of_integers[leng-2]:
        del list_of_integers[leng-1]
    return find_peak(list_of_integers)
