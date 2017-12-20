# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='crawling',
    version='1.0',
    description='爬虫demo',
    py_modules=['com'],
    packages=['com.crawling.config', 'com.crawling.database', 'com.crawling.domain', 'com.crawling.mongo', 'com.crawling.spider', 'com.crawling.utils'],
    install_requires=['bs4', 'selenium', 'pymongo', 'pymysql', 'configparser']
)
