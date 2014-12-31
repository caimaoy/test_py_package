# -*- coding: UTF-8 -*-

import thread
import time

def func():
    for i in xrange(5):
        print 's %d time'% i
        time.sleep(1)

    thread.exit()

argv = ('test')
thread.start_new(func, ())


'''
sys.excepthook is missing
lost sys.stderr

建议不要使用thread
'''


