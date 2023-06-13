from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

# 1.创建一个浏览器对象,executable_path指定当前浏览器的驱动程序
# 注意：我当前是mac系统，驱动程序也是mac版本的，如果是window系统注意更换驱动
bro = webdriver.Chrome()
# 2.浏览器的请求发送
bro.get('https://www.jd.com/')
# 3.标签定位:调用find系列的函数进行标签定位
search_box = bro.find_element(By.XPATH, '//*[@id="key"]')
# 4.节点交互
search_box.send_keys('mac pro m1')
# 向指定标签中录入内容
sleep(2)
btn = bro.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button')
btn.click()  # 点击按钮
sleep(2)
# js注入
bro.execute_script('document.documentElement.scrollTo(0,2000)')
sleep(5)
# 关闭浏览器
bro.quit()
