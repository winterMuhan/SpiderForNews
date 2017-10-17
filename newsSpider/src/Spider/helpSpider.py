#!/user/local/bin/python2.7
#encoding:utf-8

from Spider.newSpider import news
import time
from multiprocessing import Pool
import copy_reg
import types
import warnings
from Sql.v9_python import v9_python
from Sql.v9_python_data import v9_python_data
import multiprocessing
#忽略警告

warnings.filterwarnings("ignore",".*",Warning,"Sql.sqlHelper",62)

#处理进程池问题
def _pickle_method(m):
    if m.im_self is None:
        return getattr, (m.im_class, m.im_func.func_name)
    else:
        return getattr, (m.im_self, m.im_func.func_name)
copy_reg.pickle(types.MethodType, _pickle_method)

#程序运行主函数
def main(keyword):
    start = time.time()
    deleteAllFromTable()
    new = news()
    #创建多进程：此处使用的是单进程。
    new.parseData(keyword)
    '''
    for i in range(1):
        p = multiprocessing.Process(target = new.parseData,args=(keyword,))
        p.start()
        p.join()
        '''
    end = time.time()
    print '程序运行用时 %ds'%(end-start)

#删除数据库里边所有数据，重新插入数据。
def deleteAllFromTable():
    v9 = v9_python()
    v9_data = v9_python_data()
    v9.deleteAllFromV9()
    v9_data.deleteAllFromV9_data()
    return '数据删除成功！'

#根据关键词从数据库搜索新闻
def searchNews():
    v9 = v9_python()
    datas = v9.selectAllFromV9()
    list_search = []
      
    flag1 = True
    while flag1:
        choice = raw_input('要搜索新闻吗？(Y/N):')
        if choice == 'Y'or choice =='y':
            #判断是否搜索出内容，若有，打印出匹配的语句
            keyword = raw_input('请输入新闻关键词：')
            for data in datas:
                if keyword in data[3]:
                    list_search.append(str(data[0])+" "+data[3])
            if list_search:
                print '-----------------共得到%d条数据！-------------------'%len(list_search)
                for data in list_search:
                    print data
                list_search=[]
            else:
                print 'sorry,没有你所要搜索的内容！'
            
        elif choice == 'N'or choice =='n':
            print '************退出程序！************'
            flag1 =False
        else:
            print '请按要求输入,谢谢配合！'
        
    

    