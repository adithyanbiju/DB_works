import sqlite3

con=sqlite3.connect('company.db')

command="""create table if not exists employee(empid int primary key,
#                                 name varchar(30),
#                                 age int,
#                                place varchar(30),
#                                gender varchar(10),
#                                 designation varchar(30),
#                                 salary int)"""
# # con.execute(command)
# # con.commit()
# # print("table created")
#
# # insertion
#
# command="""insert into employee(empid,name,age,place,gender,designation,salary)
#             values(101,"amal",20,"ekm","male","developer",25000),
#                     (102,"arun",21,"tvm","male","driver",15000),
#                     (103,"arya",23,"kollam","female","developer",24000),
#                     (104,"anagha",20,"alapzha","female","tester",22000)"""
# # con.execute(command)
# # con.commit()
#
# # command="select * from employee"
# #
# # # e=con.execute(command)
# # #
# # # print(e.fetchall())
# # e=con.execute('select name,age from employee')
# # print(e.fetchall())
# #
# #
# # e=con.execute('select * from employee where empid=101')
# # print(e.fetchall())
# #
# # e=con.execute('select name,age from employee where empid=101')
# # print(e.fetchall())
#
#
# # =,<,>,!=,<=,>=,and,or,not,between,like,in,distinct,order by
#
# #read all employee records having age>=25 and salary<30000
# #
# # e=con.execute('select * from employee where age>=25 and salary<30000')
# #
# # print(e.fetchall())
# # # read all employee record with empid other than 102
# # e=con.execute('select * from employee where not (empid=102)')
# # print(e.fetchall())
# #
# # # read all employee records having place=ekm or age<=2
# # e=con.execute('select * from employee where place="ekm" or age<=25')
# # print(e.fetchall())
# #
# # # between
# # employee records having salary between 20000 and 30000(including 20000  and 30000)
#
# # e=con.execute('select *from employee where salary between 20000 and 30000')
# # print(e.fetchall())
#
# # employee record having age between 20 and 25(return name,age)
#
# # e=con.execute('select name,age from employee where age between 20 and 25')
# # print(e.fetchall())
#
# # like
# # pattern matching
# # % - 0 or more character
# # _ -exactly one character
#
# # employee record having name starting with 'A'
# # e=con.execute('select * from employee where name like "A%" ')
# # print(e.fetchall())
# # #employee record having 3 starting with 'A'
# # e=con.execute('select * from employee where name like "A__"')
# # print(e.fetchall())
#
# # employee record with place starting with "E"
# # e=con.execute('select * from employee where place like "E%"')
# # print(e.fetchall())
# #
# # # employee record having 3 letter place name ending with letter "m"
# # e=con.execute("select * from employee where place like '__M'")
# # print(e.fetchall())
# # # employee record having age<25 and name starting with letter 'A'
# # e=con.execute("select * from employee where age<25 and name like 'A%'")
# # print(e.fetchall())
# # # employee record having salary =10000 and palce atrting with k
# # e=con.execute("select * from employee where salary=10000 and place like 'K__'")
# # print(e.fetchall())
#
#
# # IN
#
# # employee recod having age=30 or age =25
#
# # e=con.execute('select * from employee where age in (20,30)')
# # print(e.fetchall())
#
# # order by(acending order)
# # e=con.execute('select * from employee order by name')
# # print(e.fetchall())
# # # Descending order by name
# # e=con.execute('select * from employee order by name desc')
# # print(e.fetchall())
# # # descending oreder by age
# # e=con.execute('select * from employee order by age desc')
# # print(e.fetchall())
#
#
# # Distinct
# # e=con.execute('select distinct(place) from employee')
# # print(e.fetchall())
#
# # update
# # con.execute('update employee set name="kiran",age=30 where empid=101')
# # con.commit()
# # print("Table created")
# sql
# # delection
#
# con.execute('delete from employee where empid=102')
# con.commit()