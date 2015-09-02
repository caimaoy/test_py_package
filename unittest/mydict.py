# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-01-14 17:05:11
Edit time: 2015-01-14 17:05:30
File name: mydict.py
Edit by caimaoy
'''

__author__ = 'caimaoy'


class Dict(dict):

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__ == '__main__':
    pass
