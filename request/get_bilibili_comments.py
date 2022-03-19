#!/usr/bin/python3
#-*- codeing = utf-8 -*-

import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Cookie": "",
    'referer': 'https://www.bilibili.com/'}
comments = []
# original_url = "https://api.bilibili.com/x/v2/reply?jsonp=jsonp&type=1&oid=585286365&sort=2&pn="
original_url = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&type=1&oid=39807944&sort=2&pn='

for page in range(1, 39):  # 页码这里就简单处理了
    url = original_url + str(page)
    print(url)
    try:
        html = requests.get(url, headers=header)
        data = html.json()
        if data['data']['replies']:
            for one_data in data['data']['replies']:
                comments.append(one_data['content']['message'])
    except Exception as err:
        print(url)
        print(err)

print(comments)