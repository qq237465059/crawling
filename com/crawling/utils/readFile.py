# -*- coding: UTF-8 -*-

import configparser
import os
import sys

class ReadFile:

    @staticmethod
    def readFile():
        config = {}
        file_path = sys.path[1]
        print(file_path)
        os.chdir(file_path)
        cf = configparser.ConfigParser()
        cf.read("config.conf")
        opts = cf.items("mongodb")  # 获取mongodb配置
        config["mongodb"] = opts
        opts = cf.items("database")  # 获取mongodb配置
        config["database"] = opts
        return config


