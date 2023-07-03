import requests
from bs4 import BeautifulSoup
import re
import sys

print("请输入豆瓣书籍id：")

page_id = ""
token = ""

book_id = str(input())
douban_url = "https://book.douban.com/subject/" + book_id

# 请求头------------------------------------------------------------------------------------------------------------
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 '
                  'Safari/537.36'}

data = requests.get(douban_url, headers=headers)
result = data.text
soup = BeautifulSoup(result, "html.parser")

# 开始爬取网页上的数据-------------------------------------------------------------------------------------------------

name = soup.select('#wrapper > h1 > span')[0]
author = soup.select('#info > span:nth-child(1) > a')[0]

出版社= soup.select('#info > a:nth-child(4)')[0]
丛书 = soup.select('#info > a:nth-child(15)')[0]

print(name)
