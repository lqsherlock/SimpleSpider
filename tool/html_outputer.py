'''
Created on 2016年9月8日

@author: Luo Qiang
'''


class HtmlOutputer(object):
    
    def __init__(self):
        self.datas=[]
     
    def collect_data(self,new_data):
        if new_data is None:
            return
        self.datas.append(new_data)
    
    def output_html(self):
        fout = open('outputer_html','w',encoding='utf-8')
        
        fout.write('<html>')
        fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
        fout.write('<body>')
        fout.write('<table>')

        # ascii python 默认编码
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        
        fout.close()
        
        
        
        
        