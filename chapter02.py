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

    astr = raw_input('please input five numerics: ').split()

    numlist = []
    for i in range(5):
        numlist.append(astr[i])

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

    while True:
        anum = raw_input('input a number between 1 and 100: ').strip()
        if anum.isdigit() and 1 < anum < 100:
            print 'done well, you input: ', anum
            break


def ex0211():
    """menu-driven text applications"""

    procedures = {'1': ex0207, '2': ex0208, '3': ex0210}

    while True:
        print '\n\n======Operation Menu======\n'
        print '(1): ex0207: loops and strings'
        print '(2): ex0208: loops and operators'
        print '(3): ex0210: user input with loops and conditionals'
        print '(X): quit'

        choosed = raw_input('======please choose your operation: ').strip()[0].lower()

        if choosed == 'x':
            print '\nBye-bye, have a nice day!!!'
            break
        else:
            procedures[choosed]()


def ex0215():
    """elementary sorting without using lists"""

    input_str = raw_input('input 3 numeric: ')
    input_str = input_str.split()

    num1 = float(input_str[0])
    num2 = float(input_str[1])
    num3 = float(input_str[2])

    if num1 > num2:
        # tmp = num1
        # num1 = num2
        # num2 = tmp
        num1, num2 = num2, num1
        if num3 < num1:
            # tmp = num3
            # num3 = num2
            # num2 = num1
            # num1 = tmp
            num1, num2, num3 = num3, num1, num2
        elif num3 < num2:
            # tmp = num3
            # num3 = num2
            # num2 = tmp
            num2, num3 = num3, num2

    inc_or_dec = raw_input('Sorting ====\nincreasingly (I)?\ndecreasingly(D)? ')
    if inc_or_dec.lower() == 'i':
        print 'Sorted increasingly: ', num1, num2, num3
    else:
        print 'sorted decreasingly: ', num3, num2, num1


if __name__ == '__main__':
    # test1()
    # ex0204()
    #ex0205()
    #ex0207()
    #ex0208()
    #ex0210()
    ex0211()
    #ex0215()