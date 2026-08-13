import re

with open(r'c:\xampp\htdocs\RoyalBakers\html\ltr\Dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all card styles with the correct ones
content = re.sub(r'class="card[^"]*" style="background-color:[^"]*"', 'class="card"', content)
content = re.sub(r'class="card" style="background-color:[^"]*"', 'class="card"', content)

# 1. Total Products
content = re.sub(r'(<div class="card")(>.*?Total\s+Products.*?<h6 class="([^"]*)")([^>]*>\{myresult1\})', r'\1 style="background-color:#fbb218 !important;"\2 style="color:black;"\4', content, flags=re.DOTALL)
content = content.replace('text-white  m-b-0" style="color:black;"', 'text-dark m-b-0" style="color:black;"')

# 2. Total Categories
content = re.sub(r'(<div class="card")(>.*?Total\s+Categories.*?<h6 class="([^"]*)")([^>]*>\{myresult3\})', r'\1 style="background-color:#ed222d !important;"\2 style="color:white;"\4', content, flags=re.DOTALL)

# 3. Total Customers
content = re.sub(r'(<div class="card")(>.*?Total\s+Customers.*?<h6 class="([^"]*)")([^>]*>\{myresult2\})', r'\1 style="background-color:#fbb218 !important;"\2 style="color:black;"\4', content, flags=re.DOTALL)

# 4. Total Active Customers
content = re.sub(r'(<div class="card")(>.*?Total\s+Active\s+Customers.*?<h6 class="([^"]*)")([^>]*>\{myresult4\})', r'\1 style="background-color:#ed222d !important;"\2 style="color:white;"\4', content, flags=re.DOTALL)

# 5. Total Blocked Customers
content = re.sub(r'(<div class="card")(>.*?Total\s+Blocked\s+Customers.*?<h6 class="([^"]*)")([^>]*>\{myresult5\})', r'\1 style="background-color:#fbb218 !important;"\2 style="color:black;"\4', content, flags=re.DOTALL)

# 6. Total Orders
content = re.sub(r'(<div class="card")(>.*?Total\s+Orders.*?<h6 class="([^"]*)")([^>]*>\{myresult6\})', r'\1 style="background-color:#ed222d !important;"\2 style="color:white;"\4', content, flags=re.DOTALL)

# 7. Pending Orders
content = re.sub(r'(<div class="card")(>.*?Pending\s+Orders.*?<h6 class="([^"]*)")([^>]*>\{myresult7\})', r'\1 style="background-color:#fbb218 !important;"\2 style="color:black;"\4', content, flags=re.DOTALL)

# 8. Accepted Orders
content = re.sub(r'(<div class="card")(>.*?Accepted\s+Orders.*?<h6 class="([^"]*)")([^>]*>\{myresult8\})', r'\1 style="background-color:#ed222d !important;"\2 style="color:white;"\4', content, flags=re.DOTALL)

with open(r'c:\xampp\htdocs\RoyalBakers\html\ltr\Dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
