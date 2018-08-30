import bs4
import requests
import json
import re
import time

main_url = 'https://www.douban.com'
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
account = '374894000@qq.com'
password = '********'

#先不考虑验证码了
class login_session(requests.Session):

    def login(self, account, password):
        login_url = 'https://accounts.douban.com/login'
        headers = {'User-Agent':User_Agent, 'Referer':'https://www.douban.com/'}
        post_data = {'source':'index_nav', 'form_email':account, 'form_password':password}

        self.post(login_url, data=post_data, headers=headers)



tags = {}
req = requests.get('https://movie.douban.com/chart')
soup = bs4.BeautifulSoup(req.text, 'lxml')
labels = soup.find('div', class_='types').find_all('a')
for i in labels:
    '''
    'sort':'id'
    '''
    tags[i.text] = re.search( 'type=\d+',i.get('href')).group()[5:]
range_list = [str(i+10)+'%3A'+str(i) for i in range(0,100,10)]
format_url = 'https://movie.douban.com/j/chart/top_list?type={0}&interval_id={1}&action=&start=0&limit=9999'
'''
for k,v in tags.items():
    print(k,v)
    for interval_id in range_list:
        print(  format_url.format(v, interval_id )  )
'''
session = login_session()
session.login(account, password)

with open('score_data.json','w') as fp:
    json.dump([1],fp)


data = []
for k,v in tags.items():
    print(k,v)
    for interval_id in range_list:
        print(  format_url.format(v, interval_id )  )
        req = session.get( format_url.format(v, interval_id ) )

        data += json.loads(req.text, encoding='utf-8')

        with open('score_data.json', 'w', encoding='utf-8') as fp:
            json.dump(data,fp, ensure_ascii=False)

        time.sleep(1)

         
