from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
EMAIL='18235121656@163.com'
PWD='qwertyui123'

class CrackGeetest():
    def __init__(self):
        self.url='https://account.geetest.com/login'
        self.browser=webdriver.Chrome()
        self.wait=WebDriverWait(self.browser,20)
        self.email=EMAIL
        self.password=PWD