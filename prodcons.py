#!/usr/bin/env python
__author__ = 'Wang Zhicheng'

from Queue import Queue
from time import sleep
from random import randint
from atexit import register
from myThread import MyThread
from threading import Lock

lock = Lock()

def writeQ(queue):
    with lock:
        print 'producing object for Q...',
        queue.put('xxx', 1)
        print 'size now', queue.qsize()


def readQ(queue):
    with lock:
        queue.get(1)
        print 'consumed object from Q... size now', queue.qsize()


def writer(queue, loops):
    for _ in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))


def reader(queue, loops):
    for _ in range(loops):
        readQ(queue)
        sleep(randint(2, 5))


@register
def _atexit():
    print '-' * 50
    print 'all DONE!!'


funcs = [writer, reader]
nfuncs = range(len(funcs))


def _main():
    nloops = randint(2, 5)
    q = Queue(maxsize=32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()


if __name__ == '__main__':
    _main()
