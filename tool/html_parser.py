'''
Created on 2016年9月8日

@author: Luo Qiang
'''
import re
import urllib

from bs4 import BeautifulSoup


class HtmlParser(object):
          
    
    
    def get_new_urls(self,page_url,soup):
        new_urls =set() 
        # /view/123.html
        links = soup.find_all('a',href=re.compile(r'/view/\d+.htm'))
       
        for link in links:
            new_url = link['href'] #提取属性href的内容
            #让new_url以page_url为模板拼接成一个新的url
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            print(new_full_url)
            new_urls.add(new_full_url)
        return new_urls
    
    
    def get_new_data(self,page_url,soup):
        
        res_data = {}#用字典来存储提取的内容
        
        res_data['url'] = page_url
        
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title")#解析出标题
        
        if title_node == None:
            res_data['title'] = ''
            res_data['summary'] = ''
            return res_data
        else:
            title_node = title_node.find('h1')
            res_data['title'] = title_node.get_text()
            summary_node = soup.find('div',class_="lemma-summary")
           
            if summary_node == None:
                res_data['summary'] = ''
            else:
                res_data['summary'] = summary_node.get_text() #解析出摘要
                
                return res_data
    
    def parser(self,page_url,html_cont):
        
       
        if page_url is None or html_cont is None:
            return 
       
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding = 'utf-8')
        #提取新的URL
        new_url = self.get_new_urls(page_url,soup)
        #提取标题和摘要
        new_data = self.get_new_data(page_url,soup)
        return new_url,new_data
    
    