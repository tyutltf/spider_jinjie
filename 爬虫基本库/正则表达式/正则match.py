import re

con='Hello 123 4567 World_This is a Regex Demo'
print(len(con))
result=re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',con)
print(result)
print(result.group())
print(result.span())

result=re.match('^Hello\s(\d+)\s(\d+)\sWorld',con)
print(result)
print(result.group())
print(result.group(1),result.group(2))
print(result.span())


result=re.match('^Hello.*Demo',con)
print(result)
print(result.group())
print(result.span())

result=re.match('^He.*?(\d+).*Demo',con)
print(result)
print(result.group(1))


con1='http://weibo.com/comment/ltf'
result1=re.match('^http.*?comment/(.*?)',con1)
result2=re.match('^http.*?comment/(.*)',con1)
print(result1.group(1))
print(result2.group(1))

con2='''Hello 123 4567 World_This 
is a Regex Demo'
'''
result=re.match('Hell.*?(\d+).*?Demo',con2,re.S)
print(result)
print(result.group(1))

con3='(百度)www.baidu.com'
result=re.match('\(百度\)www\..*?\..*',con3)
print(result)
print(result.group())