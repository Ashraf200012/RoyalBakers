#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
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
query=f"""Select * from cart where userid='{userid}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
grand_total=0
for x in myresult:
    Price=int(x[5])
    quantity=int(x[1])
    total=Price*quantity
    grand_total+=total
    tr_html+=f"""
<!---for loop row star---->
                                    <div class="wishlist-area">
                                        <div class="wishlist-details">
                                            
                                            <div class="wishlist-all-pro">
                                                <div class="wishlist-pro" style="width:100%">
                                                    <div class="wishlist-pro-image" style="width:100%">
                                                        <a href="">
                                                            <img src="html/ltr/Product/{x[3]}/{x[6]}" class="img-fluid" alt="p-1" style="width:150px">
                                                        </a>
                                                    </div>
                                                    <div class="pro-details">
                                                        <h4>{x[4]}</h4>
                                                    </div>

                                                    <div class="pro-details">
                                                        <h4>{x[5]} /-Rs.</h4> 
                                                    </div>

                                                    <div class="pro-details">
                                                        <h4> {x[1]} </h4> 
                                                    </div>

                                                     <div class="pro-details">
                                                        <h4> {total} /-Rs.</h4> 
                                                    </div>

                                                     <div class="pro-details">
                                                       <a href="DeleteItem.py?id={x[0]}&userid={userid}"><button class="btn btn-style2" >Delete</button></a>
                                                    </div>
                                                    
                                                      </div>
                                                 
                                                 
                                            </div>
                                        </div>
                                    </div>
                                   <!--- for loop row end----->
"""
import header

print(f"""
<section class="order-histry-area section-ptb">
    <div class="container">
        <div class="row">
            <div>

                <div class="profile-wishlist">

                    <div class="section-capture">
                        <div class="section-title">
                            <span class="sub-title">Cart Details</span>
                            <h2><span>My Cart</span></h2>
                        </div>
                    </div>

                    <!-- Heading Row -->
                    <div class="wishlist-area" style="font-weight:bold; background:#f5f5f5; padding:15px; border-radius:5px;">
                        <div class="wishlist-details">
                            <div class="wishlist-all-pro">
                                <div class="wishlist-pro" style="width:100%; display:flex; align-items:center;">

                                    <div style="width:20%; text-align:center;">
                                        Image
                                    </div>

                                    <div style="width:16%; text-align:center;">
                                        Product Name
                                    </div>

                                    <div style="width:15%; text-align:center;">
                                        Price
                                    </div>

                                    <div style="width:25%; text-align:center;">
                                        Quantity
                                    </div>

                                    <div style="width:25%; text-align:center;">
                                        Total
                                    </div>

                                    <div style="width:25%; text-align:center;">
                                        Delete Item
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>

                    {tr_html}

                </div>

            </div>
        </div>
    </div>

    <div class="pro-details text-center mt-4">
    <h3 style="padding:30px; color:#ed222d; ">Grand Total =<span>{grand_total}</span></h3>
        <a href="Checkout.py?userid={userid}" class="add-wishlist btn btn-style">
            Checkout
        </a>
    </div>

</section>
""")

import footer
