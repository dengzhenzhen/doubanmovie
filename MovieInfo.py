from HomemadeFunctions import *
import os
import time


FILEOPEN = open('urllist.txt','r')
urllist = FILEOPEN.readlines()
FILEOPEN.close()

FO = open('score.txt','w',encoding='utf-8')

PageNum = len(urllist)
count = 1
for i in urllist:
    #----------------------无聊做个进度条----------------------------------------
    os.system('cls')
    print('url:',i)
    percent = count/PageNum*100
    print('*'*int(percent)+'-'*(100-int(percent))+'|'+'%.2f'%percent,'%')
    count += 1
    #---------------------------------------------------------------------------

    ScoreInfo = GetHtmlWithUA(i)
    FO.write(ScoreInfo+'\n')
    time.sleep(5)

FO.close()

    
print('Complete')
