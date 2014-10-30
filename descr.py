#!/usr/bin/env python
__author__ = 'Wang Zhicheng'
"""
This class is crude but represents an interesting use of descriptors --
being able to store the contents of an attribute on the filesystem.
"""

import os
import pickle


class FileDescr(object):
    saved = []  # keep track of all attributes with descriptor access.

    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner=None):
        if self.name not in FileDescr.saved:
            raise AttributeError('%r used before assignment' % self.name)

        try:
            f = open(self.name, 'r')
            val = pickle.load(f)
            f.close()
            return val
        except (pickle.UnpicklingError, IOError, EOFError,
            AttributeError, ImportError, IndexError) as e:
            raise AttributeError('Could not read %r: %s' % self.name)

    def __set__(self, instance, value):
        f = open(self.name, 'w')

        try:
            pickle.dump(val, f)
            FileDescr.saved.append(self.name)
        except (TypeError, pickle.PicklingError) as e:
            raise AttributeError('could not pickle %r' % self.name)
        finally:
            f.close()

    def __delete__(self, instance):
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except (OSError, ValueError) as e:
            pass
