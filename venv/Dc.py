import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",password="varudhini1979",database="Student")
mycursor=mydb.cursor()
mycursor.execute("Create table student(name varchar(50),Idno int(10))")
mycursor.execute("show tables")