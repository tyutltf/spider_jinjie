import requests

url='http://localhost:8050/render.html?url=https://www.baidu.com'
res=requests.get(url)
print(res)