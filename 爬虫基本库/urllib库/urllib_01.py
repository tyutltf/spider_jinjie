import urllib.request
import urllib.parse
import urllib.error


response=urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

data=bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf8')
response=urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read())

response=urllib.request.urlopen('http://httpbin.org/get',timeout=1)
print(response.read())
