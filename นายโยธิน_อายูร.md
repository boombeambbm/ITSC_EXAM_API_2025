# ITSC_EXAM_API_2025
จงพัฒนา Web API ตาม Requirement ดังต่อไปนี้
<br>
## Technical Requirement <br>
1 พัฒนา Web API ตาม Stack ในปัจจุบันใดก็ได้ที่ตัวเองถนัดที่สุด และใช้ ฐานข้อมูลชนิดใด ก็ได้ไม่ว่าจะเป็น SQL หรือ NoSQL โดยใช้ Framework ORM ในการเชื่อมต่อ<br>
2 Web API ต้องพัฒนาให้อยู่ในรูปแบบของ REST API ตาม Spec OpenAPI Specification ในปัจจุบัน<br>
3 จงกำหนดค่าตัวแปร ของ Application ด้วย file ENV  และ gitignore  (10 คะแนน) <br>
4 จงเขียน Dockerfile และ เลือกใช้ Base Image ที่เหมาะสมและ กิน resource น้อย (10 คะแนน)<br>
5 จงเขียน Docker-compose เพื่อ Run ระบบ โดย กำหนดให้ Web API  Run ที่Port  8080  (10 คะแนน)<br>
6 เมื่อ Login แล้ว ให้สร้าง JWT token สำหรับ User  ในการทำ api Authentication and Authorization ของ API ที่ Required การauthentication and authorization <br>
<br>

## Optional Technical Requirement คะแนนพิเศษเพิ่มจากคะแนนเต็มซึ่งไม่ทำก็ได้<br>
1 Web API มีโครงสร้าง Code รองรับการ Run Automate Test   บน CI/CD และ Database เป็น Inmemmory เมื่อ กำหนด ตัวแปร ENV RunMode = test<br>
2 ใช้ Code First ในการพัฒนา และ มีการทำ Database Migration<br>
<br>

## Business Requirement <br>
บริษัท ต้องการพัฒนาระบบ Backend สำหรับจัดการคลังสินค้าและคำสั่งซื้อ (Order Management System) สำหรับร้านค้า E-commerce ขนาดเล็กที่ต้องการความรวดเร็วและประสิทธิภาพสูง จงพัฒนา Web API เพื่อรองรับฟังก์ชันการทำงานหลักของระบบนี้"<br>

1 มี Function Seed Data Product Item และ Seed Data Product Status Reference  แบบ Auto ในกรณีที่ Data collection เป็น empty  (5 คะแนน)

2 มีFunction ลงทะเบียน Create User Account (API Create User)   (10 คะแนน) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1 Function Create User Account  มี Data ที่ต้องกรอกคือ<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Email(คือ User account ไม่สามารถซ้ำได้ แต่ไม่ใช่ Primary Key)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ชื่อ<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- นาม สกุล <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- เบอร์โทร(Optional เข้ารหัสด้วย Symmetric Encryption ได้คะแนนพิเศษ)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Password (Optional เข้ารหัสด้วย Hashing Encryption ได้คะแนนพิเศษ)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ConfirmPassword (Optional เข้ารหัสด้วย Hashing Encryption ได้คะแนนพิเศษ)<br>
3 มีFunction User Login (API User Login)  (10 คะแนน)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1 User สามารถ login ด้วย User(Email) และ Password<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.2 API return User Basic Info คือ Email,ชื่อ, นาม สกุล, อยู่ใน Payload ของ JWT Token<br>

4 มี Function จัดการสินค้า ของ Admin (API Admin Search Order List)) (API Authentication ด้วยการ  Basic Authentication  กำหนด ตัวแปร User & password นี้ที่ ENV)  (10 คะแนน) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1 สามารถค้นหา เลขคำสั่งซื้อสินค้า  OrderNumber,ชื่อ นาม สกุล ผู้สั่ง<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.2 Data Return Order Product List พร้อมสถาณะคำสั่งซื้อ { รอยืนยันคำสั่งซื้อ , ยืนยันคำสั่งซื้อ }  แต่ละ Order มี data Order Detail<Order> <br>

5 มี Function เพิ่มคำสั่งซื้อสินค้า (API User Create Order)( API request JWT สำหรับ Authentication and Authorization )  (5 คะแนน) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1 Data ที่ต้อง Add Order Detail โดย 1 คำสั่งซื้อสามารถ เลือกสินได้หลายอย่าง แต่ละอย่างมีจำนวนแตกต่างกัน และ return OrderNumber โดย Order Detail         		ประกอบด้วย<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Product Number <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- จำนวน item<br>

6 มี Function แก้ไข คำสั่งซื้อสินค้า (API User Update Order)( API request JWT สำหรับ Authentication and Authorization )  (10 คะแนน) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.1 Data ที่ต้อง แก้ไขได้ ตาม คำสั่งซื้อ OrderNumber<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Product Number <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- จำนวน<br>

7 มี Function User ยืนยัน สั่งซื้อสินค้า (API User Confirm Order)( API request JWT สำหรับ Authentication and Authorization )  (5คะแนน) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.1 Data ที่ต้อง Put ซึ่งต้องตามคำสั่งซื้อOrderNumber <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-ที่อยู่จัดส่ง<br>

8 มี Function Admin  update สถาณะคำสั่งซื้อ (API Admin Approve Order ) (API Authentication ด้วยการ  Basic Authentication กำหนด ตัวแปร User & password นี้ที่ ENV)  (5 คะแนน) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.1 Admin สามารถ select เลือกยืนยัน user Order  ได้หลายOrderพร้อมกัน เพื่อเปลี่ยน สถาณะ เป็น  ยืนยันคำสั่งซื้อ<br>

