import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",password="varudhini1979",database="Hospital")
mycursor=mydb.cursor()
mycursor.execute("select * from medicine")
for db in mycursor:
    print(db)