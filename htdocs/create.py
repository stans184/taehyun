#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

import cgi                          # cgi package를 사용하겠다
import os

files = os.listdir('data')          # data 폴더 안의 파일 이름들을 가져와서 files에 list로 저장
liststr = ''
for item in files:
  liststr = liststr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

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
  <form action="process_create.py" method="post">
    <p><input type="text" name="title" placeholder="title"></p>
    <p><textarea rows="4" name="description" placeholder="contents"></textarea></p>
    <p><input type="submit"></p>
  </form>
</body>
</html>'''.format(title=pageId, desc = description, liststr = liststr))