#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
form=cgi.FieldStorage()
#print(form)
id=form.getvalue("userid")
#print(id)
import os
import mysql.connector
mydb = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", ""),  
    database=os.environ.get("DB_NAME", "royalbakers"), port=int(os.environ.get("DB_PORT", 3306)))
mycursor = mydb.cursor()
query=f"""select * from registration where id={id}"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
#print(myresult)
import header
print(f"""
  <section class="customer-page section-ptb">
                <div class="container">
                    <div class="row">
                        <div class="col">
                            <div class="acc-form">
                                <div class="log-acc-page" id="CustomerLoginForm">
                                    <!-- account title start -->
                                    <div class="content-main-title">
                                        <div class="section-cont-title">
                                            <h2><span>Registration</span></h2>
                                            <p>Please Create Your account  </p>
                                        </div>
                                    </div>
                                    <!-- account title end -->
                                    <!-- account login start -->
                                    <div class="acc-page">
                                        <div class="login">
                                            <form method="post" action="UpdateAccount.py" enctype="multipart/form-data">
                                                <div class="login-form-container">
                                                    <ul class="fill-form">
                                                        <li class="log-email">
                                                            <label>Sr No</label>
                                                            <input type="text" name="id" id="id"  class="input-full" placeholder="First Name" value="{myresult[0]}" readonly >
                                                        </li>
                                                        <li class="log-email">
                                                            <label>First Name</label>
                                                            <input type="text" name="FirstName" id="FirstName"  class="input-full" placeholder="First Name" value="{myresult[1]}" >
                                                        </li>
                                                        <li class="log-pwd">
                                                            <label>Middle Name</label>
                                                            <input type="text" name="MiddleName" id="MiddleName" class="input-full" placeholder="Middle Name" value="{myresult[2]}">
                                                        </li>
                                                        <li class="log-pwd">
                                                            <label>Last Name</label>
                                                            <input type="text" name="LastName" id="LastName" class="input-full" placeholder="Last Name" value="{myresult[3]}">
                                                        </li>
                                                        <li class="log-pwd">
                                                            <label>Phone No</label>
                                                            <input type="tel" name="PhoneNo" id="PhoneNo" class="input-full" placeholder="Phone No" value="{myresult[4]}">
                                                        </li>
                                                          <li class="log-pwd">
                                                            <label>Email</label>
                                                            <input type="email" name="Email" id="Email" class="input-full" placeholder="Email" value="{myresult[5]}" readonly>
                                                        </li>
                                                         <li class="log-pwd">
                                                            <label>Password</label>
                                                            <input type="text" name="Password" id="Password" class="input-full" placeholder="Password" value="{myresult[6]}">
                                                        </li>
                                                        
                                                    </ul>
                                                    <div class="form-action-button">
                                                        <button type="submit" class="btn btn-style2">Register Now</button>
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
