# -*- coding: UTF-8 -*-

from com.crawling.dao.runSpider import RunSpider

import sys
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    s = RunSpider()
    url = "http://www.biquge.com.tw/"
    s.run(url)