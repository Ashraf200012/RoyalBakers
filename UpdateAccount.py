#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")
import os
import mysql.connector
mydb = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", ""),  
    database=os.environ.get("DB_NAME", "royalbakers"), port=int(os.environ.get("DB_PORT", 3306)))
mycursor = mydb.cursor()
form=cgi.FieldStorage()
#print(form)
id=form.getvalue("id")
#print(id)
FirstName=form.getvalue("FirstName")
MiddleName=form.getvalue("MiddleName")
LastName=form.getvalue("LastName")
PhoneNo=form.getvalue("PhoneNo")
Email=form.getvalue("Email")
Password=form.getvalue("Password")
query=f"""update registration set FirstName='{FirstName}',MiddleName='{MiddleName}',LastName='{LastName}',PhoneNo='{PhoneNo}',Email='{Email}',Password='{Password}' where id='{id}'"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("User Information Change  Successfully!");
    location.href="home.py";
    </script>''')
