from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 '
    'Safari/537.36')

web = Chrome(options=chrome_options)
# Selenium在打开任何页面之前，先运行这个Js文件。
with open('./stealth.min.js') as f:
    js = f.read()
# 进行js注入，绕过检测
web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": js
})

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
for i in range(5):
    action.move_by_offset(50, 0).perform()
    sleep(0.5)
sleep(3)
web.close()