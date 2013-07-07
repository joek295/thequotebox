"""
The QuoteBox - ver 0.0
URL: https://github.com/nm523/thequotebox.git

Using web.py, and horrible encapsulation
"""

import web, quotebox
from web import form

### URL Mapping

urls = (
    '/', 'index',
    '/random', 'random',
    '/admin', 'admin',
    '/about', 'about',
    '/quotes/(\d+)', 'quotes',
    '/quote/(\d+)', 'quote',
    '/add', 'add'
)
addForm = form.Form(
    form.Textbox("Perpetrator"),
    form.Textbox("Quote"),
    form.Button("Add Quote"),
)
app = web.application(urls, globals())

### Templates
render = web.template.render('templates', base='base', globals={'getQuote': quotebox.getQuote, 'randomQuote': quotebox.randomQuote})

class index:
   def GET(self):
       return render.index(self)

class about:
   def GET(self):
       pass

class admin:
    def GET(self):
        pass

class quote:
   def GET(self, id):
       return render.quote(id)

class random:
    def GET(self):
        return render.random(self) 

class quotes:
    def GET(self, id):
        return render.quotes(id)

class add:
    def GET(self):
        form = addForm()
        return render.add(form,0)
    def POST(self):
        form = addForm()
        if not form.validates():
            return render.add(addForm)
        else: 
            quotebox.addQuote(form.d.Perpetrator, form.d.Quote)
            return render.add(addForm,1)

if __name__ == "__main__":
    app.run()
       
