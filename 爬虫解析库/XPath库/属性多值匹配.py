from lxml import etree
text='''
<li class="li li-first"><a href="link-html">first</a></li>
'''
html=etree.HTML(text)
result=html.xpath('//li[@class="li"]/a/text()')
print(result)

result=html.xpath('//li[contains(@class,"li")]/a/text()')
print(result)
#加 contains（）函数可以匹配多值

#多属性匹配
text='''
<li class="li li-first" name="item"><a href="link-html">first</a></li>
'''
html=etree.HTML(text)
result=html.xpath('//li[contains(@class,"li")and @name="item"]/a/text()')
print(result)
#多属性匹配 加运算符