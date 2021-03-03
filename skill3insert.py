import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",password="varudhini1979")
mycursor=mydb.cursor()
mycursor.execute("use Hospital")
# form="insert into doctor(Doctor_id,Doctor_Name,Joining_Date,Speciality,Salary,Experience) values(%s,%s,%s,%s,%s,%s)"
# doctors=[(101,"David","2005-2-10","Pediatric",40000,2),
#          (102,"Michael","2018-07-23","Oncologist",20000,4),
#          (103,"Susan","2016-05-19","Garnacologist",25000,6),
#          (104,"Robert","2017-12-28","Pediatric",28000,8),
#          (105,"Linda","2004-06-04","Garnacologist",42000,5),
#          (106,"William","2012-09-11","Dermatologist",30000,3),
#          (107,"Richard","2014-08-21","Garnacologist",32000,5),
#          (108,"Karen","2011-10-17","Radiologist", 30000,4)]
# form1="insert into Patient(Patient_Id,Patient_name,date_of_joining,disease,treatment,medicine,discharge_date,bill) values(%s,%s,%s,%s,%s,%s,%s,%s)"
# patients=[(1004,"Armita Sen","2012-02-10","Tubercluosis","self-care","Isoniazid","2012-02-20","Rs.1,00,000/-"),
#           (1005,"Amisha Patel","2012-07-11","Sinustiitis","Inhale With Oregano Oil","Otrovin Drops(Adult)","2012-07-16","Rs.50,000/-"),
#           (1006,"Bhanu Prakash","2014-08-21","Hyper Thyroidism","Iodine:oral medication","Ygeiax 7 Thyroid Care","2014-08-29","Rs.25,000/-"),
#           (1007,"Catherine","2014-11-14","Tubercluosis","prescribed antibiotics","rifampicin","2014-11-14","Rs.1,50,000/-"),
#           (1008,"Carol Teresa","2016-05-19","Malaria","Primaquine for 14 days","chloroquine","2016-05-30","Rs.75,000/-"),
#           (1009,"Dhanya Chakravarthy","2016-10-24","Dengue","Home Remedy:Papaya Leaf Juice","Dexa","2016-10-31","Rs.30,000/-"),
#           (1010,"Rakesh Kumar","2017-12-28","Hypo Thyroidism","follow proper medication","levothyroxine","2018-01-05","Rs.20,000/-"),
#           (1011,"Vardhan Sai","2017-12-31","Asthama","nebulizer","Omalizumab(Xolair)","2018-01-15","Rs.30,000/-")]
# mycursor.executemany(form1,patients)
# form2="insert into medicine(name,price,Mfd,expiry_date,no_of_strips,power) values(%s,%s,%s,%s,%s,%s)"
# medicines=[("Montek LC","Rs.149/10 tablets","2012-02-20","2013-02-20",10,"2 mg"),
#            ("Dolo 650","Rs.29.06/15 tablets","2012-07-16","2013-05-16",5,"650 mg"),
#            ("Azivent 500mg","Rs.95.60/5 tablets","2014-08-29","2014-12-29",5,"500 mg"),
#            ("Acitrom 2mg","Rs.377.30/30 pack","2014-11-14","2015-02-14",8,"2 mg"),
#            ("PAN 20mg","Rs.87.55/strip","2016-05-30","2017-05-30",2,"20 mg"),
#            ("Estradiol","$35","2016-10-31","2016-11-25",8,"5 mg"),
#            ("Amikacin","$74","2018-01-05","2018-02-05",8,"250mg/ml"),
#            ("Thyronorm 100mg","Rs.135/bottle","2018-01-05","2018-07-05",100,"100 mg per bottle")]
# mycursor.executemany(form2,medicines)
mydb.commit()