# import requests
# from  bs4 import  BeautifulSoup
# reqpend = requests.get('http://www.a-hospital.com/w/四川省三级甲等医院列表')
# htmlop = BeautifulSoup(reqpend.content,'html.parser')
# soup  = htmlop.find_all('div',id ='bodyContent')
# print(soup)
# for kok in soup:
#     print(kok.ul.a.get('title'))
from lxml import etree

html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//a[@href="link4.html"]/../@class')
print(result)

result=html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

#一种通过..获取，另一种通过parent::*获取父节点

#属性匹配
result=html.xpath('//li[@class="item-0"]')
print(result)

#文本获取
result=html.xpath('//li[@class="item-1"]/a/text()')
print(result)

result=html.xpath('//li[@class="item-1"]//text()')
print(result)

#属性获取
result=html.xpath('//li/a/@href')
print(result)