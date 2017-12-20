# -*- coding:UTF-8 -*-
"""
运行
@author: HY
"""
from com.crawling.spider import url_Manage
from com.crawling.spider import html_DownLoad
from com.crawling.spider import html_Perser
from com.crawling.spider import html_Output

class SpiderMain(object):
    def __init__(self):
        # 初始化URL管理器
        self.urls = url_Manage.UrlManage()
        # 初始化HTML下载器
        self.download = html_DownLoad.HtmlDownLoad()
        # 初始化HTML解析器
        self.parser = html_Perser.HtmlPerser()
        # 初始化HTML输出器
        self.output = html_Output.HtmlOutPut()

    def runSpider(self, url, typeid, id):
        # 定义一个变量来记录当前的是第几个URL
        count = 1
        dayurl = url
        print(dayurl)
        # 将URL添加到URL管理器
        self.urls.add_new_url(dayurl);
        # 判断URL管理器中是否有未爬取过的新URL
        while self.urls.has_new_url():
            # 为了防止URL不能访问,所以可以把执行放到Try里面执行
            try:
                # 获取新URL
                new_url = self.urls.get_new_url()
                # 输出提示这是第几个URL
                print("这是第%d个URL,地址为:%s" % (count, new_url))
                # 执行HTML下载器
                html_content = self.download.DownLoad(new_url)
                # 调用解析器解析
                new_data = self.parser.getAllType(html_content)
                # new_data = self.parser.Parse(new_url, html_content)
                # 将URL添加到URL管理器
                # self.urls.add_new_urls(new_urls)
                # 将数据放到output中存放
                self.output.collect_data(new_data)

                # 不能一直爬取  可以自己设置一个爬取的上限
                if count > 999:
                    break

                # 变量++
                count += 1

            # 如果没有URL,那么就在控制台打印出
            except:
                print("没有此URL")

        try:
            print("执行sql")
            # 调用output_html方法输出数据
            self.output.output_html(typeid, id)
            print("执行SQL完毕")
        except:
            print("添加数据失败")
        # 关闭浏览器
        self.download.closeBrowser()


if __name__ == "__main__":
    s = SpiderMain()
    url = "http://www.biquge.com.tw/"
    s.runSpider(url, 1, 1)