import requests
from pyquery import PyQuery as pq

url='https://www.zhihu.com/explore'   #今日最热
#url='https://www.zhihu.com/explore#monthly-hot'   #本月最热
headers={
    'User-Agent':"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
}
html=requests.get(url,headers=headers).text
doc=pq(html)
#print(doc)
items=doc('.explore-feed.feed-item').items()
for item in items:
    question=item.find('h2').text()
    #获取问题
    print(question)
    author=item.find('.author-link').text()
    #获取作者
    print(author)
    answer=pq(item.find('.content').html()).text()
    #获取答案（老师写的没看懂，可能需要jquery知识）
    print(answer)
    print('===='*10)
    answer1=item.find('.zh-summary').text()
    #自己写的获取答案。。。
    print(answer1)

    #第一种写入方法
    file=open('知乎.txt','a',encoding='utf-8')
    file.write('\n'.join([question,author,answer]))
    file.write('\n'+'****'*50+'\n')
    file.close()

    #第二种写入方法 不需要写关闭方法
    with open('知乎.txt','a',encoding='utf-8') as fp:
        fp.write('\n'.join([question, author, answer]))
        fp.write('\n' + '****' * 50 + '\n')