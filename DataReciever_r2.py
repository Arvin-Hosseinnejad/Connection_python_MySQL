import mysql.connector
import time

n_eps = 10

Mydb = mysql.connector.connect(
    
    host="localhost",
    user="root",
    password="welcome123",
    database="DataStream"
)

Mycursor = Mydb.cursor()

for j in range(n_eps):

    print("######################")
    print(f"This is {j}th episode")
    print("######################\n\n")

    Mycursor.execute(f"SELECT * FROM T{j}")
    results = Mycursor.fetchall()
    print(results)

    for row in results:
        time.sleep(0.3)
        print(row[1]+row[2]+row[3])
