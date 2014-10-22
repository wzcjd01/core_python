#!/usr/bin/env python
"""
demonstration of a decorator (and closures):
    decorate (or overlay) a function, returning the altered
    function object and reassignin it to the original identifier,
    forever losing access to the original function object."""

from time import ctime, sleep


def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()
    return wrappedFunc


@tsfunc
def foo():
    pass


foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()
