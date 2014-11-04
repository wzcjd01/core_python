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

# sorted with lambda functions
reviews = [{'rating': 4.5, 'date': '2013-03-10', 'comment': 'A++, will eat again'},
           {'rating': 5, 'date': '2013-03-11', 'comment': 'Shut up and take my money!'},
           {'rating': 1, 'date': '2013-03-08', 'comment': 'I want my money back'},
           {'rating': 4, 'date': '2013-03-10', 'comment': 'Great food!'}]

sorted(reviews, key=lambda review: (review['date'], review['rating']), reverse=True)

# None is less than any number
sorted([1, 2, None, 4.5, float('-Inf')])

# Named subgroups in regular expressions
import re
m = re.match(r"(?P<first>\w+) (?P<last>\w+)", "John Smith")
print m.groupdict()


# Creating 'enums'
# http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    # support for converting the values back to names
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

Color = enum('RED', 'GREEN', 'BLUE', CYAN=4, BLACK=5, MAGENTA=6)
print Color.RED, Color.GREEN, Color.BLUE, Color.MAGENTA
