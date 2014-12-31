# -*- coding: UTF-8 -*-


'''
Last modified time: 2014-12-18 11:27:28
Edit time: 2014-12-22 09:32:10
File name: def_ocr.py
Edit by caimaoy
'''


import urllib2
import re

def _main():
    url = r'http://www.pythonchallenge.com/pc/def/equality.html'
    text = urllib2.urlopen(url).read()
    with open('out.txt', 'w') as f:
        f.write(text)


def _re():
    import re
    # print re.sub(r'[^a-z]', '', text)
    reg = r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'

    '''
    ret = re.findall(reg, text)
    print ret # .groups()
    '''
    print ''.join(re.findall(reg, text))


def _do_it():
    # http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=80992
    base_url = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

    nothing = 80992
    nothing = 16044 / 2
    nothing = 63579

    while True:
        url = ''.join([base_url, str(nothing)])
        print url
        ret = urllib2.urlopen(url).read()
        print ret
        nothing = re.search(r'\d{1,100}', ret).group(0)
        print nothing

if __name__ == '__main__':
    # _main()
    _do_it()
