#!/usr/bin/python3
#-*- codeing = utf-8 -*-
#@Time : 1/13/2021 3:07 PM
#@Author : Liu
#@File : 发送数据.py
#@Software : PyCharm

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import re
import random
import openpyxl
import xlsx_get

def mul_as(li_len,t_as_):
    asw_list_m = []
    sum_sum = 0
    for li in range(li_len):
        ls = random.random() - t_as_[li]/2
        asw_one = ls < 0.25
        asw_list_m.append(asw_one)
        sum_sum = sum_sum + asw_one
    if sum_sum <= 1:
        return t_as_
    return asw_list_m


def sig_as(li_len,t_as_1,q_id):
    qa = (q_id % 10) * 0.01
    if random.random() <= (0.3+ qa) :
        asw_one = t_as_1
    else:
        asw_one = int(1+ random.random() * li_len* 0.999)

    return asw_one


'''

'''
def wjx_sump(url,filename):
    # url = 'https://www.wjx.cn/jq/74717566.aspx'
    '''filename = './t.xlsx' 本地正确答案所在名称
    '''

    imp_data = xlsx_get.get_asw(filename, 1)  # 输出答案
    net_hold = webdriver.Chrome('chromedriver.exe')
    net_hold.get(url)
    time.sleep(2)

    for i in range(1, len(imp_data) + 1):
        q_id = 'div' + str(i)
        question_hold = net_hold.find_element_by_id(q_id)

        t_as = imp_data[i]  # 第i题的标准答案

        try:  # 判断是否为多选
            q_type = question_hold.find_element_by_class_name('qtypetip').get_attribute('textContent')
            q_type = re.sub(r'[^\u4e00-\u9fa5]', '', q_type)
            if q_type == '':
                raise Exception("抛出一个异常")
        except Exception:
            q_type = '单选题'
        print(q_id, q_type)

        q_ui = question_hold.find_element_by_xpath('.//ul')
        list_li = q_ui.find_elements_by_xpath('./li')
        li_len = list_li.__len__()  # 获得问题个数

        if q_type == '多选题':
            asw_list = mul_as(li_len, t_as)
            for li_i in range(1, li_len + 1):
                if asw_list[li_i - 1] == 1:
                    q_as_id = './/li[{}]'.format(li_i)
                    # '/ul/li[1]'
                    q_as_hold = question_hold.find_element_by_xpath(q_as_id)
                    q_as_hold.click()
                    time.sleep(0.01)
            del asw_list

        elif q_type == '单选题':
            asw_o = sig_as(li_len, t_as[0], i)
            q_as_id = './/li[{}]'.format(asw_o)
            print()
            q_as_hold = question_hold.find_element_by_xpath(q_as_id)
            q_as_hold.click()
            del asw_o
        del question_hold
        del q_ui
        print('结束...')
        time.sleep(0.5 * random.random())
    time.sleep(0.5)
    sump_hold = net_hold.find_element_by_xpath('//*[@id="submit_table"]/tbody/tr/td[1]')
    sump_hold.click()
    time.sleep(3)
    net_hold.quit()








