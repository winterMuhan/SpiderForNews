#!/user/local/bin/python2.7
# encoding:utf-8
import urllib2
import requests
import json
from bs4 import BeautifulSoup as bs
from lxml import etree
from Sql.v9_python import v9_python
from Sql.v9_python_data import v9_python_data

class news(object):
    #试一下是否可以以列表或者字典的形式传参
    #定义需要获取的字段
    def __init__(self):
        self.v9 = v9_python()
        self.v9_data = v9_python_data()
        
        
    #输入关键词信息
    def inputKeyword(self):
        keyword = raw_input('请输入你所查找的关键词：')
        return keyword
    #获取数据  
    def getData(self,keyword):
        datas=[]
        #每20条数据为一个json，即一个data中包含20条数据。
        for new_num in xrange(0,160,20):
            key_url = 'https://www.toutiao.com/search_content/?offset='+str(new_num)+'&format=json&keyword='+str(keyword)+'&autoload=true&count=20&cur_tab=1'
            #伪装浏览器访问链接
            headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
            
            #wbdata = requests.get(key_url,headers=headers).text
            
            req = urllib2.Request(key_url,headers=headers)
            wbdata = urllib2.urlopen(req).read()
            #将响应的数据json化，并索引到新闻数据的位置
            data = json.loads(wbdata)
            datas.append(data)
        return datas
            
    #解析数据
    def parseData(self,keyword):
        count = 0
        lis = []
        lis_v9_data=[]
        datas =self.getData(keyword)
        for data in datas:
            news = data['data']   
            #遍历和提取索引出来的json数据
            for n in news:
                #异常控制
                try:
                    v9_data = 0
                    template = 'show'
                    catid = 11
                    typeid = 0
                    title = n['title']
                    #style = None
                    #thumb = None
                    keywords = keyword
                    description = n['abstract']
                    posids = 0
                    url = n['article_url']
                    listorder = 0
                    status = 99
                    sysadd = 1
                    islink = 0
                    username = 'admin'
                    inputtime = n['publish_time']
                    updatetime = n['create_time']
                    #source = n['source']
                    #comment_count = n['comment_count']
                    #img_url = n['image_url']
                    count += 1
                    prames_v9=(count,catid, typeid, title,keywords, description, posids, url, listorder, status, sysadd, islink, username, inputtime, updatetime)
                    prames_v9_data = (count,title,v9_data,v9_data,template,v9_data)
                    lis.append(prames_v9)
                    lis_v9_data.append(prames_v9_data)
                    #print prames

                except Exception:
                    continue
        #向v9_python中插入数据
        self.v9.insertManyDataToV9(lis)
        #向v9_python_data中插入数据
        self.v9_data.insertManyDataToV9_data(lis_v9_data)
        #print len(lis)
        print '*****************一共收集到%d条数据,请到数据库查看！**********************'%count
        
        

        


        
        
            
    
        
        
        
        
        
        
        
    
        
        
        
        
        
        
