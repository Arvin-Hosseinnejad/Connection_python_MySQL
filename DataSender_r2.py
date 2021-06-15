from DataGenerator import generator as g
import mysql.connector

n_row = 10  # number of data to be generated and send to database
n_eps = 10   # number of episode to be stored / number of tables 	

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="welcome123",
    database="DataStream"
)
cursor = db.cursor()


for j in range(n_eps):
    cursor.execute(f"Create Table T{j}(Dataid int(2) not null auto_increment,txid float(1) not null,uxid float(1) not null,Transfer float(1),primary key(Dataid))")
    sql = f"INSERT INTO T{j} (txid, uxid, Transfer) VALUES (%s, %s, %s)"
    db.commit()

    for i in range(n_row):

         result = g()
         cursor.execute(sql, (result[0], result[1], result[2]))
         db.commit()
         print(result)

