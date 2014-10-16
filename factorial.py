#!/usr/bin/env python
__author__ = 'Wang Zhicheng'


def factorial(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1

    return fact
