import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",password="varudhini1979")
mycursor=mydb.cursor()
mycursor.execute("create database Student")
mycursor.execute("Show Databases")
for db in mycursor:
    print(db)