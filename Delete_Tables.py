
import mysql.connector

n_eps = 10

Mydb = mysql.connector.connect(
    
    host="localhost",
    user="root",
    password="welcome123",
    database="DataStream"
)

Mycursor = Mydb.cursor()

for j in range(n_eps): 
    Mycursor.execute(f"DROP TABLE IF EXISTS T{j}")

