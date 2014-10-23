#!/usr/bin/env python
__author__ = 'Wang Zhicheng'


def max2(obj1, obj2):
    return obj1 if obj1 > obj2 else obj2


def min2(obj1, obj2):
    return obj2 if obj1 > obj2 else obj1


def my_max(*seq):
    return reduce(max2, seq)


def my_min(*seq):
    return reduce(min2, seq)


def _test():
    nums = (82.9, 1.2e10, .145, 101, -13.2)
    strs = ('abc', '123', 'abd', '012', 'xyz', 'uvw')
    print 'max:', my_max(*nums)
    print 'max:', my_max(*strs)
    print 'min:', my_min(*nums)
    print 'min:', my_min(*strs)


if __name__ == '__main__':
    _test()
