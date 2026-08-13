#!/usr/bin/env python3
import cgi
import cgitb
import os
cgitb.enable()
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
#print(form)
Email=form.getvalue("Email")
#print(Email)
Password=form.getvalue("Password")
#print(Password)
import mysql.connector
mydb = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", ""),  
    database=os.environ.get("DB_NAME", "royalbakers"), port=int(os.environ.get("DB_PORT", 3306)))
mycursor = mydb.cursor()
query=f"""select * from adminlogin where Email='{Email}' AND Password='{Password}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
#print(myresult)
if mycursor.rowcount==1:
    print(f'''
    <script>
    localStorage.clear();
    localStorage.setItem("id",'{myresult[0]}');
    localStorage.setItem("username",'{myresult[3]}');
    localStorage.setItem("Email",'{myresult[1]}');
    alert(" login  Successfully!");
    location.href="UnitList.py";
    </script>''')
else:
    print(f'''
        <script>alert(" login  UnSuccessfully!");
        location.href="adminlogin.py";
        </script>''')

   
