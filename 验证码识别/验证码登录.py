#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 8:58
# @Author  : tf.yuxuan
# @File    : login.py
# @Software: PyCharm
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from io import BytesIO
from PIL import Image
import pytesseract
import time

user='zhang'
password='123'
url='http://10.0.0.200'
driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)

#识别验证码
def acker(content):
    im_erzhihua=erzhihua(content,127)
    result=pytesseract.image_to_string(im_erzhihua,lang='eng')
    return result

#验证码二值化
def erzhihua(image,threshold):
    ''':type image:Image.Image'''
    image=image.convert('L')
    table=[]
    for i in range(256):
        if i <  threshold:
            table.append(0)
        else:
            table.append(1)
    return image.point(table,'1')

#自动登陆
def login():
    try:
        driver.get(url)
        #获取用户输入框
        input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#loginname'))) #type:WebElement
        input.clear()
        #发送用户名
        input.send_keys(user)
        #获取密码框
        inpass=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#password'))) #type:WebElement
        inpass.clear()
        #发送密码
        inpass.send_keys(password)
        #获取验证输入框
        yanzheng=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#code'))) #type:WebElement
        #获取验证码在画布中的位置
        codeimg=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#codeImg'))) #type:WebElement
        image_location = codeimg.location
        #截取页面图像并截取掩码码区域图像
        image=driver.get_screenshot_as_png()
        im=Image.open(BytesIO(image))
        imag_code=im.crop((image_location['x'],image_location['y'],488,473))
        #输入验证码并登陆
        yanzheng.clear()
        yanzheng.send_keys(acker(imag_code))
        time.sleep(2)
        yanzheng.send_keys(Keys.ENTER)
    except TimeoutException as e:
        print('timeout:',e)
    except WebDriverException as e:
        print('webdriver error:',e)

if __name__ == '__main__':
    login()