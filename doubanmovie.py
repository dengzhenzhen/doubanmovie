import urllib.request
import time
import re
from HomemadeFunctions import *


'''
Type = range(0,100)
step = 1000
Rank = range(0,1000,step)
URL = 'https://movie.douban.com/j/chart/top_list?type='+'24'+'&interval_id=100%3A90&action=&start='+str(Rank)+'&limit=1'

FILEOPEN = open('scores.txt','w',encoding='utf-8')

for j in Type:
    time.sleep(5)
    URL = 'https://movie.douban.com/j/chart/top_list?type='+str(j)+'&interval_id=100%3A90&action=&start='+str(0)+'&limit='+str(1)
    Response = urllib.request.urlopen(URL)
    HTML = Response.read().decode('utf-8')
    if(HTML.find('[]') == 0):
        continue
    else:
        for i in Rank:
            time.sleep(1)
            URL = 'https://movie.douban.com/j/chart/top_list?type='+str(j)+'&interval_id=100%3A90&action=&start='+str(i)+'&limit='+str(step)
            Response = urllib.request.urlopen(URL)
            HTML = Response.read().decode('utf-8')
    
            if(HTML.find('[]') == 0):
                break
            else:
                print('type=',j)
                FILEOPEN.write(HTML)

FILEOPEN.close()

'''



#---------------------------获取所有分类的链接，存放在列表URLlist，写在urllist.txt中-------------------------------------------------------------------------------------------------------------------------

Type = range(1,40)
step = 1000
Rank = range(0,2000,step)
Position = [[100,90],[90,80],[80,70],[70,60],[60,50],[50,40],[40,30],[30,20],[20,10],[10,0]]
URLlist = []
count = 0

FO = open('urllist.txt','w')

for i in Type:
    for j in Position:

        URL = 'https://movie.douban.com/j/chart/top_list_count?type='+str(i)+'&interval_id='+str(j[0])+'%3A'+str(j[1])
        html = GetHtmlWithUA(URL)

        Flag = re.compile('"total":\d+')
        a = Flag.search(html)
        TotalNum = int(a.group()[8:])

        if TotalNum != 0:

            tempdict = {'type':i,
                        'position':j,
                        'totalnum':TotalNum,
                        'url':'https://movie.douban.com/j/chart/top_list?type='+str(i)+'&interval_id='+str(j[0])+'%3A'+str(j[1])+'&action=&start=0&limit='+str(TotalNum)
                        }

            URLlist.append(tempdict)
            FO.write(tempdict['url']+'\n')

        count += 3
        print('等待3秒,','当前共等待',count,'秒')
        time.sleep(3)

FO.close()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
