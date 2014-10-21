#!/usr/bin/env python

__author__ = 'Wang Zhicheng'

"""
this module defines two new exception, FileError and NetworkError,
as well as reimplements more diagnostic  versions of open() and
socket.connect().
"""

import os
import socket
import errno
import types
import tempfile


class NetworkError(IOError):
    pass


class FileError(IOError):
    pass


def updArgs(args, newarg=None):
    if isinstance(args, IOError):
        myargs = []
        myargs.extend([arg for arg in args])
    else:
        myargs = list(args)

    if newarg:
        myargs.append(newarg)

    return tuple(myargs)


def fileArgs(fn, mode, args):
    """
    FileError arguments construction
    :param fn:
    :param mode:
    :param args:
    :return:
    """
    if args[0] == errno.EACCES and 'access' in dir(os):
        # construct permission string for file: fn
        perms = ''
        permd = {'r': os.R_OK, 'w': os.W_OK, 'x': os.X_OK}
        pkeys = permd.keys()
        pkeys.sort()
        pkeys.reverse()

        for eachPerm in 'rwx':
            if os.access(fn, permd[eachPerm]):
                perms += eachPerm
            else:
                perms += '-'

        # list-ize 'args' temporarily
        if isinstance(args, IOError):
            myargs = []
            myargs.extend([arg for arg in args])
        else:
            myargs = list(args)

        # alter the error string to contain the permission string constructed before
        myargs[1] = "'%s' %s (perms: '%s')" % (mode, myargs[1], perms)

        myargs.append(args.filename)

    else:
        myargs = args

    return tuple(myargs)


def myconnect(sock, host, port):
    try:
        sock.connect((host, port))
    except socket.error as args:
        myargs = updArgs(args)  # convert instance to tuple
        if len(myargs) == 1:    # no #s on some errs
            myargs = (errno.ENXIO, myargs[0])

        raise NetworkError, updArgs(myargs, host + ':' + str(port))


def myopen(fn, mode='r'):
    try:
        fo = open(fn, mode)
    except IOError as args:
        raise FileError, fileArgs(fn, mode, args)

    return fo


def testfile():
    fn = tempfile.mktemp()
    f = open(fn, 'w')
    f.close()

    for eachTest in ((0, 'r'), (0100, 'r'), (0400, 'w'), (0500, 'w')):
        try:
            os.chmod(fn, eachTest[0])
            f = myopen(fn, eachTest[1])

        except FileError as args:
            print "%s: %s" % (args.__class__.__name__, args)

        else:
            print fn, "opened ok... perm ignored"
            f.close()

    os.chmod(fn, 0777)  # enable all perms
    os.unlink(fn)


def testnet():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for eachHost in ('deli', 'www'):
        try:
            myconnect(s, eachHost, 8080)
        except NetworkError as args:
            print "%s: %s" % (args.__class__.__name__, args)


if __name__ == '__main__':
    testfile()
    testnet()
