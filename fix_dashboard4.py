import re

with open(r'c:\xampp\htdocs\RoyalBakers\html\ltr\Dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

def make_card(bg_color, icon, title_html, num_color, result_var):
    return f'''<div class="card" style="background-color:{bg_color} !important; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                    <div class="m-r-20">
                                        <h1 class="m-b-0"> <img src="icons/{icon}" style="width:75px;"></h1>
                                    </div>
                                    <div>
                                        <h6 class="m-b-5" style="font-size:18px; color:black; font-weight:bold;">{title_html}</h6>
                                        <h3 class="m-b-0" style="font-size:36px; font-weight:900; color:{num_color}; margin-top:5px;">{{{result_var}}}</h3>
                                    </div>
                                </div>
                            </div>
                        </div>'''

cards = [
    ('{myresult1}', '#fbb218', '1.png', 'Total Products', 'black'),
    ('{myresult2}', '#ed222d', '2.png', 'Total Categories', 'white'),
    ('{myresult3}', '#fbb218', '3.png', 'Total Customers', 'black'),
    ('{myresult9}', '#ed222d', '3.png', 'Total Active Customers', 'white'),
    ('{myresult10}', '#fbb218', '3.png', 'Total Blocked Customers', 'black'),
    ('{myresult4}', '#ed222d', '4.png', 'Total Orders', 'white'),
    ('{myresult5}', '#fbb218', '5.png', 'Pending Orders', 'black'),
    ('{myresult6}', '#ed222d', '6.png', 'Accepted Orders', 'white'),
]

for var, bg, icon, title_html, num_color in cards:
    idx = content.find(var)
    if idx != -1:
        start_idx = content.rfind('<div class="card"', 0, idx)
        end_idx = content.find('</div>', idx)
        for _ in range(3):
            end_idx = content.find('</div>', end_idx + 1)
        end_idx += 6
        
        replacement = make_card(bg, icon, title_html, num_color, var[1:-1])
        if start_idx != -1 and end_idx != -1:
            content = content[:start_idx] + replacement + content[end_idx:]

with open(r'c:\xampp\htdocs\RoyalBakers\html\ltr\Dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
