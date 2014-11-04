#!/usr/bin/env python
# https://www.quora.com/What-are-the-Python-features-you-wish-youd-known-earlier

import sys
sys.setrecursionlimit(100000)


# Memoizations: memoizers could potentially take any recursive functions
# as an input and return a memoized version of it, which makes the code
# to run significantly faster.
def memoize(f):
    def memf(*args):
        if args not in memf.cache:
            memf.cache[args] = f(*args)
        return memf.cache[args]
    memf.cache = {}
    return memf


# memoized recursive function
@memoize
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# recursive version
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


def _test():
    from timer import Timer

    with Timer() as t1:
        fact(100000)

    with Timer() as t2:
        factorial(100000)

    print 'Recursive version time:', t1.interval
    print 'Memoized recursive version time:', t2.interval

if __name__ == '__main__':
    _test()
