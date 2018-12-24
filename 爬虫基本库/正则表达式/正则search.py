import re
con='EXO hero Hello 123 4567 World_This is a Regex Demo'
result=re.search('Hell.*?Demo',con)
print(result)
print(result.group())

html=''''
<li>
<input type="checkbox" value="9762@" name="Url" class="check">
<span class="songNum ">24.</span>
<a target="_1" href="/play/9762.htm" class="songName ">一生有你 </a>
</li>
<li>
<input type="checkbox" value="2247@" name="Url" class="check">
<span class="songNum ">25.</span>
<a target="_1" href="/play/2247.htm" class="songName ">红豆 </a>
</li>
<li>
<input type="checkbox" value="671@" name="Url" class="check">
<span class="songNum ">26.</span>
<a target="_1" href="/play/671.htm" class="songName ">真的爱你 </a>
</li>
<li>
<input type="checkbox" value="22985@" name="Url" class="check">
<span class="songNum ">27.</span>
<a target="_1" href="/play/22985.htm" class="songName ">容易受伤的女人 </a>
</li>
<li>
<input type="checkbox" value="649@" name="Url" class="check">
<span class="songNum ">28.</span>
<a target="_1" href="/play/649.htm" class="songName ">海阔天空 </a>
</li>
<li>
<input type="checkbox" value="1545@" name="Url" class="check">
<span class="songNum ">29.</span>
<a target="_1" href="/play/1545.htm" class="songName cRed">同桌的你 </a>
</li>
'''
result=re.search('li.*?songNum ">(.*?)</span>.*?>(.*?)</a>',html,re.S)
#print(result)
#print(result.group())
print(result.group(1))
print(result.group(2))

results=re.findall('li.*?songNum ">(.*?)</span>.*?>(.*?)</a>',html,re.S)
print(results)
print(results[0])

conte='ahfgi123ahfuo358bjhif134'
conten=re.sub('\d+',' afanti ',conte)
print(conten)

content1='2015-9-12 12:00'
content2='2016-12-22 13:55'
content3='2017-10-1 11:40'
pattern=re.compile('\d{2}:\d{2}')
print(pattern)
result1=re.sub(pattern,'',content1)
result2=re.sub(pattern,'',content2)
result3=re.sub(pattern,'',content3)
print(result1,result2,result3)