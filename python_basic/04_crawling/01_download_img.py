# import urllib.request

# # 1. url = 'https://kr-mb.theepochtimes.com/assets/uploads/2019/11/a58d75581e050bbc5c6acfe08ad418ff.png'
# url = '이미지 url주소' #2. 파일 생기면 수정
# savename = 'test.png'

# urllib.request.urlretrieve(url, savename)

#from urllib import request

url = 'http://www.naver.com/'
#mem = request.urlopen(url).read()
#print(mem.decode('utf-8'))

import requests

r = requests.get('http://api.github/user', auth=('user', 'pass'))
print(r.status_code)
print(r.encoding)
print(r.json())



