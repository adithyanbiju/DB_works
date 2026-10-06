# dynamic input
import sqlite3

con=sqlite3.connect('mydb.db')

con.execute('create table if not exists person(id int primary key,name varchar(20),age int)')
# #
# con.execute('insert into person(id,name,age)values(1,"arun",23)')
#
# con.commit()


# i=int(input("Enter id"))
# n=input("enter name")
# a=int(input("enter age"))
#
# con.execute('insert into person(id,name,age)values(?,?,?)',(i,n,a))
#
# con.commit()

# read operation

i=int(input("enter the id"))
e=con.execute('select * from person where id=?',(i,))
print(e.fetchall())