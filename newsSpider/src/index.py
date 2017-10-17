#!/user/local/bin/python2.7
# encoding:utf-8
from Spider import helpSpider
import sys
from Sql.v9_python import v9_python 
import time 

if __name__=='__main__':
    
    
    #程序主函数
    keyword = raw_input('请输入关键词：')
    #keyword = sys.argv[1]
    helpSpider.main(keyword)
    

    '''
    #设置自动化爬虫
    #time.sleep()
    #获取全部新闻的url
    for url in v9_python.selectUrlFromV9():
        print url[0]
    print len(v9_python.selectUrlFromV9())
    
    #根据关键词从数据库搜索新闻
    helpSpider.searchNews()  
    '''
      
    

