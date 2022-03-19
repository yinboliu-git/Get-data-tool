#!/usr/bin/python3
#-*- codeing = utf-8 -*-
#@Time : 1/25/2021 11:50 PM
#@Author : Liu
#@File : get_cy.py
#@Software : PyCharm


from selenium import webdriver
import selenium
import time
import random

i = 1
one_numb = [11, 10, 9]
while i < 100:
    net = webdriver.Chrome('chromedriver.exe')
    numb = random.uniform(0.5, 1) * 3
    try:
        net.get('https://ur1.one/51F25KIr')
    except selenium.common.exceptions.WebDriverException:
        print('网络断开...')
        time.sleep(5-numb)
        net.close()
        net.quit()
        time.sleep(5 + numb)
        continue

    try:
        time.sleep(20+numb)
        px = 1000 + random.randint(600,1000)
        net.execute_script("window.scrollTo(0,{})".format(px))
        time.sleep(10-numb)
    except selenium.common.exceptions.WebDriverException:
        print('网络断开...')
        time.sleep(5 - numb)
        net.close()
        net.quit()
        time.sleep(5 + numb)
        continue

    try:
        net_div = net.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[5]/div/div[2]/ul/li[1]/div/dl/div[1]/dd[{}]'.format(random.randint(1, 10)))
        net_div.click()
        time.sleep(5 + numb)
        net.back()
        time.sleep(10)
        x = 1000 + random.randint(600, 1000)
        net.execute_script("window.scrollTo(0,{})".format(px))
    except Exception as e:
        print('网络异常...')
        time.sleep(10)
        net.close()
        net.quit()
        time.sleep(5 + numb)
        continue

    time.sleep(5)
    net.close()
    print('现在在执行的次数为第 {} 次...'.format(i))
    i += i
    time.sleep(one_numb[i % 3])
    time.sleep(5)
    net.quit()

print('全部结束..')







