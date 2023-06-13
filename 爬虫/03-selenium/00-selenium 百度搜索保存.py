from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
# driver = webdriver.Chrome(r'./chromedriver.exe')
driver = webdriver.Chrome()
# 用get打开百度页面
driver.get("http://www.baidu.com")
# 查找页面的“设置”选项，并进行点击
driver.find_element(By.ID, "s-usersetting-top").click()
sleep(2)
driver.find_element(By.LINK_TEXT, "搜索设置").click()
# # 打开设置后找到“搜索设置”选项，设置为每页显示50条
sleep(2)

# 选中每页显示50条
driver.find_element(By.XPATH, '//*[@id="nr_3"]').click()
sleep(2)

# 点击保存设置
driver.find_element(By.XPATH, '//*[@id="se-setting-7"]/a[2]').click()
sleep(2)

# 处理弹出的警告页面   确定accept() 和 取消dismiss()
alert = driver.switch_to.alert
alert.accept()
sleep(2)
# 找到百度的输入框，并输入 美女
driver.find_element(By.ID, 'kw').send_keys('美女')
sleep(2)
# 点击搜索按钮
driver.find_element(By.ID, 'su').click()
sleep(2)
# 在打开的页面中找到“Selenium - 开源中国社区”，并打开这个页面
driver.find_element(By.XPATH, '//*[@id="1"]/div/h3/a').click()
sleep(3)

# 关闭浏览器
driver.quit()
