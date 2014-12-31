# -*- coding: UTF-8 -*-


'''
Last modified time: 2014-12-19 10:38:13
Edit time: 2014-12-19 10:38:33
File name: watch_log.py
Edit by caimaoy
'''

import urllib2
import time
import re

reg = re.compile(r'\d{10}')

def _my_print(l):
    try:
        print '.',
        if l:
            print ''
        for i in l:
            # print i
            # if i.find('pre>') is not -1:
            i = i.replace(r'<pre>', '')
            i = i.replace(r'</pre>', '').strip()
            if i:
                print reg.sub(_stamp_repl, i)
    except Exception as e:
        print e


def _stamp_repl(match):
    '''Return the time for a stamp
    '''
    # print match.group()
    time_array = time.localtime(int(match.group()))
    # print time_array
    strftime = time.strftime('%Y-%m-%d %H:%M:%S', time_array)
    # print strftime

    return strftime


def _main():
    try:
        old_text = urllib2.urlopen(r'http://client.baidu.com:8811/webapi/seekpilog').read()
    except Exception as e:
        print e
        old_text = ''

    old_text = old_text.split('\n')
    _my_print(old_text)


    while True:
        time.sleep(1)
        try:
            new_text = urllib2.urlopen(r'http://client.baidu.com:8811/webapi/seekpilog').read()
            new_text = set(new_text.split('\n'))
            diff_text = [i for i in new_text if i not in old_text]
            _my_print(diff_text)
            old_text = new_text
        except Exception as e:
            print e



if __name__ == '__main__':
    _main()
