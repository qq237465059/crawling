# -*- coding:UTF-8 -*-
"""
Html输出器
输出爬取到的数据
@author: HY
"""

class HtmlOutPut(object):
    def __init__(self):
        # 初始化一个用于存放数据的
        self.datas = []

    # 用于收集数据
    def collect_data(self, data):
        if data is None:
            print("空")
            return
        # 将数据存放
        self.datas.append(data)

    # 用于将收集到的数据放到HTml页面中
    def output_html(self, typeid, id):

        sql = u"insert into `new`(typeid,newname,pdfpath,newDate) values"
        strsql = u""
        for data in self.datas:
            for da in data:
                strsql = strsql + u"(%s,'%s','%s',%s)," % (
                typeid, da['title'].encode('utf-8'), da['url'].encode('utf-8'), id)
        sql = sql + strsql[:-1]
        print(sql)
        print("-------------------------------------")
        # mysqldb=Mysqldb.putMySqlDb.putMySqlDb()
        # mysqldb.addNew(sql)
