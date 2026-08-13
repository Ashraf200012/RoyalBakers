#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
#print(form)
FlavourName=form.getvalue("FlavourName")
#print(FlavourName)
Status=form.getvalue("Status")
#print(Status)
import os
import mysql.connector
mydb = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", ""),  
    database=os.environ.get("DB_NAME", "royalbakers"), port=int(os.environ.get("DB_PORT", 3306)))
mycursor = mydb.cursor()
query=f"""insert into flavour(FlavourName,Status)VALUES('{FlavourName}','{Status}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" Flavour Master Added Successfully!");
    location.href="FlavourList.py";
    </script>''')
