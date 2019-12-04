from bs4 import BeautifulSoup

import  requests

# url='http://tieba.baidu.com/f?kw=豆瓣&ie=utf-8&pn=50'
url = input('please enter your url')
with open(file='/Users/a10.12/Documents/title.txt',mode='w+') as file:
    '''
    打开文件并往文件写数据
    '''
    try:
      response = requests.get(url)

      while response.status_code != 200:
           url = input('please valid url ')
      else:
        html = BeautifulSoup(response.text, 'lxml')
        i = 0
        for te in html.find_all('a'):
            if te.text != '' and te.has_attr('rel') and te.has_attr('href') and te.has_attr('title') and te.has_attr(
                    'target') and te.has_attr('class'):
                i = i + 1
                file.write(str(i)+' '+te.text+'\n')
    except ConnectionError:
        print('connect error')
    except IOError:
        print('io error')
