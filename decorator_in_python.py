#!/usr/bin/env python
# http://stackoverflow.com/questions

print '-' * 50
# /739654/how-can-i-make-a-chain-of-function-decorators-in-python/1594484#1594484


def shout(word='yes'):
    return word.capitalize() + '!'

print shout()

# as an object, you can assign the function to a variable like any object.
scream = shout

print scream()

del shout

try:
    print shout()
except NameError, e:
    print e

print scream()


def talk():

    # you can define a function on the fly in 'talk'
    def whisper(word='yes'):
        return word.lower() + '...'

    print whisper()

talk()

# but 'whisper' does not exist outside 'talk'
try:
    print whisper()
except NameError, e:
    print e


"""
 functions are objects. therefore, functions:
     can be assigned to a variable
     can be defined in another function
     can be returned by another function
"""


def getTalk(kind='shout'):

    def shout(word='yes'):
        return word.capitalize() + '!'

    def whisper(word='yes'):
        return word.lower() + '...'

    if kind == 'shout':
        return shout
    else:
        return whisper

talk = getTalk()
print talk  # 'talk' is here a function object

print talk()

print getTalk('whisper')()


# you can pass one function as a parameter
def doSomethingBefore(func):
    print 'i do Something before then i call the function you gave me'
    print func()

doSomethingBefore(scream)

print '-' * 50
# a decorator is a function that expects ANOTHER function as parameter


def my_shiny_new_decorator(a_function_to_decorate):

    # inside, decorator defines a function on the fly: the wrapper.
    # this function is going to wrap around the original function
    # so it can execute code before and after it
    def the_wrapper_around_original_function():

        # put here the code you want to be executed BEFORE the
        # original function is calledself.
        print 'before the function runs'

        # call the function here
        a_function_to_decorate()

        # put here the code you want to be executed AFTER
        # the original function is called.
        print 'after the function runs'
    return the_wrapper_around_original_function


def a_stand_alone_function():
    print "I am a standalone function, don't you dare modify me"

a_stand_alone_function()

# decorate by passing to decorator
a_stand_alone_function_decorated = my_shiny_new_decorator(
    a_stand_alone_function)
a_stand_alone_function_decorated()

a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()


@my_shiny_new_decorator
def another_stand_alone_function():
    print 'leave me alone'

another_stand_alone_function()

print '-' * 50
# accumulate decorators: chains of decorators


def bread(func):
    def wrapper():
        print "</''''''\>"
        func()
        print "<\______/>"
    return wrapper


def ingredients(func):
    def wrapper():
        print "#tomatoes#"
        func()
        print "~salad~"
    return wrapper


def sandwich(food="--ham--"):
    print food


sandwich()
sandwich = bread(ingredients(sandwich))
sandwich()


@bread
@ingredients
def sandwich(food="--ham--"):
    print food

sandwich()

print '-' * 50
# passing arguments to the decorated function: you just have to let
# the wrapper pass the argument.


def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print 'I ggot args! Look:', arg1, arg2
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments


@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print 'My name is', first_name, last_name


print_full_name('Peter', 'Venkman')

print '-' * 50
# decorating methhods. The only difference between methonds and functions
# is that methonds expect that their first argument is a refrence to
# the current object (self)


def method_friendly_decorator(methond_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3   # very friendly, decrease age even more:-)
        return methond_to_decorate(self, lie)
    return wrapper


class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print 'I am %s, what did you think?' % (self.age + lie)


l = Lucy()
l.sayYourAge(-3)

print '-' * 50
# if you're making general-purpose decorator -- one you'll apply to any
# function or method, no matter its arguments -- then just use *args,
# **kwargs.:


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # the wrapper accepts any arguments
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print 'do i have args?:'
        print args
        print kwargs
        # then you unpack the arguments, here *args, **kwargs
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_arguments():
    print 'python is cool, no argument here.'

function_with_no_arguments()


@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print a, b, c

function_with_arguments(1, 2, 3)


@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus='why not?'):
    print 'Do %s, %s and %s like platypus? %s' % (a, b, c, platypus)

