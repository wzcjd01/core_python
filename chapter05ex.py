# __author__ = 'Wang Zhicheng'
"""
exercises of chapter 5. page 151
"""
from __future__ import division
import corepython


# ex5-2
def wzc_prod(num1, num2):
    return num1 * num2


def _test():
    years = (1992, 1996, 2000, 1967, 1900, 2400)
    for i in years:
        print '%4i is leap?\t %s' % (i, corepython.isleepyear(i))

    change = (.78, .89, .14, .33)
    for i in change:
        i_c = corepython.coin_count(i)
        print '$%2f has\n' % i
        print '%i quarters, %i dimes, %i nickels and %i pennies' % (
            i_c['quarter'], i_c['dime'], i_c['nickel'], i_c['penny']
        )


if __name__ == '__main__':
    _test()
