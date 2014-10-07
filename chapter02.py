__author__ = 'Wang Zhicheng'

import sys

sys.path.append('~/PycharmProjects/core.python')

import corepython

debug = True


def test1():
    """test1 function"""

    foo1 = corepython.FooClass()
    foo1.showname()
    foo1.showver()
    print foo1.addme2me(5)
    print foo1.addme2me('xyz')

    foo2 = corepython.FooClass('w z c')
    foo2.showname()

    if debug:
        print "run test1()"


def ex0204():
    """user input with raw_input()"""

    foo = raw_input('please input: ')
    print 'you have just input: '
    print foo

    bar = raw_input('please input a numeric: ')
    print 'you have just input: ', int(bar)


def ex0205():
    """loops and numbers"""

    times = 0
    while times <= 10:
        print times,
        times += 1
    print

    for i in range(11):
        print i,
    print


def ex0207():
    """loops and strings"""

    instr = raw_input('input something: ')
    instrlen = len(instr)
    i = 0

    while i < instrlen:
        print instr[i] + ' ',
        i += 1

    for i in range(len(instr)):
        print instr[i] + '-',

    print


def ex0208():
    """loops and operators"""

    numlist = [0, 0, 0, 0, 0]
    astr = raw_input('please input five numerics: ')
    alist = astr.split()

    for i in range(5):
        numlist[i] = float(alist[i])

    # numsum the inputted numeric
    # while version
    numsum0 = 0
    i = 0
    while i < len(numlist):
        numsum0 += numlist[i]
        i += 1
    print 'numsum0 is: ', numsum0

    # for version
    numsum1 = 0
    for i in range(len(numlist)):
        numsum1 += numlist[i]
    print 'numsum1 is: ', numsum1


def ex0210():
    """user input with loops and conditionals"""

    donewell = False

    while not donewell:
        anum = raw_input('input a number between 1 and 100: ')
        anum = int(anum)
        if 1 < anum < 100:
            donewell = True
            print 'done well, you input: ', anum


if __name__ == '__main__':
    # test1()
    #ex0204()
    #ex0205()
    #ex0207()
    #ex0208()
    ex0210()