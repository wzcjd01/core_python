__author__ = 'Wang Zhicheng'
"""
exercises of chapter 5. page 151
"""


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


if __name__ == '__main__':
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
