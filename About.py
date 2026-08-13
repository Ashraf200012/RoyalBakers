#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
#print("Content-Type: text/html\n")
import header
print("""
  <section class="about-vision2">
                <div class="container">
                    <div class="row">
                        <div class="col">
                            <div class="about-content">
                                <div class="section-capture">
                                    <div class="section-title">
                                        <span class="sub-title">Amazing things</span>
                                        <h2><span>About us</span></h2>
                                    </div>
                                </div>
                                <div class="about-banner banner-hover">
                                    <img src="img/about-us/about-us-3/about-us-3.jpg" class="img-fluid" alt="about-us-3">
                                </div>
                                <div class="abt-vision">
                                    <ul>
                                        <li>
                                            <div class="abt-vision-content">
                                                <img src="img/about-us/Our-mission.png" class="img-fluid" alt="mission">
                                                <h6>Our mission</h6>
                                                <p>Lorem ipsum is simply dummy text of the printing and typesetting industry's standard dummy text ever since the 1500s</p>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="abt-vision-content">
                                                <img src="img/about-us/Our-idea.png" class="img-fluid" alt="idea">
                                                <h6>Our idea</h6>
                                                <p>Lorem ipsum is simply dummy text of the printing and typesetting industry's standard dummy text ever since the 1500s</p>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <section class="project-count">
                <div class="container">
                    <div class="row">
                        <div class="col">
                            <div class="single-count">
                                <ul>
                                    <li class="count-wrap">
                                        <!-- project info start -->
                                        <div class="count-info">
                                            <div class="count">
                                                <span class="count-number">10</span>
                                                <span>+</span>
                                            </div>
                                            <h6>Years</h6>
                                        </div>
                                        <!-- project info end -->
                                        <!-- project icon start -->
                                        <div class="counter-icon">
                                            <a href="javascript:void(0)">
                                                <img src="img/about-us/services/Years.png" class="img-fluid" alt="Years">
                                            </a>
                                        </div>
                                        <!-- project icon end -->
                                    </li>
                                    <li class="count-wrap">
                                        <!-- project info start -->
                                        <div class="count-info">
                                            <div class="count">
                                                <span class="count-number">10</span>
                                                <span>M+</span>
                                            </div>
                                            <h6>Clients</h6>
                                        </div>
                                        <!-- project info end -->
                                        <!-- project icon start -->
                                        <div class="counter-icon">
                                            <a href="javascript:void(0)">
                                                <img src="img/about-us/services/Clients.png" class="img-fluid" alt="Clients">
                                            </a>
                                        </div>
                                        <!-- project icon end -->
                                    </li>
                                    <li class="count-wrap">
                                        <!-- project info start -->
                                        <div class="count-info">
                                            <div class="count">
                                                <span class="count-number">50</span>
                                                <span>+</span>
                                            </div>
                                            <h6>Shops</h6>
                                        </div>
                                        <!-- project info end -->
                                        <!-- project icon start -->
                                        <div class="counter-icon">
                                            <a href="javascript:void(0)">
                                                <img src="img/about-us/services/Shops.png" class="img-fluid" alt="Shops">
                                            </a>
                                        </div>
                                        <!-- project icon end -->
                                    </li>
                                    <li class="count-wrap">
                                        <!-- project info start -->
                                        <div class="count-info">
                                            <div class="count">
                                                <span class="count-number">17</span>
                                                <span>M+</span>
                                            </div>
                                            <h6>Sales</h6>
                                        </div>
                                        <!-- project info end -->
                                        <!-- project icon start -->
                                        <div class="counter-icon">
                                            <a href="javascript:void(0)">
                                                <img src="img/about-us/services/Sales.png" class="img-fluid" alt="Sales">
                                            </a>
                                        </div>
                                        <!-- project icon end -->
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <section class="about-team-3">
                <div class="container">
                    <div class="row">
                        <div class="col">
                            <div class="our-team-3">
                                <div class="section-capture">
                                    <div class="section-title">
                                        <span class="sub-title">Strong mission</span>
                                        <h2><span class="title-main">Our team</span></h2>
                                    </div>
                                </div>
                                <ul class="team-wrap">
                                    <li class="team-content banner-hover">
                                        <div class="team-content">
                                            <a href="javascript:void(0)" class="banner-hover">
                                                <img src="img/about-us/team-1.jpg" class="img-fluid" alt="team-1">
                                            </a>
                                            <div class="team-info">
                                                <h6>Johnny walker</h6>
                                                <span>Web designer</span>
                                                <p>Vestibulum porttitor egestas orci, vitae ullamcorper risus rutrum massa quis.</p>
                                            </div>
                                        </div>
                                    </li>
                                    <li class="team-content banner-hover">
                                        <div class="team-content">
                                            <a href="javascript:void(0)" class="banner-hover">
                                                <img src="img/about-us/team-2.jpg" class="img-fluid" alt="team-2">
                                            </a>
                                            <div class="team-info">
                                                <h6>Rebecca flex</h6>
                                                <span>Support staff</span>
                                                <p>Vestibulum porttitor egestas orci, vitae ullamcorper risus rutrum massa quis.</p>
                                            </div>
                                        </div>
                                    </li>
                                    <li class="team-content banner-hover">
                                        <div class="team-content">
                                            <a href="javascript:void(0)" class="banner-hover">
                                                <img src="img/about-us/team-3.jpg" class="img-fluid" alt="team-3">
                                            </a>
                                            <div class="team-info">
                                                <h6>Jan ringo</h6>
                                                <span>Deputy sale</span>
                                                <p>Vestibulum porttitor egestas orci, vitae ullamcorper risus rutrum massa quis.</p>
                                            </div>
                                        </div>
                                    </li>
                                    <li class="team-content banner-hover">
                                        <div class="team-content">
                                            <a href="javascript:void(0)">
                                                <img src="img/about-us/team-4.jpg" class="img-fluid" alt="team-4">
                                            </a>
                                            <div class="team-info">
                                                <h6>Ringo kai</h6>
                                                <span>Policy member</span>
                                                <p>Vestibulum porttitor egestas orci, vitae ullamcorper risus rutrum massa quis.</p>
                                            </div>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </main>
        <!-- main section end-->
""")
import footer
