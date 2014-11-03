#!/usr/bin/env python


def closest(position, positions):
    x0, y0 = position
    dbest, ibest = None, None

    for i, (x, y) in enumerate(positions):
        # squared Euclidean distance from every position to the position of
        # interest.
        d = (x - x0) ** 2 + (y - y0) ** 2
        if dbest is None or d < dbest:
            dbest, ibest = d, i
    return ibest


def _test():
    from random import random
    from timeit import timeit
    positions = [(random(), random()) for _ in xrange(100000)]
    timeit('closest((.5, .5), positions)')

if __name__ == '__main__':
    _test()
