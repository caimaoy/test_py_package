# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-01-13 11:41:53
Edit time: 2015-01-13 11:42:23
File name: test_getattr.py
Edit by caimaoy
'''

class Chain(object):

    """test of __getattr__"""

    def __init__(self, path=''):
        """TODO: to be defined1.

        :path: TODO

        """
        self._path = path

    def __getattr__(self, path):
        print 'self is %s' % self
        print 'path is %s' % path
        return Chain('%s/%s' % (self._path, path))


    def __str__(self):
        return self._path


if __name__ == '__main__':
    print Chain().status.user.timeline.list
