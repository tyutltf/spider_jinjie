import requests

requests.get('http://httpbin.org/cookies/set/number/123456789')
r=requests.get('http://httpbin.org/cookies')
print(r.text)

s=requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r=s.get('http://httpbin.org/cookies')
print(r.text)

response=requests.get('http://www.12306.cn',verify=False)
print(response.status_code)