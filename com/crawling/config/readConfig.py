# -*- coding: UTF-8 -*-

import pymongo
import pymysql
from com.crawling.utils.readFile import ReadFile

class ReadConfig:
    """ 　读取文件配置信息 """

    __config = ReadFile.readFile()

    def __init__(self):
        print("初始化")
        self.__mongodbConn = None
        self.__databaseConn = None

    "获取mongodb的连接"
    def getMongodb(self, db=None):
        if self.__mongodbConn is None:
            mongodb = self.__config.get("mongodb")
            url = mongodb[0][1]
            port = mongodb[1][1]
            if db is None:
                db = mongodb[2][1]
            self.__mongodbConn = pymongo.MongoClient(url, int(port))[db]
        print("连接Mongodb成功")
        return self.__mongodbConn

    def getDatabase(self):
        if self.__databaseConn is None:
            database = self.__config.get("database")
            url = str(database[0][1])
            port = int(database[1][1])
            name = str(database[2][1])
            user = str(database[3][1])
            password = str(database[4][1])
            self.__databaseConn = pymysql.connect(host=url, port=port, user=user, passwd=password, db=name, charset='utf8')
        print("连接数据库成功")
        return self.__databaseConn


if __name__ == "__main__":
    print("开始")
    config = ReadConfig()
    db = config.getDatabase().cursor()
    db.execute("select * from book_info")
    selectResultList = db.fetchall()
    for i in range(len(selectResultList)):
        print(selectResultList[i])
