"""
This is the modlue with which you can connect to 
MySQL Managment server and check if it is succesful
"""
# To connect with Mysql Data Management server
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "welcome123",
    database = "TempData"
)

# to check if the connection is OK
print(db)

if(db):
    print("the connection successful")
else:
    print("connecntion failed")

test = db.cursor()

test.execute("DESCRIBE T1")

for item in test:
    print(item)


