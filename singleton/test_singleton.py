# -*- coding: UTF-8 -*-

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class MyClass(object):
    a = 1
    def __init__(self, x=0):
        self.x = x


if __name__ == '__main__':
    one = MyClass()
    two = MyClass()


    print id(one)
    print id(two)

    one.a = 3
    print one.a
    print two.a

    print one.x
    print two.x
