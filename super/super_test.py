# -*- coding: UTF-8 -*-


class A(object):
    f = 'aaa'
    def foo(self):
        print 'I\'m A'
        print self.f


class B(A):
    def foo(self):
        super(B, self).foo()
        print self.f

b = B()
b.foo()


