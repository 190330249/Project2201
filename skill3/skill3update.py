import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",password="varudhini1979",database="Hospital")
mycursor=mydb.cursor()
mycursor.execute("Update patient SET bill='Rs.1,10,000/-' WHERE Patient_id=1004")
mydb.commit()