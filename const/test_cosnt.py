# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-06-10 17:14:54
Edit time: 2015-06-10 17:15:21
File name: test_cosnt.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

import const

def test_cosnt_error():
    const.NAME = 'caimaoy'
    const.NAME = 'jessie'

def test_cosnt_case_error():
    const.name = 'caimaoy'

def catch_error():
    try:
        test_cosnt_error()
    except Exception as e:
        print repr(e)

    try:
        test_cosnt_case_error()
    except Exception as e:
        print repr(e)

if __name__ == '__main__':
    catch_error()
