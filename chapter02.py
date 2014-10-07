__author__ = 'Wang Zhicheng'

import sys
sys.path.append('~/PycharmProjects/core.python')

import corepython

debug = True


def test1():
    """test1 function"""
    foo = corepython.FooClass()
    if debug:
        print "run test1()"


if __name__ == '__main__':
    test1()