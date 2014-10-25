#!/usr/bin/env python
# http://simeonfranklin.com/blog/2012jul/1/python-decorators-in-12-steps/


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coord: " + str(self.__dict__)


# bounds checking decorator
def wrapper(func):
    def checker(a, b):
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0,
                             ret.y if ret.y > 0 else 0)
        return ret

    return checker


@wrapper
def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)


@wrapper
def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)


def _test1():
    one = Coordinate(100, 200)
    two = Coordinate(300, 200)
    three = Coordinate(-100, -100)

    print sub(one, two)
    print add(one, three)


def logger(func):
    def inner(*args, **kwargs):
        print "Arguments were: %s, %s" % (args, kwargs)
        return func(*args, **kwargs)
    return inner


@logger
def foo1(x, y=1):
    return x * y


@logger
def foo2():
    return 2


def _test2():
    print foo1(5, 4)
    print foo1(1)
    print foo2()


if __name__ == '__main__':
    _test1()
    _test2()
