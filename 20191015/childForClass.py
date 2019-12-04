import pymysql
connect=pymysql.connect(host='127.0.0.1',port=3306,db='projectin',user='root',password='111111')
mycur=connect.cursor()
# sql='insert into user_login(name)values(%s)'
# val=['小王子2','广告2','学编程2']
# mycur.executemany(sql,val)
# connect.commit()
# mycur.execute('show databases')
# for db in mycur:
#     print(db)

mycur.execute("select * from user_login")
# rows=mycur.fetchall()
# for row in rows:
#     print(row)
# print(mycur.fetchone())
# print(mycur.fetchone())
# print(mycur.fetchmany(4))
mycur.scroll(4,mode='absolute')
print(mycur.fetchone())
connect.close()

