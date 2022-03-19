#!/usr/bin/python3
#-*- codeing = utf-8 -*-
#@Time : 1/11/2021 11:27 PM
#@Author : Liu
#@File : 网页截图识别.py
#@Software : PyCharm

from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from PIL import Image
from allv_lib import ocr

net_hold = webdriver.Chrome('chromedriver.exe')

net_hold.get("https://so.gushiwen.cn/user/login.aspx")

window_size = net_hold.get_window_size()
width, height = window_size['width'], window_size['height']

time.sleep(5)
net_hold.save_screenshot('html.png')


image_code_l = net_hold.find_element_by_xpath('//*[@id="aspnetForm"]/div[4]/div[5]/a[3]')
image_location = image_code_l.location

image_code_s = net_hold.find_element_by_xpath('//*[@id="imgCode"]')
image_size = image_code_s.size

print(image_location,image_size)

image_xy = (image_location['x'], image_location['y'], image_location['x']+image_size['width'], image_location['y']+image_size['height'])

img_hold = Image.open('html.png')

img_hold = img_hold.resize((width,height))

code_hold = img_hold.crop(image_xy)
code_hold.save('code.png')


code_return = ocr.get_text('code.png', 2)

user = net_hold.find_element_by_id('email')
key = net_hold.find_element_by_id('pwd')
code = net_hold.find_element_by_id('code')

user.send_keys('371509452@qq.com')
time.sleep(1)
key.send_keys('123456789.mmm')
time.sleep(1)
code.send_keys(code_return)
time.sleep(1)

login = net_hold.find_element_by_id('denglu')

login.click()

time.sleep(10)
