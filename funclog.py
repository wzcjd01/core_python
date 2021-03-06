#!/usr/bin/env python
"""
This example shows a decorator that takes an argument that ultimately
determines which closure will be used."""

from time import time


def logged(when):
    def log(f, *args, **kwargs):
        print '''Called:
            function: %s
            args: %r
            kwargs: %r''' % (f, args, kwargs)

    def pre_logged(f):
        def wrapper(*args, **kwargs):
            log(f, *args, **kwargs)
            return f(*args, **kwargs)
        return wrapper

    def post_logged(f):
        def wrapper(*args, **kwargs):
            now = time()
            try:
                return f(*args, **kwargs)
            finally:
                log(f, *args, **kwargs)
                print "time delta: %s" % (time() - now)
        return wrapper

    try:
        return {"pre": pre_logged, "post": post_logged}[when]
    except KeyError as e:
        raise ValueError(e), 'must be "pre" or "post"'


@logged("post")
def hello(name):
    print "Hello,", name


hello("World!")
