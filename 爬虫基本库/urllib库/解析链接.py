from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
from urllib.parse import urljoin
from urllib.parse import urlencode
from urllib.parse import parse_qs
from urllib.parse import parse_qsl
from urllib.parse import quote
from urllib.parse import unquote
from urllib.robotparser import RobotFileParser

result=urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result))
print(result)
print(result[0])
print(result.netloc)


data=['http','www.baidu.com','index.html','user','id=5','comment']
print(urlunparse(data))  #参数拼接成链接  长度为6

result=urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)

data=['http','www.baidu.com','index.html','id=5','comment']
print(urlunsplit(data))  #参数拼接成链接 长度为5

print(urljoin('http://www.baidu.com','FAQ.html'))
print(urljoin('http://www.baidu.com','http://ltfcsdn.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html','http://ltfcsdn.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html','http://ltfcsdn.com/FAQ.html?queestion=2'))
print(urljoin('http://www.baidu.com?wd=abc','http://ltfcsdn.com/index.php'))
print(urljoin('http://www.baidu.com','category=2#comment'))
print(urljoin('www.baidu.com','category=2#comment'))

parms={
    'name':'germey',
    'age':22
}
bash_url='http://www.baidu.com'
url=bash_url+urlencode(parms)
print(url)    #序列化

query='name=bob&age=21'
print(parse_qs(query)) #反序列化  字典

print(parse_qsl(query)) #反序列化 元组

keyword='壁纸'
url='http://www.baidu.com/s?wd='+quote(keyword)
print(url)  #url编码

url='http://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))   #url解码


rp=RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*','http://www.jianshu.com'))
