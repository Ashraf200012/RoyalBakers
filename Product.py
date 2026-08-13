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
query=f"""select * from product"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
for x in myresult:
    tr_html+=f"""
    <li class="st-col-item st-col">
                                                                        <div class="single-product-wrap">
                                                                            <!-- product-img start -->
                                                                            <div class="product-image">
                                                                                <a href="product-template2.html" class="pro-img">
                                                                                    <img src="html/ltr/Product/{x[0]}/{x[7]}" style="width:250px;height:250px;" class="img-fluid img1" alt="p-1">
                                                                                    <img src="html/ltr/Product/{x[0]}/{x[7]}" style="width:250px;height:250px;" class="img-fluid img2" alt="p-2">
                                                                                </a>
                                                                                <!-- product-label start -->
                                                                                <!-- <div class="product-label">
                                                                                    <span class="new-sale-title">New</span>
                                                                                </div> -->
                                                                                <!-- product-label end -->
                                                                                <!-- product-action start -->
                                                                                <div class="product-action">
                                                                                    <a href="" class="wishlist-product wishlistLink" data-productid="{x[0]}">
                                                                                        <span class="tooltip-text">Wishlist</span>
                                                                                        <span class="wishlist-icon"><i class="feather-heart"></i></span>
                                                                                    </a>
                                                                                    <a href="javascript:void(0)" class="wishlist-product cartLink" data-productid="{x[0]}">
                                                                                        <span class="tooltip-text">Add to cart</span>
                                                                                        <span class="cart-icon"><i class="feather-shopping-bag"></i></span>
                                                                                    </a>
                                                                                   
                                                                                </div>
                                                                                <!-- product-action end -->
                                                                            </div>
                                                                            <!-- product-img end -->
                                                                            <!-- product-content start -->
                                                                            <div class="product-content">
                                                                                <!-- product-rating start-->
                                                                                <div class="product-rating">
                                                                                    <span class="star-rating">
                                                                                        <i class="far fa-star"></i>
                                                                                        <i class="far fa-star"></i>
                                                                                        <i class="far fa-star"></i>
                                                                                        <i class="far fa-star"></i>
                                                                                        <i class="far fa-star"></i>
                                                                                    </span>
                                                                                </div>
                                                                                <!-- product-rating end -->
                                                                                <!-- product-title start -->
                                                                                <h6><a href="">{x[1]}</a></h6>
                                                                                <!-- product-title end -->
                                                                                <!-- product-price start -->
                                                                                <div class="price-box">
                                                                                    <span class="new-price">{x[5]} /- Rs.</span>
                                                                                    
                                                                                </div>
                                                                                <!-- product-price end -->
                                                                                <a href="Productdetails.py?proid={x[0]}" style="margin-top:30px;"><button type="submit" class="btn btn-style2">Product Detail</button></a>
                                                  
                                                                                
                                                                            </div>
                                                                            
                                                                            <!-- product-content end -->
                                                                        </div>
                                                                    </li>
"""
import header
print(f"""
<section class="main-content-wrap shop-page section-ptb">
                <div class="container">
                <div class="section-capture">
                                    <div class="section-title">
                                        <span class="sub-title">All Products</span>
                                        <h2><span>Our Best Products</span></h2>
                                    </div>
                                </div>
                    <div class="row">
                        <div class="col">
                            <div class="pro-grli-wrap product-grid">
                                <div class="collection-img-wrap">
                                    
                                     
                                </div>
                               
                                <div class="get-data-products">
                                    <div class="shop-grid">
                                        <div id="ProductGridContainer">
                                            <div class="product-grid-view">
                                                <div class="shop-product-wrap collection grid-3">
                                                    <div class="row">
                                                        <div class="col">
                                                            <ul class="product-view" id="product-grid">
                                                                {tr_html}
                                                               
                                                            </ul>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                        </div>
                    </div>
                </div>
            </section>
""")
import footer    
