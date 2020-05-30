#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# print("Content-Type: text/html")    # HTML is following

import cgi

form = cgi.FieldStorage()
title = form["title"].value                     # form 을 통해 넘어온 data 중, title 변수
description = form['description'].value         # form 을 통해 넘어온 data 중, description 변수

opened_file = open('data/'+title, 'w')          # title 변수 이름을 가진 파일 생성
opened_file.write(description)                  # 해당 파일 안에 description 내용 저장
opened_file.close()

#Redirection => header가 사용자를 다른 page로 보내버리는 header
print("Location: index.py?id="+title)           # header 값, location 지정
print()                                         # blank line, end of headers