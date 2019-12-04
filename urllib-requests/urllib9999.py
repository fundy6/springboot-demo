import json
import requests
from bs4 import BeautifulSoup
response=requests.get('http://www.taobao.com')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
data={
    'name':'Tom',
    'age':22
}
response1=requests.get('http://httpbin.org/get',params=data)
print(response1.text)

json.loads(response1.text)
print(type(response1.json()))
print(type(json.dumps(response1.json())))


url = 'http://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text  # 服务器返回响应

soup = BeautifulSoup(demo, "lxml")
"""
demo 表示被解析的html格式的内容
html.parser表示解析用的解析器
"""
print(soup)  # 输出响应的html对象
print('--------')
print(soup.prettify())  # 使用prettify()格式化显示输出