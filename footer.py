#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
#print("Content-Type: text/html\n")
print("""
   <footer>
            <div class="footer-top-area section-ptb" style="background-color:#fbb218;">
                <div class="container">
                    <div class="row">
                        <div class="col">
                            <div class="footer-list-wrap">
                                <ul class="footer-list">
                                    <li class="ftlink-li ft-info">
                                        <div class="footer-logo">
                                            <a href="index-4.html" class="theme-footer-logo">
                                                <img src="img/logo.png" class="img-fluid" alt="logo" style="width:155px;">
                                            </a>
                                        </div>
                                        
                                    </li>
                                    <li class="ftlink-li ft-menu">
                                        <div class="footer-menu">
                                            <h6 class="ft-title">Quick link</h6>
                                            <div class="footer-sublist">
                                                <ul>
                                                    <li class="ftsublink-li">
                                                        <a href="" class="ft-sublink">About us</a>
                                                    </li>
                                                    <li class="ftsublink-li">
                                                        <a href="" class="ft-sublink">Contact us</a>
                                                    </li>
                                                    <li class="ftsublink-li">
                                                        <a href="" class="ft-sublink"> Products</a>
                                                    </li>
                                                    <li class="ftsublink-li">
                                                        <a href="" class="ft-sublink">Category</a>
                                                    </li>
                                                     
                                                </ul>
                                            </div>
                                        </div>
                                    </li>
                                    <li class="ftlink-li ft-social">
                                        <div class="footer-menu">
                                            <h6 class="ft-title">My Details</h6>
                                            <div class="footer-sublist">
                                                <div class="footer-social">
                                                    <ul>
                                                        <li>
                                                            <a href=""><span class="icon-title">Login</span></a>
                                                        </li>
                                                        <li>
                                                            <a href=""><span class="icon-title">Register</span></a>
                                                        </li>
                                                        <li>
                                                            <a href=""><span class="icon-title">Logout</span></a>
                                                        </li>
                                                        
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </li>
                                    <li class="ftlink-li ft-contact">
                                        <div class="footer-menu">
                                            <h6 class="ft-title">Contact us</h6>
                                            <div class="footer-sublist">
                                                <ul class="footer-contact">
                                                    <li class="ftcon-li ftcon-li-add">
                                                        <span class="con-icon"><i class="bi bi-geo"></i></span>
                                                        <span class="con-add" style="color:black;">
                                                            <span>Akshya nagar 1st block 1st,</span>
                                                            <span>rammurthy nagar, bangalore</span>
                                                        </span>
                                                    </li>
                                                    <li class="ftcon-li">
                                                        <span class="con-icon"><i class="bi bi-telephone"></i></span>
                                                        <a href="tel:(+33)123456789" class="con-add"  style="color:black;">(+33) 1 23 45 67 89</a>
                                                    </li>
                                                    <li class="ftcon-li">
                                                        <span class="con-icon"><i class="bi bi-envelope"></i></span>
                                                        <a href="mailto:demo@demo.com" class="con-add"  style="color:black;">demo@demo.com</a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="footer-bottom-area">
                <div class="container">
                    <div class="row">
                        <div class="col">
                            <ul class="ft-bottom">
                                <li class="grid-wrapper copy-right">
                                    <p>
                                        <span>Copyright</span>
                                        <span class="copy-icon"><i class="far fa-copyright"></i></span>
                                        <span  style="color:black;">2026 by Royal Bakers</span>
                                    </p>
                                </li>
                                
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
        
        <!-- search-popup start -->
        <div class="modal fade" id="seachmodal">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-body">
                        <div class="container">
                            <div class="row">
                                <div class="col">
                                    <div class="crap-search">
                                        <!-- search-button-close start -->
                                        <div class="button-close">
                                            <button type="button" class="search-close" data-bs-dismiss="modal"><i class="feather-x"></i></button>
                                        </div>
                                        <!-- search-button-close end -->
                                        <!-- search-form start -->
                                        <form method="get" class="search-bar">
                                            <div class="form-search">
                                                <input type="search" name="q" placeholder="Search product here.." class="input-text" required>
                                                <button type="submit" class="search-btn"><i class="feather-search"></i></button>
                                            </div>
                                        </form>
                                        <!-- search-form end -->
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- search-popup end -->
        <!-- mobile-menu start -->
        <div class="mobile-menu" id="menu-toggle">
            <div class="main-menu-area">
                <!-- box-header start -->
                <div class="box-header"><button class="close-menu" type="button"><i class="feather-x"></i></button></div>
                <!-- box-header end -->
                <div class="megamenu-content">
                    <div class="mainwrap collapse show" id="resp-main">
                        <ul class="main-menu">
                            <li class="menu-link">
                                <a href="home.py" class="link-title">
                                    <span class="sp-link-title">Home</span>
                                      </a>
                                
                            </li>
                            <li class="menu-link">
                                <a href="home.py" class="link-title">
                                    <span class="sp-link-title">About</span>
                                      </a>
                                
                            </li>
                            <li class="menu-link">
                                <a href="home.py" class="link-title">
                                    <span class="sp-link-title">Contact</span>
                                      </a>
                                
                            </li>
                            <li class="menu-link">
                                <a href="home.py" class="link-title">
                                    <span class="sp-link-title">Category</span>
                                      </a>
                                
                            </li>
                            <li class="menu-link">
                                <a href="home.py" class="link-title">
                                    <span class="sp-link-title">Product</span>
                                      </a>
                                
                            </li>
                            <li class="menu-link">
                                <a href="home.py" class="link-title">
                                    <span class="sp-link-title">Login</span>
                                      </a>
                                
                            </li>
                            
                            <li class="menu-link">
                                <a href="home.py" class="link-title">
                                    <span class="sp-link-title">Register</span>
                                      </a>
                                
                            </li>
                            <li class="menu-link">
                                <a href="home.py" class="link-title">
                                    <span class="sp-link-title">Logout</span>
                                      </a>
                                
                            </li>
                        </ul>
                    </div>
                </div>
                <!-- mega-menu end -->
            </div>
        </div>
        <!-- mobile-menu end -->
        <!-- notification-bottom start -->
        <div class="notification-bottom">
            <ul class="shop-element-menu navigation-menu">
                <li class="side-wrap home-wrap">
                    <div class="home-wrapper">
                        <a href="index-4.html" class="home-modal">
                            <span class="home-icon"><i class="feather-home"></i></span>
                            <span class="header-title">Home</span>
                        </a>
                    </div>
                </li>
                <li class="side-wrap search-wrap">
                    <div class="search-wrapper">
                        <a href="#seachmodal" data-bs-toggle="modal" class="search-modal">
                            <span class="search-icon"><i class="feather-search"></i></span>
                            <span class="header-title">Search</span>
                        </a>
                    </div>
                </li>
                <li class="side-wrap wishlist-wrap">
                    <div class="wishlist-wrapper">
                        <div class="wish-det">
                            <a href="wishlist-product.html" class="wishlist-count">
                                <span class="wishlist-icon"><i class="feather-heart"></i></span>
                                <span class="wishlist-counter">5</span>
                                <span class="header-title">Wishlist</span>
                            </a>
                        </div>
                    </div>
                </li>
                <li class="side-wrap cart-wrap">
                    <div class="cart-wrapper">
                        <div class="cart-det">
                            <a href="javascript:void(0)" class="add-to-cart cart-count">
                                <span class="cart-icon"><i class="feather-shopping-bag"></i></span>
                                <span class="cart-counter">8</span>
                                <span class="header-title">Cart</span>
                            </a>
                        </div>
                    </div>
                </li>
                <li class="side-wrap user-wrap">
                    <div class="user-wrapper">
                        <a href="login-account.html" class="user-login">
                            <span class="user-icon"><i class="feather-user"></i></span>
                            <span class="header-title">User</span>
                        </a>
                    </div>
                </li>
            </ul>
        </div>
        <!-- notification-bottom end -->
        <!-- mini-cart start -->
        <div class="mini-cart">
            <div class="cart-text">
                <!-- minicart-empty start -->
                <p class="d-none">No products in the cart.</p>
                <!-- minicart-empty end -->
                <!-- minicart-fill start -->
                <p>
                    <span class="cart-count-desc">There are</span>
                    <span class="cart-count">8</span>
                    <span class="cart-count-desc">products</span>
                </p>
                <!-- minicart-fill end -->
                <!-- minicart-close start -->
                <button class="cart-close"><i class="feather-x"></i></button>
                <!-- minicart-close end -->
            </div>
            <!-- minicart empty-content start -->
            <div class="empty-cart d-none">
                <span class="cart-icon"><i class="bi bi-bag-dash"></i></span>
                <a href="collection.html" class="btn btn-style">Continue shopping</a>
            </div>
            <!-- minicart empty-content end -->
            <ul class="cart-item">
                <li class="cart-product">
                    <div class="cart-img">
                        <!-- minicart-img start -->
                        <a href="product-template.html" class="img-area">
                            <img src="img/product-list/p-17.jpg" class="img-fluid" alt="p-17">
                        </a>
                        <!-- minicart-img end -->
                    </div>
                    <div class="cart-content">
                        <!-- minicart-title start -->
                        <h6><a href="product-template2.html">Donuts yeast donut strawberry</a></h6>
                        <!-- minicart-title end -->
                        <div class="product-info">
                            <!-- minicart-price start -->
                            <div class="info-item">
                                <span class="product-qty">1</span>
                                <span>×</span>
                                <span class="product-price">$12.00</span>
                            </div>
                            <!-- minicart-price end -->
                        </div>
                        <div class="product-quantity-action">
                            <div class="product-quantity">
                                <div class="cart-plus-minus">
                                    <button class="dec qtybutton minus"><i class="feather-minus"></i></button>
                                    <input type="text" name="quantity" value="1">
                                    <button class="inc qtybutton plus"><i class="feather-plus"></i></button>
                                </div>
                            </div>
                            <!-- minicart delete-icon start -->
                            <div class="delete-cart">
                                <a href="javascript:void(0)" class="delete-icon"><i class="feather-trash-2"></i></a>
                            </div>
                            <!-- minicart delete-icon end -->
                        </div>
                    </div>
                </li>
                <li class="cart-product">
                    <div class="cart-img">
                        <!-- minicart-img start -->
                        <a href="product-template.html" class="img-area">
                            <img src="img/product-list/p-18.jpg" class="img-fluid" alt="p-18">
                        </a>
                        <!-- minicart-img end -->
                    </div>
                    <div class="cart-content">
                        <!-- minicart-title start -->
                        <h6><a href="product-template2.html">Unicorn cup cream cake</a></h6>
                        <!-- minicart-title end -->
                        <div class="product-info">
                            <!-- minicart-price start -->
                            <div class="info-item">
                                <span class="product-qty">1</span>
                                <span>×</span>
                                <span class="product-price">$16.00</span>
                            </div>
                            <!-- minicart-price end -->
                        </div>
                        <div class="product-quantity-action">
                            <div class="product-quantity">
                                <div class="cart-plus-minus">
                                    <button class="dec qtybutton minus"><i class="feather-minus"></i></button>
                                    <input type="text" name="quantity" value="1">
                                    <button class="inc qtybutton plus"><i class="feather-plus"></i></button>
                                </div>
                            </div>
                            <!-- minicart delete-icon start -->
                            <div class="delete-cart">
                                <a href="javascript:void(0)" class="delete-icon"><i class="feather-trash-2"></i></a>
                            </div>
                            <!-- minicart delete-icon end -->
                        </div>
                    </div>
                </li>
                <li class="cart-product">
                    <div class="cart-img">
                        <!-- minicart-img start -->
                        <a href="product-template.html" class="img-area">
                            <img src="img/product-list/p-19.jpg" class="img-fluid" alt="p-19">
                        </a>
                        <!-- minicart-img end -->
                    </div>
                    <div class="cart-content">
                        <!-- minicart-title start -->
                        <h6><a href="product-template2.html">Giant cup cream cake</a></h6>
                        <!-- minicart-title end -->
                        <div class="product-info">
                            <!-- minicart-price start -->
                            <div class="info-item">
                                <span class="product-qty">1</span>
                                <span>×</span>
                                <span class="product-price">$10.00</span>
                            </div>
                            <!-- minicart-price end -->
                        </div>
                        <div class="product-quantity-action">
                            <div class="product-quantity">
                                <div class="cart-plus-minus">
                                    <button class="dec qtybutton minus"><i class="feather-minus"></i></button>
                                    <input type="text" name="quantity" value="1">
                                    <button class="inc qtybutton plus"><i class="feather-plus"></i></button>
                                </div>
                            </div>
                            <!-- minicart delete-icon start -->
                            <div class="delete-cart">
                                <a href="javascript:void(0)" class="delete-icon"><i class="feather-trash-2"></i></a>
                            </div>
                            <!-- minicart delete-icon end -->
                        </div>
                    </div>
                </li>
                <li class="cart-product">
                    <div class="cart-img">
                        <!-- minicart-img start -->
                        <a href="product-template.html" class="img-area">
                            <img src="img/product-list/p-20.jpg" class="img-fluid" alt="p-20">
                        </a>
                        <!-- minicart-img end -->
                    </div>
                    <div class="cart-content">
                        <!-- minicart-title start -->
                        <h6><a href="product-template2.html">Strawberry cheese cake cup</a></h6>
                        <!-- minicart-title end -->
                        <div class="product-info">
                            <!-- minicart-price start -->
                            <div class="info-item">
                                <span class="product-qty">1</span>
                                <span>×</span>
                                <span class="product-price">$8.00</span>
                            </div>
                            <!-- minicart-price end -->
                        </div>
                        <div class="product-quantity-action">
                            <div class="product-quantity">
                                <div class="cart-plus-minus">
                                    <button class="dec qtybutton minus"><i class="feather-minus"></i></button>
                                    <input type="text" name="quantity" value="1">
                                    <button class="inc qtybutton plus"><i class="feather-plus"></i></button>
                                </div>
                            </div>
                            <!-- minicart delete-icon start -->
                            <div class="delete-cart">
                                <a href="javascript:void(0)" class="delete-icon"><i class="feather-trash-2"></i></a>
                            </div>
                            <!-- minicart delete-icon end -->
                        </div>
                    </div>
                </li>
                <li class="cart-product">
                    <div class="cart-img">
                        <!-- minicart-img start -->
                        <a href="product-template.html" class="img-area">
                            <img src="img/product-list/p-21.jpg" class="img-fluid" alt="p-21">
                        </a>
                        <!-- minicart-img end -->
                    </div>
                    <div class="cart-content">
                        <!-- minicart-title start -->
                        <h6><a href="product-template2.html">Gender reveal macaron cake</a></h6>
                        <!-- minicart-title end -->
                        <div class="product-info">
                            <!-- minicart-price start -->
                            <div class="info-item">
                                <span class="product-qty">1</span>
                                <span>×</span>
                                <span class="product-price">$11.00</span>
                            </div>
                            <!-- minicart-price end -->
                        </div>
                        <div class="product-quantity-action">
                            <div class="product-quantity">
                                <div class="cart-plus-minus">
                                    <button class="dec qtybutton minus"><i class="feather-minus"></i></button>
                                    <input type="text" name="quantity" value="1">
                                    <button class="inc qtybutton plus"><i class="feather-plus"></i></button>
                                </div>
                            </div>
                            <!-- minicart delete-icon start -->
                            <div class="delete-cart">
                                <a href="javascript:void(0)" class="delete-icon"><i class="feather-trash-2"></i></a>
                            </div>
                            <!-- minicart delete-icon end -->
                        </div>
                    </div>
                </li>
                <li class="cart-product">
                    <div class="cart-img">
                        <!-- minicart-img start -->
                        <a href="product-template.html" class="img-area">
                            <img src="img/product-list/p-22.jpg" class="img-fluid" alt="p-22">
                        </a>
                        <!-- minicart-img end -->
                    </div>
                    <div class="cart-content">
                        <!-- minicart-title start -->
                        <h6><a href="product-template2.html">Strawberry macaron cake</a></h6>
                        <!-- minicart-title end -->
                        <div class="product-info">
                            <!-- minicart-price start -->
                            <div class="info-item">
                                <span class="product-qty">1</span>
                                <span>×</span>
                                <span class="product-price">$13.00</span>
                            </div>
                            <!-- minicart-price end -->
                        </div>
                        <div class="product-quantity-action">
                            <div class="product-quantity">
                                <div class="cart-plus-minus">
                                    <button class="dec qtybutton minus"><i class="feather-minus"></i></button>
                                    <input type="text" name="quantity" value="1">
                                    <button class="inc qtybutton plus"><i class="feather-plus"></i></button>
                                </div>
                            </div>
                            <!-- minicart delete-icon start -->
                            <div class="delete-cart">
                                <a href="javascript:void(0)" class="delete-icon"><i class="feather-trash-2"></i></a>
                            </div>
                            <!-- minicart delete-icon end -->
                        </div>
                    </div>
                </li>
                <li class="cart-product">
                    <div class="cart-img">
                        <!-- minicart-img start -->
                        <a href="product-template.html" class="img-area">
                            <img src="img/product-list/p-23.jpg" class="img-fluid" alt="p-23">
                        </a>
                        <!-- minicart-img end -->
                    </div>
                    <div class="cart-content">
                        <!-- minicart-title start -->
                        <h6><a href="product-template2.html">Raspberry macaron cake</a></h6>
                        <!-- minicart-title end -->
                        <div class="product-info">
                            <!-- minicart-price start -->
                            <div class="info-item">
                                <span class="product-qty">1</span>
                                <span>×</span>
                                <span class="product-price">$10.00</span>
                            </div>
                            <!-- minicart-price end -->
                        </div>
                        <div class="product-quantity-action">
                            <div class="product-quantity">
                                <div class="cart-plus-minus">
                                    <button class="dec qtybutton minus"><i class="feather-minus"></i></button>
                                    <input type="text" name="quantity" value="1">
                                    <button class="inc qtybutton plus"><i class="feather-plus"></i></button>
                                </div>
                            </div>
                            <!-- minicart delete-icon start -->
                            <div class="delete-cart">
                                <a href="javascript:void(0)" class="delete-icon"><i class="feather-trash-2"></i></a>
                            </div>
                            <!-- minicart delete-icon end -->
                        </div>
                    </div>
                </li>
                <li class="cart-product">
                    <div class="cart-img">
                        <!-- minicart-img start -->
                        <a href="product-template.html" class="img-area">
                            <img src="img/product-list/p-24.jpg" class="img-fluid" alt="p-24">
                        </a>
                        <!-- minicart-img end -->
                    </div>
                    <div class="cart-content">
                        <!-- minicart-title start -->
                        <h6><a href="product-template2.html">Healthy cake pastry</a></h6>
                        <!-- minicart-title end -->
                        <div class="product-info">
                            <!-- minicart-price start -->
                            <div class="info-item">
                                <span class="product-qty">1</span>
                                <span>×</span>
                                <span class="product-price">$44.00</span>
                            </div>
                            <!-- minicart-price end -->
                        </div>
                        <div class="product-quantity-action">
                            <div class="product-quantity">
                                <div class="cart-plus-minus">
                                    <button class="dec qtybutton minus"><i class="feather-minus"></i></button>
                                    <input type="text" name="quantity" value="1">
                                    <button class="inc qtybutton plus"><i class="feather-plus"></i></button>
                                </div>
                            </div>
                            <!-- minicart delete-icon start -->
                            <div class="delete-cart">
                                <a href="javascript:void(0)" class="delete-icon"><i class="feather-trash-2"></i></a>
                            </div>
                            <!-- minicart delete-icon end -->
                        </div>
                    </div>
                </li>
            </ul>
            <!-- minicart-total start -->
            <ul class="subtotal-area">
                <li class="subtotal-info">
                    <div class="subtotal-titles">
                        <!-- minicart total-title start -->
                        <h6 class="cart-total">Subtotal:</h6>
                        <!-- minicart total-title end -->
                        <!-- minicart total-price start -->
                        <span class="subtotal-price">€369,00</span>
                        <!-- minicart total-price end -->
                    </div>
                </li>
                <li class="mini-info">
                    <!-- minicart agree-text start -->
                    <label class="box-area">
                        <span class="agree-text">I have read and agree with the <a href="terms-condition.html">terms & condition.</a></span>
                        <input type="checkbox" class="cust-checkbox">
                        <span class="cust-check"></span>
                    </label>
                    <!-- minicart agree-text end -->
                    <!-- minicart button start -->
                    <div class="cart-btn">
                        <a href="cart-page.html" class="btn btn-style2">View cart</a>
                        <a href="checkout-style1.html" class="btn btn-style2 checkout disabled">Checkout</a>
                    </div>
                    <!-- minicart button end -->
                </li>
            </ul>
            <!-- minicart-total end -->
        </div>
        <!-- minicart end -->
        <!-- quickview modal start -->
        <div class="productmodal">
            <div class="modal fade" id="quickview" tabindex="-1">
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h6 class="modal-quickview">Quickview</h6>
                            <button type="button" class="close" data-bs-dismiss="modal"><i class="feather-x"></i></button>
                        </div>
                        <div class="modal-body">
                            <!-- swiper slider start -->
                            <div class="quickview-main-area">
                                <div class="quickview-slider">
                                    <div class="swiper gallery-top">
                                        <div class="swiper-wrapper">
                                            <div class="swiper-slide">
                                                <a href="product-template.html"><img src="img/product/p-1.jpg" class="img-fluid" alt="p-1"></a>
                                            </div>
                                            <div class="swiper-slide">
                                                <a href="product-template.html"><img src="img/product/p-2.jpg" class="img-fluid" alt="p-2"></a>
                                            </div>
                                            <div class="swiper-slide">
                                                <a href="product-template.html"><img src="img/product/p-3.jpg" class="img-fluid" alt="p-3"></a>
                                            </div>
                                            <div class="swiper-slide">
                                                <a href="product-template.html"><img src="img/product/p-4.jpg" class="img-fluid" alt="p-4"></a>
                                            </div>
                                            <div class="swiper-slide">
                                                <a href="product-template.html"><img src="img/product/p-5.jpg" class="img-fluid" alt="p-5"></a>
                                            </div>
                                        </div>
                                        <div class="swiper-button">
                                            <button class="quick-prev"><i class="fas fa-chevron-left"></i></button>
                                            <button class="quick-next"><i class="fas fa-chevron-right"></i></button>
                                        </div>
                                    </div>
                                    <div class="swiper gallery-thumbs">
                                        <div class="swiper-wrapper">
                                            <div class="swiper-slide">
                                                <a href="javascript:void(0)"><img src="img/product/p-1.jpg" class="img-fluid" alt="p-1"></a>
                                            </div>
                                            <div class="swiper-slide">
                                                <a href="javascript:void(0)"><img src="img/product/p-2.jpg" class="img-fluid" alt="p-2"></a>
                                            </div>
                                            <div class="swiper-slide">
                                                <a href="javascript:void(0)"><img src="img/product/p-3.jpg" class="img-fluid" alt="p-3"></a>
                                            </div>
                                            <div class="swiper-slide">
                                                <a href="javascript:void(0)"><img src="img/product/p-4.jpg" class="img-fluid" alt="p-4"></a>
                                            </div>
                                            <div class="swiper-slide">
                                                <a href="javascript:void(0)"><img src="img/product/p-5.jpg" class="img-fluid" alt="p-5"></a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- swiper slider end -->
                                <!-- quick-view content start -->
                                <div class="quick-view-content">
                                    <div class="product-rating">
                                        <span class="star-rating">
                                            <i class="far fa-star"></i>
                                            <i class="far fa-star"></i>
                                            <i class="far fa-star"></i>
                                            <i class="far fa-star"></i>
                                            <i class="far fa-star"></i>
                                        </span>
                                    </div>
                                    <div class="product-title"><h6 class="product_title">Candy nut chocolate</h6></div>
                                    <!-- product-price start -->
                                    <div class="price-box">
                                        <span class="new-price">$11,00</span>
                                        <span class="old-price">$19,00</span>
                                    </div>
                                    <!-- product-price end -->
                                    <div class="product-desc"><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magn</p></div>
                                    <form method="post">
                                        <div class="quick-view-select variants select-option-part">
                                            <div class="variants_selects">
                                                <div class="selector-wrapper">
                                                    <label>Flavor</label>
                                                </div>
                                                <div class="select-icon">
                                                    <select class="single-option-selector select--wd">
                                                        <option value="Sponge">Sponge</option>
                                                        <option value="Pumpkin">Pumpkin</option>
                                                        <option value="Velvet">Velvet</option>
                                                    </select>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="product-quantity-action">
                                            <h6>Quantity:</h6>
                                            <div class="product-quantity">
                                                <div class="cart-plus-minus">
                                                    <button class="dec qtybutton minus"><i class="fa-solid fa-minus"></i></button>
                                                    <input type="text" name="quantity" value="1">
                                                    <button class="inc qtybutton plus"><i class="fa-solid fa-plus"></i></button>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="quickview-buttons">
                                            <button type="submit" class="addtocartqv"><span class="cart-title">Add to cart</span></button>
                                        </div>
                                    </form>
                                </div>
                                <!-- quick-view content end -->
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- quickview modal end -->
        <!-- screen-bg start -->
        <div class="screen-bg"></div>
        <!-- screen-bg end -->
        <!-- preloader start -->
        <div class="preloader">
            <div class="loader"></div>
        </div>
        <!-- preloader end -->
        <!-- back-to-top start -->
        <a href="javascript:void(0)" id="top" class="scroll">
            <span><i class="feather-arrow-up"></i></span>
        </a>
        <!-- back-to-top end -->
        <!-- jquery -->
        <script src="js/jquery-3.6.3.min.js"></script>
        <!-- bootstrap js -->
        <script src="js/bootstrap.min.js"></script>
        <script src="js/popper.min.js"></script>
        <!-- magnific-popup js -->
        <script src="js/jquery.magnific-popup.min.js"></script>
        <!-- owl js -->
        <script src="js/owl.carousel.min.js"></script>
        <!-- swiper-bundle js -->
        <script src="js/swiper-bundle.min.js"></script>
        <!-- slick js -->
        <script src="js/slick.min.js"></script>
        <!-- waypoints js -->
        <script src="js/waypoints.min.js"></script>
        <!-- counter js -->
        <script src="js/counter.js"></script>
        <!-- main js -->
        <script src="js/main4.js"></script>
        <script>
const wishlistUserid = localStorage.getItem("id");
const wishlistFirstName = localStorage.getItem("FirstName");

document.querySelectorAll(".wishlistLink").forEach(function(link) {

     let productid = link.dataset.productid;

    if (wishlistFirstName) {
        link.href = `WishListBackEnd.py?userid=${wishlistUserid}&productid=${productid}`;
    } else {
        link.href = "Login.py";
    }
});
document.querySelectorAll(".cartLink").forEach(function(link) {
    let productid = link.dataset.productid;

    if (wishlistFirstName) {
        link.href = `cartdetail.py?userid=${wishlistUserid}&productid=${productid}`;
    } else {
        link.href = "Login.py";
    }
});
</script>
    </body>

<!-- Mirrored from spacingtech.com/html/banno/banno-ltr/index-4.html by HTTrack Website Copier/3.x [XR&CO'2014], Sun, 19 Jul 2026 08:36:57 GMT -->
</html>
""")
