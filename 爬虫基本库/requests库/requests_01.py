import requests

r=requests.get('http://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

r=requests.get('http://httpbin.org/get')
print(r.text)
print(type(r.text))  #字符串类型
print(r.json())
print(type(r.json()))  #字典类型

data={
    'age':21,
    'name':'ltf'
}
r=requests.get('http://httpbin.org/get',params=data)
print(r.text)