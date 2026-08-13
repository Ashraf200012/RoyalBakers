import re
with open(r'c:\xampp\htdocs\RoyalBakers\html\ltr\header.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_nav = '''                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:black;"></i> <span class="hide-menu" style="color:black;font-weight:bold">... DASHBOARD</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="Dashboard.py" aria-expanded="false"><i class="mdi mdi-format-list-bulleted" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Admin Dashboard</span></a></li>
                        
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:black;"></i> <span class="hide-menu" style="color:black;font-weight:bold">... UNIT</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="UnitMaster.py" aria-expanded="false"><i class="mdi mdi-plus-circle-outline" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Add Unit</span></a></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="UnitList.py" aria-expanded="false"><i class="mdi mdi-format-list-bulleted" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Unit List</span></a></li>
                        
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:black;"></i> <span class="hide-menu" style="color:black;font-weight:bold">... FLAVOURS</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="FlavourMaster.py" aria-expanded="false"><i class="mdi mdi-plus-circle-outline" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Add Flavour</span></a></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="FlavourList.py" aria-expanded="false"><i class="mdi mdi-format-list-bulleted" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Flavour List</span></a></li>
                        
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:black;"></i> <span class="hide-menu" style="color:black;font-weight:bold">... CATEGORY</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="Category.py" aria-expanded="false"><i class="mdi mdi-plus-circle-outline" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Add Category</span></a></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="CategoryList.py" aria-expanded="false"><i class="mdi mdi-format-list-bulleted" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Category List</span></a></li>
                        
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:black;"></i> <span class="hide-menu" style="color:black;font-weight:bold">... PRODUCT</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="Product.py" aria-expanded="false"><i class="mdi mdi-plus-circle-outline" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Add Product</span></a></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="ProductList.py" aria-expanded="false"><i class="mdi mdi-format-list-bulleted" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Product List</span></a></li>
                        
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:black;"></i> <span class="hide-menu" style="color:black;font-weight:bold">... CUSTOMER</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="CustomerList.py" aria-expanded="false"><i class="mdi mdi-format-list-bulleted" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Customer List</span></a></li>
                        
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:black;"></i> <span class="hide-menu" style="color:black;font-weight:bold">... PASSWORD</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="" id="ChangePasswordLink" aria-expanded="false"><i class="mdi mdi-lock-reset" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Change Password</span></a></li>
                        
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:black;"></i> <span class="hide-menu" style="color:black;font-weight:bold">... ORDER</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="allOrders.py" aria-expanded="false"><i class="mdi mdi-format-list-bulleted" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Order List</span></a></li>
                    </ul>'''

pattern = r'(\<li class="nav-small-cap"\>\<i class="mdi mdi-dots-horizontal" style="color:black;"\>\<\/i\> \<span class="hide-menu" style="color:black;font-weight:bold"\>Dashboard\<\/span\>\<\/li\>.*?)(\s*\<\/ul\>\s*\<\/nav\>)'
new_content = re.sub(pattern, new_nav + r'\2', content, flags=re.DOTALL)

with open(r'c:\xampp\htdocs\RoyalBakers\html\ltr\header.py', 'w', encoding='utf-8') as f:
    f.write(new_content)
