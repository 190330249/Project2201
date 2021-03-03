import mysql.connector as mysql
def read():
    mydb = mysql.connect(host="localhost", user="root", password="varudhini1979", database="Hospital")
    mycursor = mydb.cursor()
    mycursor.execute("select patient_id from patient where patient_name='Amrita sen'")
    return mycursor
print(read())
