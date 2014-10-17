#!/usr/bin/env python
__author__ = 'Wang Zhicheng'


# todo:
def file_diff_seek(fobj1, fobj2):
    """
    line number and column number where the first difference
    occurs between two files.
    :param fobj1:
    :param fobj2:
    :return:
    """

    line = 0
    col = 0

    while True:
        line1 = fobj1.readline()
        line2 = fobj2.readline()
        len1 = len(line1)
        len2 = len(line2)
        m = 0
        n = 0

        while m < len1 and n < len2:
            if line1[m] == line[n]:
                m += 1
                n += 1
            else:
                col = m
                break
        else:
            line += 1

    return line, col
