# from lxml import etree #如果这种方式报错，使用下面方式导入etree
from lxml.html import etree
fp = open('test.html','r')
#1.将本地存储好的文件中的数据加载到etree对象中进行数据解析
tree = etree.parse(fp)
#2.调用etree对象的xpath方法结合不同形式的xpath表达式进行标签定位和数据提取
#xpath返回的一定是列表，列表中存储的是定位到的标签对象
title_tag = tree.xpath('/html/head/title')
# title_tag = tree.xpath('/html//title')
# title_tag = tree.xpath('//head/title')
# title_tag = tree.xpath('//title') #推荐
#最左侧为/:表示必须从树的根标签（html标签）开始进行定位
#最左侧为//:可以从任意位置进行标签的相对位置定位
#非最左侧的/:表示一个层级
#非最左侧的//:表示多个层级
# tag = tree.xpath('//div') #定位所有的div标签

#属性定位：根据标签的属性定位标签
#//tagName[@attrName='attrValue']
# tag = tree.xpath('//div[@class='song']')#定位class属性值为song的div标签
# tag = tree.xpath('//a[@id='feng']')
# tag = tree.xpath('//div[@class='tang']/ul/li/a[@id='feng']')
#索引定位：索引是从1开始的
# tag = tree.xpath('//div[@class='tang']/ul/li[3]')#定位到第三个li标签
#获取定位到标签中的文本内容
    # /text()获取标签中直系的文本内容：返回的列表中只会有一个列表元素
    # //text()获取标签中所有的文本内容：通常返回列表中存在多个元素
# tag = tree.xpath('//div[@class='song']/p[3]/text()')
# tag = tree.xpath('//div[@class='song']//text()')
#获取定位到标签中的属性值://tag/@attrName
tag = tree.xpath('//img/@src')
print(tag)