import requests
import re
from  bs4 import BeautifulSoup
url='http://tieba.baidu.com/f?kw=豆瓣&ie=utf-8&pn=50'#input("please enter your url")
pattern='<li.*?<div.*?<div.*?<div.*?<div.*?<a.*?rel="noreferrer".*?>(.*)</a>.*?<div.*?</li>'
#url='https://book.douban.com/latest?icn=index-latestbook-all'
# pattern='<li>.*?<a.*?cover".*?href="(.*?)">.*?<img.*?src="(.*?)".*?</li>'
# pattern='<li>.*?<div.*?detail-frame">.*?href="(.*?)">(.*?)</a>.*?<span.*?color-lightgray">(.*?)</span>.*?<p.*?color-gray">(.*?)</p>.*?<p.*?detail">.*?"(.*)"</p>.*?</li>'
# pattern = '<div\sclass="detail-frame".*?href="(.*?)">(.*?)</a>.*?color-lightgray">(.*?).*?color-gray">(.*?)</p>.*?detail">(.*?)</p>'
# <span.*?color-lightgray">(.*?)</span>.*?<p.*?color-gray">(.*?)</p><p.*?detail">"(.*?)".*?</p>
pattern=re.compile(pattern,re.S)
response= requests.get(url)
while response.status_code!=200:
    input("请输入合法url地址")
   # html=BeautifulSoup(response.text,'lxml')
   # ofile=open(file='/Users/a10.12/Documents/a.html',mode='w')
   # ofile.write(html.prettify())
   # results=re.findall(pattern,response.text,re.S)

   # print(results)
   # for li,title in results:
   #  print(li,title)
else:
    html=BeautifulSoup(response.text,'lxml')
    ofile=open(file='/Users/a10.12/Documents/a.html',mode='w')
    ofile.write(html.prettify())
    results = re.findall(pattern, response.text)
    print(results)

# url=input("please enter your url")
# pattern='<'