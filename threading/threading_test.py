# -*- coding: UTF-8 -*-

import threading

def func(s):
    print 'just a test of func'
    print s

t = threading.Thread(target=func, args=('test',))
t.start()


class My_thread(threading.Thread):

    def run(self):
        print 'My_thread test'

t = My_thread()
t.start()
