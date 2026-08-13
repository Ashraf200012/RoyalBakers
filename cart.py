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
quantity=form.getvalue("quantity")
#print(quantity)
userid=form.getvalue("userid")
#print(userid)
proid=form.getvalue("proid")
#print(proid)
ProductName=form.getvalue("ProductName")
#print(ProductName)
Price=form.getvalue("Price")
#print(Price)
Photo=form.getvalue("Photo")
#print(Photo)
query=f"""insert into cart(quantity,userid,proid,ProductName,Price,Photo)VALUES('{quantity}','{userid}','{proid}','{ProductName}','{Price}','{Photo}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("product add to cart Successfully!");
    location.href="CartDetail.py?userid={userid}";
    </script>''')
