# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-01-29 19:47:06
Edit time: 2015-01-29 19:47:32
File name: test_Coroutine.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

import time

def consumer():
    r = ''
    while True:
        '''
        import pdb
        pdb.set_trace()
        '''
        n = yield r
        if not n:
            # 正常这里是不是会执行的, 调用next函数时，抛出异常
            print 'nnnnn'
            print n
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'

def produce(c):
    c.next()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__=='__main__':
    c = consumer()
    produce(c)
