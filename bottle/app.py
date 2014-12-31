# -*- coding: UTF-8 -*-


'''
Last modified time: (无效)
Edit time: 2014-09-25 15:00:48
File name: app.py
Edit by caimaoy
'''

from bottle import route, run

@route('/hello/:name')
def index(name = 'World'):
    return '<strong>Hello {}!'.format(name)



if __name__ == '__main__':
    run(host='localhost', port=8080)

