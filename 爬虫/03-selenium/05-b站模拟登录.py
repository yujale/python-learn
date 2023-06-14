from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
import verificationCode

chrome = webdriver.Chrome()

login_url = 'https://passport.bilibili.com/login'
chrome.get(url=login_url)

sleep(1)

user_box = chrome.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input')
user_box.send_keys('18371919563')
sleep(2)

password_box = chrome.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[3]/input')
password_box.send_keys('123456')
sleep(2)

login_btn = chrome.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]')
login_btn.click()
sleep(2)

code_tag = chrome.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[6]/div/div')
print(code_tag)
code_tag.screenshot('./code.png')  # 将验证码对话框截图保存

# 打码平台识别
result = verificationCode.getImgCodeText('./code.png', 27)
# result = '154,251|145,167'
print(result)
sleep(2)

result_list = result.split('|')
print(result_list)
# result_list == ['154,251','145,167']
for qos in result_list:
    print(qos)
    x = int(qos.split(',')[0])
    y = int(qos.split(',')[1])
    print(x)
    print(y)
    ActionChains(chrome).move_to_element_with_offset(code_tag, x, y).click().perform()
    sleep(2)

confirm_btn = chrome.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[6]/div/div/div[3]/a/div')
confirm_btn.click()
sleep(3)


chrome.quit()
