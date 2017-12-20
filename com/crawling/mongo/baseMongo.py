# -*- coding: UTF-8 -*-

from com.crawling.config.readConfig import ReadConfig

class BaseMongo:
    def __init__(self):
        config = ReadConfig()
        self.__db = config.getMongodb()["log"]

    def add(self, map):
        return self.__db.insert(map)

    def get(self, map):
        return self.__db.find_one(map)

    def update(self, map):
        return self.__db.save(map)

    def batchUpdate(self, wheres, map):
        return self.__db.update(wheres, {"$set": map})

    def deleteById(self, _id):
        return self.__db.remove(_id)

    def deleteAll(self):
        return self.__db.remove()

    def deleteByMap(self, map):
        return self.__db.remove(map)