function_with_named_arguments('Bill', 'Linus', 'Steve', platypus='Indeed!')


class Mary(object):

    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3):
        print 'I am %s, what did you think?' % (self.age + lie)

m = Mary()
m.sayYourAge()

print '=' * 50
# passing arguments to the decorator itself? This can get somewhat twisted,
# since a decorator must accept a function as an argument. Therefore, you
# cannot pass the decorated function's arguments directly to the
# decorator.

# a little reminder first
# Decorators are ORDINARY functions


def my_decorator(func):
    print 'I am an ordinary function'

    def wrapper():
        print 'I am function returned by the decorator'
        func()
    return wrapper


def lazy_function():
    print 'zzzzzz...'

# Therefore, you can call it without any '@'
decorated_function = my_decorator(lazy_function)


@my_decorator       # 'my_decorator' is called.
def lazy_function():
    print 'zzzzzz...'

print '-' * 50


def decorator_maker():

    print 'I make decorators! I am executed only once: ' +\
        'when you make me create a decorator.'

    def my_decorator(func):

        print ('I am a decorator! I am executed only '
               'when you decorate a function.')

        def wrapped():
            print ('I am the wrapper around the decorated function. '
                   'I am called when you call the decorated function. '
                   'As the wrapper, I return the RESULT '
                   'of the decorated function.')
            return func()

        print 'As the decorator, I return the wrapped function.'

        return wrapped

    print 'As a decorator maker, I return a decorator.'
    return my_decorator

# let's create a decorator
new_decorator = decorator_maker()

# then we decorate the function


def decorated_function():
    print 'I am the decorated function.'

decorated_function = new_decorator(decorated_function)

# let's call the function:
decorated_function()

print '-' * 50


def decorated_function():
    print 'I am the decorated function.'

decorated_function = decorator_maker()(decorated_function)

# finally
decorated_function()

print '-' * 50
# let's make it even shorter: using a function call with the '@' syntax!


@decorator_maker()
def decorated_function():
    print 'I am the decorated function.'

# eventually
decorated_function()

print '=' * 50
# so back to decorators with arguments. If we can use functions to generate
# the decorator on the fly, we can pass arguments to that function.


def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):

    print ('I make decorators! And I accept arguments:',
           decorator_arg1, decorator_arg2)

    def my_decorator(func):
        # The ability to pass arguments here is a gift from closures.
        print ('I am the decorator. Somehow you passed me argument:',
               decorator_arg1, decorator_arg2)

        # don't confuse decorator arguments and function arguments!
        def wrapped(function_arg1, function_arg2):
            print ('I am the wrapper around the decorated function.\n'
                   'I can access all the variables\n'
                   '\t- from the decorator: {0} {1}\n'
                   '\t- from the function call: {2} {3}\n'
                   .format(decorator_arg1, decorator_arg2,
                           function_arg1, function_arg2))
            return func(function_arg1, function_arg2)
        return wrapped
    return my_decorator


@decorator_maker_with_arguments('Leonard', 'Sheldon')
def decorated_function_with_arguments(function_arg1, function_arg2):
    print ('I am the decorated function and only knows about my arguments: '
           '{0} {1}'.format(function_arg1, function_arg2))

decorated_function_with_arguments('Rajesh', 'Howard')

print '-' * 50
# a decorator with arguments. Arguments can be set as variable:

c1 = 'Penny'
c2 = 'Leslie'


@decorator_maker_with_arguments('Leonard', c1)
def decorated_function_with_arguments(function_arg1, function_arg2):
    print ('I am the decorated function and only knows about my arguments: '
           '{0} {1}'.format(function_arg1, function_arg2))

decorated_function_with_arguments(c2, 'Howard')
