#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
#print("Content-Type: text/html\n")
import header
print("""
  <section class="customer-page section-ptb">
                <div class="container">
                    <div class="row">
                        <div class="col">
                            <div class="acc-form">
                                <div class="log-acc-page" id="CustomerLoginForm">
                                    <!-- account title start -->
                                    <div class="content-main-title">
                                        <div class="section-cont-title">
                                            <h2><span>Login account</span></h2>
                                            <p>Please login account detail</p>
                                        </div>
                                    </div>
                                    <!-- account title end -->
                                    <!-- account login start -->
                                    <div class="acc-page">
                                        <div class="login">
                                            <form method="post" action="LoginBackEnd.py">
                                                <div class="login-form-container">
                                                    <ul class="fill-form">
                                                        <li class="log-email">
                                                            <label>Email address</label>
                                                            <input type="email" name="Email" id="Email" class="input-full" placeholder="Email address" autocomplete="off">
                                                        </li>
                                                        <li class="log-pwd">
                                                            <label>Password</label>
                                                            <input type="password" name="Password" id="Password" class="input-full" placeholder="Password">
                                                        </li>
                                                    </ul>
                                                    <div class="form-action-button">
                                                        <button type="submit" class="btn btn-style2">Sign In</button>
                                                   </div>
                                                </div>
                                            </form>
                                        </div>
                                        <div class="acc-wrapper">
                                            <h6>Don't have account?</h6>
                                            <div class="account-optional-action">
                                                <a href="Registration.py">Create account</a>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- account login end -->
                                </div>
                               
                            </div>
                        </div>
                    </div>
                </div>
               
            </section>
""")
import footer
