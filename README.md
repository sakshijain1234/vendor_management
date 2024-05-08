<h1>Prerequisites:</h1>
<p>Python 10.0.3 version installed on your system, <br>
`pip` virtual environment</p>

<h2>get to postman to test api's: </h2>

<p>download postman from:<br>
https://www.postman.com/downloads/</p>

<h2>signin to postman to test api's: </h2>
 <p>
username: sjsakshi20.05@gmail.com<br>
password: 05Sakshi*hello</p>

<h2>you will redirect to :</h2>

![Screenshot (584)](https://github.com/sakshijain1234/vendor_management/assets/82942988/770a1c31-e6fd-4051-b9c4-dfd10f95ae3d)

<h3>now click on :</h3>

![Screenshot (584)](https://github.com/sakshijain1234/vendor_management/assets/82942988/4f92fc73-33ae-4147-a754-413cdb5f6601)

<h3>you will redirect to :</h3>

![Screenshot (585)](https://github.com/sakshijain1234/vendor_management/assets/82942988/18e3b6f1-cf47-4c41-b6e3-747a4b84429d)

<h3>you can change request method from:</h3>

![Screenshot (586)](https://github.com/sakshijain1234/vendor_management/assets/82942988/7f59c849-084b-42a4-ac01-d23086c93000)

<h3>Setup Instructions</h3>

<p>1.)Run the following command in the Terminal of your code editor

git clone "https://github.com/sakshijain1234/vendor_management"

2.)Run the following commands in the command prompt with opening the vendor_management folder:

virtualenv env<br>
cd env\scripts<br>
activate<br>
cd..<br>
cd..<br>
pip install django<br>
django-admin startproject vendor_management<br>
cd vendor_management<br>
pip install djangorestframework</p>

<h3>Run the project using</h3>

<p>python manage.py runserver</p>

<h2>These are the apis that will gonna work as mentioned in assignment</h2>
<h4>Vendor Profile Management:</h4>
<ul>
    <li><strong>POST /api/vendors/</strong>: Create a new vendor.</li>
    <li><strong>GET /api/vendors/</strong>: List all vendors.</li>
    <li><strong>GET /api/vendors/{vendor_id}/</strong>: Retrieve a specific vendor's details.</li>
    <li><strong>PUT /api/vendors/{vendor_id}/</strong>: Update a vendor's details.</li>
    <li><strong>DELETE /api/vendors/{vendor_id}/</strong>: Delete a vendor.</li>
</ul>

<h2>Exmples</h2>
<h4>GET /api/vendors/</h4>
![Screenshot (591)](https://github.com/sakshijain1234/vendor_management/assets/82942988/84971773-30d5-4787-8906-04a2e3ab1dcd)

<h4>POST /api/vendors/></h4>
![Screenshot (592)](https://github.com/sakshijain1234/vendor_management/assets/82942988/9f04c416-ff33-4379-a972-e134f21a70db)

<h4>GET /api/vendors/{vendor_id}/</h4>
![Screenshot (593)](https://github.com/sakshijain1234/vendor_management/assets/82942988/1872986a-fcaa-487b-9123-73105c0db32a)

<h4>PUT /api/vendors/{vendor_id}/</h4>
![Screenshot (594)](https://github.com/sakshijain1234/vendor_management/assets/82942988/66a413f4-03a0-4f87-b00f-d59c211376d8)

<h4>DELETE /api/vendors/{vendor_id}/</h4>
![Screenshot (595)](https://github.com/sakshijain1234/vendor_management/assets/82942988/33caa700-10b5-4723-a0d5-7a94903bfa29)


<h4>Purchase Order Tracking:</h4>
<ul>
    <li><strong>POST /api/purchase_orders/</strong>: Create a purchase order.</li>
    <li><strong>GET /api/purchase_orders/</strong>: List all purchase orders with an option to filter by vendor.</li>
    <li><strong>GET /api/purchase_orders/{po_id}/</strong>: Retrieve details of a specific purchase order.</li>
    <li><strong>PUT /api/purchase_orders/{po_id}/</strong>: Update a purchase order.</li>
    <li><strong>DELETE /api/purchase_orders/{po_id}/</strong>: Delete a purchase order.</li>
</ul>

<h4>Vendor Performance Evaluation:</h4>
<ul>
    <li><strong>GET /api/vendors/{vendor_id}/performance</strong>: Retrieve a vendor's performance metrics.</li>
</ul>


