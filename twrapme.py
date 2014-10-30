#!/usr/bin/env python
"""
Class definition that wraps any buit-in type, adding time attributes;
get(), set(), and string representation methods; and delegating all
remaining attribute access to those of the standard type. """

from time import time, ctime, sleep


class TimeWrapMe(object):
    def __init__(self, obj):
        self.__data = obj
        self.__ctime = self.__mtime = self.__atime = time()

    def get(self):
        self.__atime = time()
        return self.__data

    def gettimeval(self, t_type):
        if not isinstance(t_type, str) or t_type[0] not in 'cma':
            raise TypeError("argument of 'c', 'm' or 'a' required")
        # name 'mangling': local attribute, no delegation.
        return getattr(self, '_%s__%stime' % (
            self.__class__.__name__, t_type[0]))
        # return getattr(self, '__%stime' % t_type[0])

    def gettimestr(self, t_type):
        return ctime(self.gettimeval(t_type))

    def set(self, obj):
        self.__data = obj
        self.__mtime = self.__atime = time()

    def __repr__(self):
        self.__atime = time()
        return repr(self.__data)

    def __str__(self):
        self.__atime = time()
        return str(self.__data)

    def __getattr__(self, item):    # delegate
        self.__atime = time()
        return getattr(self.__data, item)

if __name__ == '__main__':
    timeWrappedObj = TimeWrapMe(932)
    print timeWrappedObj.gettimestr('c')
    print timeWrappedObj.gettimestr('m')
    print timeWrappedObj.gettimestr('a')

    sleep(2)
    print timeWrappedObj

    print timeWrappedObj.gettimestr('a')
    print timeWrappedObj.gettimestr('m')

    print '-' * 40
    timeWrappedStr= TimeWrapMe('abc')
    print timeWrappedStr.gettimestr('c')
    print timeWrappedStr.gettimestr('m')
    print timeWrappedStr.gettimestr('a')

    sleep(2)
    print timeWrappedStr

    print timeWrappedStr.gettimestr('a')
    print timeWrappedStr.gettimestr('m')

    print timeWrappedStr.upper()    # Delegation
