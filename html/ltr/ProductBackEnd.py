#!/usr/bin/env python3
import cgi
import cgitb
import os
cgitb.enable()
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
#print(form)
ProductName=form.getvalue("ProductName")
#print(ProductName)
CategoryName=form.getvalue("CategoryName")
#print(CategoryName)
FlavourName=form.getvalue("FlavourName")
#print(FlavourName)
UnitName=form.getvalue("UnitName")
#print(UnitName)
Price=form.getvalue("Price")
#print(Price)
Description=form.getvalue("Description")
#print(Description)
fi=form["photo"]
#print(fi)
fn=os.path.splitext(fi.filename)
#print(fn)
UploadFileName='abc'+fn[1]
#print(UploadFileName)
import mysql.connector
mydb = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", ""),  
    database=os.environ.get("DB_NAME", "royalbakers"), port=int(os.environ.get("DB_PORT", 3306)))
mycursor = mydb.cursor()
query=f"""insert into product(ProductName,CategoryName,FlavourName,UnitName,Price,Description,photo)VALUES('{ProductName}','{CategoryName}','{FlavourName}','{UnitName}','{Price}','{Description}','{UploadFileName}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
Cat_id=mycursor.lastrowid
#print(Cat_id)
upload_dir=f"""Product/{Cat_id}"""
#print(upload_dir)
os.makedirs(upload_dir,exist_ok=True)
file_path=os.path.join(upload_dir,UploadFileName)
open(file_path,'wb').write(fi.file.read())
print(f'''
    <script>alert(" Product  Added Successfully!");
    location.href="ProductList.py";
    </script>''')


