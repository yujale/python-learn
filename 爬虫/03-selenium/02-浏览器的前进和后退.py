from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')

browser.back()
time.sleep(2)
browser.forward()
time.sleep(2)

browser.close()
