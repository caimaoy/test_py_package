# -*- coding: UTF-8 -*-
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        print time.time() - start
        return r
    return wrapper


@timeit
def foo():
    print 'in foo()'


def foo2():
    print 'in foo2()'

foo2 = timeit(foo2)


@timeit
def test(a):
    print a

foo()
foo2()
test('test')
