#!/usr/bin/env python
#__author__ = 'Wang Zhicheng'

from __future__ import print_function

def getFactors(num):
    factors = [num, 1]
    counter = num / 2

    while counter > 1:
        if num % counter == 0:
            factors.append(counter)
        counter -= 1

    return  factors


def _test():
    import random
    n = random.randrange(1, 10000)

    print('{0:d} factors:\n\t{1:s}'.format(n, getFactors(n)))


if __name__ == '__main__':
    _test()
