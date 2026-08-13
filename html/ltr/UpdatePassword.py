#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
#print(form)
id=form.getvalue("id")
#print(id)
Email=form.getvalue("Email")
#print(Email)
Password=form.getvalue("Password")
#print(Password)
username=form.getvalue("username")
#print(username)
import os
import mysql.connector
mydb = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", ""),  
    database=os.environ.get("DB_NAME", "royalbakers"), port=int(os.environ.get("DB_PORT", 3306)))
mycursor = mydb.cursor()
query=f"""update adminlogin set Email='{Email}',Password='{Password}',username='{username}' where id='{id}'"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" Admin Information Changed  Successfully!");
    location.href="adminlogin.py";
    </script>''')
