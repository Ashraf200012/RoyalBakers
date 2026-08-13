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
CategoryName=form.getvalue("CategoryName")
#print(CategoryName)
query=f"""select * from product where CategoryName='{CategoryName}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
for x in myresult:
    tr_html+=f"""
<li class="blog-slider banner-hover">
                                            <div class="blog-post">
                                                <div class="blog-main-img">
                                                    <a href="" class="blog-img">
                                                        <img src="html/ltr/Product/{x[0]}/{x[7]}" style="width:300px;height:300px;" class="img-fluid" alt="backery-blog-1-1" >
                                                        <span class="blog-icon"><i class="bi bi-link-45deg"></i></span>
                                                    </a>
                                                </div>
                                                <div class="blog-post-content">
                                                    <h6 class="blog-title">  {x[1]} </h6>
                                                    <p class="blog-desc" style="text-align:justify;"> {x[6]} </p>
                                                     
                                                  <a href="Productdetails.py?proid={x[0]}"><button type="submit" class="btn btn-style2">Product Details</button></a>
                                                </div>
                                            </div>
                                        </li>
"""
import header
print(f"""
 <section class="blog-content-wrap section-ptb">
                <div class="container">

                <div class="section-capture">
                                <div class="section-title">
                                    <span class="sub-title"> category</span>
                                    <h2><span>All Category Products</span></h2>
                                </div>
                            </div>

                    <div class="row">
                        <div class="col">
                            <div class="blog-grid-wrapper">
                                <div class="blog-grid-wrap blog-grid">
                                    <ul class="single-blog-area">
                                        {tr_html}

                                        


                                        
                                        
                                    </ul>
                                   
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
""")
import footer    
