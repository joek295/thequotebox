"""
The QuoteBox - ver 0.0
URL: https://github.com/nm523/thequotebox.git

Using web.py
"""

import web

### URL Mapping

urls = {
    '/', 'Index',
    '/random', 'Random',
    '/admin', 'Admin',
    '/about', 'About',
    '/quotes', 'Quotes'
    '/quote/(\d+)', 'Permalink'
}

### Templates
render = web.template.render('templates, base='base')
