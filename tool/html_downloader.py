'''
Created on 2016年9月8日

@author: Luo Qiang
'''

from urllib import request

class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None
        
        response = request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response
    
    