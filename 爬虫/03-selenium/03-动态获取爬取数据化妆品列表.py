from selenium import webdriver
import time
from lxml.html import etree

from selenium.webdriver.common.by import By

url = 'https://www.nmpa.gov.cn/datasearch/search-result.html'

bro = webdriver.Chrome()
bro.get(url)
time.sleep(2)
result = bro.page_source
print(result)

# 将前5页的页面源码数据存储到该列表中
all_page_text_list = [result]
for i in range(4):
    # 点击下一页
    next_page_btn = bro.find_element(By.XPATH, '//*[@id="pageIto_next"]')

    next_page_btn.click()
    time.sleep(1)
    all_page_text_list.append(bro.page_source)

for page_text in all_page_text_list:
    # 解析数据
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="gzlist"]/li')
    for li in li_list:
        title = li.xpath('./dl/@title')[0]
        print(title)

time.sleep(2)
bro.quit()
