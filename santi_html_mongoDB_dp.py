# -*- coding: utf-8 -*-
import time
import random
import requests
from lxml import etree
from pymongo import MongoClient      #非关系型数据库mongoDB版本引入

client = MongoClient("127.0.0.1",27017)        #实例化一个MongoClient，默认端口号是27017,相当于建立好一个连接
# db = client[DB]                              #连接到数据库，名为db
# collection = db[COLLECTION]                  #连接到集合，相当于关系型数据库里的表
collection = client["douban"]["santi"]         #创建数据库douban及集合santi

def get_url_list():                 #1.url的规律，构造一堆url出来
    url_list = []
    url_temp = "https://book.douban.com/subject/3259440/comments/hot?p={}"                      #书籍作品短评论页面地址
    for i in range(1,100):
        url = url_temp.format(i)
        url_list.append(url)
    return url_list

def parse_url(url):                #2.遍历url_list,发送请求，获取响应
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3298.4 Safari/537.36"}
    cookies = {    }                                                                            #cookies需要填写
    r = requests.get(url,headers=headers,cookies=cookies,timeout=10)
    html_str = r.content.decode()
    html = etree.HTML(html_str)     #使用etree处理得到非结构element数据对象，能够使用xpath方法
    return html

def get_content_list(html):         #3.提取数据
    li_list = html.xpath("//div[@id='comments']/ul/li")
    content_list = []
    for li in li_list:
        comment_temp = {}
        comment_temp["content"] = li.xpath("./div[@class='comment']/p/text()")
        content_list.append(comment_temp)
    return content_list

def save_content_list(content_list):                      #4.保存数据
    for contents in content_list:
        print(contents)
        print("*"*100)
        collection.insert(contents)


def run():
    #1.url的规律，构造一堆url出来
    url_list = get_url_list()
    #2.遍历url_list,发送请求，获取响应
    for url in url_list:
        html = parse_url(url)
        #3.提取数据
        content_list = get_content_list(html)
        #4.保存数据
        save_content_list(content_list)
        #5.设置随机休眠防止IP被封
        time.sleep(3 + float(random.randint(1, 20)) / 20)    #设置休眠时间间隔，防止很快被反爬程序封杀

if __name__ == '__main__':
    run()