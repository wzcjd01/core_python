#!/usr/bin/env python
__author__ = 'Wang Zhicheng'
# https://www.quora.com/What-are-some-cool-Python-tricks

# dict and set comprehensions
d = {x: 10 * x for x in range(5)}
s = {10 * x for x in range(5)}


# transposing a matrix with zip
m = [[1, 2, 3], [4, 5, 6]]
mt = zip(*m)

# dividing a list into groups of n
l = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]
l1 = zip(*[iter(l)] * 3)

# create infinities
my_inf = float('Inf')
print 999999999999999999 > my_inf

my_neg_inf = float('-Inf')
print my_neg_inf > -9999999999999999999999


# Splat call: '*' is called the splat operator. It automatically
# unpacks stuff in a function call


def foo(a, b, c):
    print a, b, c

mydict = {'a': 1, 'b': 2, 'c': 3}
mylist = [10, 20, 30]

foo(*mydict)    # output: a c b
foo(**mydict)   # output: 1 2 3
foo(*mylist)


# itertools
from itertools import chain
print ''.join(x for x in chain('XFAEOEAEQA', 'EEAEKAEE') if x == 'O' or x == 'K')

# random *
from random import randint
print "\n".join(str(i)+":\t"+"*"*randint(1,10) for i in range(1,11))


# find the longest line in a file
print max(open('cooltricks.py'), key=len)

# sum the digits in an unsigned integer
print sum(map(int, str(19873538195)))