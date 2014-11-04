#!/usr/bin/env python
__author__ = 'Wang Zhicheng'

import time


class Timer(object):

    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start


with Timer() as t:
    pass

print t.interval
