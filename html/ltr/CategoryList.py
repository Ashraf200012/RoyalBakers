#!/usr/bin/env python3
import cgi
import cgitb
import os
cgitb.enable()
import header
import mysql.connector
mydb = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", ""),  
    database=os.environ.get("DB_NAME", "royalbakers"), port=int(os.environ.get("DB_PORT", 3306)))
mycursor = mydb.cursor()
query=f"""select * from category"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
for x in myresult:
    tr_html+=f"""
    <tr>
                                        <th scope="row"><a href="CategoryDelete.py?id={x[0]}"><button class="btn-delete">Delete</button></a>
                                        </th>
                                            <th scope="row">{x[0]}</th>
                                            <td>{x[1]}</td>
                                            <td>{x[2]}</td>
                                            <td><img src="Category/{x[0]}/{x[3]}" style="width:200px;height:200px;"></td>
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
                        <h4 class="page-title">Category Master</h4>
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
                                <h4 class="card-title">Category List</h4>
                                <div class="table-responsive">
                                    
                                </div>
                            </div>
                            <div class="table-responsive">
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <th scope="col">Action</th>
                                            <th scope="col">Sr No</th>
                                            <th scope="col">Category Name</th>
                                            <th scope="col">Description</th>
                                            <th scope="col">Category Image</th>
                                            
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
            <!-- footer -->
            <!-- ============================================================== -->
            <footer class="footer text-center">
       All Rights Reserved by Xtreme admin. Designed and Developed by <a href="https://wrappixel.com/">WrapPixel</a>.
</footer>
            <!-- ============================================================== -->
            <!-- End footer -->
            <!-- ============================================================== -->
        </div>
        <!-- ============================================================== -->
        <!-- End Page wrapper  -->
        <!-- ============================================================== -->
    </div>
    <!-- =======================================
      
    <div class="chat-windows"></div>
    <!-- ============================================================== -->
    <!-- All Jquery -->
    <!-- ============================================================== -->
    <script src="../../assets/libs/jquery/dist/jquery.min.js"></script>
    <!-- Bootstrap tether Core JavaScript -->
    <script src="../../assets/libs/popper.js/dist/umd/popper.min.js"></script>
    <script src="../../assets/libs/bootstrap/dist/js/bootstrap.min.js"></script>
    <!-- apps -->
    <script src="../../dist/js/app.min.js"></script>
    <script src="../../dist/js/app.init.js"></script>
    <script src="../../dist/js/app-style-switcher.js"></script>
    <!-- slimscrollbar scrollbar JavaScript -->
    <script src="../../assets/libs/perfect-scrollbar/dist/perfect-scrollbar.jquery.min.js"></script>
    <script src="../../assets/extra-libs/sparkline/sparkline.js"></script>
    <!--Wave Effects -->
    <script src="../../dist/js/waves.js"></script>
    <!--Menu sidebar -->
    <script src="../../dist/js/sidebarmenu.js"></script>
    <!--Custom JavaScript -->
    <script src="../../dist/js/custom.min.js"></script>
</body>


<!-- Mirrored from themedesigner.in/demo/wrappixel/admin-template/xtreme/html/ltr/table-basic.html by HTTrack Website Copier/3.x [XR&CO'2014], Wed, 06 Jun 2018 05:50:18 GMT -->
</html>
""")
