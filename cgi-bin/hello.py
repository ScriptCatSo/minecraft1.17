#!/usr/bin/env python3

print("Content-type: text/html")
print()
print("<h1>Hello world!</h1>")
print()
print("<form action=/cgi-bin/form.py>")
print("<input type=text"" name=""TEXT_1>")
print("<input type=text name=""TEXT_2>")
print("<input type=submit>")
print("</form>")