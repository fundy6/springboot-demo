from  bs4  import  BeautifulSoup
import requests
from queue import Queue
import threading

class CrawlThread(threading.Thread):
    pass


class ParseThread(threading.Thread):
    pass


if __name__ == '__main__':
    start_url='https://www.ggdown.cc/book/151/'
    url_list = []
    response = requests.get(start_url)
    parsehtml = response.content.decode(encoding=response.apparent_encoding,errors='ignore')
    soup = BeautifulSoup(parsehtml,'lxml')
    dds = soup.find('dl',class_="chapterlist").find_all('dd')
    for dd in dds:
        url= dd.find('a').get('href')
        url_list.append(url)
    count = len(url_list)
    url_queen = Queue(count)
    html_queen = Queue(count)
    lock = threading.Lock()
    filename = open('yun.txt','a','utf-8')
    base_url = 'https://www.ggdown.cc'
    for url in url_list:
        real_url = base_url+url
        url_queen.put(real_url)
    crawl_list=[]
    parse_list=[]
    for i in range(5):
        crawl_thread=CrawlThread('爬取线程'+str(i+1),url_queen,html_queen)
        crawl_thread.start()
        crawl_list.append(crawl_thread)
        parse_thread = ParseThread('解析线程'+str(i+1),html_queen,filename,lock)
        parse_thread.start()
        parse_list.append(parse_thread)
    pass

