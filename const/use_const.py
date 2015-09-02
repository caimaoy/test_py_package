# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-06-10 17:40:28
Edit time: 2015-06-10 17:40:35
File name: use_const.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

from constant import const

def use_const():
    print 'const.NAME is %s' % const.NAME
    print 'const.GAME is %s' % const.GAME

if __name__ == '__main__':
    use_const()
