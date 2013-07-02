"""
The QuoteBox - ver 0.0
URL: https://github.com/nm523/thequotebox.git

Using web.py, and horrible encapsulation
"""

import web
import csv, random

### URL Mapping

urls = (
    '/', 'index',
    '/random', 'random',
    '/admin', 'admin',
    '/about', 'about',
    '/quotes', 'quotes'
    '/quote/(\d+)', 'quote'
    '/add', 'add'
)

app = web.application(urls, globals())

### Templates
render = web.template.render('templates', base='base')

### QuoteBox Info
with open('quoteCount.txt', 'r') as quoteCount:
    quotes = 

class index:
   def GET(self):
       return render.index(pages)

class about:
   def GET(self):
       pass

class admin:
    def GET(self):
        pass

class quote:
   def GET(self):
       pass

class random:
    def GET(self):
        with open('quotes.csv', 'r') as csvQuotes:
            csvReader = csv.reader(csvQuotes, delimiter=",")
            for i, row in enumerate(csvReader)
		if i == 1:
                    quotesNumber = row[3]
                    randQuoteN = random.randint(2, quotesNumber)
                elif i == randQuoteN:
                    return "[" + str(row[0]) + "] " + row[1] + ": " + row[2] 

class quotes:
    def GET(self):
        pass

class add:
    def POST(self):
        i = web.input()
        n = 

if __name__ == "__main__":
    app.run()
       
