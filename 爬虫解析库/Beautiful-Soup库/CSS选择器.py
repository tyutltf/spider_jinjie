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
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))


for ul in soup.select('ul'):
    print(ul.select('li'))

print('===='*10)
for li in soup.select('li'):
    print('get_text',li.get_text())
    print('string',li.string)