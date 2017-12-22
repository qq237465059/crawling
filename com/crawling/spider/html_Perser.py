# -*- coding:UTF-8 -*-
"""
Html解析器
@author: HY
"""
import re
from bs4 import BeautifulSoup
from com.crawling.spider.html_DownLoad import HtmlDownLoad
import sys
reload(sys)
sys.setdefaultencoding('utf8')


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

    def getAllType(self, root_url, root_html):
        data = []
        soup = BeautifulSoup(root_html, "html.parser")
        tr = soup.select('div.nav')
        liList = soup.select('div.nav li a')
        for li in liList:
            if li.text == "网站首页":
                continue
            type = {}
            type["type"] = li.text
            type["url"] = root_url + li.get("href")
            data.append(type)
        return data

    def findBookByType(self, type_html, type):
        soup = BeautifulSoup(type_html, "html.parser")
        items = soup.select("div#hotcontent div.ll div.item")
        data = []
        urls = []
        for item in items:
            book = {}
            book["author"] = item.select_one(" dl dt span").text
            book["source"] = item.select_one(" dl dt a").get("href")
            book["bookName"] = item.select_one("div.image a img").get("alt")
            book["type"] = type
            data.append(book)
            urls.append(book["source"])

        lis = soup.select("div#newscontent li")
        for li in lis:
            book = {}
            book["author"] = li.select_one("span.s5").text
            book["source"] = li.select_one("span.s2 a").get("href")
            book["bookName"] = li.select_one("span.s2 a").text
            book["type"] = type
            data.append(book)
            urls.append(book["source"])
        return data, urls

    def findBookChapter(self, root_url, book_content, bookId):
        soup = BeautifulSoup(book_content, "html.parser")
        links = soup.select("div#list dd a")
        data = []
        for a in links:
            chapter = {}
            chapter["url"] = root_url + a.get("href")
            book = a.text.split(" ")
            chapter["chapter"] = book[0]
            chapter["title"] = book[1]
            chapter["bookId"] = bookId
            data.append(chapter)
        return data

    def getBookOneUrl(self, book_content):
        soup = BeautifulSoup(book_content, "html.parser")
        return soup.select_one("div#list dd a").get("href")

    def getBookName(self, html):
        soup = BeautifulSoup(html, "html.parser")
        return soup.select_one("div#info h1").text

    def getChapterContent(self, one_url, root_url, html):
        soup = BeautifulSoup(html, "html.parser")
        book_text = soup.select_one("div.box_con div.bookname h1").text
        book_info = str(book_text).strip().split(' ', 1)
        chapter = {}
        if book_info.__len__() > 1:
            chapter["chapter"] = book_info[0]
            chapter["title"] = book_info[1]
        else:
            chapter["chapter"] = book_info
            chapter["title"] = book_info
        chapter["content"] = soup.select_one("div#content").text
        chapter["url"] = one_url
        # 获取下一章URL
        links = soup.select("div.bookname div.bottem1 a")
        length = links.__len__()
        if links[length - 2].get("href") == links[length - 3].get("href"):
            return None, None
        return root_url + links[length - 2].get("href"), chapter
