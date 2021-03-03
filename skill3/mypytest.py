import pytest
import mysql.connector as mysql
def read():
    mydb = mysql.connect(host="localhost", user="root", password="varudhini1979", database="Hospital")
    mycursor1 = mydb.cursor()
    mycursor1.execute("select patient_id from patient where patient_name='Amrita sen'")
    return mycursor1
def test_mysql():
    mydb = mysql.connect(host="localhost", user="root", password="varudhini1979", database="Hospital")
    mycursor = mydb.cursor()
    mycursor.execute("select patient_id from patient where patient_name='Amrita sen'")
    assert mycursor == mycursor