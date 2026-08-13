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
mycursor1 = mydb.cursor(dictionary=True)
query1=f""" select count(*) from product """
#print(query1)
mycursor.execute(query1)
myresult1=mycursor.fetchone()[0]
#print(myresult1)
query2=f""" select count(*) from category """
#print(query2)
mycursor.execute(query2)
myresult2=mycursor.fetchone()[0]
#print(myresult2)
query3=f""" select count(*) from registration """
#print(query3)
mycursor.execute(query3)
myresult3=mycursor.fetchone()[0]
#print(myresult3)
query4=f""" select count(*) from ordermaster """
#print(query4)
mycursor.execute(query4)
myresult4=mycursor.fetchone()[0]
#print(myresult4)
query5=f""" select count(*) from ordermaster where status="Pending" """
#print(query5)
mycursor.execute(query5)
myresult5=mycursor.fetchone()[0]
#print(myresult5)
query6=f""" select count(*) from ordermaster where status="Accepted" """
#print(query6)
mycursor.execute(query6)
myresult6=mycursor.fetchone()[0]
#print(myresult6)
query7=f""" select count(id) as procount,CategoryName from product  GROUP BY CategoryName """
#print(query7)
mycursor1.execute(query7)
myresult7=mycursor1.fetchall()
#print(myresult7)
procount=''
for x in myresult7:
    procount+=f""" 
    ['{x['CategoryName']}',{x['procount']}],

    """
query8=""" SELECT
    SUM(total_amount) AS daytotal,
    DATE(order_date) AS order_date
FROM ordermaster
WHERE DATE(order_date) BETWEEN CURRENT_DATE() - INTERVAL 7 DAY AND CURRENT_DATE()
GROUP BY DATE(order_date)
ORDER BY DATE(order_date) """
#print(query8)
mycursor1.execute(query8)
myresult8=mycursor1.fetchall()
#print(myresult8)
weeklysale=''
for x in myresult8:
    weeklysale+=f"""
['{x['order_date']}',{x['daytotal']}],
"""
query9=f""" select count(*) from registration where status="Active" """
#print(query9)
mycursor.execute(query9)
myresult9=mycursor.fetchone()[0]
#print(myresult9)
query10=f""" select count(*) from registration where status="Block" """
#print(query10)
mycursor.execute(query10)
myresult10=mycursor.fetchone()[0]
#print(myresult10)
import header
print("""
 <!----Sales chart start----->
 <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Week Days','Sales'],
          """ + weeklysale + """
        ]);

        var options = {
          title: 'Royal Bakers  Performance',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

        chart.draw(data, options);
      }
    </script>
    <!----Sales chart end----->



<!----Category wise product start-------------->

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
        ['Categrory Name','Product count'],
         """ + procount + """
          
        ]);

        var options = {
          title: 'My Categries Wise Product Count'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
    </script>
<!---------Category wise product end--------------->
""")
print(f"""
    <div class="page-wrapper">
            <!-- ============================================================== -->
            <!-- Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <div class="page-breadcrumb" style="border-bottom:2px solid black;">
                <div class="row">
                    <div class="col-5 align-self-center" >
                        <h4 class="page-title" style="color:black !important">Dashboard</h4>
                        
                        <div class="d-flex align-items-center">
                            <nav aria-label="breadcrumb">
                              
                            </nav>
                        </div>
                        
                    </div>
                     
                </div>
            </div>

    <div class="container-fluid">
             <div class="card-body">
                                <!-- title -->
                                <div class="d-md-flex align-items-center">
                                    <div>
                                        <h4 class="card-title" style="color: #ed222d;">Quick Summary of Your Bakery Store</h4>
                                           </div>
                                     
                                </div>
                                <!-- title -->
            </div>
               
                <div class="row">
                    <!-- crypto -->
                    
                    <div class="col-sm-12 col-lg-4">
                        <div class="card" style="background-color:white !important; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
                            <div class="card-body" >
                                <div class="d-flex align-items-center">
                                    <div class="m-r-20">
                                        <h1 class="m-b-0"> <img src="icons/1.png" style="width:75px;"></h1>
                                    </div>
                                    <div>
                                        <h6 class="m-b-5" style="font-size:18px; color:black; font-weight:bold;">Total Products</h6>
                                        <h3 class="m-b-0" style="font-size:36px; font-weight:900; color:black; margin-top:5px;">{myresult1}</h3>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>


                     <div class="col-sm-12 col-lg-4">
                        <div class="card" style="background-color:white  !important; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                    <div class="m-r-20">
                                        <h1 class="m-b-0"> <img src="icons/2.png" style="width:75px;"></h1>
                                    </div>
                                    <div>
                                        <h6 class="m-b-5" style="font-size:18px; color:black; font-weight:bold;">Total Categories</h6>
                                        <h3 class="m-b-0" style="font-size:36px; font-weight:900; color:black; margin-top:5px;">{myresult2}</h3>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>


                     <div class="col-sm-12 col-lg-4">
                        <div class="card" style="background-color:white  !important; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                    <div class="m-r-20">
                                        <h1 class="m-b-0"> <img src="icons/3.png" style="width:75px;"></h1>
                                    </div>
                                    <div>
                                        <h6 class="m-b-5" style="font-size:18px; color:black; font-weight:bold;">Total Customers</h6>
                                        <h3 class="m-b-0" style="font-size:36px; font-weight:900; color:black; margin-top:5px;">{myresult3}</h3>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-sm-12 col-lg-4">
                       <div class="card" style="background-color:white  !important; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                    <div class="m-r-20">
                                        <h1 class="m-b-0"> <img src="icons/3.png" style="width:75px;"></h1>
                                    </div>
                                    <div>
                                        <h6 class="m-b-5" style="font-size:18px; color:black; font-weight:bold;">Total Active Customers</h6>
                                        <h3 class="m-b-0" style="font-size:36px; font-weight:900; color:black; margin-top:5px;">{myresult9}</h3>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-sm-12 col-lg-4">
                       <div class="card" style="background-color:white  !important; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                    <div class="m-r-20">
                                        <h1 class="m-b-0"> <img src="icons/3.png" style="width:75px;"></h1>
                                    </div>
                                    <div>
                                        <h6 class="m-b-5" style="font-size:18px; color:black; font-weight:bold;">Total Blocked Customers</h6>
                                        <h3 class="m-b-0" style="font-size:36px; font-weight:900; color:black; margin-top:5px;">{myresult10}</h3>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                </div>






                <div class="card-body">
                                <!-- title -->
                                <div class="d-md-flex align-items-center">
                                    <div>
                                        <h4 class="card-title" style="color: #ed222d;">Order Summary</h4>
                                           </div>
                                     
                                </div>
                                <!-- title -->
                </div>



                        <div class="row">
                    <!-- crypto -->
                    
                    <div class="col-sm-12 col-lg-4">
                        <div class="card" style="background-color:white  !important; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                    <div class="m-r-20">
                                        <h1 class="m-b-0"> <img src="icons/4.png" style="width:75px;"></h1>
                                    </div>
                                    <div>
                                        <h6 class="m-b-5" style="font-size:18px; color:black; font-weight:bold;">Total Orders</h6>
                                        <h3 class="m-b-0" style="font-size:36px; font-weight:900; color:black; margin-top:5px;">{myresult4}</h3>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>


                     <div class="col-sm-12 col-lg-4">
                        <div class="card" style="background-color:white !important; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                    <div class="m-r-20">
                                        <h1 class="m-b-0"> <img src="icons/5.png" style="width:75px;"></h1>
                                    </div>
                                    <div>
                                        <h6 class="m-b-5" style="font-size:18px; color:black; font-weight:bold;">Pending Orders</h6>
                                        <h3 class="m-b-0" style="font-size:36px; font-weight:900; color:black; margin-top:5px;">{myresult5}</h3>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>


                     <div class="col-sm-12 col-lg-4">
                        <div class="card" style="background-color:white  !important; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
                            <div class="card-body">
                                <div class="d-flex align-items-center">
                                    <div class="m-r-20">
                                        <h1 class="m-b-0"> <img src="icons/6.png" style="width:75px;"></h1>
                                    </div>
                                    <div>
                                        <h6 class="m-b-5" style="font-size:18px; color:black; font-weight:bold;">Accepted Orders</h6>
                                        <h3 class="m-b-0" style="font-size:36px; font-weight:900; color:black; margin-top:5px;">{myresult6}</h3>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>



<div class="row">
                    <!-- column -->
                    <div class="col-sm-12 col-lg-6">
                        <div class="card card-hover">
                            <div class="card-body">
                                <h4 class="card-title" style="color: #ed222d;">Sales Summary</h4>
                                 
                                
                                <div id="curve_chart" style="width: 500px; height: 500px"></div>
                            </div>
                        </div>
                    </div>
                    <!-- column -->
                    <div class="col-sm-12 col-lg-6">
                        <div class="card card-hover">
                            <div class="card-body">
                                <h4 class="card-title" style="color: #ed222d;">Category-wise Products</h4>

                                  <div id="piechart" style="width: 500px; height: 500px;"></div>
                                
                            </div>
                        </div>
                    </div>
                   
                </div>




























    </div>
                    
""")
import footer
