#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")
print("""<!DOCTYPE html>
<html dir="ltr" lang="en">


<!-- Mirrored from themedesigner.in/demo/wrappixel/admin-template/xtreme/html/ltr/form-basic.html by HTTrack Website Copier/3.x [XR&CO'2014], Wed, 06 Jun 2018 05:49:08 GMT -->
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!-- Tell the browser to be responsive to screen width -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <!-- Favicon icon -->
    <link rel="icon" type="image/png" sizes="16x16" href="../../assets/images/favicon.png">
    <title>Xtreme admin Template - The Ultimate Multipurpose admin template</title>
    <!-- Custom CSS -->
    <link href="../../dist/css/style.min.css" rel="stylesheet">
    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
<![endif]-->
</head>

<body>
    <!-- ============================================================== -->
    <!-- Preloader - style you can find in spinners.css -->
    <!-- ============================================================== -->
    <div class="preloader">
        <div class="lds-ripple">
            <div class="lds-pos"></div>
            <div class="lds-pos"></div>
        </div>
    </div>
    <!-- ============================================================== -->
    <!-- Main wrapper - style you can find in pages.scss -->
    <!-- ============================================================== -->
    <div id="main-wrapper">
        <!-- ============================================================== -->
        <!-- Topbar header - style you can find in pages.scss -->
        <!-- ============================================================== -->
        <header class="topbar">
            <nav class="navbar top-navbar navbar-expand-md navbar-dark" >
                <div class="navbar-header" style="background-color:#ed222d !important;">
                    <!-- This is for the sidebar toggle which is visible on mobile only -->
                    <a class="nav-toggler waves-effect waves-light d-block d-md-none" href="javascript:void(0)"><i class="ti-menu ti-close"></i></a>
                    <!-- ============================================================== -->
                    <!-- Logo -->
                    <!-- ============================================================== -->
                    <a class="navbar-brand" href="index.html">
                        <!-- Logo icon -->
                        <b class="logo-icon">
                            <!--You can put here icon as well // <i class="wi wi-sunset"></i> //-->
                           
                            <!-- Light Logo icon -->
                            <img src="logo.jpeg" alt="homepage" class="light-logo" style="height:50px;width:100px;padding-left : 15px;"/>
                        </b>
                        <!--End Logo icon -->
                        
                    </a>
                    <!-- ============================================================== -->
                    <!-- End Logo -->
                    <!-- ============================================================== -->
                    <!-- ============================================================== -->
                    <!-- Toggle which is visible on mobile only -->
                    <!-- ============================================================== -->
                    <a class="topbartoggler d-block d-md-none waves-effect waves-light" href="javascript:void(0)" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="true" aria-label="Toggle navigation"><i class="ti-more"></i></a>
                </div>
                <!-- ============================================================== -->
                <!-- End Logo -->
                <!-- ============================================================== -->
                <div class="navbar-collapse collapse" id="navbarSupportedContent" style="background-color:#ed222d !important;">
                    <!-- ============================================================== -->
                    <!-- toggle and nav items -->
                    <!-- ============================================================== -->
                    <ul class="navbar-nav float-left mr-auto">
                        <li class="nav-item d-none d-md-block"><a class="nav-link sidebartoggler waves-effect waves-light" href="javascript:void(0)" data-sidebartype="mini-sidebar"><i class="mdi mdi-menu font-24"></i></a></li>
                        <!-- ============================================================== -->
                        
                        <!-- ============================================================== -->
                        <!-- ============================================================== -->
                        <!-- create new -->
                        <!-- ============================================================== -->
                        
                        <!-- ============================================================== -->
                        
                    </ul>
                    <!-- ============================================================== -->
                    <!-- Right side toggle and nav items -->
                    <!-- ============================================================== -->
                    <ul class="navbar-nav float-right">
                        <!-- ============================================================== -->
                        <!-- create new -->
                        <!-- ============================================================== -->
                        <li class="nav-item dropdown">
                            
                            <div class="dropdown-menu dropdown-menu-right  animated bounceInDown" aria-labelledby="navbarDropdown2">
                                <a class="dropdown-item" href="#"><i class="flag-icon flag-icon-us"></i> English</a>
                                <a class="dropdown-item" href="#"><i class="flag-icon flag-icon-fr"></i> French</a>
                                <a class="dropdown-item" href="#"><i class="flag-icon flag-icon-es"></i> Spanish</a>
                                <a class="dropdown-item" href="#"><i class="flag-icon flag-icon-de"></i> German</a>
                            </div>
                        </li>
                        <!-- ============================================================== -->
                        <!-- Comment -->
                        <!-- ============================================================== -->
                        <li class="nav-item dropdown">
                            
                            <div class="dropdown-menu dropdown-menu-right mailbox animated bounceInDown">
                                <span class="with-arrow"><span class="bg-primary"></span></span>
                                <ul class="list-style-none">
                                    <li>
                                        <div class="drop-title bg-primary text-white">
                                            <h4 class="m-b-0 m-t-5">4 New</h4>
                                            <span class="font-light">Notifications</span>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="message-center notifications">
                                            <!-- Message -->
                                            <a href="javascript:void(0)" class="message-item">
                                                <span class="btn btn-danger btn-circle"><i class="fa fa-link"></i></span>
                                                <div class="mail-contnet">
                                                    <h5 class="message-title">Luanch Admin</h5> <span class="mail-desc">Just see the my new admin!</span> <span class="time">9:30 AM</span> </div>
                                            </a>
                                            <!-- Message -->
                                            <a href="javascript:void(0)" class="message-item">
                                                <span class="btn btn-success btn-circle"><i class="ti-calendar"></i></span>
                                                <div class="mail-contnet">
                                                    <h5 class="message-title">Event today</h5> <span class="mail-desc">Just a reminder that you have event</span> <span class="time">9:10 AM</span> </div>
                                            </a>
                                            <!-- Message -->
                                            <a href="javascript:void(0)" class="message-item">
                                                <span class="btn btn-info btn-circle"><i class="ti-settings"></i></span>
                                                <div class="mail-contnet">
                                                    <h5 class="message-title">Settings</h5> <span class="mail-desc">You can customize this template as you want</span> <span class="time">9:08 AM</span> </div>
                                            </a>
                                            <!-- Message -->
                                            <a href="javascript:void(0)" class="message-item">
                                                <span class="btn btn-primary btn-circle"><i class="ti-user"></i></span>
                                                <div class="mail-contnet">
                                                    <h5 class="message-title">Pavan kumar</h5> <span class="mail-desc">Just see the my admin!</span> <span class="time">9:02 AM</span> </div>
                                            </a>
                                        </div>
                                    </li>
                                    <li>
                                        <a class="nav-link text-center m-b-5" href="javascript:void(0);"> <strong>Check all notifications</strong> <i class="fa fa-angle-right"></i> </a>
                                    </li>
                                </ul>
                            </div>
                        </li>
                        <!-- ============================================================== -->
                        <!-- End Comment -->
                        <!-- ============================================================== -->
                        <!-- ============================================================== -->
                        <!-- Messages -->
                        <!-- ============================================================== -->
                        <li class="nav-item dropdown">
                            
                            <div class="dropdown-menu dropdown-menu-right mailbox animated bounceInDown" aria-labelledby="2">
                                <span class="with-arrow"><span class="bg-danger"></span></span>
                                <ul class="list-style-none">
                                    <li>
                                        <div class="drop-title text-white bg-danger">
                                            <h4 class="m-b-0 m-t-5">5 New</h4>
                                            <span class="font-light">Messages</span>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="message-center message-body">
                                            <!-- Message -->
                                            <a href="javascript:void(0)" class="message-item">
                                                <span class="user-img"> <img src="../../assets/images/users/1.jpg" alt="user" class="rounded-circle"> <span class="profile-status online pull-right"></span> </span>
                                                <div class="mail-contnet">
                                                    <h5 class="message-title">Pavan kumar</h5> <span class="mail-desc">Just see the my admin!</span> <span class="time">9:30 AM</span> </div>
                                            </a>
                                            <!-- Message -->
                                            <a href="javascript:void(0)" class="message-item">
                                                <span class="user-img"> <img src="../../assets/images/users/2.jpg" alt="user" class="rounded-circle"> <span class="profile-status busy pull-right"></span> </span>
                                                <div class="mail-contnet">
                                                    <h5 class="message-title">Sonu Nigam</h5> <span class="mail-desc">I've sung a song! See you at</span> <span class="time">9:10 AM</span> </div>
                                            </a>
                                            <!-- Message -->
                                            <a href="javascript:void(0)" class="message-item">
                                                <span class="user-img"> <img src="../../assets/images/users/3.jpg" alt="user" class="rounded-circle"> <span class="profile-status away pull-right"></span> </span>
                                                <div class="mail-contnet">
                                                    <h5 class="message-title">Arijit Sinh</h5> <span class="mail-desc">I am a singer!</span> <span class="time">9:08 AM</span> </div>
                                            </a>
                                            <!-- Message -->
                                            <a href="javascript:void(0)" class="message-item">
                                                <span class="user-img"> <img src="../../assets/images/users/4.jpg" alt="user" class="rounded-circle"> <span class="profile-status offline pull-right"></span> </span>
                                                <div class="mail-contnet">
                                                    <h5 class="message-title">Pavan kumar</h5> <span class="mail-desc">Just see the my admin!</span> <span class="time">9:02 AM</span> </div>
                                            </a>
                                        </div>
                                    </li>
                                    <li>
                                        <a class="nav-link text-center link" href="javascript:void(0);"> <b>See all e-Mails</b> <i class="fa fa-angle-right"></i> </a>
                                    </li>
                                </ul>
                            </div>
                        </li>
                        <!-- ============================================================== -->
                        <!-- End Messages -->
                        <!-- ============================================================== -->
                        <!-- ============================================================== -->
                        <!-- User profile and search -->
                        <!-- ============================================================== -->
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle text-muted waves-effect waves-dark pro-pic" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true"><img src="../../assets/images/users/1.jpg" alt="user" class="rounded-circle" width="31"></a>
                            <div class="dropdown-menu dropdown-menu-right user-dd animated flipInY">
                                <span class="with-arrow"><span class="bg-primary"></span></span>
                                <div class="d-flex no-block align-items-center p-15 bg-primary text-white m-b-10" style="background-color:#ed222d !important;">
                                    <div class=""><img src="../../assets/images/users/1.jpg" alt="user" class="img-circle" width="60"></div>
                                    <div class="m-l-10">
                                        <h3 class="m-b-0" id="displayname" style="color:black;"></h3>
                                        <p class=" m-b-0" id="userEmail" style="color:black;"></p>
                                    </div>
                                </div>
                                
                                
                                
                                <a class="dropdown-item" href="Logout.py"><i class="fa fa-power-off m-r-5 m-l-5"></i> Logout</a>
                                <div class="dropdown-divider"></div>
                                
                            </div>
                        </li>
                        <!-- ============================================================== -->
                        <!-- User profile and search -->
                        <!-- ============================================================== -->
                    </ul>
                </div>
            </nav>
        </header>
        <!-- ============================================================== -->
        <!-- End Topbar header -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- Left Sidebar - style you can find in sidebar.scss  -->
        <!-- ============================================================== -->
        <aside class="left-sidebar" style="background-color:#fbb218 !important;">
            <!-- Sidebar scroll-->
            <div class="scroll-sidebar" >
                <!-- Sidebar navigation-->
                <nav class="sidebar-nav" >
                    <ul id="sidebarnav" style="background-color:#fbb218">
                        <!-- User Profile-->
                        <li>
                            <!-- User Profile-->
                            <div class="user-profile d-flex no-block dropdown m-t-20" >
                                <div class="user-pic"><img src="../../assets/images/users/1.jpg" alt="users" class="rounded-circle" width="40" /></div>
                                <div class="user-content hide-menu m-l-10">
                                    <a href="javascript:void(0)" class="" id="Userdd" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                                        <h3 class="m-b-0 user-name font-medium" id="displayname1" style="color:black;font-weight:bold;"> <i class="fa fa-angle-down"></i></h3>
                                        <span class="op-5 user-email" id="userEmail1" style="color:black"></span>
                                    </a>
                                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="Userdd">
                                        
                                        <a class="dropdown-item" href="Logout.py"><i class="fa fa-power-off m-r-5 m-l-5"></i> Logout</a>
                                    </div>
                                </div>
                            </div>
                            <!-- End User Profile-->
                        </li>
                        
                        <!-- User Profile-->
                                                <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:#ed222d;"></i> <span class="hide-menu" style="color:#ed222d;font-weight:bold">DASHBOARD</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="Dashboard.py" aria-expanded="false"><i class="mdi mdi-format-list-bulleted" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Admin Dashboard</span></a></li>
                        
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:#ed222d;"></i> <span class="hide-menu" style="color:#ed222d;font-weight:bold"> Unit</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="UnitMaster.py" aria-expanded="false"><i class="mdi mdi-plus-circle-outline" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Add Unit</span></a></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="UnitList.py" aria-expanded="false"><i class="mdi mdi-format-list-bulleted" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Unit List</span></a></li>
                        
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:#ed222d;"></i> <span class="hide-menu" style="color:#ed222d;font-weight:bold">FLAVOURS</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="FlavourMaster.py" aria-expanded="false"><i class="mdi mdi-plus-circle-outline" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Add Flavour</span></a></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="FlavourList.py" aria-expanded="false"><i class="mdi mdi-format-list-bulleted" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Flavour List</span></a></li>
                        
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:#ed222d;"></i> <span class="hide-menu" style="color:#ed222d;font-weight:bold"> Category</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="Category.py" aria-expanded="false"><i class="mdi mdi-plus-circle-outline" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Add Category</span></a></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="CategoryList.py" aria-expanded="false"><i class="mdi mdi-format-list-bulleted" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Category List</span></a></li>
                        
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:#ed222d;"></i> <span class="hide-menu" style="color:#ed222d;font-weight:bold"> Product</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="Product.py" aria-expanded="false"><i class="mdi mdi-plus-circle-outline" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Add Product</span></a></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="ProductList.py" aria-expanded="false"><i class="mdi mdi-format-list-bulleted" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Product List</span></a></li>
                        
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:#ed222d;"></i> <span class="hide-menu" style="color:#ed222d;font-weight:bold">CUSTOMER</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="CustomerList.py" aria-expanded="false"><i class="mdi mdi-format-list-bulleted" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Customer List</span></a></li>
                        
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:#ed222d;"></i> <span class="hide-menu" style="color:#ed222d;font-weight:bold">PASSWORD</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="" id="ChangePasswordLink" aria-expanded="false"><i class="mdi mdi-lock" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Change Password</span></a></li>
                        
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal" style="color:#ed222d;"></i> <span class="hide-menu" style="color:#ed222d;font-weight:bold">ORDER</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link waves-effect waves-dark" href="allOrders.py" aria-expanded="false"><i class="mdi mdi-format-list-bulleted" style="color:black;"></i><span class="hide-menu" style="color:black;font-weight:bold">Order List</span></a></li>
                    </ul>
                    </ul>
                </nav>
               
                
                <!-- End Sidebar navigation -->
            </div>
            <!-- End Sidebar scroll-->
        </aside>
<style>
.sidebar-nav ul .sidebar-item .sidebar-link.active, .sidebar-nav ul .sidebar-item .sidebar-link:hover {
    background-color: #ed222d !important;
    opacity: 1;
}
.sidebar-nav ul .sidebar-item .sidebar-link.active i, .sidebar-nav ul .sidebar-item .sidebar-link.active span,
.sidebar-nav ul .sidebar-item .sidebar-link:hover i, .sidebar-nav ul .sidebar-item .sidebar-link:hover span {
    color: white !important;
}
/* Delete Button Styling */
.table button.btn-delete {
    background-color: #ed222d !important;
    color: white !important;
}
.table button.btn-delete:hover {
    background-color: #c91822 !important;
    box-shadow: 0 4px 8px rgba(237,34,45,0.4) !important;
}

/* Change Button Styling */
.table button.btn-change {
    background-color: #007bff !important;
    color: white !important;
}
.table button.btn-change:hover {
    background-color: #0069d9 !important;
    box-shadow: 0 4px 8px rgba(0,123,255,0.4) !important;
}
</style>
<style>
/* Custom Table Styling to Match Theme */
.table {
    border-collapse: separate !important;
    border-spacing: 0 !important;
    border-radius: 8px !important;
    overflow: hidden !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
    border: 1px solid #eee !important;
    background-color: #fff !important;
}
.table thead th {
    background-color: #ed222d !important;
    color: white !important;
    font-weight: bold !important;
    border: none !important;
    padding: 15px !important;
    text-transform: uppercase !important;
    font-size: 14px !important;
    letter-spacing: 0.5px !important;
    white-space: nowrap !important;
}
.table tbody tr {
    transition: background-color 0.2s !important;
}
.table tbody tr:hover {
    background-color: #fff9e6 !important;
}
.table tbody td, .table tbody th {
    padding: 12px 15px !important;
    vertical-align: middle !important;
    border-top: 1px solid #f0f0f0 !important;
    border-bottom: none !important;
}

/* Custom Button Styling inside tables */
.table button, .table input[type="submit"], .table input[type="button"] {
    background-color: #fbb218 !important;
    color: black !important;
    border: none !important;
    padding: 8px 16px !important;
    border-radius: 6px !important;
    font-weight: bold !important;
    cursor: pointer !important;
    transition: all 0.2s ease-in-out !important;
    margin-right: 5px !important;
    margin-bottom: 5px !important;
    font-size: 13px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    white-space: nowrap !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
}
.table button:hover, .table input[type="submit"]:hover, .table input[type="button"]:hover {
    background-color: #ed222d !important;
    color: white !important;
    box-shadow: 0 4px 8px rgba(237,34,45,0.3) !important;
    transform: translateY(-2px) !important;
}
/* Delete Button Styling */
.table button.btn-delete {
    background-color: #ed222d !important;
    color: white !important;
}
.table button.btn-delete:hover {
    background-color: #c91822 !important;
    box-shadow: 0 4px 8px rgba(237,34,45,0.4) !important;
}

/* Change Button Styling */
.table button.btn-change {
    background-color: #007bff !important;
    color: white !important;
}
.table button.btn-change:hover {
    background-color: #0069d9 !important;
    box-shadow: 0 4px 8px rgba(0,123,255,0.4) !important;
}
</style>
<script>
$(document).ready(function() {
    setTimeout(function() {
        var activeLink = $('.sidebar-link.active');
        if (activeLink.length > 0) {
            var sidebar = $('.scroll-sidebar');
            if (sidebar.length > 0) {
                var linkOffset = activeLink.offset().top;
                var sidebarOffset = sidebar.offset().top;
                var currentScroll = sidebar.scrollTop();
                sidebar.animate({
                    scrollTop: currentScroll + (linkOffset - sidebarOffset) - 100
                }, 300);
            }
        }
    }, 200);
});
</script>
        <script>let username=localStorage.getItem("username");
                console.log(username);
                let Email=localStorage.getItem("Email");
                console.log(Email);
                let id=localStorage.getItem("id");
                console.log(id);
                document.getElementById("displayname").textContent=username;
                document.getElementById("displayname1").textContent=username;
                document.getElementById("userEmail").textContent=Email;
                document.getElementById("userEmail1").textContent=Email;
                document.getElementById("ChangePasswordLink").href="ChangePassword.py?id="+encodeURIComponent(id);
        </script>

""")

