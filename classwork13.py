# Create a database file school.db
import mysql.connector


con=mysql.connector.connect(user="root",password="root",host="localhost")
c=con.cursor()
c.execute('create database school')
con=mysql.connector.connect(user="root",password="root",host="localhost",database="school")
c=con.cursor()
c.execute('''create table if not exists Student(roll_no int primary key,
name varchar(20),age int,gender varchar(20),course varchar(20),mark int)''')
print("table created")
def insert_record():
    roll_no=int(input("enter roll no:"))
    name=input("enter your name:")
    age=int(input("enter your age:"))
    gender=input("enter your gender:")
    course=input("enter your course:")
    mark=int(input("enter your mark"))
    c.execute('''insert into Student(roll_no,name,age,gender,course,mark)values(%s,%s,%s,%s,%s,%s)''')
def delete_record():
    pass
def search_record():
    pass
def update_record():
    pass
while(1):
    pass
#
# create a table Student with fields roll_no(pk),name,age,gender,course,mark
#
# write a menu driven code
#
#                     1.Insert Student details
#                     2.Read all student details
#                     3.search a student by rollno
#                     4.update the mark of a student
#                     5.Delete a student record
#                     6.Exit
