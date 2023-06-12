from lxml import etree
import requests
import verificationCode

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 Safari/537.36'
}
# 将验证码图片请求后保存到本地
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
page_text = requests.get(url=login_url, headers=headers).text
tree = etree.HTML(page_text)
img_src = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]
code_data = requests.get(url=img_src, headers=headers).content
with open('./code.jpg', 'wb') as fp:
    fp.write(code_data)

# 识别验证码图片内容
result = verificationCode.getImgCodeText('./code.jpg', 3)
print(result)
