#!/usr/bin/env python
__author__ = 'Wang Zhicheng'

from atexit import register
from random import randrange
from time import sleep, ctime
from threading import Thread, Lock, BoundedSemaphore

lock = Lock()
MAX = 5     # total 5 slots in this vending machine
candytray = BoundedSemaphore(MAX)


def refill():
    with lock:
        print 'Refilling candy...'
        try:
            candytray.release()
        except ValueError:
            print 'full, skipping'
        else:
            print 'OK'


def buy():
    with lock:
        print 'Buying candy...'
        if candytray.acquire(False):
            print 'OK'
        else:
            print 'empty, skipping'


def producer(loops):
    for i in xrange(loops):
        refill()
        sleep(randrange(3))


def consumer(loops):
    for i in xrange(loops):
        buy()
        sleep(randrange(3))


def _main():
    print 'starting at:', ctime()
    nloops = randrange(2, 6)
    print 'THE CANDY MACHINE (full with %d bars)!' % MAX

    # buyer
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()
    # vender
    Thread(target=producer, args=(nloops,)).start()


@register
def _atexit():
    print '-' * 50
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    _main()
