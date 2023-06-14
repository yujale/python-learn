from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
# 获取cookie
cookies = browser.get_cookies()
# 解析cookie
dic = {}
for cookie in cookies:
    key = cookie['name']
    value = cookie['value']
    dic[key] = value
print(dic)  # 在爬虫中可以使用的cookie
browser.close()
