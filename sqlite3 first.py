import sqlite3
con=sqlite3.connect('abc1.db')
cr=con.cursor()

a="""Create table if not exists veer(
staff_number integer,
fname varchar(20),
lname varchar(20),
gender char(1),
joining date
);"""

cr.execute(a)

a="""insert into veer
values(1,"Veer","Khushal","m","2023-06-13");"""
cr.execute(a)
con.commit()

cr.execute("select * from veer")
ans=cr.fetchall()

con.close()



