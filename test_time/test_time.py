# -*- coding: UTF-8 -*-
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        print time.time() - start
        return r
    return wrapper


def test_times(arg):
    def _deco(func):
        def __deco(*args, **kwargs):
            start = time.time()
            for i in xrange(arg):
                func(*args, **kwargs)
                # func()
            print time.time() - start
        return __deco
    return _deco


@timeit
def foo():
    print 'in foo()'


def foo2():
    print 'in foo2()'



@timeit
def test(a):
    print a


s = 'dkfjdkfjdkfjdkfjdkfjdkf' * 80
a = ''
@test_times(1000)
def boo():
    global a
    a += s

@test_times(1000)
def boo2():
    a = ''.join([s])

@test_times(1000)
def boo3():
    a = s



def _test():
    boo()
    boo2()
    boo3()



if __name__ == '__main__':
    _test()
