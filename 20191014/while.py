
u=0
s=10
sum=0
while u<s:
 sum=sum+u
 u=u+1
 if u==3:
   break
else:
 print('is over')
print('1go {0} is sum {1}'.format(s,sum))

for i in range(2,100):
 for x in range (2,i):
  if i%x==0:
   print(i,"等于",x,"**",i//x)
   break
 else:
  print(i,"是质数")

def dyname(*args,**kwargs):
 for param in args:
  print(param)
 for key in kwargs:
  print(key,kwargs[key])
dyname('ddd','66',sex='sss')

total = 0
def hello(a,b):
 total = a+b
 return total
print(total)
myll=lambda x:x+1
print(myll(2))

numlist=[1,2,3,4,5,6,7,8,9]
newlist=list(filter(lambda x:x%2==0,numlist))
print(newlist)

import sys
import numpy
from pymysql import  connect

print(sys.path)
print(numpy.sqrt(36))