import random
class Role:
    def __init__(self,name):
      self.name=name
    def  att(self,enemy):
      enemy.life_value-=self.att_active
      print(self.name,"攻击了",enemy.name)
    def is_dead(self):
      return self.life_value<=0
class Person(Role):
    life_value=200
    att_active=40

class Monster(Role):
    life_value=150
    att_active=25

p_list=[]

m_list=[]
p1=Person('p1')
p2=Person('p2')

m1=Monster('m1')
m2=Monster('m2')
m3=Monster('m3')
p_list.append(p1)
p_list.append(p2)
m_list.append(m1)
m_list.append(m2)
m_list.append(m3)
while len(p_list)!=0 and len(m_list)!=0:
    p=p_list[random.randint(0,len(p_list)-1)]
    m=m_list[random.randint(0,len(m_list)-1)]
    num=random.randint(0,1)
    if num==0:
       p.att(m)
       print(m.name,"剩余生命值",m.life_value)
    elif num==1:
       m.att(p)
       print(p.name, "剩余生命值", p.life_value)
    if p.life_value<=0:
       print(p.name,'已死')
       p_list.remove(p)
    if m.life_value<=0:
       print(m.name,'已死')
       m_list.remove(m)