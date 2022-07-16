from selenium import webdriver
from threading import Thread
import requests
import re
import func_timeout
import time

# driver =webdriver.Chrome('./chromedriver.exe')
# driver.get('https://www.baidu.com/')
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
url = 'https://cdn7.hbhaoyi.com:65/20220312/VQfqzCAB/2537kb/hls/index.m3u8'
a =requests.get(url=url,headers=headers)
a = a.text
K = re.sub('#E.*','',a)
list_org = K.split()
list_data =[]
for a in list_org:
    url1 = 'https://cdn7.hbhaoyi.com:65' + a
    list_data.append(url1)
print(list_data)
class MyThread(Thread):
    def __init__(self,url_single):
        super().__init__()
        self.url_sigle = url_single
        self.result = None
        self.headers  ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

    def run(self):
        self.result = requests.get(url=self.url_sigle,headers=self.headers).content


    def get_result(self):
        return self.result

list_threading = []
for uu in list_data:
    list_threading.append(MyThread(f'{uu}'))
with open('./dianying.mp4','ab') as webben:
    for kk in list_threading:
        kk.start()
        kk.join()
        DATA = kk.get_result()
        webben.write(DATA)
        print(kk)




