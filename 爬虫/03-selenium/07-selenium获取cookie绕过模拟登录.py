from selenium.webdriver import Chrome
import time
import json
import requests

from selenium.webdriver.common.by import By

web = Chrome()
web.get('https://www.17k.com/')
time.sleep(3)

web.find_element(By.XPATH, '//*[@id="header_login_user"]/a[1]').click()
iframe = web.find_element(By.XPATH, '/html/body/div[20]/div/div[1]/iframe')
web.switch_to.frame(iframe)

web.find_element(By.XPATH, '/html/body/form/dl/dd[2]/input').send_keys("15027900535")
web.find_element(By.XPATH, '/html/body/form/dl/dd[3]/input').send_keys("bobo328410948")
web.find_element(By.XPATH, '//*[@id="protocol"]').click()
web.find_element(By.XPATH, '/html/body/form/dl/dd[5]/input').click()

time.sleep(3)
cookies = web.get_cookies()
print(cookies)

with open('cookies.txt', mode='w', encoding='utf-8') as f:
    f.write(json.dumps(cookies))

# 组装cookie字典, 直接给requests用
dic = {}
for cook in cookies:
    dic[cook["name"]] = cook["value"]
# 衔接. 把cookie直接怼进去
# 访问的书架（获取书架内容）
url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
headers = {
    "cookie": dic
}
resp = requests.get(url, cookies=dic)
print(resp.text)

web.close()
