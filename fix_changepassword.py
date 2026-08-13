import sys

file_path = r'c:\xampp\htdocs\RoyalBakers\html\ltr\ChangePassword.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacement = '''query=f"""select * from adminlogin where id={id}"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()

# Fallback if id is invalid or deleted (e.g. stale localStorage)
if myresult is None:
    mycursor.execute("SELECT * FROM adminlogin LIMIT 1")
    myresult=mycursor.fetchone()
'''

content = content.replace('''query=f"""select * from adminlogin where id={id}"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()''', replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
