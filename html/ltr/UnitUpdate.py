#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
#print(form)
id=form.getvalue("id")
#print(id)
UnitName=form.getvalue("UnitName")
#print(UnitName)
Description=form.getvalue("Description")
#print(Description)
import os
import mysql.connector
mydb=mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", ""),  
    database=os.environ.get("DB_NAME", "royalbakers"), port=int(os.environ.get("DB_PORT", 3306)))
mycursor=mydb.cursor()
query=f"""update unit set UnitName='{UnitName}',Description='{Description}' where id='{id}'"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" Unit Master updated   Successfully!");
    location.href="UnitList.py";
    </script>''')
