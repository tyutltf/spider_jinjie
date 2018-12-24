from lxml import etree
import os
print(os.getcwd())
text='''
<div>
<ul>
<li class="item-0"><a href='link.html'>first item</a></li>
<li class="item-1"><a href='link.html'>second item</a></li>
<li class="item-2"><a href='link.html'>third item</a></li>
<li class="item-3"><a href='link.html'>fourth item</a></li>
<li class="item-4"><a href='link.html'>fifth item</a>
</ul>
</div>
'''
html=etree.HTML(text)
print(html)
result=etree.tostring(html)
print(result.decode('utf-8'))   #输出html文本

html1=etree.parse('./test.html',etree.HTMLParser())  #第一次没有加方法
print(html1)
result1=etree.tostring(html1)
print(result1.decode('utf-8'))  #输出html文本

result2=html.xpath('//*')
print(result2)  #获取html文本中的所有节点

result3=html.xpath('//li')
print(result3)  #获取所有li节点，是一个列表
print(result3[0])   #输出列表第一个元素

print('''子节点''')

result4=html.xpath('//li/a')
print(result4) #输出所有li节点下的a子节点

result5=html.xpath('//ul/a')
print(result5)   #啥都输不出 ul节点下面 没有 a 标签

