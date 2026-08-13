#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
import os
import mysql.connector
mydb = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", ""),  
    database=os.environ.get("DB_NAME", "royalbakers"), port=int(os.environ.get("DB_PORT", 3306)))
mycursor =mydb.cursor()
form=cgi.FieldStorage()
#print(form)
id=form.getvalue("id")
#print(id)
query = f"""UPDATE registration SET status='Block' WHERE id={id}"""  
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("Customer Blocked Successfully!");
    location.href="CustomerList.py";
    </script>''')
