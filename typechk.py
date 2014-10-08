__author__ = 'Wang Zhicheng'


# version 1
def display_num_type1(num):
    print num, 'is',
    if type(num) == type(0):
        print 'an integer'
    if type(num) == type(0L):
        print 'a long'
    if type(num) == type(0.0):
        print 'a float'
    if type(num) == type(0+0j):
        print 'a complex'
    else:
        print 'not a number at all!!'


# version 2
def display_num_type2(num):
    import types
    print num, 'is',
    if type(num) == types.IntType:
        print 'an integer'
    if type(num) == types.LongType:
        print 'a long'
    if type(num) == types.FloatType:
        print 'a float'
    if type(num) == types.ComplexType:
        print 'a complex'
    else:
        print 'not a number at all!!'


# version 3
def display_num_type3(num):
    # import types
    # reduce the number of lookups
    from types import IntType, LongType, ComplexType, FloatType
    print num, 'is',
    # if type(num) is types.IntType:
    if type(num) is IntType:
        print 'an integer'
    # if type(num) is types.LongType:
    if type(num) is LongType:
        print 'a long'
    # if type(num) is types.FloatType:
    if type(num) is FloatType:
        print 'a float'
    # if type(num) is types.ComplexType:
    if type(num) is ComplexType:
        print 'a complex'
    else:
        print 'not a number at all!!'


def display_num_type(num):
    print num, 'is',
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type: ', type(num).__name__
    else:
        print 'not a number at all!!'

display_num_type(-69)
display_num_type(9999999999999999999999999999l)
display_num_type(88.8)
display_num_type(-5.2+1.9j)
display_num_type('xxx')
