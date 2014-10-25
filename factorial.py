#!/usr/bin/env python
__author__ = 'Wang Zhicheng'


def factorial1(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1

    return fact


def factorial2(num):
    return reduce(lambda x, y: x * y, range(1, num + 1))


def factorial3(num):
    if num ==  0 or num == 1:
        return 1
    else:
        return num * factorial3(num - 1)


def _test():
    from timeit import timeit
    n = 10000
    pr = "result: %d\tTime elapsed: %f"
    print "loop---", pr % timeit(factorial1, n)
    print "reduce---", pr % timeit(factorial2, n)
    # print "recursion---", pr % timeit(factorial3, n)


if __name__ == '__main__':
    _test()
