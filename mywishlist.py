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
query=f"""select product.id,product.ProductName,product.Description,product.Price,product.Photo from wishlist INNER JOIN product ON wishlist.productid=product.id where wishlist.userid='{userid}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
for x in myresult:
    tr_html+=f"""
                    <!---for loop row star---->
                                    <div class="wishlist-area">
                                        <div class="wishlist-details">
                                            
                                            <div class="wishlist-all-pro">
                                                <div class="wishlist-pro" style="width:100%">
                                                    <div class="wishlist-pro-image" style="width:100%">
                                                        <a href="">
                                                            <img src="html/ltr/Product/{x[0]}/{x[4]}" class="img-fluid" alt="p-1" style="width:150px">
                                                        </a>
                                                    </div>
                                                    <div class="pro-details">
                                                        <h4>{x[1]}</h4>
                                                    </div>

                                                    

                                                    <div class="pro-details">
                                                        <h4>{x[3]} /-Rs.</h4> 
                                                    </div>
                                                     <div class="pro-details">
                                                         <a href="Productdetails.py?proid={x[0]}" class="add-wishlist btn btn-style">Product Details</a>
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
                               
                                <!-- profile-wishlist start -->
                                <div class="profile-wishlist">
                                    <div class="section-capture">
                                <div class="section-title">
                                    <span class="sub-title">Wishlist Items</span>
                                    <h2><span>My Wishlist</span></h2>
                                </div>
                            </div>

                            {tr_html}
                                </div>
                                <!-- profile-wishlist end -->
                            </div>
                         
                    </div>
                </div>
            </section>
""")
import footer   
