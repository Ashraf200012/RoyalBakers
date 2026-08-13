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
userid=form.getvalue("userid")
#print(userid)
status="Pending"
query=f"""select * from cart where userid='{userid}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
grand_total=0
for x in myresult:
    Price=int(x[5])
    quantity=int(x[1])
    total=Price*quantity
    grand_total+=total
query1=f"""insert into ordermaster(userid,total_amount,status)VALUES('{userid}','{grand_total}','{status}')"""
#print(query1)
mycursor.execute(query1)
order_id=mycursor.lastrowid
#print(order_id)
for x in myresult:
    proid=x[3]
    ProductName=x[4]
    Photo=x[6]
    Price=x[5]
    quantity=int(x[1])
    total=Price*quantity
    query2=f"""insert into order_details(order_id,proid,ProductName,Photo,Price,quantity,total)VALUES('{order_id}','{proid}','{ProductName}','{Photo}','{Price}','{quantity}','{total}')"""
    #print(query2)
    mycursor.execute(query2)
query3=f"""delete from cart where userid='{userid}'"""
#print(query3)
mycursor.execute(query3)
mydb.commit()
print(f'''
    <script>alert("Order Placed Successfully");
    location.href="Product.py?userid={userid}";
    </script>''')
