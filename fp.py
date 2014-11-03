# functional programming with python
# http://kachayev.github.io/talks/uapycon2012/index.html
# by alexey kachayev, 2012

############################################################
# imperative style (actions that cha
############################################################
expr, res = "28+32+++32++39", 0
for t in expr.split("+"):
    if t != "":
        res += int(t)

print res

############################################################
# functional style = appy transformation and composition
############################################################
from operator import add
expr = "28+32+++32++39"
print reduce(add, map(int, filter(bool, expr.split("+"))))

############################################################
# module 'operator'
############################################################
import operator
operator.add(1,2)
operator.mul(3,10)
operator.pow(2,3)
operator.itemgetter(1)([1,2,3])

############################################################
# module 'itertools'
############################################################
list(itertools.chain([1,2,3], [10,20,30]))
list(itertools.chain(*(map(xrange, range(5)))))
list(itertools.imap(pow, (2,3,10), (5,2,3)))
dict(itertools.izip("ABCD", [1,2,3,4]))
list(itertools.starmap(lambda k,v: "%s => %s" % (k,v), ...
                       {"a":1, "b":2}.item()))['a => 1', 'b => 2']

############################################################
## can we avoid loops?
############################################################
name = None
while name is None:
    name = raw_input()
    if len(name) < 2:
        name = None
        
# recursion
def get_name():
    name = raw_input()
    return name if len(name) >= 2 else get_name()

############################################################
# tail recursion
############################################################

############################################################
# first-class functions
############################################################
def add(a,b):
    return a + b

add = lambda a, b: a + b

def calculations(a,b):
    def add():
        return a + b
    return a, b, add

############################################################
# high-ordered function
############################################################
# pass functions as argument
map(lambda x: x^2, [1,2,3,4,5])

# function return function as result
def speak(topic):
    print "My speech is " + topic

def timer(fn):
    def inner(*args, **kwargs):
        t = time()
        fn(*args, **kwargs)
        print "took {time}".format(time=time() - t)

    return inner
speaker = timer(speak)
speaker("FP with Python")

############################################################
## how to write good code dealing with functions
############################################################
# Partial Function Application
# papply : (((a x b) -> c) x a) -> (b -> c) = \lambda(f,x). \lambda y . f (x,y)
# "the process of fixing a number of arguments to a function, producing another function of smaller arity"

def log(level, message):
    print "[{level}]: {msg}".format(level=level, msg=message)

log("debug", "start doing something")
log("debug", "continue with someting")
log("debug", "finished. profile?")

def debug(message):
    log("debug", message)
# simplify...
from functools import partial
debug = partial(log, "debug")

############################################################
## Currying
############################################################
# curry: ((a x b) -> c) -> (a -> (b -> c)) = \lambda f. \lambda x. \lambda y. f (x, y)
# "the technique of transforming a function that takes multiple arguments in such a way that it can be called as a chain of functions each with a single argument"

## segment sum
def simple_sum(a,b):
    return sum(range(a, b+1))

simple_sum(1,100)

## squares
def square_sum(a,b):
    return sum(map(lambda x:x**2, range(a,b+1)))

square_sum(1,100)

## logarithms
def log_sum(a,b):
    return sum(map(math.log, range(a,b+1)))

log_sum(1,100)

## in general ...
def fsum(f):
    def apply(a,b):
        return sum(map(f, range(a,b+1)))
    return apply

log_sum = fsum(math.log)
square_sum = fsum(lambda x: x**2)
simple_sum = fsum(int)  # fsum(lambda x: x)

fsum(lambda x: x*2)(1,10)

import functools
fsum(functools.partial(operator.mul, 2))(1,10)

############################################################
## currying (standard library)
############################################################
from operator import itemgetter
itemgetter(3)([1,3,5,7,9])

from operator import attrgetter as attr
class Speaker(object):
    def __init__(self, name):
        self.name = "[name] " + name

alexey = Speaker("alexey")
attr("name")(alexey)

from operator import methodcaller
methodcaller("__str__")([1,2,3,4,5])
methodcaller("keys")(dict(name="alexey", topic='fp'))
values_extractor = methodcaller("values")
values_extractor(dict(name="alexey", topic="fp"))
methodcaller("count", 1)([1,1,1,2,2])

############################################################
## good function is small function
############################################################
ss = ["UA", "PyCon", "2012"]
reduce(lambda acc, s: acc + len(s), ss, 0)  ## BAD
reduce(lambda l,r: l+r, map(lambda s: len(s), ss)) ## NOT BAD...
reduce(operator.add, map(len, ss)) # GOOD

############################################################
## types are callable
map(str, range(5))

## classes are callable
class Speaker(object):
    def __init__(self, name):
        self.name = name

map(Speaker, ["alexey", "andrey", "wzc"])

## instance methods are callable
map([1,2,3,4,5].count, [1,2,3,10,11])

############################################################
## Mutable Data
############################################################
