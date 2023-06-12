from bs4 import BeautifulSoup
import requests
import time
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Safari/537.36'
}
# 构建一个代理池
proxy_url = 'http://webapi.http.zhimacangku.com/getip?num=20&type=2&pro=&city=0&yys=0&port=11&pack=320953&ts=0&ys=0' \
            '&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
json_data = requests.get(url=proxy_url, headers=headers).json()
json_list = json_data['data']
proxy_list = []  # 代理池,每次请求，可以随机从代理池中选择一个代理来用
for dic in json_list:
    ip = dic['ip']
    port = dic['port']
    n_dic = {
        'https': ip + ':' + str(port)  # {'https':'111.1.1.1:1234'}
    }
    proxy_list.append(n_dic)

# 爬取多页
# 1.创建一个通用的url(可以变换成任意页码的url)
url = 'https://www.kuaidaili.com/free/inha/%d/'
# 2.通过循环以此生成不同页码的url
for page in range(1, 4):
    print('----------正在爬取第%d页的数据！-----------' % page)
    # format用来格式化字符串的（不可以修改url这个字符串本身）
    new_url = format(url % page)
    # 循环发送每一页的请求
    # 注意：get方法是一个阻塞方法！
    page_text = requests.get(url=new_url, headers=headers, proxies=random.choice(proxy_list)).text
    time.sleep(1)
    soup = BeautifulSoup(page_text, 'lxml')
    trs = soup.select('tbody > tr')
    for tr in trs:
        t1 = tr.findAll('td')[0]
        t2 = tr.findAll('td')[1]
        ip = t1.string
        port = t2.string
        print(ip, port)
