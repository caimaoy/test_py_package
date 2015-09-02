# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-01-13 15:56:26
Edit time: 2015-01-13 15:59:33
File name: test_metaclass.py
Edit by caimaoy
'''

# metaclss 必须从'type'类型派生

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        attrs['caimaoy'] = lambda self: self.append('caimaoy')
        return type.__new__(cls, name, bases, attrs)


class MyList(list):
    __metaclass__ = ListMetaclass # 指明使用ListMetaclass来定制


if __name__ == '__main__':
    l = MyList()
    l.add('test')
    l.caimaoy()
    print l
