import requests
import re

headers={
    'User-Agent':"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5"
}

r=requests.get('https://www.zhihu.com/explore',headers=headers)
pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles=re.findall(pattern,r.text)
print(titles)


r=requests.get("https://github.com/favicon.ico")
#print(r.text)
#print(r.content)
with open('favicon.ico','wb') as f:
    f.write(r.content)

data={'name':'ltf','age':22}
r=requests.post("http://httpbin.org/post",data=data)
print(r.text)


r=requests.get('http://www.jianshu.com')
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)
print(type(r.history),r.history)