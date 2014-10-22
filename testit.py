#!/usr/bin/env python
"""
testit() invokes a given function with its arguments, returning
True packaged with the return value of the function on success
or False with the cause of failure."""


def testit(func, *nkwargs, **kwargs):
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)
    except Exception as diag:
        result = (False, str(diag))
    return result


def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print '-' * 20
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)
            if retval[0]:
                print '%s(%s) = ' % \
                    (eachFunc.__name__, repr(eachVal)), retval[1]
            else:
                print '%s(%s) = FAILED:' % \
                    (eachFunc.__name__, repr(eachVal)), retval[1]


if __name__ == '__main__':
    test()
