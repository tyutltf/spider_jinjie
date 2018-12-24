import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser=webdriver.Chrome()
url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo=browser.find_element_by_class_name('loho')
except NoSuchElementException:
    print('NO LOGO')
browser.switch_to.parent_frame()
logo1=browser.find_element_by_class_name('logo')
print(logo1)
print(logo1.text)