#!/usr/bin/env python3
import cgi
import cgitb
import os
cgitb.enable()
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
#print(form)
id=form.getvalue("id")
#print(id)
import mysql.connector
mydb = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", ""),  
    database=os.environ.get("DB_NAME", "royalbakers"), port=int(os.environ.get("DB_PORT", 3306)))
mycursor = mydb.cursor()
query=f"""delete from product where id={id}"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" Product  Deleted Successfully!");
    location.href="ProductList.py";
    </script>''')
