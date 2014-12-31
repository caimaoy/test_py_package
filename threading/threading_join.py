# -*- coding: UTF-8 -*-

import threading
import time

def context(t_join):
    print 'in thread_context.'
    t_join.start()

    # 将阻塞t_context直到thread_join终止
    t_join.join()

    print 'out thread_context.'

def join():
    print 'in thread_join'
    time.sleep(1)
    print 'out thread_join'

t_join = threading.Thread(target=join)
tContext = threading.Thread(target=context, args=(t_join,))

tContext.start()

