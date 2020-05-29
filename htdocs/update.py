#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

import cgi                          # cgi package를 사용하겠다
import os, view

form = cgi.FieldStorage()

if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId,'r').read()
else:
    pageId = 'welcome'
    description = 'Hello. Web'

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {liststr}
  </ol>
  <a href="create.py">create</a>
  <form action="process_update.py" method="post">
    <input type="hidden" name="pageId" value="{form_default_title}">
    <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
    <p><textarea rows="10" name="description" placeholder="contents">{form_default_description}</textarea></p>
    <p><input type="submit"></p>
  </form>
</body>
</html>'''.format(title=pageId, desc = description, liststr = view.getList(), form_default_title = pageId, form_default_description = description))
