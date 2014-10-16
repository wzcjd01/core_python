#!/usr/bin/env python
from __future__ import print_function

__author__ = 'Wang Zhicheng'

from isPrime import isPrime as _isPrime
from getFactors import getFactors as _getFactors


def prime_factorization(num):
    factors = _getFactors(num)
    primes = filter(_isPrime, factors)
    prime_fact = []

    for prime in primes:
        tmp = num
        while True:
            if tmp % prime == 0:
                prime_fact.append(prime)
                tmp = tmp / prime
            else:
                break

    return prime_fact


def _test():
    import random

    n = random.randrange(1, 10000)
    prime_fact_n = prime_factorization(n)
    print('{0:d} prime factorizenum as:\n\t{1:s}'.format(n, prime_fact_n))


if __name__ == '__main__':
    _test()
