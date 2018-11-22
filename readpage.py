import requests
from bs4 import BeautifulSoup
import os
import sys
import imghdr
import string
if(os.name=='nt'):
    print(u'windows 系统')
else:
    print(u'linux')
f=open("page.html",'r',encoding='utf8')
#coding=utf-8
htmlFile=f.read()
itemSoup=BeautifulSoup(htmlFile,'lxml')
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

itemName=itemSoup.select("body div[id='wrap'] div[id='postlist'] div[id] table tr td[class='postcontent'] div[class='defaultpost'] table tr td img[file]")
print(itemName)
title=itemSoup.title.string
print(title)
path='C:/picture/pic/'+title+'/'

for i in range(0,len(itemName)):
    fileUrl=itemName[i].get('file')
    image_name=fileUrl.split("/")[-1]
    print('http://f.91p35.space/'+fileUrl)
    print(image_name)
    '''
    imageUrl=requests.get(fileUrl,headers=header)
    if not(os.path.exists(path)):
        os.makedirs(path)
    os.chdir(path)
    f=open(image_name,'wb')
    f.write(imageUrl.content)
    f.close()
    '''
print("打印完成")
