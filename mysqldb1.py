import errno

import mysql.connector

# con=mysql.connector.connect(user="root",password="root",host="localhost")
#
#         # connection to db server
# c=con.cursor()
#
#
# c.execute("create database mydb3")
# print("database created")

con=mysql.connector.connect(user="root",password="root",host="localhost",database="mydb2")

c=con.cursor()
#
# c.execute('''create table if not exists employee(empid int primary key,
# name varchar(20),age int ,salary int ,gender varchar(20),place varchar(20))''')
# print("table created")
#
# c.execute('''insert into employee(empid,name,age,salary,gender,place)
#             values(1,"aadhil",20,2500,"male","ekm"),
#                   (2,"akhilesh",20,3500,"male","alpy"),
#                   (3,"pooja",18,4500,"female","kollam"),
#                   (4,"ajith",27,5500,"male","kottayam"),
#                   (5,"anu",30,6500,"female","tvm")''')
# con.commit()
# c.execute('select * from employee')
# k=c.fetchall()
# print(k)

# c.execute('select * from employee where empid=1')
# k=c.fetchall()
# print(k)

# read all records with attribute name and age
# c.execute('select name,age from employee')
# k=c.fetchall()
# # print(k)

# c.execute('select * from employee where age>20')
# k=c.fetchall()
# print(k)


# c.execute('select * from employee where salary between 5000 and 7000')
# k=c.fetchall()
# print(k)
