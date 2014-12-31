# -*- coding: UTF-8 -*-

'''
Last modified time: (ÎÞÐ§)
Edit time: 2014-12-12 14:17:27
File name: app.py
Edit by caimaoy
'''

import web

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index(object):
    def GET(self):
        greeting = 'Hello World'
        ret = render.index(greeting = greeting)
        return ret


if __name__ == '__main__':
    app.run()
