import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",password="varudhini1979")
print(mydb)
if(mydb):
    print("successful")
else:
    print("unsuccessful")