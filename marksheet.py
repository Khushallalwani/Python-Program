import sqlite3 

con=sqlite3.connect('marksheet.db')
crsr=con.cursor()
sql_create="""create table if not exists bca11(
b1acno integer primary key,
se301 integer
);"""

crsr.execute(sql_create)

sql_create2="""create table if not exists bca12(
b3acno integer primary key,
se301 integer
);"""
crsr.execute(sql_create2)



crsr.execute('''UPDATE bca11 SET(se301)=(SELECT bca12.se301 FROM bca12 WHERE bca12.b3acno=bca11.b1acno)''')
con.commit()

crsr.execute("select * from bca11")
ans=crsr.fetchall()
for i in ans:
    print(i)

crsr.execute("select * from bca12")
ans=crsr.fetchall()
for i in ans:
    print(i)   

con.close()

