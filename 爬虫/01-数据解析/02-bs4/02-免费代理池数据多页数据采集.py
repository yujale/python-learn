from bs4 import BeautifulSoup
import requests
import time
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/97.0.4692.71 Safari/537.36'
}

url = "https://www.kuaidaili.com/free/inha/%d/"
for page in range(1,11):
    print("---------正在爬取第 % d页的数据！----------- " % page)
    # format用来格式化字符串的（不可以修改url这个字符串本身）
    new_url = format(url % page)
    result = requests.get(url=new_url, headers=headers).text
    time.sleep(1)
    soup = BeautifulSoup(result, 'html.parser')
    trs = soup.select('tbody > tr')

    for tr in trs:
        t1 = tr.findAll('td')[0]
        t2 = tr.findAll('td')[1]
        ip = t1.string
        port = t2.string
        print("ip 为 %s,端口为 %s" % (ip, port))