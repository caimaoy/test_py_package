# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-01-15 15:56:52
Edit time: 2015-01-15 15:57:34
File name: multiprocessing.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

import os
from multiprocessing import Process


def test():
    """
    only works on POSIX
    """

    print 'Process (%s) start ...' % os.getpid()

    pid = os.fork()
    if pid == 0:
        print 'I am chiled process(%s) and my parent is %s.' % (
            os.getpid(),
            os.getppid)
    else:
        print 'I am (%s) just create a child process (%s)' % (
            os.getpid(),
            pid)


def run_proc(name):
    print 'Run child proess %s (%s)...' % (name, os.getpid())


if __name__ == '__main__':
    # test()
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test', ))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end'
