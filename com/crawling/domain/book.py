# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Book:
    """ 书信息 """

    def __init__(self, bookName, author, source, type):
        self.bookName = bookName  # 书名
        self.author = author  # 作者
        self.source = source  # 来源平台
        self.type = type  # 分类
