from lxml import etree
import requests
import verificationCode

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
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
# 模拟登录
url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data = {
    "__VIEWSTATE": "opfVI7oolwkr7MLRVzsNSMASqLRUuO1dg5ZP5EIRa4FyM+mOYKEs6KWEKQKaba2ulLoZQIaLFiKK4mr5K3ci1v8ua28wtcRtabKWjOtJtU/i2etH+zSduegTMcg=",
    "__VIEWSTATEGENERATOR": "C93BE1AE",
    "from": "http://so.gushiwen.cn/user/collect.aspx",
    "email": "15027900535",
    "pwd": "bobo@15027900535",
    "code": result,
    "denglu": "登录"
}
# 获取了登录成功后的页面源码数据
login_page_text = requests.post(url=url, headers=headers, data=data).text
with open('wushiwen.html', 'w') as fp:
    fp.write(login_page_text)
