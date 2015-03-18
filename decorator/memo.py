# -*- coding: UTF-8 -*-

'''
Last modified time: (无效)
Edit time: 2015-03-18 10:30:51
File name: memo.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

from functools import wraps
from time import time

def memo(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
            print 'cache', args, result
        return result

    return wrapper


def timeit(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        s = time()
        fn(*args, **kwargs)
        e = time()
        print e -s

    return wrapper


@memo
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n -2)

if __name__ == '__main__':
    # print fib(5)
    # print fib(10)
    import sys
    sys.setrecursionlimit(1000000)


    s = time()
    fib(1000)
    e = time()
    print e - s

    s = time()
    fib(1000)
    e = time()
    print e - s
