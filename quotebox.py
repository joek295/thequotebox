"""
The QuoteBox - ver 0.0
URL: https://github.com/nm523/thequotebox.git

Using web.py, and horrible encapsulation
"""

import web
from web import form
import csv, time
from random import randint

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

def getQuote(n):
    with open('quotes.csv', 'r') as csvQuotes:
            csvReader = csv.reader(csvQuotes, delimiter=",")
            quoteToGet = n
            for i, row in enumerate(csvReader):
                if i == quoteToGet:
                    return "[" + str(n) + "] " + row[1] + ": " + row[2]

### Templates
render = web.template.render('templates', base='base', globals={'getQuote': getQuote})

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
       return getQuote(int(id))

class random:
    def GET(self):
        return randomQuote() 

class quotes:
    def GET(self, id):
        return render.quotes(id)

class add:
    def GET(self):
        #addQuote("Niall", str(quoteCount()))
        #return "Added!"
        form = addForm()
        return render.add(form)
    def POST(self):
        form = addForm()
        if not form.validates():
            return render.new(addForm)
        else: 
            addQuote(form.d.Perpetrator, form.d.Quote)
            return "Quote Added!"

def randomQuote():
    randQuoteN = -1
    quotesNumber = quoteCount()
    randQuoteN = randint(1, quotesNumber)
    return getQuote(randQuoteN)

def quoteCount():
    with open('quoteCount.txt', 'r') as quoteReader:
        return int(quoteReader.read())

def addQuote(perpetrator, quote):
    newQuoteCount = quoteCount() + 1
    with open('quotes.csv', 'a') as csvQuotes:
        csvWriter = csv.writer(csvQuotes, delimiter=",")
        csvWriter.writerow([str(time.time()), perpetrator, quote])
    with open('quoteCount.txt', 'wb') as quoteWriter:
        quoteWriter.seek(0)
        quoteWriter.write(str(newQuoteCount))



if __name__ == "__main__":
    app.run()
       
