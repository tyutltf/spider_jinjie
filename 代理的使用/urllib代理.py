from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy='123.58.10.36:8080'  #使用本地代理
#proxy='username:password@123.58.10.36:8080'  #购买代理
proxy_handler=ProxyHandler({
    'http':'http://'+proxy,
    'https':'https://'+proxy
})
opener=build_opener(proxy_handler)
try:
    response=opener.open('http://httpbin.org/get') #测试ip的网址
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)