#!/usr/bin/env python
#__author__ = 'Wang Zhicheng'

from __future__ import print_function


def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print('largest factor of {0:d} is {1:d}'.format(num, count))
            break
        count -= 1
    else:
        print('{0:d} is prime'.format(num))


def _test():
    for eachNum in range(10, 21):
        showMaxFactor(eachNum)


if __name__ == '__main__':
    _test()
