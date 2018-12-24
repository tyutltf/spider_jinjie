from lxml import etree

text='''
<div>
<ul>
<li class="item-0"><a href='link.html'><p>1 item</p></a></li>
<li class="item-1"><a href='link.html'>2 item</a></li>
<li class="item-2"><a href='link.html'>3 item</a></li>
<li class="item-3"><a href='link.html'>4 item</a></li>
<li class="item-4"><a href='link.html'>5 item</a></li>
</ul>
</div>
'''
html=etree.HTML(text)

result=html.xpath('//li[1]/a/text()')
print(result) #第一个节点

result=html.xpath('//li[last()]/a/text()')
print(result) #最后一个节点

result=html.xpath('//li[position()<3]/a/text()')
print(result) #位置小与3

result=html.xpath('//li[last()-2]/a/text()')
print(result) #倒数第三

result=html.xpath('//li[4]/a/text()')
print(result)  #第四个节点


#节点轴选择
result=html.xpath('//li[1]/ancestor::*')
print(result)  #祖先节点

result=html.xpath('//li[1]/attribute::*')
print(result)  #获取属性值

result=html.xpath('//li[1]/child::*')
print(result)  #子节点

result=html.xpath('//li[1]/descendant::p')
print(result)  #子孙节点

result=html.xpath('//li[1]/following::*')
print(result)  #获取li[1]后的所有节点

result=html.xpath('//li[1]/following-sibling::*/a/text()')
print(result)  #获取li[1]后的所有节点

