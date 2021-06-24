#!/usr/bin/env python3
import cgi
import html

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text2 = form.getfirst("TEXT_2", "не задано")
text1 = html.escape(text1)
text2 = html.escape(text2)
name=(text1+"!")
print("Content-type: text/html\n")
print("<p>Привет {}</p>".format(name))