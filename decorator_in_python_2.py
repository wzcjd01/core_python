#!/usr/bin/env python
# http://stackoverflow.com/questions/739654
# /how-can-i-make-a-chain-of-function-decorators-in-python

# in order to make decorator accept arguments, we created our decorator using
# another function. We wrapped the decorator with another decorator.


def decorator_with_args(decorator_to_enhouce):
    """
    This function is supposed to be used as a decorator. It must decorate
    another function, that is intended to be used to a decorator.
    It will allow any decorator to accept an arbitrary number of arguments,
    saving you the headache to remember how to do that every time.
    """

    # We use the same trick we did to pass arguments
    def decorator_maker(*args, **kwargs):

        # We create on the fly a decorator that accepts only a function
        # but keeps the passed arguments from the maker.
        def decorator_wrapper(func):

            # We return the result of the original decorator, which, after all,
            # IS JUST AN ORDINARY FUNCTION (which returns a function).
            # Only pitfall: the decorator must have this specific signature or
            return decorator_to_enhouce(func, *args, **kwargs)

        return decorator_wrapper

    return decorator_maker

# You create the function you will use as a decorator. And stick a decorator
# on it :-) Don't forget, the signature is "decorator(func, *args, **kwargs)"


@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    def wrapper(function_arg1, function_arg2):
        print "Decorated with", args, kwargs
        return func(function_arg1, function_arg2)
    return wrapper

# Then you decorate the functions you wish with your brand new
# decorated decorator.


@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1, function_arg2):
    print "Hello", function_arg1, function_arg2

decorated_function("Universe and", "everything")
# outputs:
# Decorated with (42, 404, 1024) {}
# Hello Universe and everything

# Whoooot!

# The functools module was introduced in Python 2.5. It includes the function
# functools.wraps(), which copies the name, module, and docstring of the
# decorated function to its wrapper.
print '=' * 50

# For debugging, the stacktrace prints you the function __name__


def foo():
    print "foo"

print foo.__name__
# outputs: foo

# With a decorator, it gets messy


def bar(func):
    def wrapper():
        print "bar"
        return func()
    return wrapper


@bar
def foo():
    print "foo"

print foo.__name__
# outputs: wrapper

# "functools" can help for that

import functools


def bar(func):
    # We say that "wrapper", is wrapping "func"
    # and the magic begins
    @functools.wraps(func)
    def wrapper():
        print "bar"
        return func()
    return wrapper


@bar
def foo():
    print "foo"

print foo.__name__
# outputs: foo

print '=' * 50


def benchmark(func):
    """
    A decorator that prints the time a function takes to execute
    """

    import time

    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock() - t
        return res
    return wrapper


def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging!)
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print func.__name__, args, kwargs
        return res
    return wrapper


def counter(func):
    """
    A decorator that counts and prints the number of times a function
    has been executed
    """
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print "{0} has been used: {1}x".format(func.__name__, wrapper.count)
        return res
    wrapper.count = 0
    return wrapper


@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))

print reverse_string("Able was I ere I saw Elba")
print reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, "
                     "a coloratura, maps, snipe, percale, macaroni, "
                     "a gag, a banana bag, a tan, a tag, a banana "
                     "bag again (or a camel), a crepe, pins, Spam, "
                     "a rut, a Rolo, cash, a jar, sore hats, a peon, "
                     "a canal: Panama!")

# outputs:
# reverse_string ('Able was I ere I saw Elba',) {}
# wrapper 0.0
# wrapper has been used: 1x
# ablE was I ere I saw elbA

# reverse_string ('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura,
# maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana
# bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar,
# sore hats, a peon, a canal: Panama!',) {}

# wrapper 0.0
# wrapper has been used: 2x
# !amanaP :lanac a ,noep a ,stah eros ,raj a ,hsac ,oloR a ,tur a ,mapS ,snip ,
# eperc a ,)lemac a ro( niaga gab ananab a ,gat a ,nat a ,gab ananab a ,gag a ,
# inoracam ,elacrep ,epins ,spam ,arutaroloc a ,shajar ,soreh ,atsap ,eonac a ,
# nalp a ,nam A


@counter
@benchmark
@logging
def get_random_futurama_quote():
    from urllib import urlopen
    result = urlopen("http://subfusion.net/cgi-bin/quote.pl?quote=futurama"
                     ).read()
    try:
        value = result.split("<br><b><hr><br>")[1].split("<br><br><hr>")[0]
        return value.strip()
    except:
        return "No, I'm ... doesn't!"


print get_random_futurama_quote()
print get_random_futurama_quote()

# outputs:
# get_random_futurama_quote () {}
# wrapper 0.02
# wrapper has been used: 1x
# The laws of science be a harsh mistress.
# get_random_futurama_quote () {}
# wrapper 0.01
# wrapper has been used: 2x
# Curse you, merciful Poseidon!

# Of course the good thing with decorators is that you can use them
# right away on almost anything without rewriting.
print '=' * 50


@counter
@benchmark
@logging
def get_random_futurama_quote():
    from urllib import urlopen
    result = urlopen("http://subfusion.net/cgi-bin/quote.pl?quote=futurama"
                     ).read()
    try:
        value = result.split("<br><b><hr><br>")[1].split("<br><br><hr>")[0]
        return value.strip()
    except:
        return "No, I'm ... doesn't!"


print get_random_futurama_quote()
print get_random_futurama_quote()

# outputs:
# get_random_futurama_quote () {}
# wrapper 0.02
# wrapper has been used: 1x
# The laws of science be a harsh mistress.
# get_random_futurama_quote () {}
# wrapper 0.01
# wrapper has been used: 2x
# Curse you, merciful Poseidon!
