#!/usr/bin/env python3
import cgi
import cgitb
import os
#import sys
#sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()
import header
import mysql.connector
mydb = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", ""),  
    database=os.environ.get("DB_NAME", "royalbakers"), port=int(os.environ.get("DB_PORT", 3306)))
mycursor = mydb.cursor()
query=f"""select * from registration"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
for x in myresult:
    tr_html+=f"""
    <tr>
                                        <th scope="row">
                                            <a href="BlockCustomer.py?id={x[0]}"><button class="btn-delete" style="padding: 6px 14px; margin-bottom: 5px; border-radius: 6px; min-width: 80px; font-weight:600; letter-spacing:0.5px;">Block</button></a>
                                            <br>
                                            
                                        </th>
                                            <th scope="row">{x[0]}</th>
                                            <td>{x[1]}</td>
                                            <td>{x[4]}</td>
                                            <td><img src="../../Registration/{x[0]}/{x[7]}" style="width:100px;height:100px;"></td>
                                        </tr>
    """
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
                        <h4 class="page-title">Customer Master</h4>
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
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h4 class="card-title">Customer List</h4>
                                <div class="table-responsive">
                                    
                                </div>
                            </div>
                            <div class="table-responsive">
                                <table class="table">
                                    <thead>
                                    <tr style="background-color:#1E293B; color:white;">
                                            <th scope="col" style="color:white;">Action</th>
                                            <th scope="col" style="color:white;">Sr No</th>
                                            <th scope="col" style="color:white;">Customer Name</th>
                                            <th scope="col" style="color:white;">Phone No</th>
                                            <th scope="col" style="color:white;">Profile Image</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {tr_html}
                                       
                                        
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                    
              
                </div>
               
            </div>
            <!-- ============================================================== -->
            <!-- End Container fluid  -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
""")
import footer
