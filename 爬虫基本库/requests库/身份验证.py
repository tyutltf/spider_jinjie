import requests
from requests.auth import HTTPBasicAuth
from requests import Request,Session

r=requests.get('http://www.6mao.com',auth=('1234','ltf1234'))
print(r.status_code)

url='http://httpbin.org/post'
data={
    'name':'germey'
}
headers={
'User-Agent':"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5"
}

s=Session()
req=Request('POST',url,data=data,headers=headers)
prepped=s.prepare_request(req)
r=s.send(prepped)
print(r.text)
