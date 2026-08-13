#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
print("""
<!DOCTYPE html>
<html lang="en">
    
<!-- Mirrored from spacingtech.com/html/banno/banno-ltr/index-4.html by HTTrack Website Copier/3.x [XR&CO'2014], Sun, 19 Jul 2026 08:36:21 GMT -->
<!-- Added by HTTrack --><meta http-equiv="content-type" content="text/html;charset=UTF-8" /><!-- /Added by HTTrack -->
<head>
        <meta charset="utf-8">
        <meta name="description" content="A best stylish, creative, modern responsive template for different eCommerce business or industries."/>
        <meta name="keywords" content="food template, bakery products, html, eCommerce html template, responsive, pizza, burger, furniture, mobile, watches, electronics, computers accessories, toys, jewellery, restaurant accessories"/>
        <meta name="author" content="spacingtech_webify">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- title -->
        <title>Banno - The Bakery & Chocolate eCommerce HTML5 Template</title>
        <!-- favicon -->
        <link rel="icon" type="image/x-icon" href="img/logo/favicon.png">
        <!-- bootstrap css -->
        <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
        <!-- magnific-popup css -->
        <link rel="stylesheet" type="text/css" href="css/magnific-popup.css">
        <!-- animate css -->
        <link rel="stylesheet" type="text/css" href="css/animate.min.css">
        <!-- bootstrap icon -->
        <link rel="stylesheet" type="text/css" href="css/bootstrap-icons.css">
        <!-- font-awesome css -->
        <link rel="stylesheet" type="text/css" href="css/all.min.css">
        <!--fether css -->
        <link rel="stylesheet" type="text/css" href="css/feather.css">
        <!-- owl css -->
        <link rel="stylesheet" type="text/css" href="css/owl.carousel.min.css">
        <link rel="stylesheet" type="text/css" href="css/owl.theme.default.min.css">
        <!-- swiper-bundle css -->
        <link rel="stylesheet" type="text/css" href="css/swiper-bundle.min.css">
        <!-- slick slider css -->
        <link rel="stylesheet" type="text/css" href="css/slick.css">
        <!-- style css -->
        <link rel="stylesheet" type="text/css" href="css/style4.css">
         <link rel="stylesheet" type="text/css" href="css/other-page.css">
         <link rel="stylesheet" type="text/css" href="css/style.css">
         <link rel="stylesheet" type="text/css" href="css/blog.css">
         <link rel="stylesheet" type="text/css" href="css/collection-page.css">
          <link rel="stylesheet" type="text/css" href="css/product-page.css">
            <link rel="stylesheet" type="text/css" href="css/account.css">
    </head>
    <body>
        <!-- top-notification-bar start -->
        <section class="top-notification-bar">
            <div class="container">
                <div class="row">
                    <div class="col">
                       <marquee direction="left" style="color:white;font-weight:bold;font-size:25px;">Turning Your Dreams into Delicious Reality</marquee>
                    </div>
                </div>
            </div>
        </section>
        <!-- top-notification-bar end -->
        <!-- header start -->
        <header class="header-area">
            <div class="container-fluid">
                <div class="row">
                    <div class="col">
                        <div class="header-main">
                            <!-- header logo start -->
                            <div class="header-element logo">
                                <a href="home.py" class="theme-header-logo">
                                    <img src="img/logo.png" class="img-fluid" alt="logo">
                                </a>
                            </div>
                            <!-- header logo end -->
                            <!-- header megamenu start -->
                            <div class="header-element megamenu-content">
                                <div class="mainwrap collapse show" id="main-collapse">
                                    <ul class="main-menu">
                                        <li class="menu-link">
                                            <a href="home.py" class="link-title">
                                                <span class="sp-link-title">Home</span>
                                                  </a>
                                            
                                            
                                        </li>
                                        <li class="menu-link">
                                            <a href="About.py" class="link-title">
                                                <span class="sp-link-title">About  </span>
                                          </a>
                                             
                                           
                                        </li>
                                        <li class="menu-link">
                                            <a href="Contact.py" class="link-title">
                                                <span class="sp-link-title">Contact    </span>
                                          </a>
                                         </li>
                                         <li class="menu-link">
                                            <a href="Category.py" class="link-title">
                                                <span class="sp-link-title">Category    </span>
                                          </a>
                                         </li>
                                          <li class="menu-link">
                                            <a href="Product.py" class="link-title">
                                                <span class="sp-link-title">Products    </span>
                                          </a>
                                         </li>
                                         <li class="menu-link" id="loginMenu">
    <a href="Login.py" class="link-title">
        <span class="sp-link-title" id="loginText">Login</span>
    </a>
</li>

<li class="menu-link" id="profileMenu" style="display:none;">
    <a href="blog-grid.html" class="link-title">
        <span class="sp-link-title">My Profile</span>
        <span class="menu-arrow"><i class="feather-chevron-down"></i></span>
    </a>

    <a href="#desk-single-blog" data-bs-toggle="collapse" class="link-title link-title-lg">
        <span class="sp-link-title">My Profile</span>
        <span class="menu-arrow"><i class="feather-chevron-down"></i></span>
    </a>

    <div class="menu-dropdown single-menu collapse" id="desk-single-blog">
        <ul class="container ul p-0">
            <li class="singlemenu-li"><a href="" class="singlelink-title" id="myCartLink">My Cart</a></li>
            <li class="singlemenu-li"><a href="" class="singlelink-title" id="myWishlistLink">My Wishlist</a></li>
            <li class="singlemenu-li"><a href="" class="singlelink-title" id="myOrderLink">My Orders</a></li>
            <li class="singlemenu-li"><a href="" class="singlelink-title" id="myAccountLink">My Account</a></li>
        </ul>
    </div>
</li>

<li class="menu-link" id="registerMenu">
    <a href="Registration.py" class="link-title">
        <span class="sp-link-title">Register</span>
    </a>
</li>

<li class="menu-link" id="logoutMenu" style="display:none;">
    <a href="Logout.py" class="link-title">
        <span class="sp-link-title">Logout</span>
    </a>
</li>
                                        
                                    </ul>
                                </div>
                            </div>
                            <!-- header megamenu end -->
                            <!-- right-block-box start-->
                            <div class="header-element right-block-box">
                                <ul class="shop-element">
                                    <!-- button toggler start -->
                                    <li class="side-wrap toggle-wrap">
                                        <button class="toggler-button"><i class="feather-menu"></i></button>
                                    </li>
                                    <!-- button toggler end -->
                                     
                                    
                                    
                                </ul>
                            </div>
                            <!-- right-block-box end-->
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <!-- header end -->
        <script>

let FirstName=localStorage.getItem("FirstName");
//console.log(FirstName);

let Photo=localStorage.getItem("Photo");
//console.log(Photo);

let userid=localStorage.getItem("id");
//console.log(userid);

if(FirstName)
{
         let imagePath = `Registration/${userid}/${Photo}`;
console.log(imagePath);

    document.getElementById("loginText").innerHTML = `
    <img src="${imagePath}" 
         alt="Profile" 
         style="width:30px;height:30px;border-radius:50%;margin-right:8px;object-fit:cover;vertical-align:middle;">
    <span>${FirstName}</span>`;

    

     
    document.querySelector("#loginMenu a").href = "#";
    document.getElementById("myAccountLink").href = `myaccount.py?userid=${userid}`;
    document.getElementById("myWishlistLink").href = `mywishlist.py?userid=${userid}`;
    document.getElementById("myCartLink").href = `CartDetail.py?userid=${userid}`;
    document.getElementById("myOrderLink").href = `MyOrder.py?userid=${userid}`;

    document.getElementById("profileMenu").style.display = "block";

     
    document.getElementById("logoutMenu").style.display = "block";

     
    document.getElementById("registerMenu").style.display = "none";

} else {
    
        

    document.querySelector("#loginMenu a").href = "Login.py";
    
    document.getElementById("myAccountLink").href = "Login.py";

    document.getElementById("myWishlistLink").href = "Login.py";
   
    document.getElementById("myCartLink").href = "Login.py";
    
    document.getElementById("myOrderLink").href = "Login.py";

    document.getElementById("profileMenu").style.display = "none";

     
    document.getElementById("logoutMenu").style.display = "none";

     
    document.getElementById("registerMenu").style.display = "block";
}




</script>
""")
