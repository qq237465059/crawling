# -*- coding: UTF-8 -*-

from com.crawling.spider import url_Manage
from com.crawling.spider import html_DownLoad
from com.crawling.spider import html_Perser
from com.crawling.spider import html_Output
from com.crawling.database.SqlHelper import SqlHelper
import time

import sys
reload(sys)
sys.setdefaultencoding('utf8')


class RunSpider:
    def __init__(self):
        # 初始化URL管理器
        self.urls = url_Manage.UrlManage()
        # 初始化HTML下载器
        self.download = html_DownLoad.HtmlDownLoad()
        # 初始化HTML解析器
        self.parser = html_Perser.HtmlPerser()
        # 初始化HTML输出器
        self.output = html_Output.HtmlOutPut()
        # 初始化db
        self.db = SqlHelper()

    def run(self, root_url):
        try:
            # 下载首页
            html_content = self.download.DownLoad(root_url)
            # 调用解析器解析分类，获取URL
            new_data = self.parser.getAllType(root_url, html_content)
            # 定义一个变量来记录当前的是第几个URL
            count = 1
            for type in new_data:
                type_html = self.download.DownLoad(type["url"])
                typeName = type["type"]
                data, urls = self.parser.findBookByType(type_html, typeName)
                # todo 将该分类的书本信息写入数据库
                for map in data:
                    if int(self.db.sqlQuery("select count(1) from book_info where bookName='%s'" % map["bookName"])[0][0]) < 1:
                        self.db.insertByTable("book_info", map)
                # 将获取到的该分类的数据添加到URL管理器中
                self.urls.add_new_urls(urls)
                while self.urls.has_new_url():
                    # 为了防止URL不能访问,所以可以把执行放到Try里面执行
                    try:
                        # 获取新URL
                        new_book_url = self.urls.get_new_url()
                        # 输出提示这是第几个URL
                        print("这是第%d个URL,地址为:%s" % (count, new_book_url))
                        # 执行HTML下载器
                        book_html_content = self.download.DownLoad(new_book_url)
                        # todo 获取书名并在数据库中匹配并获取书籍ID
                        bookName = self.parser.getBookName(book_html_content)
                        bookId = int(self.db.sqlQuery("select id from book_info where bookName='%s' " % (bookName))[0][0])
                        # 获取第一章
                        one_url = self.parser.getBookOneUrl(book_html_content)
                        one_url = root_url + one_url
                        # 获取最后一章
                        chapter_url = self.db.sqlQuery("select url from book_article where bookId = %d order by id desc limit 1 " % bookId)
                        if len(chapter_url) > 0:
                            one_url = chapter_url[0][0]
                        # 拿到页面数据
                        one_html_content = self.download.DownLoad(one_url)
                        self.getBookByOne(one_html_content, bookId)

                    # 如果没有URL,那么就在控制台打印出
                    except Exception as e:
                        print(e)
        except Exception as t:
            print(t)
        # 关闭浏览器
        self.download.closeBrowser()

    def getBookByOne(self, one_html_content, bookId):
        try:
            while 1:
                # 获取 “下一章” 按钮
                driver = self.download.getBrowser()
                print("当前链接为：" + driver.current_url)
                nextBtn = driver.find_element("link text", "下一章")
                # 解析网页
                chapter = self.parser.addBookByContent(one_html_content)
                if chapter is not None:
                    chapter["bookId"] = int(bookId)
                    chapter["url"] = driver.current_url
                    self.db.insertByTable("book_article", chapter)
                nextBtn.click()
                # time.sleep(1)
                print(driver.title)
                one_html_content = driver.page_source
        except Exception as e:
            return
        return

