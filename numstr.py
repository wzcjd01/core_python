#!/usr/bin/env python


class NumStr(object):

    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string

    def __str__(self):
        return '[%d :: %r]' % (self.__num, self.__string)

    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, NumStr):
            return self.__class__(self.__num + other.__num,
                                  self.__string + other.__string)
        else:
            raise TypeError('Illegal argument type for built-in operation')

    def __mul__(self, num):
        if isinstance(num, int):
            return self.__class__(self.__num * num,
                                  self.__string * num)

    def __nonzero__(self):  # False if both are
        return self.__num or len(self.__string)

    def __cmp__(self, other):   # define for cmp()
        return cmp(self.__num, other.__num) + \
            cmp(self.__string, other.__string)

if __name__ == '__main__':
    a = NumStr(3, 'foo')
    b = NumStr(3, 'goo')
    c = NumStr(2, 'foo')
    d = NumStr()
    e = NumStr(string='boo')
    f = NumStr(1)
    g = NumStr(-1, 'goo')

    for each in (a, b, c, d, e, f, g):
        print each

    print a < b
    print b < c
    print b * 2
    print a + b
    print b + a
    print a == g

    if d:
        print 'd: True'
    else:
        print 'd: False'
