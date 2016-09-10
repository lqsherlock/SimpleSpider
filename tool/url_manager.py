'''
Created on 2016年9月8日

@author: Luo Qiang
'''
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    
    def add_new_url(self,url):
        if url is None:
            return 
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)  
            
    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            print("urls is none")
            return
        for url in urls:
            self.new_urls.add(url)
            
    def has_new_url(self):
        return len(self.new_urls)
    
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    
    
    
    
    
    
    