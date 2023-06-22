import sqlite3
con=sqlite3.connect('abc.db')
cr=con.cursor()

a="""Create table if not exists emp(
staff_number integer primary key,
fname varchar(20),
lname varchar(20),
gender char(1),
joining date
);"""


cr.execute(a)
a="""insert into emp
values(2,"abc","Khushal","m","2023-06-13");"""
cr.execute(a)
cr.execute("select * from veer")
ans=cr.fetchall()
for i in ans:
    print(i)
cr.execute(a)
con.close()



