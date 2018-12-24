from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
#print(browser.page_source)
'''
input_first=browser.find_element_by_id('q')
input_second=browser.find_element_by_css_selector('#q')
input_third=browser.find_element_by_xpath('//*[@id="q"]')
print(input_first,'\n',input_second,'\n',input_third)
'''

#单个节点
# input_first=browser.find_element(By.ID,'q')
# print(input_first)

#多个节点
# lis=browser.find_elements_by_css_selector('.service-bd li')
# print(lis)

#节点交互
input=browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button=browser.find_element_by_class_name('btn-search')
button.click()
#关闭浏览器
#browser.close()