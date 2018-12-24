html='''
<html lang="zh-hans" dir="ltr">
<head><title>The Dormouse's story</title></head>
<body>
<ul>
<li><a href="1.html" title="四川省二级甲等医院列表">二甲医院<p class="fuck">fuck 你</p></a></li>
<li><a href="2.html" title="四川省二级乙等医院列表">二乙医院</a></li>
<li><a href="3.html" title="四川省二级丙等医院列表">二丙医院</a></li>
<li><a href="4.html" title="四川省一级甲等医院列表">一甲医院</a></li>
<li><a href="5.html" title="四川省一级乙等医院列表">一乙医院</a></li>
<li><a href="6.html" title="四川省一级丙等医院列表">一丙医院</a></li>
</ul>
<p class="story">死亡如风，常伴我身</p>
'''

from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
#print(soup.prettify())
#获取节点
print(soup.title)
print(soup.title.string)
print(soup.p)
print(soup.a)

#获取属性
print(soup.title.name)

print(soup.p.attrs)
print(soup.p.attrs['class']) #获取属性
print(soup.p['class'])
print(soup.p.string) #获取文本

#嵌套选择
print(soup.head.title.string)

print('=='*20)
#关联选择
print(soup.ul.contents)

print(soup.ul.children)