# coding=utf-8
# __author__ = 'Wang Zhicheng'
from __future__ import division
import random


class FooClass(object):
    """my very first class: FooClass"""
    version = 0.1  # class (data) attribute

    def __init__(self, nm='John Doe'):
        """constructor"""
        self.name = nm  # class instance (data) attribute
        print 'Created a class instance for', nm

    def showname(self):
        """display instance attribute and class name"""
        print 'your name is', self.name
        print 'my name is ', self.__class__.__name__

    def showver(self):
        """display class(static) attribute"""
        print 'version is ', self.version

    def addme2me(self, x):  # doses not use 'self'
        return x + x


# ex 5-3
def wzc_letter_grade(score):
    """
    take test score and output letter grade."""

    letters = ('A', 'B', 'C', 'D', 'F')
    tenth = int(score // 10)

    if tenth < 6:
        return letters[-1]
    elif tenth == 10:
        return letters[0]
    else:
        return letters[9 - tenth]


# ex 5-4
def isleepyear(year):
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
    coins = {'quarter': quan // 25,
             'dime': quan % 25 // 10,
             'nickel': quan % 25 % 10 // 5,
             'penny': quan % 5}
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
    op_index = operator.indexOf(ops, op)

    num1 = float(expr[0])
    num2 = float(expr[2])

    if op_index == 0:
        return num1 + num2
    elif op_index == 1:
        return num1 - num2
    elif op_index == 2:
        return num1 * num2
    elif op_index == 3:
        return num1 / num2
    elif op_index == 4:
        return num1 % num2
    elif op_index == 5:
        return num1 ** num2


# ex 5-17
def wzc_random_elements_sample(maxnum):
    """

    generate a list of random numbers (0 <= N <= maxnum) with
    random number (1 < n <=100) of elements.
    :param maxnum: maxisum different integers of population.
    :return: sorted sample list
    """

    # sampling volume
    n = random.randint(1, 100)
    # sampling 'n' items from population [0, maxnum]
    rng = range(maxnum + 1)
    while len(rng) < n:
        rng *= 2
    lst = random.sample(rng, n)

    return lst


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


def wzc_cmp(astr, bstr, case_insensitivity=False):
    alen = len(astr)
    blen = len(bstr)

    i = 0
    while i < alen and i < blen:
        if not case_insensitivity:
            if astr[i] > bstr[i]:
                return 1
            if astr[i] < bstr[i]:
                return -1
        if case_insensitivity:
            if astr[i].lower() > bstr[i].lower():
                return 1
            if astr[i].lower() < bstr[i].lower():
                return -1
        i += 1

    if alen == blen:
        return 0
    elif alen < blen:
        return -1
    else:
        return 1


def wzc_ispalindromic(s, strict=True):
    """
    determine if a string is palindromic.
    :param s:
    :param strict: false to suppress symbols and whitespace wherein.
    :return: True if argument 's' is palindromic.
    """
    from string import ascii_letters

    result = True
    if not strict:
        s = [c for c in s if c in ascii_letters]

    slen = len(s)
    i = 0

    while i < slen // 2:
        if s[i] != s[-1 - i]:
            result = False
            break
        i += 1

    return result


def int_eng(i):
    """
    given an integer value, return a string with the equivalent
    Englist text of each digit.
    """

    rslt = []
    txt = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    il = list(str(i))
    times = len(il)

    k = 0
    while k < times:
        index = int(il.pop(0))
        rslt.append(txt[index])
        k += 1

    return '-'.join(rslt)


def atoc(s):
    """

    :param s: a string representation of a complex numbers
    :return: complex number object represented by 's'
    """
    chars = "0123456789.+-eEjJ"
    # todo: atoc()


def dayslapse(datefrom, dateto):
    """
    ex 6-15
    :param datefrom: beginning date in format MM/DD/YY or MM/DD/YYYY
    :param dateto: end date in format MM/DD/YY or MM/DD/YYYY
    :return: days between the two dates
    """
    import string

    date_from = string.split(datefrom, '/')
    date_to = string.split(dateto, '/')

    # ‘YY' default to be a 21st century year when YY <= '20'
    dl1 = [int(date_from[i]) for i in (2, 0, 1)]  # [YYYY, MM, DD]
    dl2 = [int(date_to[i]) for i in (2, 0, 1)]  # [YYYY, MM, DD]

    days = 0
    if dl1[1:] == [2, 29]:
        dl1[2] = 28     # so that every year after have the day 'Feb. 28'
        days -= 1

    leap = 0

    date_from = string.split(datefrom, '/')
    date_to = string.split(dateto, '/')

    # ‘YY' default to be a 21st century year when YY <= '20'
    dl1 = [int(date_from[i]) for i in (2, 0, 1)]  # [YYYY, MM, DD]
    # default YY: (1920, 2020]
    if dl1[0] <= 20:
        dl1[0] += 2000
    elif dl1[0] < 100:
        dl1[0] += 1900

    dl2 = [int(date_to[i]) for i in (2, 0, 1)]  # [YYYY, MM, DD]
    if dl2[0] <= 20:
        dl2[0] += 2000
    elif dl2[0] < 100:
        dl2[0] += 1900

    days = 0

    l = 0
    while True:
        dl1[0] += 1  # step: 1 year
        if dl1 <= dl2:
            days += 365
            # leap day
            leap += 1
            if leap // 4:
                days += 1
                leap = 0
            l += 1
            # leap day
            if l // 4:
                days += 1
                l = 0
        else:
            break

    month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    day1 = 0
    day2 = 0
    if dl1[1] > 1:
        for m in range(1, dl1[1]):
            day1 += month[m-1]
    if dl2[1] > 1:
        for m in range(1, dl2[1]):
            day2 += month[m-1]

    days += ((day2 + dl2[2]) - (day1 + dl1[2])) % 365

    return days
