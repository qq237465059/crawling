﻿# -*- coding:UTF-8 -*-
"""
HTML下载器
下载HTML
@author: HY
"""
from selenium import webdriver
import time


class HtmlDownLoad(object):

    def __init__(self):
        self.driver = webdriver.PhantomJS(executable_path="E:\\phantomjs\\bin\\phantomjs.exe")

    # 实现页面的下载
    def DownLoad(self, url):
        if url is None:
            return None
        # 使用浏览器请求页面
        self.driver.get(url)
        # 获取整个加载后的网站
        # html = driver.find_element_by_tag_name("body")
        html = self.driver.page_source.encode()
        # 返回下载好的内容
        return html

    def getBrowser(self):
        return self.driver

    def closeBrowser(self):
        # 关闭浏览器
        if self.driver is None:
            self.driver.close()
