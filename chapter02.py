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


def ex0211():
    """menu-driven text applications"""

    enough = False
    procedures = ['ex0207', 'ex0208', 'ex0210']

    while not enough:
        print '\n\n======Operation Menu======\n'
        print '(1): ex0207: loops and strings'
        print '(2): ex0208: loops and operators'
        print '(3): ex0210: user input with loops and conditionals'
        print '(X): quit'

        choosed = raw_input('======please choose your operation: ')

        if choosed[0].lower() == 'x':
            enough = True
            print '\nBye-bye, have a nice day!!!'
        else:
            item = int(choosed[0]) - 1
            #TODO program into specific prodedures dispatched by procedure list item. procedures[item]()


def ex0215():
    """elementary sorting without using lists"""

    input_str = raw_input('input 3 numeric: ')
    input_str = input_str.split()

    num1 = float(input_str[0])
    num2 = float(input_str[1])
    num3 = float(input_str[2])

    if num1 > num2:
        tmp = num1
        num1 = num2
        num2 = tmp
        if num3 < num1:
            tmp = num3
            num3 = num2
            num2 = num1
            num1 = tmp
        elif num3 < num2:
            tmp = num3
            num3 = num2
            num2 = tmp

    inc_or_dec = raw_input('Sorting ====\nincreasingly (I)?\ndecreasingly(D)? ')
    if inc_or_dec.lower() == 'i':
        print 'Sorted increasingly: ', num1, num2, num3
    else:
        print 'sorted decreasingly: ', num3, num2, num1

if __name__ == '__main__':
    # test1()
    #ex0204()
    #ex0205()
    #ex0207()
    #ex0208()
    #ex0210()
    #ex0211()
    ex0215()