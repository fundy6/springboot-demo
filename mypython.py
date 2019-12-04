list=['name','age','yw','sx','yy']
mydict=dict.fromkeys(list)
mydict2=mydict.copy()
mydict2['name']='张强';mydict2['age']=23;mydict2['yw']=75;mydict2['sx']=82;mydict2['yy']=78
mydict['name']='李明';mydict['age']=25;mydict['yw']=80;mydict['sx']=75;mydict['yy']=85
listdict=[]
listdict.insert(0,mydict);listdict.insert(1,mydict2)
for element in listdict:
    if element['name']=='李明':
        element['python']=60;del(element['age'])
    elif element['name']=='张强':
        element['python']=80;element['sx']=89
print(listdict)

res=input('please enter your name:')
if res=='':
    input('please input your name agein:')
    age=input('input your age:')
    if age.isdigit():
        age=int(age)
        if age>18:
            print('aluit')
        else:
            print('child')
    else:
        print('please enter a number')
print('444','555',sep='***')
def func(a,b):
    '''

    :param a: 
    :param b: 
    :return: 
    '''

name = 'Tom'

print('<1> name=',name)

def myfunc(obj):
    print('<2> hel');
class myclass(object):
    print ('<3> class')
    def getObj(self):
        print('<4> 11')
if name=='Tom':
        print('<5> Tom is go')
for b in name:
    print('<6>',b)
myfunc(1)
myobj=myclass()
myobj.getObj()
print ('<8> end')