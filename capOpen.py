#!/usr/bin/env python
__author__ = 'Wang Zhicheng'
"""
This class extends on the example from one of the Python FAQs, providing
a file-like object that customizes the write() method while delegating the
rest of the functionality to the file object.
"""


class CapOpen(object):
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return repr(self.file)

    def write(self, line):
        self.file.write(line.upper())

    def __getattr__(self, item):
        return getattr(self.file, item)


if __name__ == '__main__':
    import tempfile

    fname = tempfile.mktemp()
    f = CapOpen(fname, 'w')
    f.write('delegation example\n')
    f.write('faye is good\n')
    f.write('at delegation\n')
    f.close()

    f = CapOpen(fname, 'r')
    for eachLine in f:
        print eachLine
