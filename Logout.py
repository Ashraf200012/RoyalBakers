#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
form=cgi.FieldStorage()
print(f'''
    <script>
    localStorage.clear();
    alert("logout Successfully!");
    location.href="login.py";
    </script>''')
