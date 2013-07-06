"""
Functions for handling the quotes, essentially the backend of the operation
"""

import csv, time
from random import randint

def getQuote(n):
    with open('quotes.csv', 'r') as csvQuotes:
            csvReader = csv.reader(csvQuotes, delimiter=",")
            quoteToGet = n
            for i, row in enumerate(csvReader):
                if i == quoteToGet:
                    return [str(n),row[1],row[2]]
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


