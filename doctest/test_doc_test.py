# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-07-13 11:32:16
Edit time: 2015-07-13 11:33:05
File name: test_doc_test.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

import re

def test():
    '''
    >>> test()
    aaa
    '''
    print 'aaa'

def change_place(s):
    '''
    >>> change_place('caimaoy&jessie')
    'jessie&caimaoy'
    '''
    return re.sub(r'(caimaoy)(&)(jessie)', r'\3\2\1', s)

def change_place_and_joiner(s):
    '''
    >>> change_place_and_joiner('caimaoy&jessie')
    'jessie with caimaoy'
    '''
    return re.sub(r'(caimaoy)(&)(jessie)', r'\3 with \1', s)

def change_place_and_joiner_with_number(s):
    '''
    >>> change_place_and_joiner_with_number('caimaoy&jessie')
    'jessie0caimaoy'
    '''
    return re.sub(r'(caimaoy)(&)(jessie)', r'\g<3>0\g<1>', s)

def change_place_and_upper(s):
    '''
    >>> change_place_and_upper('caimaoy&jessie')
    'JESSIE&CAIMAOY'
    '''
    def _upper(matched):
        return matched.group(3).upper() + matched.group(2) + matched.group(1).upper()
    return re.sub(r'(caimaoy)(&)(jessie)', _upper, s)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
