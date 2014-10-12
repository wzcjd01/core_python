#__author__ = 'Wang Zhicheng'

from string import atof as _atof


def ex0603():
    instr = raw_input('Enter a list of numbers (space delimited: >> ').split()
    innumlist = [_atof(x) for x in instr]
    innumlist.sort(reverse=True)
    print "\nNumbers sorted as: >> ", innumlist
    print "-" * 30

    instr2 = raw_input('Enter a list of strings (space delimited: >> ').split()
    instr2.sort(reverse=True)
    print "\nStrings sorted as: >> ", instr2

if __name__ == '__main__':
    print "*" * 5, "exercise 6-3 ", "*" * 5
    ex0603()
