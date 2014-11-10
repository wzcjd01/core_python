#!/usr/bin/env python
__author__ = 'Wang Zhicheng'


def count(byte, infile):
    """return the times of a byte value 'BYTE' appearing
    in the file 'INFILE', single thread version
    """

    with open(infile) as f:
        times = sum([eachLine.count(byte) for eachLine in f])

    return times


def _main():
    from timeit import timeit

    fname = raw_input('What file to find in:')
    byte = raw_input('to find what byte:')
    assert len(byte) == 1

    times, elapsed = timeit(count, byte, fname)

    print '{0} found {1} times in {2}'.format(byte, times, fname)
    print 'timeit:', elapsed


if __name__ == '__main__':
    _main()
