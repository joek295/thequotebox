"""
The QuoteBox - ver 0.0
URL: https://github.com/nm523/thequotebox.git

Using web.py
"""

import web

### URL Mapping

urls = (
    '/', 'index',
    '/random', 'random',
    '/admin', 'admin',
    '/about', 'about',
    '/quotes', 'quotes'
    '/quote/(\d+)', 'quote'
)

app = web.application(urls, globals())

### Templates
render = web.template.render('templates', base='base')

class index:
   def GET(self):
       return render.index(pages)

class about:
   def GET(self):
       pass

class admin:
    def GET(self):
        pass

class quotes:
   def GET(self):
       pass

class quote:
    def GET(self):
        pass

if __name__ == "__main__":
    app.run()
       
