# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='crawling',
    version='1.0',
    description='爬虫demo',
    py_modules=['com.crawling.dao.runSpider'],
    packages=['com', 'com.crawling', 'com.crawling.config', 'com.crawling.database', 'com.crawling.domain', 'com.crawling.mongo', 'com.crawling.spider', 'com.crawling.utils'],
    package_data={'': ['config.conf']}
)
