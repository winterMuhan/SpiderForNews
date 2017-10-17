# -*- coding:utf-8 -*-
import web
from Sql.v9_python import v9_python

urls = (
    '/','Index',
    '/page/list_(\d+).html','Page',
    '/page_(\d+)','Search',
    '/s','Search'   
        )
#加载模板，使用绝对路径    
render = web.template.render('D:/Eclipae with pydev/wokespace/newsSpider/src/template')

#首页路由
class Index(object):
    def __init__(self):
        self.v9 = v9_python()
    '''
    def GET(self):
        newid = 0
        Page = 1
        datas = self.v9.selectFromV9For15(newid)
        return render.news(datas,Page-1,Page+1)
    '''
    def GET(self):
        return render.index('')

class Page(object):
    def __init__(self):
        self.v9 = v9_python()
    def GET(self,pageNum):
        #从数据库提取title标签,根据页码来确定id
        pageNum = int(pageNum)
        newid = (pageNum-1)*15
        datas = self.v9.selectFromV9For15(newid)
        #简单分页
        if pageNum==1:
            return render.news(datas,'',pageNum+1)
        if len(datas)<15:
            endpage = pageNum
            return render.news(datas,pageNum-1,'')
        return render.news(datas,pageNum-1,pageNum+1  )
    
class Search(object):
    def __init__(self):
        self.v9 = v9_python()
    def GET(self):
        #获取输入的关键词
        datas = []
        inputData = web.input()  
        keyword = inputData['wd']
        #查询数据库
        news = self.v9.selectAllFromV9()
        #根据关键词检索数据
        for new in news:
            if keyword in new[3] and new not in datas:
                datas.append(new)
        #去重 ：set()集合形式输出无序
        datas = list(set(datas))
        if len(datas)>0:
            return render.search(datas,0,0)
        else:
            return render.index('sorry,没有您所搜索的内容！')
    
if __name__ == '__main__':
    web.application(urls,globals()).run()
    
    
    
    