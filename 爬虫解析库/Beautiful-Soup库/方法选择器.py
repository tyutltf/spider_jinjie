html='''
<div class="panel">
<div class="panel-heading">
<h4>hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">foo hhh</li>
<li class="element">bar</li>
<li class="element">jay</li>
</ul>
<ul class="list-small" id="list-2" name="elements">
<li class="element">foo</li>
<li class="element">bar</li>
</ul>
</div>
</div>
'''
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)

print('传属性来查询')
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))

print('===='*10)
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))

print('++==++'*10)
import re
print(soup.find_all(text=re.compile('foo')))