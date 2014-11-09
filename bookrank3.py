#!/usr/bin/env python
__author__ = 'Wang Zhicheng'

from atexit import register
from threading import Thread
from re import compile
from time import ctime
from urllib.request import urlopen

REGEX = compile(b'#([\d,]+) in Books ')
AMZN = 'http://www.amozon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356239': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}


def getRanking(isbn):
    page = urlopen('%s%s' % (AMZN, isbn))
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]


def _showRanking(isbn):
    print('- %r ranked %s' % (ISBNs[isbn], getRanking(isbn)))


def _main():
    print('At', ctime(), 'on Amazon...')
    for isbn in ISBNs:
        # _showRanking(isbn)
        Thread(target=_showRanking, args=(isbn,)).start()


@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()
