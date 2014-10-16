#!/usr/bin/env python
from __future__ import print_function
__author__ = 'Wang Zhicheng'


def isperfect(num):
    import getFactors

    if sum(i for i in getFactors.getFactors(num)) == 2 * num:
        return 1
    else:
        return 0


def _test():
    for n in range(1, 10000):
        if isperfect(n):
            print('{0:d} is a perfect number!'.format(n))


if __name__ == '__main__':
    _test()

