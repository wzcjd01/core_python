#!/usr/bin/env python
# http://www.artima.com/weblogs/viewpost.jsp?thread=240808

print '-' * 50


class myDecorator(object):
    def __init__(self, f):
        print "inside myDecorator.__init__()"
        f()     # prove that function definition was completed

    def __call__(self):
        print "inside myDecorator.__call__()"


@myDecorator
def aFunction():
    print "inside aFunction()"

print "Finished decorating aFunction()"

aFunction()

print '-' * 50


class entryExit(object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print "Entering", self.f.__name__
        self.f()
        print "Exited", self.f.__name__


@entryExit
def func1():
    print "inside func1()"


@entryExit
def func2():
    print "inside func2()"


func1()
func2()

print '-' * 50


class decoratorWithoutArguments(object):
    def __init__(self, f):
        """
        if there are no decorator arguments, the function to be decorated
        is passed to the constructor.
        """
        print "inside __init__()"
        self.f = f

    def __call__(self, *args):
        """
        the __call__ method is not called until the decorated function
        is called.
        """
        print "inside __call__()"
        self.f(*args)
        print "after slef.f(*args)"

print '-' * 50


@decoratorWithoutArguments
def sayHello(a1, a2, a3, a4):
    print 'sayHello arguments:', a1, a2, a3, a4


print 'after decoration'

print 'Preparing to call sayHello()'
sayHello("say", "hello", "argument", "list")
print "after first sayHello() call"
sayHello("a", "different", "set of", "arguments")
print "after second sayHello() call"

print '-' * 50


class decoratorWithArguments(object):
    def __init__(self, arg1, arg2, arg3):
        """
        if there are decorator arguments, the function to be decorated is
        not passed to the decorator!
        """
        print 'inside __init__()'
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """
        if there are decorator arguments, __call__() is only called once, as
        part of the decoration process! you can only give it a single argument,
        which is the function object.
        """
        print 'inside __call__()'

        def wrapped_f(*arg):
            print 'inside wrapped_f()'
            print 'decorator arguments:', self.arg1, self.arg2, self.arg3
            f(*arg)
            print 'after f(*arg)'
        return wrapped_f


@decoratorWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print 'sayHello arguments:', a1, a2, a3, a4


print 'after decoration'

print 'preparing to call sayHello()'
sayHello("say", "hello", "argument", "list")

print "after first sayHello() call"
sayHello("a", "different", "set of", "arguments")
print "after second sayHello() call"

print '-' * 50


def decoratorFunctionWithArguments(arg1, arg2, arg3):
    def wrap(f):
        print 'inside wrap()'

        def wrapped_f(*args):
            print 'inside wrapped_f()'
            print 'decorator arguments:', arg1, arg2, arg3
            f(*args)
            print 'after f(*arg)'
        return wrapped_f
    return wrap


@decoratorFunctionWithArguments('hello', 'world', 42)
def sayHello(a1, a2, a3, a4):
    print 'sayHello arguments:', a1, a2, a3, a4


print 'after decoratoin'

print 'preparing to call sayHello()'
sayHello("say", "hello", "argument", "list")
print "after first sayHello() call"
sayHello("a", "different", "set of", "arguments")
print "after second sayHello() call"
