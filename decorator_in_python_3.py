#!/usr/bin/env python
from functools import wraps


def wrap_in_tags(tag):
    def factory(func):
        @wraps(func)
        def decorator(val):
            return func('<%(tag)s>%(rv)s</%(tag)s>' %
                        {'tag': tag, 'rv': val})
        return decorator
    return factory


@wrap_in_tags('b')
@wrap_in_tags('i')
def say(val):
    return val

say('Hello')
