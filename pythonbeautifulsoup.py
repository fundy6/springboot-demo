import json
import requests
import pypinyin
from bs4 import BeautifulSoup

list = []
iplist=[]
def dyname_proxy():
    url="https://www.kuaidaili.com/free/inha"
    response = requests.get(url)
    if(response.status_code==200):
        html = response.text
        soup = BeautifulSoup(html,'lxml')
        tbody = soup.find('tbody')
        tr = tbody.find_all('tr')
        for tds in tr:
            if tds:
                ipport = {}
                ipport['IP']=tds.find('td',attrs={'data-title':'IP'}).text
                ipport['PORT']= tds.find('td', attrs={'data-title': 'PORT'}).text
                iplist.append(ipport)

def get_html(kw,pn):
    # url = 'http://tieba.baidu.com/f?ie=utf-8'
   for obj in iplist:
    url='https://maoyan.com/?utm_source=meituanweb'
    data = {
        'key': 'a8b932b7661aee98fcb3c89984626302',
        'city': '广州'
    };
    proxies={
        "http":"http://{IP}:{PORT}".format(IP=obj['IP'],PORT=obj['PORT'])
    }
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15'}

    # param={'pn':pn,'kw':kw}
    html=requests.get(url,headers=headers)
    if html.status_code == 200 :
      ss = BeautifulSoup(html.text,'lxml')
      dl = ss.find('dl',attrs={'class':'movie-list'})
      dds = dl.find_all('dd')
      for dd in dds:
           obj = {}
           obj['title'] = dd.find('div',attrs={'class':'movie-title'}).text
           imgtags = dd.find('img',attrs={'class':'poster-default'})
           brother=imgtags.find_next_sibling()
           obj['src']=brother['data-src']
           list.append(obj)
      print(list)
      break
    # lis = ul.find_all('li')
    # for li in lis:
    #   title = li.find('a',attrs={'class':'j_th_tit','rel':'noreferrer'})
    #   if title:
    #      list.append(title.get_text())
    #      print(title.get_text())get_text

def hp(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s
'''
猫眼电影爬虫 https://maoyan.com/films?showType=2&offset=0
其中 showType 1 正在热映 2  即将上映 3 经典影片
offset 开始 0  步长 30 
'''
def parseMaoyanMovie(showType,offset):
  for obj in iplist:
      proxies = {
          "http": "http://{IP}:{PORT}".format(IP=obj['IP'], PORT=obj['PORT'])
      }
      headers = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15'}
      url = 'https://maoyan.com/films?showType={showType}&offset={offset}'.format(showType=showType,offset=offset)
      html=requests.get(url,headers=headers,proxies=proxies)
      if html.status_code == 200:
          soup=BeautifulSoup(html.text,'lxml')
          dl = soup.find('dl',attrs={'class':'movie-list'})
          dds = dl.find_all('dd')
          for dd in dds:
              obj={}
              obj['src']=dd.find('img',attrs={'class':'poster-default'}).find_next_sibling()['data-src']
              obj['title']=dd.find('div',attrs={'class':'channel-detail movie-item-title'})['title']
              list.append(obj)
          break

def saveImage():
    for obj in list:
        r = requests.request('get',obj['src'])
        title=hp(obj['title'])
        if r.status_code==200:
         with open(file='/Users/a10.12/WeChatProjects/miniprogram-1/images/{key}.png'.format(key=title),mode='wb') as f:
           f.write(r.content)
         f.close()
         obj['src']='../../images/{key}.png'.format(key=title)

def saveFile(list):
    with open(file='/Users/a10.12/Documents/title.txt',mode='wb',errors='ignore') as f:
        i=0;
        for strs in list:
            i=i+1
            f.writelines(str(i)+' '+strs+'\n')

# kw = input("请输入你要查询的关键字")
# pn = input("请输入你要查询的页数")
# while True:
#     if pn.isdigit():
#        pn = int(pn)
#        for i in range(pn):
#           get_html(kw,i*50)
#        break;
#     else:
#        input("请输入您要查询的页数")
dyname_proxy()
#get_html(1,2)
kw = input("请输入你的类型")
pn = input("请输入你要查询的页数")

while True:
    if pn.isdigit():
        pn = int(pn)
        for i in range(pn):
         parseMaoyanMovie(kw,30*i)
        break

saveImage()
print(list)
# saveFile(list)
