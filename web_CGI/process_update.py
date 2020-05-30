#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# print("Content-Type: text/html")    # HTML is following

import cgi
import os

form = cgi.FieldStorage()
pageId = form["pageId"].value                   # form 을 통해 넘어온 data 중, pageId 변수
title = form["title"].value                     # form 을 통해 넘어온 data 중, title 변수
description = form['description'].value         # form 을 통해 넘어온 data 중, description 변수

opened_file = open('data/'+pageId, 'w')         # title 변수 이름을 가진 파일 생성 // update.py에 의해 title은 수정될 수 있으므로, 변하지 않는 pageId를 받는다
opened_file.write(description)                  # 해당 파일 안에 description 내용 저장
opened_file.close()

os.rename('data/'+pageId, 'data/'+title)                        # file의 이름을 기존의 pageId에서, 입력한 title로 수정

#Redirection => header가 사용자를 다른 page로 보내버리는 header
print("Location: index.py?id="+title)           # header 값, location 지정
print()                                         # blank line, end of headers