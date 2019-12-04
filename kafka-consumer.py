from kafka import KafkaConsumer
import json
import datetime
import sys
import os
from hdfs import InsecureClient
from hdfs.client import Client
import  pyhdfs
def comsumer():
  consumer = KafkaConsumer(topic, bootstrap_servers=['remoteHost:9092,remoteHost:9093,remoteHost:9094'])



  for msg in consumer:
    datestr = datetime.datetime.now()
    if fs.exists('/data/' + datestr.strftime("%Y-%m-%d %H:%M:%S.%f")[0:10]) == False:
        fs.mkdirs('/data/' + datestr.strftime("%Y-%m-%d %H:%M:%S.%f")[0:10])
    array = json.loads(msg.value).get('result')
    jsonobjct={'time':datestr.strftime("%Y-%m-%d %H:%M:%S.%f")}
    keys = []
    for s in array:
        jsonobjct[s['a_tag']] = s['value_number']
    keys = jsonobjct.keys()
    if len(keys) == 677:
        print('ss',keys)
    if fs.exists(r'/data/' + datestr.strftime("%Y-%m-%d %H:%M:%S.%f")[0:10] + '/'+ str(jsonobjct.get('PROJECT_ID'))) == False:
        fs.create(path='/data/' + datestr.strftime("%Y-%m-%d %H:%M:%S.%f")[0:10] + '/' + str(jsonobjct.get('PROJECT_ID')),data=','.join(str(i) for i in keys)+'\n')
    saveHdfs(jsonobjct)

def saveHdfs(obj):
    time = obj.get('time')[0:10]
    values = obj.values()

    projectid = str(obj.get('PROJECT_ID'))
    syspath = '/data/' + time + '/' + projectid
    fs.append(path=syspath, data=','.join(str(i) for i in values)+'\n')

    # read_hdfs_file(syspath)
    # for key in obj.keys():
    #  print(key)
    # fs.append(path='/kafka-consumer.py', data=obj)
    # response = fs.open(syspath)
    # print(response.read())

    # fp = fs.listdir("/")
    # print(fp)
    # print(fs.exists('/user/hadoop'))
    #
    # print('hi',fs.exists('/kafka-consumer.py'))
    # print(fs.get_home_directory())

    '''    
    :param obj: 
    :return: 
    '''

    # root_path = "/"
    # time = obj.get('time')[0:10]
    # c = InsecureClient(url="http://master:50070", user='root', root=root_path)
    # c.write('/' + time + '/' + obj.get('PROJECT_ID'), obj, True)
    # hdfs_files = c.list('/', True)
    # for f in hdfs_files:
    #     print(f)
def read_hdfs_file(syspath):
    client = Client('http://master:50070')

    lines = []
    response = fs.open(syspath)
    with client.read(hdfs_path=syspath, encoding='utf-8', delimiter='\n') as reader:
        for line in reader:
            print(line)

if __name__== '__main__':
   i = 0
   fs = pyhdfs.HdfsClient(hosts='master',user_name='root')
   fs.mkdirs("/sl-data")
   topic = sys.argv[1]
   ipaddr=sys.argv[2]
   port = sys.argv[3]
   comsumer()




def getDirPath(filename):
    return os.path.dirname(filename)