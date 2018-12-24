import requests
from  bs4 import  BeautifulSoup
reqpend = requests.get('http://www.a-hospital.com/w/四川省三级甲等医院列表')
html = BeautifulSoup(reqpend.content,'html.parser')
soup = html.find_all(name='b')
print(soup)
for b in soup:
    print(b.find_all(name='a'))
    for yiyuan in b.find_all(name='a'):
        print(yiyuan.string)

