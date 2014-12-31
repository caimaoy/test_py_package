# -*- coding: UTF-8 -*-

'''
Last modified time: 2014-12-05 11:51:11
Edit time: 2014-12-05 11:52:08
File name: delay_start.py
Edit by caimaoy
'''


import time
import subprocess

def _main():
    # hour = int(time.strftime('%H'))
    hour = int(time.strftime('%M'))
    wait_hour = 8
    while hour == wait_hour:
        time.sleep(1)
        print 'wait_hour %s' % hour
        hour = int(time.strftime('%M'))
    else:
        subprocess.Popen('notepad')



if __name__ == '__main__':
    _main()
