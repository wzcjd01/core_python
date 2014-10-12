# __author__ = 'Wang Zhicheng'

from __future__ import division
from string import atoi as _atoi

import corepython


def ex0603():
    instr = raw_input('Enter a list of numbers (space delimited: >> ').split()
    innumlist = [_atoi(x, 0) for x in instr]
    innumlist.sort(reverse=True)
    print "\nNumbers sorted as: >> ", innumlist
    print "-" * 50

    instr2 = raw_input('Enter a list of strings (space delimited: >> ').split()
    instr2.sort(reverse=True)
    print "\nStrings sorted as: >> ", instr2


def ex0604():
    scores = raw_input('Enter test scores (space delimited: >> ').split()
    scoresnum = [float(x) for x in scores]
    scoresletter = [corepython.wzc_letter_grade(x) for x in scoresnum]
    average = corepython.wzc_letter_grade(sum(scoresnum) / len(scoresnum))

    print "\nScores in letters are: >> ", scoresletter
    print "Average score is: >> ", average


def ex0605():
    print "\n** 6-5-a"
    instr = raw_input('input something: ')

    for i in range(len(instr)):
        print instr[i], '-', instr[-i - 1]

    print "\n** 6-5-b"
    fst = raw_input("string compare: enter first string: >> ")
    scnd = raw_input("string compare: enter second string: >> ")
    rst = corepython.wzc_cmp(fst, scnd)

    output = {1: "First String larger", 0: "Strings tie", -1: "First String smaller"}
    print output[rst]

    print "\n** 6-5-c"
    s = raw_input("Enter a string: >> ")
    strict = raw_input("palindromic string determined strictly or not(Y/N: >> ").strip().lower()

    if strict == 'y':
        strict = True
    elif strict == 'n':
        strict = False
    else:
        print "Palindromic string determined default as strictly"

    print "Your input: ", repr(s),
    if corepython.wzc_ispalindromic(s, strict):
        print "is palindromic!!"
    else:
        print "is not palindromic!!!"


def ex0608():
    i1 = 9873535
    print corepython.int_eng(i1)


if __name__ == '__main__':
    print "*" * 5, "exercise 6-3 ", "*" * 5
    ex0603()

    # print "*" * 5, "exercise 6-2 ", "*" * 5
    # ex0604()

    # print "*" * 5, "exercise 6-5 ", "*" * 5
    # ex0605()

    # print "*" * 5, "exercise 6-8 ", "*" * 5
    # ex0608()