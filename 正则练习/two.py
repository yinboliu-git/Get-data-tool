#!/usr/bin/python3
#-*- codeing = utf-8 -*-
#@Time : 1/9/2021 5:38 PM
#@Author : Liu
#@File : two.py
#@Software : PyCharm

import re

a = '''wwww
 asdfhellopass:
    worldaf
    wwww
    mmmm
    '''
b = re.findall('hello(.*?)world',a)
c = re.findall('hello(.*?)world',a,re.S)
print(b)
print(c)

d1 = re.findall('^\w+?',a)
d2 = re.findall('^\w+',a,re.S)
d3 = re.findall('^\w+',a,re.M)

print(d1)
print(d2)
print(d3)


s = 'e12 \ne23ww \ne56'

d1 = re.findall('^\w+?',s)
d2 = re.findall('\w(.*)',s,re.S)
d3 = re.findall('\w(.*)',s,re.M)

print(d1)
print(d2)
print(d3)
