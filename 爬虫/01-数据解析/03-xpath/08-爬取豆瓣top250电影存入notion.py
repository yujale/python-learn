from itertools import cycle

import requests
from lxml import etree
import re
import time

page_id = ""
token = ""

douban_top_url = "https://movie.douban.com/top250?start=%d&filter="
user_agents = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
]

index = 0
headers = {
    'User-Agent': ''
}


def get_movie_list(url):
    headers['User-Agent'] = user_agents[0]
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    tree = etree.HTML(page_text)
    movie_list = tree.xpath('//*[@id="content"]/div/div[1]/ol/li')
    return movie_list


def get_movie_details(movie):
    movie_url = movie.xpath('./div/div[2]/div[1]/a/@href')[0]
    movie_name = movie.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
    print(f"片名: {movie_name}")
    print(f"URL: {movie_url}")
    time.sleep(2)
    user_agents_cycle = cycle(user_agents)
    headers['User-Agent'] = next(user_agents_cycle)
    movie_detail_response = requests.get(url=movie_url, headers=headers)
    movie_detail_response.encoding = 'utf-8'
    movie_detail_text = movie_detail_response.text
    movie_tree = etree.HTML(movie_detail_text)
    print(movie_tree)
    if movie_tree is None:
        return None
    # 开始爬取网页上的数据-------------------------------------------------------------------------------------------------

    # 中文片名
    name = "".join(movie_tree.xpath("/html/head/title/text()"))
    name = (name.replace("(豆瓣)", "")).strip()  # 去掉电影名称中多余的字
    print("搜索中……")

    # 原文片名
    native = "".join(movie_tree.xpath("//*[@id='mainpic']/a/img/@alt"))

    # 海报
    post = "".join(movie_tree.xpath("//*[@id='mainpic']/a/img/@src"))

    # 导演
    director = ",".join(movie_tree.xpath("//*[@id='info']/span[1]/span[2]/a/text()"))

    # 编剧
    writer = ",".join(movie_tree.xpath("//*[@id='info']/span[2]/span[2]/a/text()"))

    # 演员
    actor = ",".join(movie_tree.xpath("//meta[@property='video:actor']/@content"))

    # 类型
    genre = movie_tree.xpath("//span[./text()='类型:']/following::span[@property='v:genre']/text()")
    genre += [" ", " ", " ", " "]  # 加上几个空格元素增加列表长度，避免提交的时候溢出

    # 地区
    region = ",".join(movie_tree.xpath("//span[./text()='制片国家/地区:']/following::text()[1]"))
    region = region.split("/")  # 分割为列表
    region = [i.strip() for i in region]  # 去除空格
    region += [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]  # 增加列表长度

    # 语言
    language = ",".join(movie_tree.xpath("//span[./text()='语言:']/following::text()[1]"))
    language = language.split("/")  # 分割为列表
    language = [i.strip() for i in language]  # 去除空格
    language += [" ", " ", " ", " "]  # 增加列表长度

    # 时长
    duration = ",".join(movie_tree.xpath("//span[@property='v:runtime']/text()"))

    # 年份
    year = "".join(movie_tree.xpath("//span[@class='year']/text()"))
    year = re.findall(r'-?\d+\.?\d*', year)[0]  # 提取纯数字
    year = int(year)  # 数据类型转换成整数

    # 评分
    rate = "".join(movie_tree.xpath("//*[@id='interest_sectl']/div[1]/div[2]/strong/text()"))
    rate = rate.strip()
    rate = float(rate)
    print(f"已完成数据爬取: {name} {year}")
    return {
        "name": name, "native": native, "post": post, "director": director, "writer": writer, "actor": actor,
        "region": region, "language": language, "duration": duration, "year": year, "rate": rate, "genre": genre,
        "movie_url": movie_url
    }


def import_to_notion(movie_info):
    # 导入到Notion的操作
    # 开始向notion请求-----------------------------------------------------------------------------------------------------

    url = "https://api.notion.com/v1/pages"

    p = {"parent": {
        "type": "database_id",
        "database_id": page_id
    },
        "properties": {
            "片名": {"title": [{"type": "text", "text": {"content": movie_info['name']}}]},
            "原名": {"rich_text": [{"type": "text", "text": {"content": movie_info['native']}}]},
            "评分": {"number": movie_info['rate']},
            # "评分人数": {"number": raters},
            "上映年份": {"number": movie_info['year']},
            # "IMDb": {"rich_text": [{"type": "text", "text": {"content": imdb}}]},
            "导演": {"rich_text": [{"type": "text", "text": {"content": movie_info['director']}}]},
            "主演": {"rich_text": [{"type": "text", "text": {"content": movie_info['actor']}}]},
            "类型": {
                "multi_select": [{"name": movie_info['genre'][0]}, {"name": movie_info['genre'][1]},
                                 {"name": movie_info['genre'][2]}, {"name": movie_info['genre'][3]}]},
            "片长": {"rich_text": [{"type": "text", "text": {"content": movie_info['duration']}}]},
            "国家/地区": {
                "multi_select": [{"name": movie_info['region'][0]}, {"name": movie_info['region'][1]},
                                 {"name": movie_info['region'][2]}, {"name": movie_info['region'][3]},
                                 {"name": movie_info['region'][4]}, {"name": movie_info['region'][5]},
                                 {"name": movie_info['region'][6]},
                                 {"name": movie_info['region'][7]}]},
            "语言": {"multi_select": [{"name": movie_info['language'][0]}, {"name": movie_info['language'][1]},
                                      {"name": movie_info['language'][2]},
                                      {"name": movie_info['language'][3]}]},
            # "榜单": {"select": {"name": rank_li}},
            # "排名": {"number": rank_no},
            "编剧": {"rich_text": [{"type": "text", "text": {"content": movie_info['writer']}}]},
            "封面": {"files": [{"name": "封面", "type": "external", "external": {"url": movie_info['post']}}]},
            "豆瓣": {"url": movie_info['movie_url']}
        }
    }
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }

    r = requests.post(url, json=p, headers=headers)

    # 接受返回数据---------------------------------------------------------------------------------------------------------

    if r.status_code == 200:
        print("导入Notion成功！")
        time.sleep(2)
    else:
        print("导入Notion失败！")
        print(r.text)  # 返回讯息中可以看到错误提示

        # 用get请求来检测是不是连接上的错误
        print("输入000检查数据库通讯）")
        check = str(input())
        if check == "000":
            url = "https://api.notion.com/v1/databases/" + page_id
            headers = {
                "Accept": "application/json",
                "Notion-Version": "2022-06-28",
                "Authorization": "Bearer " + token
            }

            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                print("数据库通讯正常，请检查表格项目是否匹配")
            else:
                print("通讯错误，请检查integration机器人是否正确设置")

            print(r.text)


def crawl_movies():
    user_agents_cycle = cycle(user_agents)
    for page in range(75, 250, 25):
        url = douban_top_url % page
        movie_list = get_movie_list(url)
        for movie in movie_list:
            movie_info = get_movie_details(movie)
            if movie_info is None:
                continue
            import_to_notion(movie_info)
            time.sleep(2)


crawl_movies()
