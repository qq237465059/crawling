# -*- coding: UTF-8 -*-
"""
URL管理器
操作URL的传递
@author: HY
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class UrlManage(object):
    # 在构造函数中初始化URL存储器
    def __init__(self):
        # 初始化一个用于存储未爬取的URL
        self.new_urls = set()
        # 初始化一个用于存放爬取过的URL
        self.old_urls = set()

    # 向URL管理器中添加一个URL
    def add_new_url(self, url):
        # 如果URL为空,则不添加
        if url is None:
            return
        # 如果URL不在未爬取的URL列表里面,也不在爬取过的URL列表里面
        if url not in self.new_urls and url not in self.old_urls:
            # 就将他添加到URL管理器中
            self.new_urls.add(url)

    # 判断是否有没有爬取过的URL
    def has_new_url(self):
        # 如果有新的URL,那么就返回true
        return len(self.new_urls) != 0

    # 获取一个没有爬取过的URL
    def get_new_url(self):
        # 获取出一个URL,pop方法会调取出一个URL,并在原数组中移除这个URL
        new_url = self.new_urls.pop()
        # 将URL添加到已经爬取过的列表中
        self.old_urls.add(new_url)
        # 返回获取到的URL
        return new_url

    # 向URL管理器中添加一堆URL
    def add_new_urls(self, urls):
        # 如果URL不为空,或者里面没有数据了
        if urls is None or len(urls) == 0:
            return
        # 循环添加URL
        for url in urls:
            # 就将他添加到URL管理器中
            self.new_urls.add(url)
