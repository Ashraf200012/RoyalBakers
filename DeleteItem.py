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
userid=form.getvalue("userid")
#print(userid)
query=f"""delete from cart where id='{id}'"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("Item Deleted from the  cart Successfully!");
    location.href="CartDetail.py?userid={userid}";
    </script>''')
