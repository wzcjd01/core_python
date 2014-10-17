# /usr/bin/env python
from __future__ import print_function

__author__ = 'Wang Zhicheng'


def decomment(fobj):
    for line in fobj:
        if len(line) != 0:
            i = 0
            while True:
                char = line[i]
                if char != '\n' and char != '#':
                    i += 1
                else:
                    break

            print('{0:s}\n'.format(line[:i]))




if __name__ == '__main__':
    decomment(open('ospathex.py', 'r'))
