import requests
import re
import time
import json

def get_one_page(url):
    headers={
        'User-Agent': "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5"
    }
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    return None

def parse_one_page(html):

    pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>'
                       +'(.*?)</a>.*?star">(.*?)</p>'
                    +'.*?releasetime">(.*?)</p>.*?integer">(.*?)'
                     +'</i>.*?fraction">(.*?)</i></p>.*?</dd>',
        re.S)

    '''
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    '''
    items = re.findall(pattern, html)
    for item in items:
        yield {
            '排名':item[0],
            '图片':item[1],
            '名字':item[2].strip(),
            '演员':item[3].strip()[3:]if len(item[3])>3 else '',
            '时间':item[4].strip()[5:]if len(item[4])>5 else '',
            '评分':item[5].strip()+item[6].strip()
        }

def write_to_file(content):
    with open('movie.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
    url='https://maoyan.com/board/4?offset='+str(offset)
    html=get_one_page(url)
    #print(html)
    for item in parse_one_page(html):
        print(item)
        #write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)
