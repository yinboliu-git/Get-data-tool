#!/usr/bin/python3
#-*- codeing = utf-8 -*-
#@Time : 1/9/2021 4:09 PM
#@Author : Liu
#@File : one.py
#@Software : PyCharm
import re

s = '1\nabc@126.com'
rs = r'^1\\n(\w+)@(126|163|gmail)\.(com|cn|net)$'
out = re.match(r'^1\n(\w+)@(126|163|gmail)\.(com|cn|net)$',s)
print(out.group())
print(rs)

s1 = '<h1><h2>abc刘</h2></h1>'
rs = r'^(<(?P<key1>h1)>)<(?P<key_name>h2)>(.*)</(?P=key_name)>(</(?P=key1)>)$'

out = re.match(rs,s1)
print(out.group())

import re
a = 'python php Py liu py'

c = re.match(r'\W*py\W*',a)
print(c.group())


def pl(s):
    print(s.group())
    return s.group()+'hao'


d = re.search('py$',a)
print(d)

c = re.sub(r'\bpy\b',pl,a)

print(c)

