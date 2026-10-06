# 1.Create a table named students to store student information.
# Table: students
# Column Name
# Data Type
# Description
#
# student_id
# INT (Primary Key)
# Unique student ID
#
# name
# VARCHAR(100)
# Name of the student
#
# age
# INT
# Age of the student
#
# gender
# VARCHAR(10)
# Gender
#
# course
# VARCHAR(100)
# Enrolled course
#
# marks
# INT
# Marks obtained
#
# city
# VARCHAR(100)
# City of the student
import sqlite3
con=sqlite3.connect('student.db')

student="""create table if not exists student(student_id int primary key,
                                                name varchar(100),
                                                age int,
                                                gender varchar(10),
                                                course varchar(100),
                                                mark int,
                                                city varchar(100))"""
# con.execute(student)
# con.commit()
# print("table created")

student="""insert into student(student_id,name,age,gender,course,mark,city)
                        values(1,"adithyan",20,"male","bsc",100,"alappuzha"),
                               (2,"ajith",27,"male","btech",100,"kottayam"),
                               (3,"kiren",25,"male","bca",98,"kannur"),
                               (4,"mary",18,"female","nursing",80,"kochi"),
                               (5,"saddie",19,"female","bsc",30,"banglore"),
                               (6,"pooja",22,"female","computer science",30,"kochi")"""
# con.execute(student)
# con.commit()




# Questions
# Display all records from the students table.
# e=con.execute('select * from student')
# print(e.fetchall())
#
# # Display name, course, and marks for all students.
# e=con.execute('select name,course,mark from student')
# print(e.fetchall())
# Display names and marks of students who scored more than 80.
# e=con.execute('select name,mark from student where mark > 80')
# print(e.fetchall())
# # Display all details of students enrolled in Computer Science.
# e=con.execute('select * from student where course = "computer science" ')
# print(e.fetchall())

# Display names, ages, and cities of students whose age is between 18 and 22.
# e=con.execute('select name,age from student where age between 18 and 22 ')
# print(e.fetchall())
# # Display names, marks, and courses of students from Kochi, sorted by marks in descending order.
# e=con.execute('select name,mark,course from student where city ="kochi" order by mark desc')
# print(e.fetchall())

# Insert a new record into the students table.
# student="""insert into student(student_id,name,age,gender,course,mark,city)
#                     values(12,"arun",32,"male","bca",79,"kannur")"""
# con.execute(student)
# con.commit()

# # Update marks of all students who scored below 50 by adding 5 bonus marks.
con.execute('update student set mark=mark+5 where mark < 50 ')
con.commit()
# # # Delete all student records where marks are less than 35.
con.execute('delete from student where mark < 50')
con.commit()
