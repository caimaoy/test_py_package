# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-03-03 16:03:23
Edit time: 2015-03-03 16:03:40
File name: my_xiami.py
Edit by caimaoy
'''

__author__ = 'caimaoy'

import requests

email = 'chenyue3721@qq.com'
password = '117721'

s = requests.Session()


def login():
    login_data = {
        'done': '/',
        'email': email,
        'password': password,
        'submit': '登 录',
    }
    login_url = r'http://www.xiami.com/member/login'
    login_headers = {
        'Referer': 'http://www.xiami.com/web/login',
        'User-Agent': 'Opera/9.60',
    }
    s.post(
        login_url,
        data=login_data,
        headers=login_headers
    )


def signin():
    signin_url = 'http://www.xiami.com/task/signin'
    signin_headers = {
        'Referer': 'http://www.xiami.com/',
        'User-Agent': 'Opera/9.60',
    }
    r = s.get(signin_url, headers=signin_headers)
    print r.text
    file_name = r'D:\caimaoy\python\xiami\my_xiami.log'
    with open(file_name, 'a') as f:
        from datetime import datetime
        t = datetime.now()
        l = '%s: %s\n' % (t, r.text)
        f.write(l)


def main():
    login()
    signin()

if __name__ == '__main__':
    main()
