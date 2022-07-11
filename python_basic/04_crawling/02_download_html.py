#https://www.google.com/search?q=%ED%96%84%EC%8A%A4%ED%84%B0+%EC%82%AC%EC%A7%84&rlz=1C5CHFA_enKR986KR986&oq=%ED%96%84%EC%8A%A4%ED%84%B0+%EC%82%AC%EC%A7%84&aqs=chrome..69i57l2j69i59l2j69i61l3.1498j0j15&sourceid=chrome&ie=UTF-8

import urllib.request #요청할 때
import urllib.parse #쿼리 뒷쪽 =%ED%96%84%EC% 이 값들이 한글인데 꺠지기 때문에 url호출할 때 인코딩을 맞춰주어야 한다

url = 'https://www.google.com/search'
values = {
    'q' : '%ED%96%84%EC%8A%A4%ED%84%B0+%EC%82%AC%EC%A7%84&',
    'rlz' : '1C5CHFA_enKR986KR986&oq=%ED%96%84%EC%8A%A4%ED%84%B0+%EC%82%AC%EC%A7%84&',
    'aqs' : 'chrome..69i57l2j69i59l2j69i61l3.1498j0j15&',
    'sourceid' : 'chrome&',
    'ie' : 'UTF-8'
}

param = urllib.parse.urlencode(values)
url = url + '?' + param
print(url)

data = urllib.request.urlopen(url).read().decode('utf-8')
print(data)