# -*- coding:UTF-8 -*-
"""
Html解析器
@author: HY
"""
import re
from bs4 import BeautifulSoup
from com.crawling.spider.html_DownLoad import HtmlDownLoad

class HtmlPerser(object):

    # url补全
    def urljoin(self, page_url, new_url):
        new_url = new_url.replace('\.\./', ' ')
        new_url = re.sub('\.\./', '', new_url, re.M)
        page_url = page_url.split('/html')
        print(page_url[0] + '/')
        #         path= page_url[0]+'/'+new_url
        path = '%s/%s' % (page_url[0], new_url)
        return path

    # 执行解析
    def Parse(self, page_url, html_content):
        # 判断是否为空
        if page_url is None or html_content is None:
            return
            # 定义一个数组,用来存放数据字典
        data = []
        print(html_content)
        # 匹配最终的正则
        #         rega=u'<a.*?id=pageLink.*?>(.*?)</a>'
        rega = u'<a.*?id=pageLink.*?>(.*?)</a>'
        regpdf = u'><a.*?href=(.*?)\.pdf>.*?<img.*?>.*?</a>'
        try:
            # 匹配PDF文件
            contPDF = re.findall(regpdf, html_content, re.M)
            # 匹配名字
            contA = re.findall(rega, html_content, re.S)
            i = len(contPDF)
            j = 0
            # 循环获取所需要的数据,并存放进字典中
            while j < i:
                res_data = dict()
                new_url = self.urljoin(page_url, contPDF[j])
                res_data['url'] = new_url + ".pdf"
                print(res_data['url'])
                res_data['title'] = contA[j].encode('utf-8')
                print(res_data['title'])
                # 将字典追加进data数组中
                data.append(res_data)
                j = j + 1
        except:
            print('没有')
        # 返回获取出来的数据
        return data

    def getAllType(self, root_url,root_html):
        data = []
        soup = BeautifulSoup(root_html, "html.parser")
        tr = soup.select('div.nav')
        liList = soup.select('div.nav li a')
        for li in liList:
            if li.text == "网站首页":
                continue
            print(li.get("href"))
            type["name"] = li.text
            type["url"] = li.get("href")
            data.append(type)
        print(data)
        return type
