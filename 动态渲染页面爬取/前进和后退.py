import time
from selenium import webdriver

browser=webdriver.Chrome()
'''
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('https://www.python.org')
browser.back()  #回到第二个页面
time.sleep(3)
browser.forward()  #去往第三个页面 共访问了五个页面
browser.close()
'''

browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies()) #获得cookies
browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})  #cookies重新赋值
print(browser.get_cookies())
browser.delete_all_cookies()  #删除所有cookies
print(browser.get_cookies())
browser.close()