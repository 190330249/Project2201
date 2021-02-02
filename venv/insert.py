import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",password="varudhini1979",database="Student")
mycursor=mydb.cursor()
form="insert into student(name,Idno) values(%s,%s)"
students=[("Nithya",249),("Nikhila",171),("Sravani",229),("Shivani",18)]
mycursor.executemany(form,students)
mydb.commit()