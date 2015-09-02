# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-01-12 15:09:04
Edit time: 2015-01-15 20:25:14
File name: Lock2.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance
