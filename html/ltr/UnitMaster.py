#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
import header
print("""
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
                        <h4 class="page-title" style="color:black;">Unit Master</h4>
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
                                <h4 class="card-title" style="color:black;">Unit Form</h4>
                               
                                <form class="m-t-30" action="UnitBackEndMaster.py" method="POST">
                                    <div class="form-group">
                                        <label for="exampleInputEmail1" style="color:black;">Unit Name</label>
                                        <input type="text" class="form-control" id="UnitName" name="UnitName" aria-describedby="emailHelp" placeholder="Unit Name"  >
                                        
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1" style="color:black;">Description</label>
                                        <input type="text" class="form-control" id="Description" name="Description" placeholder="Description"  >
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
