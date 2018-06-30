import urllib.request
import re
import pymysql
import traceback


#-----------------------读取文件--------------------------------------------------------
FO = open('score.txt','r',encoding='utf-8')
html = FO.read()
FO.close()

LOGGING = open('error.log','w',encoding='utf-8')
#---------------------------------------------------------------------------------------

#-----------------------ResulstList存放每部电影的数据------------------------------------
Unit = re.compile('{[\s\S]+?}')
Result = Unit.findall(html)
ResultList = []
for i in Result:
    i = i.replace(':true',':True').replace(':false',':False')
    temp = eval(i)
    temp['actors'] = str(temp['actors']).replace('"',"'")
    temp['title'] = str(temp['title']).replace('"',"'")
    ResultList.append(temp)


#--------------------------------------------------------------------------------------

DataBase = pymysql.connect('127.0.0.1','root','123456','douban',charset='utf8')

#--------------------------创建表MOVIES------------------------------------------------
sql = '''
        CREATE TABLE MOVIES(
        rating varchar(255),
        rank int,
        cover_url text,
        is_playable char(5),
        id int not null,
        types varchar(255),
        regions varchar(255),
        title varchar(255),
        url text,
        release_date char(10),
        actor_count int,
        vote_count int,
        score float,
        actors text,
        is_watched char(5)
        )
      '''
cursor = DataBase.cursor()
cursor.execute('DROP TABLE IF EXISTS MOVIES')
cursor.execute(sql)
#--------------------------------------------------------------------------------------

ErrorCount = 0
for temp in ResultList:
    sqlins = '''
           INSERT INTO MOVIES(
           rating,
           rank,
           cover_url,
           is_playable,
           id,
           types,
           regions,
           title,
           url,
           release_date,
           actor_count,
           vote_count,
           score,
           actors,
           is_watched)
           VALUES("%s",%s,"%s","%s",%s,"%s","%s","%s","%s",%s,%s,%s,%s,"%s","%s")
         '''%(temp['rating'],
              temp['rank'],
              temp['cover_url'],
              temp['is_playable'],
              temp['id'],
              temp['types'],
              temp['regions'],
              temp['title'],
              temp['url'],
              temp['release_date'],
              temp['actor_count'],
              temp['vote_count'],
              temp['score'],
              temp['actors'],
              temp['is_watched'])
    try:
        cursor.execute(sqlins)
    except Exception:
        ErrorCount += 1
        print('--------------',ErrorCount,'-----------------------------------------------------------------------------------------------')
        print(Exception)
        print(traceback.format_exc())
        print(sqlins)
        print(temp.values())
        print('-----------------------------------------------------------------------------------------------------------------')
        LOGGING.write(str(ErrorCount)+'\n'+traceback.format_exc()+'\n'+sqlins+'\n')
        for i,j in temp.items():
            LOGGING.write(str(i)+':'+str(j)+' '+str(type(j))+'\n')
        continue
        

LOGGING.close()
DataBase.commit()
DataBase.close()