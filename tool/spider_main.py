'''
Created on 2016年9月8日

SpiderMain：主类，控制爬虫的行为，以及爬取的链接数量
UrlManager：URL管理类，方法包括添加新的URL，判断是否还有URL，获取一个URL
HtmlDownloader：网页下载类，用于下载对应URL网页的内容
HtmlParser：网页内容解析类，用于从爬取的网页内容中提取出主题，简介等信息，并提取出新的URL
HtmlOutputer：结果输出类，用于收集每轮循环后的爬取结果，并在爬取完预设的链接个数后，将所有结果通过html的格式呈现出来

由于链接及相关信息存储在字典中，因此即使爬取的起始地址相同，数量相同，每次打印出来的信息顺序也可能不同


@author: Luo Qiang
'''
from tool import url_manager, html_downloader, html_parser, html_outputer
import logging
logging.basicConfig(level=logging.INFO)

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.download = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        
    def craw(self,root_url):
        count = 1
        #设定初始链接
        self.urls.add_new_url(root_url)
        #进入爬取循环
        while self.urls.has_new_url():
            #如果出错则打印错误信息
            try:
                #获取一个新链接
                new_url = self.urls.get_new_url()
                print('********************************************')
                print('craw %d : %s' %(count,new_url))
                print('********************************************')
                #将对应URL的页面内容下载下来
                html_cont = self.download.download(new_url)
                #通过对页面的分析，提取出新的链接，和本页面的标题、简介 
                new_urls,new_data = self.parser.parser(new_url,html_cont)
                #将提取出的链接添加进列表 
                self.urls.add_new_urls(new_urls)
                #将收集到的页面信息存取
                self.outputer.collect_data(new_data)
                #判断爬取的链接数量是否到达指定数量
                if count == 3:
                    break
                count += 1   
                         
            except :
                print('crew fail:')
        #爬取完后，以html格式打印所爬取的信息
        self.outputer.output_html()     
 
        
if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/view/21087.html'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    
    
