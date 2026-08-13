import re

with open(r'c:\xampp\htdocs\RoyalBakers\html\ltr\Dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

def make_card(bg_color, icon, title, title_html, text_class, result_var):
    return f'''<div class="card" style="background-color:{bg_color} !important;">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                    <div class="m-r-10">
                                        <h1 class="m-b-0"> <img src="icons/{icon}" style="width:80px;"></h1></div>
                                    <div>
                                        <h6 class="m-b-5 op-7" style="font-size:20px;color:black">{title_html}</h6>
                                        <h6 class="{text_class} m-b-0" style="font-size:30px;text-align: center;">{{{result_var}}}</h6>
                                    </div>
                                </div>
                            </div>
                        </div>'''

# We will regex replace each card by looking for the unique variable e.g. {myresult1}
cards = [
    ('{myresult1}', '#fbb218', '1.png', 'Total Products', 'Total <br>\nProducts', 'text-dark'),
    ('{myresult2}', '#ed222d', '2.png', 'Total Categories', 'Total \nCategories', 'text-white'),
    ('{myresult3}', '#fbb218', '3.png', 'Total Customers', 'Total \nCustomers', 'text-dark'),
    ('{myresult9}', '#ed222d', '3.png', 'Total Active Customers', 'Total Active \nCustomers', 'text-white'),
    ('{myresult10}', '#fbb218', '3.png', 'Total Blocked Customers', 'Total Blocked \nCustomers', 'text-dark'),
    ('{myresult4}', '#ed222d', '4.png', 'Total Orders', ' Total Orders', 'text-white'),
    ('{myresult5}', '#fbb218', '5.png', 'Pending Orders', 'Pending Orders', 'text-dark'),
    ('{myresult6}', '#ed222d', '6.png', 'Accepted Orders', 'Accepted \nOrders', 'text-white'),
]

for var, bg, icon, title_plain, title_html, text_class in cards:
    # Match the <div class="card"...> all the way to </h6></div></div></div></div>
    # Using the variable as the unique anchor
    var_escaped = var.replace('{', r'\{').replace('}', r'\}')
    pattern = r'<div class="card"[^>]*>.*?\{' + var[1:-1] + r'\}.*?</div>\s*</div>\s*</div>\s*</div>'
    replacement = make_card(bg, icon, title_plain, title_html, text_class, var[1:-1])
    
    # We must be careful because the regex might be greedy or not greedy enough.
    # A safer way is to find the index of the variable, then find the nearest preceding <div class="card" and the nearest following closing tags.
    idx = content.find(var)
    if idx != -1:
        start_idx = content.rfind('<div class="card"', 0, idx)
        end_idx = content.find('</div>', idx)
        for _ in range(3): # Find the 4th </div> after the variable
            end_idx = content.find('</div>', end_idx + 1)
        end_idx += 6 # Include the '</div>'
        
        # Replace the chunk
        if start_idx != -1 and end_idx != -1:
            content = content[:start_idx] + replacement + content[end_idx:]

with open(r'c:\xampp\htdocs\RoyalBakers\html\ltr\Dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
