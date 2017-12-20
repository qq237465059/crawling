# -*- coding: UTF-8 -*-

class Article:
    """ 文章（每一张内容） """

    def __init__(self, bookId, chapter, title, content, url):
        self.bookId = bookId  # 书号
        self.chapter = chapter  # 章节
        self.title = title  # 标题
        self.content = content  # 内容
        self.url = url  # 地址
