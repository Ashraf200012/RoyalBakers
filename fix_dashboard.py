import re

with open(r'c:\xampp\htdocs\RoyalBakers\html\ltr\Dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix syntax error on first card
content = content.replace('class="card style="background-color:#fbb218 !important;""', 'class="card" style="background-color:#fbb218 !important;"')

# Create a list of the 8 cards
cards_order = [
    ('Total \nProducts', 'Yellow'),
    ('Total Categories', 'Red'),
    ('Total Customers', 'Yellow'),
    ('Total Active Customers', 'Red'),
    ('Total Blocked Customers', 'Yellow'),
    ('Total Orders', 'Red'),
    ('Pending Orders', 'Yellow'),
    ('Accepted Orders', 'Red'),
]

# Process each one
for title, color in cards_order:
    # Find the card container
    # The title text might have line breaks, so we regex search for it
    title_pattern = title.replace('\n', r'\s+')
    
    # We want to match the <div class="card "...> that contains this title
    # Because HTML can vary, let's find the h6 tag first
    match = re.search(r'(\<div class="card[^>]*\>).*?(\<h6[^>]*\>\s*' + title_pattern + r'\s*\<\/h6\>).*?(\<h6 class="([^"]*)"([^>]*)\>\{[^\}]+\}\<\/h6\>)', content, re.DOTALL | re.IGNORECASE)
    
    if match:
        full_match = match.group(0)
        card_div = match.group(1)
        h6_title = match.group(2)
        h6_num_full = match.group(3)
        h6_num_classes = match.group(4)
        h6_num_rest = match.group(5)
        
        # New styles
        bg_color = '#fbb218' if color == 'Yellow' else '#ed222d'
        new_card_div = re.sub(r'style="background-color:[^"]*"', f'style="background-color:{bg_color} !important;"', card_div)
        if 'style="' not in new_card_div:
            # If style missing completely, add it
            new_card_div = new_card_div.replace('class="card "', f'class="card" style="background-color:{bg_color} !important;"')
            new_card_div = new_card_div.replace('class="card"', f'class="card" style="background-color:{bg_color} !important;"')
        
        # New number styles
        if color == 'Yellow':
            new_h6_num_classes = h6_num_classes.replace('text-white', 'text-dark')
            if 'text-dark' not in new_h6_num_classes:
                new_h6_num_classes += ' text-dark'
        else:
            new_h6_num_classes = h6_num_classes.replace('text-dark', 'text-white')
            if 'text-white' not in new_h6_num_classes:
                new_h6_num_classes += ' text-white'
                
        new_h6_num_full = h6_num_full.replace(f'class="{h6_num_classes}"', f'class="{new_h6_num_classes.strip()}"')
        if color == 'Yellow':
            new_h6_num_full = new_h6_num_full.replace('color:white', 'color:black')
            if 'color:black' not in new_h6_num_full:
                 new_h6_num_full = new_h6_num_full.replace('style="', 'style="color:black;')
        else:
            new_h6_num_full = new_h6_num_full.replace('color:black', 'color:white')
            if 'color:white' not in new_h6_num_full and 'text-white' not in new_h6_num_full:
                 new_h6_num_full = new_h6_num_full.replace('style="', 'style="color:white;')
                 
        new_full_match = full_match.replace(card_div, new_card_div).replace(h6_num_full, new_h6_num_full)
        content = content.replace(full_match, new_full_match)

with open(r'c:\xampp\htdocs\RoyalBakers\html\ltr\Dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
