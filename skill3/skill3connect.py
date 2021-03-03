import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",password="varudhini1979")
mycursor=mydb.cursor()
#mycursor.execute("create database Hospital")
#mycursor.execute("Show Databases")
mycursor.execute("use Hospital")
#mycursor.execute("Create table Doctor(Doctor_Id int(12),Doctor_Name varchar(30),Joining_Date date,Speciality varchar(30),Salary int(20), Experience int(10),PRIMARY KEY (Doctor_Id))")
#mycursor.execute("Create table Patient(Patient_Id int(12),Patient_name varchar(30),date_of_joining date,disease varchar(30),treatment varchar(30),medicine varchar(30),discharge_date date,bill varchar(30),PRIMARY KEY(Patient_id))")
#mycursor.execute("Create table Medicine(name varchar(30),price varchar(20),Mfd date,expiry_date date,no_of_strips int(15),power varchar(30))")
#mycursor.execute("show tables")
for db in mycursor:
    print(db)