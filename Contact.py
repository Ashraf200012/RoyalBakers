#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
#print("Content-Type: text/html\n")
import header
print("""
 <section class="main-content-wrap contact-us-page">
                <div class="container">
                    <div class="row">
                        <div class="col">
                            <!-- contact title start -->
                            <div class="section-capture">
                                <div class="section-title">
                                    <span class="sub-title">Hear from you</span>
                                    <h2><span>Contact us</span></h2>
                                </div>
                            </div>
                            <!-- contact title end -->
                            <!-- contact map start -->
                            <div class="google-map-area">
                                <div class="map" id="map">
                                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3178.943120902953!2d-7.963813984699448!3d37.177822679872456!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd1ab161c81fb0ff%3A0x867380c80c46b1d!2sAmendoeira%20Organics!5e0!3m2!1sen!2spt!4v1631184615272!5m2!1sen!2spt" allowfullscreen="" loading="lazy"></iframe>
                                </div>
                            </div>
                            <!-- contact map end -->
                        </div>
                    </div>
                </div>
            </section>
            <section class="form-contact">
                <div class="container">
                    <div class="row">
                        <div class="col">
                            <div class="contact-content">
                                <!-- contact us from start -->
                                <div class="contact-detail form-warp">
                                    <div class="form-title">
                                        <h6>Drop us message</h6>
                                    </div>
                                    <div class="contact-form-list">
                                        <form method="post">
                                            <ul class="form-fill">
                                                <li class="name">
                                                    <label>Name</label>
                                                    <input type="text" name="q" autocomplete="name" placeholder="Name">
                                                </li>
                                                <li class="email">
                                                    <label>Email address</label>
                                                    <input type="email" name="q" autocomplete="email" placeholder="Email address">
                                                </li>
                                                <li class="phone number">
                                                    <label>Phone number</label>
                                                    <input type="tel" name="q" placeholder="Phone number">
                                                </li>
                                                <li class="message phone number">
                                                    <label>Message</label>
                                                    <textarea rows="10" placeholder="Message" class="custom-textarea"></textarea>
                                                </li>
                                            </ul>
                                            <div class="contact-submit">
                                                <button type="submit" class="btn btn-style2">
                                                <span>Send</span>
                                                </button>
                                            </div>
                                        </form>
                                    </div>
                                </div>
                                <!-- contact us from start -->
                                <!-- contact get info. start -->
                                <div class="contact-detail get-info">
                                    <div class="form-title">
                                        <h6>Get in touch</h6>
                                    </div>
                                    <ul class="contact-info-list">
                                        <li class="ftcon-li">
                                            <span class="con-icon"><i class="bi bi-geo"></i></span>
                                            <span class="con-add">
                                                <span>7882, Reliance GIDC</span>
                                                <span>Chowk bazzar, New York</span>
                                            </span>
                                        </li>
                                        <li class="ftcon-li">
                                            <span class="con-icon"><i class="bi bi-telephone"></i></span>
                                            <div class="contact-block">
                                                <a href="tel:(+91)123456789" class="con-add">(+33) 1 23 45 67 89</a>
                                                <a href="tel:(+91)123456789" class="con-add">(+33) 1 23 45 67 89</a>
                                            </div>
                                        </li>
                                        <li class="ftcon-li">
                                            <span class="con-icon"><i class="bi bi-envelope"></i></span>
                                            <div class="contact-block">
                                                <a href="mailto:demo@support.com" class="con-add">demo@support.com</a>
                                                <a href="mailto:support@spacingtech.com" class="con-add">support@spacingtech.com</a>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                                <!-- contact get info. end -->
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </main>
        <!-- main section end-->
""")
import footer
