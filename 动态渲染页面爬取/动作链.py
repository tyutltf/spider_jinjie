from selenium import webdriver
from selenium.webdriver import ActionChains
'''
browser=webdriver.Chrome()  #影响谷歌浏览器
url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source=browser.find_element_by_css_selector('#draggable') #拖拽位置
target=browser.find_element_by_css_selector('#droppable') #放置位置
actions=ActionChains(browser) #声明actions对象
actions.drag_and_drop(source,target)  #执行拖拽方法
actions.perform()  #执行动作
'''

#下拉动作
from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("to bottom")')