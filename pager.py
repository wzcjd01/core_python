#!/usr/bin/env python
from __future__ import print_function

__author__ = 'Wang Zhicheng'


def file_linenum(fobj):
    return sum([1 for line in fobj])


def pager(fobj):

    linenum = file_linenum(fobj)
    l = 0

    # fixme:
    for line in fobj:
        print(line)
        l += 1
        if l % 25 == 0 and l < linenum:
            prompt = raw_input('**** press a key to continue ****')
            if prompt != '':
                continue


def _test():
    path = raw_input('Enter filename for pager:>> ')
    f = open(path.strip(), 'r')
    pager(f)
    f.close()


if __name__ == '__main__':
    _test()
