# -*- coding: UTF-8 -*-


'''
Last modified time: 2014-12-18 11:27:28
Edit time: 2014-12-22 09:32:10
File name: def_ocr.py
Edit by caimaoy
'''


import urllib2
import re
import pickle

def _main():
    url = r'http://www.pythonchallenge.com/pc/def/equality.html'
    text = urllib2.urlopen(url).read()
    with open('out.txt', 'w') as f:
        f.write(text)

def _do_it():
    f = open('banner.p')
    data = pickle.load(f)
    fo = open('result.txt', 'w')
    for d in data:
        text = ''.join([x[0] * x[1] for x in d])
        print text
        fo.write(text)
        fo.write('\n')
    f.close()
    fo.close()



if __name__ == '__main__':
    # _main()
    _do_it()
