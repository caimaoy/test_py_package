# -*- coding: UTF-8 -*-

'''
Last modified time: 2014-11-26 14:37:59
Edit time: 2014-11-26 14:38:41
File name: test_list.py
Edit by caimaoy
'''

import time

def test():
    li = [1, 2, 3]

    for i in li:
        if i < 10:
            li.append(i + 3)
        print i
        print li
        time.sleep(3)
        print '*' * 70


if __name__ == '__main__':
    test()
