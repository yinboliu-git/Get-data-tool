import json
import pandas as pd
import  requests
from lxml import etree
from time import sleep

def get_commit(url,name):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "Refer":"https://www.zhihu.com/"
    }
    resp = requests.get(url,headers=headers)
    content = resp.content.decode('utf-8')
    res = json.loads(content)
    print(res['data'])
    data = res['data']
    list_commit = []
    for item in data:
        print(item['content'])
        list_commit.append([item['id'],item['content']])
        sleep(0.3)
        print([item['id'],"*"*30])
        # list_commit.append((item['id'],"*"*30))

    commit_data = pd.DataFrame(list_commit)
    commit_data.to_csv('./cmmit_data'+name+'.txt', header=None)


def get_bili_com(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Cookie": "",
        'referer': 'https://www.bilibili.com/'}
    comments = []
    # original_url = "https://api.bilibili.com/x/v2/reply?jsonp=jsonp&type=1&oid=585286365&sort=2&pn="
    original_url = url

    for page in range(1, 39):  # 页码这里就简单处理了
        url = original_url + str(page)

        try:
            html = requests.get(url, headers=header)
            data = html.json()
            if data['data']['replies']:
                for one_data in data['data']['replies']:
                    comments.append(one_data['content']['message'])
                    print(comments[-1])
                    print(url)

        except Exception as err:
            print(url)
            print(err)


if __name__ == '__main__':
    url_ = []

    url_.append("https://www.zhihu.com/api/v4/answers/2195638860/root_comments?order=normal&limit=20&offset=0&status=open")
    url_.append("https://www.zhihu.com/api/v4/answers/43275451/root_comments?order=normal&limit=20&offset=0&status=open")

    url_list = url_
    for name_id,url in enumerate(url_list):
        get_commit(url,str(name_id))

    url_ = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&type=1&oid=668282704&sort=2&pn='
    get_bili_com(url_)

    print('爬取已经全部完成....')