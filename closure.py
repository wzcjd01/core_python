#!/usr/bin/env python
"""
objects are data with methods attached, closures are functions
with data attached.
A closure allows you to bind variables into a function without
passing them as parameters.
"""


def make_counter():
    i = [0]

    def counter():  # counter() is a closure
        # nonlocal i
        i[0] += 1
        return i[0]
    return counter

c1 = make_counter()
c2 = make_counter()

print (c1(), c1(), c1(), c2(), c2())


def foo():
    x = 3

    def bar():
        print x
    x = 5
    return bar

bar = foo()
bar()   # print 5. The function returned from foo retains a hook to the local
        # var 'x' even though 'x' has gone out of scope.


def foo():
    x = [3]

    def bar():
        print x[0]

    def ack():
        x[0] = 7
    x[0] = 5
    return (bar, ack)

bar, ack = foo()
ack()
bar()   # print 7
