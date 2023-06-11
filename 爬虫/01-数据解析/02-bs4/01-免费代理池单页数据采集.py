# https://www.kuaidaili.com/free

from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/97.0.4692.71 Safari/537.36'
}
url = 'https://www.kuaidaili.com/free'
result = requests.get(url=url,headers=headers).text
soup = BeautifulSoup(result,'html.parser')
trs = soup.select('tbody > tr')

for tr in trs:
    t1 = tr.findAll('td')[0]
    t2 = tr.findAll('td')[1]
    ip = t1.string
    port = t2.string
    print("ip 为 %s,端口为 %s" % (ip,port))
print("代理池 ip 和端口采集完成")
