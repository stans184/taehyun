#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# print("Content-Type: text/html")    # HTML is following

import cgi, os

form = cgi.FieldStorage()
pageId = form["pageId"].value                     # form 을 통해 넘어온 data 중, pageId 변수

os.remove("data/"+pageId)

#Redirection => header가 사용자를 다른 page로 보내버리는 header
print("Location: index.py")           # header 값, location 지정
print()                                         # blank line, end of headers