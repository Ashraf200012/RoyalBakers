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
query=f"""Select * from category"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
for x in myresult:
    tr_html+=f"""
                  <li class="banner-wrap banner-hover">
                                    <div class="box-img">
                                        <a href="">
                                            <img src="html/ltr/Category/{x[0]}/{x[3]}" class="img-fluid" alt="category-05" style="width:300px;height:300px;">
                                        </a>
                                    </div>
                                    <div class="custom-banner-content">
                                        <h2>{x[1]}</h2>
                                        <a href="CategoryDetail.py?CategoryName={x[1]}" class="banner-link" style="color:#ed222d">SHOW MORE</a>
                                    </div>
                                </li>  
                    
    """
query1=f"""SELECT * from product"""
#print(query1)
mycursor.execute(query1)
myresult1=mycursor.fetchall()
#print(myresult1)
tr_pro=''
for y in myresult1:
    tr_pro+=f"""
                     <div class="swiper-slide">
                                            <!-- product start -->
                                            <div class="single-product-wrap">
                                                <!-- product-img start -->
                                                <div class="product-image">
                                                    <a href="product-template.html" class="pro-img">
                                                        <img src="html/ltr/Product/{y[0]}/{y[7]}" style="height:300px;width:300px;" class="img-fluid img1" alt="p-73">
                                                        <img src="html/ltr/Product/{y[0]}/{y[7]}" style="height:300px;width:300px;" class="img-fluid img2" alt="p-74">
                                                    </a>
                                                    <!-- product-action start -->
                                                    <div class="product-action">
                                                        <a href="" class="wishlist-product wishlistLink" data-productid="{y[0]}">
                                                            <span class="tooltip-text">Wishlist</span>
                                                            <span class="wishlist-icon"><i class="feather-heart"></i></span>
                                                        </a>
                                                        <a href="javascript:void(0)" class="wishlist-product cartLink" data-productid="{y[0]}">
                                                            <span class="tooltip-text">Add to cart</span>
                                                            <span class="cart-icon"><i class="feather-shopping-bag"></i></span>
                                                        </a>
                                                    
                                                    </div>
                                                    <!-- product-action end -->
                                                </div>
                                                <!-- product-img end -->
                                                <!-- product-content start -->
                                                <div class="product-content">
                                                    <!-- product-title start -->
                                                    <h6><a href="">{y[1]}</a></h6>
                                                    <!-- product-title end -->
                                                    <!-- product-price start -->
                                                    <div class="price-box">
                                                        <span class="new-price">{y[5]} /-Rs.</span>
                                                         
                                                    </div>
                                                    <!-- product-price end -->
                                                    <!-- product-action start -->
                                                    <div class="product-action">
                                                        <a href="javascript:void(0)" class="add-to-cart">
                                                            <span class="tooltip-text">Add to cart</span>
                                                            <span class="cart-icon"><i class="feather-shopping-bag"></i></span>
                                                        </a>
                                                        <a href="#quickview" class="quick-view" data-bs-toggle="modal" data-bs-target="#quickview">
                                                            <span class="tooltip-text">Quickview</span>
                                                            <span class="quickview-icon"><i class="feather-eye"></i></span>
                                                        </a>
                                                        <a href="wishlist-product.html" class="wishlist-product">
                                                            <span class="tooltip-text">Wishlist</span>
                                                            <span class="wishlist-icon"><i class="feather-heart"></i></span>
                                                        </a>
                                                    </div>
                                                    <!-- product-action end -->
                                                    <a href="Productdetails.py?proid={y[0]}" style="margin-top:30px;"><button type="submit" class="btn btn-style2">Product Detail</button></a>
                                                </div>
                                                
                                                <!-- product-content end -->
                                            </div>
                                            <!-- product end -->
                                        </div>
    """
import header
print(f"""

        <main>
            <!-- home-slider start -->
<section class="slider-content">
                <div class="home-slider owl-carousel owl-theme" id="home-slider">
                    <div class="item active">
                        <div class="slide-image">
                            <img src="img/slider/cake-slider-06.jpg" class="img-fluid desk-img" alt="cake-slider-06">
                            <img src="img/slider/mobile-slider-07.jpg" class="img-fluid mobile-img" alt="mobile-slider-07">
                            <div class="container slider-info-content">
                                <div class="row">
                                    <div class="col">
                                        <div class="slider-text-info slider-content-center slider-text-center">
                                            <h2 class="e1"><span>Chocolate Cup Cake</span></h2>
                                            <p class="e1">Chocolate cup cake with dried fruit</p>
                                            <a href="collection.html" class="btn btn-style e1">Shop now</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="item">
                        <div class="slide-image">
                            <img src="img/slider/cake-slider-07.jpg" class="img-fluid desk-img" alt="slider-1">
                            <img src="img/slider/mobile-slider-08.jpg" class="img-fluid mobile-img" alt="mobile-slider-08">
                            <div class="container slider-info-content">
                                <div class="row">
                                    <div class="col">
                                        <div class="slider-text-info slider-content-center slider-text-center">
                                            <h2 class="e1"><span>Pastries served with  coffee</span></h2>
                                            <p class="e1">The sweetness of the cake combined with the slightly bitter taste of coffee</p>
                                            <a href="collection.html" class="btn btn-style e1">Shop now</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="item">
                        <div class="slide-image">
                            <img src="img/slider/cake-slider-08.jpg" class="img-fluid desk-img" alt="slider-1">
                            <img src="img/slider/mobile-slider-09.jpg" class="img-fluid mobile-img" alt="img/slider/mobile-slider-09">
                            <div class="container slider-info-content">
                                <div class="row">
                                    <div class="col">
                                        <div class="slider-text-info slider-content-center slider-text-center">
                                            <h2 class="e1"><span>Fruity cream cake</span></h2>
                                            <p class="e1">Fatty cream and cool taste of fresh fruit</p>
                                            <a href="collection.html" class="btn btn-style e1">Shop now</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            
            <!-- Category start -->
            <section class="banner2 section-ptb">
                <div class="container-fluid">
                    <div class="row">
                        <div class="col">
                            <div class="banner-category">
                                <div class="section-capture">
                                    <div class="section-title">
                                        <h2>Shop by Category</h2>
                                        <span class="sub-title">My categories</span>
                                    </div>
                                </div>
                            </div>
                            <ul class="banner-block">
                                {tr_html}
                                
                            </ul>
                        </div>
                    </div>
                </div>
            </section>
            <!-- Category end -->

            <!-----------------product div start---------------->
            <section class="special-category collection-category-template section-ptb">
                <div class="container">
                    <div class="row">
                        <div class="col">
                            <div class="collection-category">
                                <div class="section-capture">
                                    <div class="section-title">
                                        <h2><Span>Our products</Span></h2>
                                        <span class="sub-title">Best collection</span>
                                    </div>
                                </div>
                            </div>
                            <div class="special-category-wrap" style="">
                                <div class="special-category-slider swiper" id="special-category">
                                    <div class="swiper-wrapper">
                                       {tr_pro}
                                        
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
  <!-----------------product div end---------------->
</main>
""")
import footer
