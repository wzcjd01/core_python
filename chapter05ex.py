#__author__ = 'Wang Zhicheng'
"""
exercises of chapter 5. page 151
"""
from __future__ import division
import random


# ex5-2
def wzc_prod(num1, num2):
    return num1 * num2


# ex 5-3
def wzc_letter_grade(score):
    """
    take test score and output letter grade."""

    letters = ('A', 'B', 'C', 'D', 'F')
    tenth = score // 10

    if tenth < 6:
        return letters[-1]
    elif tenth == 10:
        return letters[0]
    else:
        return letters[9-tenth]


# ex 5-4
def wzc_isleep(year):
    """
    determine whether a given year is a leep year"""

    isleep = not (year % 4) and (year % 100 or not year % 400)
    return bool(isleep)


# ex 5-5
def coin_count(changes):
    """

    given a value < $1, calculate the number of basic
    American coins, maximizing the number of larger
    denomination coins.
    """

    quan = 100 * changes  # dollars to cents
    coins = {}
    coins['quarter'] = quan // 25
    coins['dime'] = quan % 25 // 10
    coins['nickel'] = quan % 25 % 10 // 5
    coins['penny'] = quan % 5
    return coins


# ex 5.6
def wzc_arith(opstr):
    """

    calculator application for operators: + - * / % **
    """

    import operator

    ops = ('+', '-', '*', '/', '%', '**')
    expr = str(opstr).split()

    op = expr[1]
    ind = operator.indexOf(ops, op)
    num1 = float(expr[0])
    num2 = float(expr[2])

    if ind == 0:
        return num1 + num2
    elif ind == 1:
        return num1 - num2
    elif ind == 2:
        return num1 * num2
    elif ind == 3:
        return num1 / num2
    elif ind == 4:
        return num1 % num2
    elif ind == 5:
        return num1 ** num2


# ex 5-10 conversion
def dcelsius(fahren):
    """

    convert Fahrenheit to Celsius temperature
    """

    return (fahren - 32) * (5 / 9)


def dfahrenheit(celsius):
    """

    convert Celsius to Fahrenheit temperature
    """

    return 32 + celsius * 9 / 5


# ex 5-15 GCD and LCM
def wzc_gcd(num1, num2):
    """

    greatest common divisor
    """

    pass


def wzc_lcm(num1, num2):
    """

    least common multiple
    """

    pass


# ex 5-17
def wzc_rndset(maxnum, smp1, replace=True):
    """

    generate a list of random numbers (0 <= n <= maxnum) with
    random number (1 < N <=100) of elements. Then randomly
    select a set of these numbers.
    :param maxnum: maxisum int of population.
    :param smp1: sample number
    :return: sorted sample list
    """

    n = random.randint(1, 100)
    lst = random.sample(xrange(maxnum + 1), n)

    # fixme random.sample is sampling without replacement.
    if not 0 < smp1 < n:
        raise ValueError('sample larger than population')
    else:
        return random.sample(lst, smp1)


def _test():

    years = (1992, 1996, 2000, 1967, 1900, 2400)
    for i in years:
        print '%4i is leap?\t %s' % (i, wzc_isleep(i))

    change = (.78, .89, .14, .33)
    for i in change:
        i_c = coin_count(i)
        print '$%2f has\n' % i
        print '%i quarters, %i dimes, %i nickels and %i pennies' % (
            i_c['quarter'], i_c['dime'], i_c['nickel'], i_c['penny']
        )


if __name__ == '__main__':
    _test()
