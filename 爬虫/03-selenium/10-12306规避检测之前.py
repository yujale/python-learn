from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from time import sleep

from selenium.webdriver.common.by import By

web = Chrome()

web.get("https://kyfw.12306.cn/otn/resources/login.html")
sleep(2)
web.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[1]/a').click()
web.find_element(By.XPATH, '//*[@id="J-userName"]').send_keys("hehehe@126.com")
sleep(1)
web.find_element(By.XPATH, '//*[@id="J-password"]').send_keys("111111")
sleep(1)
web.find_element(By.XPATH, '//*[@id="J-login"]').click()
sleep(3)
action = ActionChains(web)
# 找到滑块
btn = web.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')
action.click_and_hold(btn)
for i in range(6):
    action.move_by_offset(50, 0).perform()
    sleep(0.5)
sleep(3)
web.close()
