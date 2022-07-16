import threading

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
@func_timeout.func_set_timeout(3)
def paqu(url_single):
    global headers
    data_single = requests.get(url=url_single,headers=headers).content
    return data_single

def xianchengkaishi():
    list_threading = []
    for url_single in list_data:
        list_threading.append(threading.Thread(target=paqu,args=(url_single,)))
    for th in list_threading:
        th.start()

xianchengkaishi()
