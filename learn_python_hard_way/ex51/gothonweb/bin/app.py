# -*- coding: UTF-8 -*-

'''
Last modified time: (ÎÞÐ§)
Edit time: 2014-12-12 14:17:27
File name: app.py
Edit by caimaoy
'''

import web

urls = (
    '/hello', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')

class index(object):
    def GET(self):
        return render.hello_form()
        form = web.input(name='Nobody')
        memberlist = [i for i in dir(form)]
        for m in memberlist:
            print m, getattr(form, m)

        greeting = 'Hello %s' % form.name
        ret = render.index(greeting = greeting)
        return ret

    def POST(self):
        form = web.input(name='Nobody', greet='Hello')
        greeting = '%s %s' % (form.greet, form.name)
        ret = render.index(greeting = greeting)
        return ret


if __name__ == '__main__':
    app.run()
