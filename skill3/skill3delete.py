import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",password="varudhini1979",database="Hospital")
mycursor=mydb.cursor()
mycursor.execute("Delete from patient where Patient_id=1011")
mydb.commit()