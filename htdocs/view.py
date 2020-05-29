import os

def getList():
  files = os.listdir('data')          # data 폴더 안의 파일 이름들을 가져와서 files에 list로 저장
  liststr = ''
  for item in files:
    liststr = liststr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
  return liststr