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
query=f""" select * from category"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
options_html='<option value="">Select Category Name</option>\n'
for x in myresult:
    CategoryName=x[1]
    options_html+=f'<option value="{CategoryName}">{CategoryName}</option>\n'
query1=f""" select * from flavour"""
#print(query1)
mycursor.execute(query1)
myresult1=mycursor.fetchall()
#print(myresult1)
options_html1='<option value="">Select Flavour Name</option>\n'
for x in myresult1:
    FlavourName=x[1]
    options_html1+=f'<option value="{FlavourName}">{FlavourName}</option>\n'
query2=f""" select * from unit"""
#print(query2)
mycursor.execute(query2)
myresult2=mycursor.fetchall()
#print(myresult2)
options_html2='<option value="">Select Unit Name</option>\n'
for x in myresult2:
    UnitName=x[1]
    options_html2+=f'<option value="{UnitName}">{UnitName}</option>\n'
import header
print(f"""
        <!-- ============================================================== -->
        <!-- End Left Sidebar - style you can find in sidebar.scss  -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- Page wrapper  -->
        <!-- ============================================================== -->
        <div class="page-wrapper">
            <!-- ============================================================== -->
            <!-- Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <div class="page-breadcrumb">
                <div class="row">
                    <div class="col-5 align-self-center">
                        <h4 class="page-title" style="color:black;">Product Master</h4>
                        <div class="d-flex align-items-center">
                            <nav aria-label="breadcrumb">
                                
                            </nav>
                        </div>
                    </div>
                    
                </div>
            </div>
            <!-- ============================================================== -->
            <!-- End Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- Container fluid  -->
            <!-- ============================================================== -->
            <div class="container-fluid">
                <!-- ============================================================== -->
                <!-- Start Page Content -->
                <!-- ============================================================== -->
                <!-- row -->
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h4 class="card-title" style="color:black;">Product Form</h4>
                               
                                <form class="m-t-30" action="ProductBackEnd.py" method="POST" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="exampleInputEmail1" style="color:black;">Product Name</label>
                                        <input type="text" class="form-control" id="ProductName" name="ProductName" aria-describedby="emailHelp" placeholder="Product Name"  >
                                        
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1" style="color:black;">Select Category Name</label>
                                        <select name="CategoryName" id="CategoryName" class="form-control">
                                        {options_html}
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1" style="color:black;">Select Flavour Name</label>
                                        <select name="FlavourName" id="FlavourName" class="form-control">
                                        {options_html1}
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1" style="color:black;">Select Unit Name</label>
                                        <select name="UnitName" id="UnitName" class="form-control">
                                        {options_html2}
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1" style="color:black;">Price</label>
                                        <input type="text" class="form-control" id="Price" name="Price" placeholder="Price"  >
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1" style="color:black;">Description</label>
                                        <input type="text" class="form-control" id="Description" name="Description" placeholder="Description"  >
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1" style="color:black;">Product Image</label>
                                        <input type="file" class="form-control" id="photo" name="photo"   >
                                    </div>
                                    
                                   
                                    
      
                                    <button type="submit" class="btn btn-primary" style="background-color:#ed222d;border:none;">Submit</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- row -->
                
                
                
                
                
                    
                <!-- ============================================================== -->
                <!-- End PAge Content -->
                <!-- ============================================================== -->
                <!-- ============================================================== -->
                <!-- Right sidebar -->
                <!-- ============================================================== -->
                <!-- .right-sidebar -->
                <!-- ============================================================== -->
                <!-- End Right sidebar -->
                <!-- ============================================================== -->
            </div>
            <!-- ============================================================== -->
            <!-- End Container fluid  -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            
""")
import footer
