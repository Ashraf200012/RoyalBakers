#!/usr/bin/env python3
import cgi
import cgitb
import os
cgitb.enable()
print("Content-Type: text/html\n")
form=cgi.FieldStorage()
#print(form)
FirstName=form.getvalue("FirstName")
#print(FirstName)
MiddleName=form.getvalue("MiddleName")
#print(MiddleName)
LastName=form.getvalue("LastName")
#print(LastName)
PhoneNo=form.getvalue("PhoneNo")
#print(PhoneNo)
Email=form.getvalue("Email")
#print(Email)
Password=form.getvalue("Password")
#print(Password)
fi=form["Photo"]
#print(fi)
fn=os.path.splitext(fi.filename)
#print(fn[0])
UploadFileName='abc'+fn[1]
#print(UploadFileName)
import mysql.connector
mydb = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", ""),  
    database=os.environ.get("DB_NAME", "royalbakers"), port=int(os.environ.get("DB_PORT", 3306)))
mycursor = mydb.cursor()
query=f"""insert into registration (FirstName,MiddleName,LastName,PhoneNo,Email,Password,Photo)VALUES('{FirstName}','{MiddleName}','{LastName}','{PhoneNo}','{Email}','{Password}','{UploadFileName}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
Reg_id=mycursor.lastrowid
#print(Reg_id)
upload_dir=f"""Registration/{Reg_id}"""
#print(upload_dir)
os.makedirs(upload_dir,exist_ok=True)
file_path=os.path.join(upload_dir,UploadFileName)
#print(file_path)
open(file_path,'wb').write(fi.file.read())
print(f'''
    <script>alert("Your Account Created Successfully!");
    location.href="Login.py";
    </script>''')
