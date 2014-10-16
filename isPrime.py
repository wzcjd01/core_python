#!/usr/bin/env python
# __author__ = 'Wang Zhicheng'

from __future__ import print_function


def isPrime(num):
    if num == 1:
        return False

    count = num / 2
    while count > 1:
        if num % count == 0:
            rslt = False
            break
        count -= 1
    else:
        rslt = True

    return rslt


def _test():
    import random

    n = random.randint(10, 20)
    nums = [random.randrange(0, 999) for i in range(n)]

    for num in nums:
        if isPrime(num):
            print('{0} is prime'.format(num))
        else:
            print('{0} is not prime'.format(num))


if __name__ == '__main__':
    _test()
