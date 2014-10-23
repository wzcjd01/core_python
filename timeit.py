#!/usr/bin/env python
__author__ = 'Wang Zhicheng'

from time import clock


def timeit(func, *args, **kwargs):
    now = clock()
    retval = func(*args, **kwargs)
    elapsed = clock() - now
    return retval, elapsed
